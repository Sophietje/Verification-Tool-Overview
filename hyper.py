#!/Users/grammarware/opt/anaconda3/bin/python

import latex2mathml.converter

def is_ul_item(line):
	return line.startswith('- ') or line.startswith('* ')

def is_ol_item(line):
	return len(line) > 3 and line[0].isdigit() and line[1] == '.' and line[2] == ' '

IN_NO_LIST = 0
IN_UL_LIST = 1
IN_OL_LIST = 2
IN_PRE_BLK = 3
def md2html(md_lines):
	ret_lines = []
	stack = [IN_NO_LIST]
	i = 0
	while i < len(md_lines):
		line = md_lines[i].strip()
		if stack[-1] == IN_PRE_BLK:
			if line == '```':
				ret_lines.append('</pre>')
				stack.pop()
			else:
				ret_lines.append(line)
			i += 1
			continue
		else:
			if line.startswith('```'):
				ret_lines.append('<pre>')
				stack.append(IN_PRE_BLK)
				i += 1
				continue
		# all the normal list stuff
		if stack[-1] == IN_NO_LIST:
			if is_ul_item(line):
				ret_lines.append('<ul>')
				ret_lines.append(li(line[2:].strip()))
				stack.append(IN_UL_LIST)
			elif is_ol_item(line):
				ret_lines.append('<ol>')
				ret_lines.append(li(line[2:].strip()))
				stack.append(IN_OL_LIST)
			else:
				ret_lines.append(my_md_converter(line.strip()))
		elif stack[-1] == IN_UL_LIST:
			if is_ul_item(line):
				ret_lines.append(li(line[2:].strip()))
			elif is_ol_item(line):
				ret_lines.append('<ol>')
				ret_lines.append(li(line[2:].strip()))
				stack.append(IN_OL_LIST)
			else:
				ret_lines.append('</ul>')
				stack.pop()
				continue
		elif stack[-1] == IN_OL_LIST:
			if is_ol_item(line):
				ret_lines.append(li(line[3:].strip()))
			elif is_ul_item(line):
				ret_lines.append('<ul>')
				ret_lines.append(li(line[2:].strip()))
				stack.append(IN_UL_LIST)
			else:
				ret_lines.append('</ol>')
				stack.pop()
				continue
		else:
			# cannot happen
			pass
		i += 1
	while len(stack)>1:
		if stack[-1] == IN_UL_LIST:
			ret_lines.append('</ul>')
			stack.pop()
		if stack[-1] == IN_OL_LIST:
			ret_lines.append('</ol>')
			stack.pop()
	return '\n'.join(ret_lines)

def my_md_converter(x):
	return text2text(clickable(link2link(gentle_latex2mathml(x))))

def get_key(fn):
	if fn.endswith('.md'):
		fn = fn[:-3]
	if fn.find('(') > -1 and fn.find(')') > -1:
		before = fn[0:fn.index('(')].strip()
		after = fn[fn.index('(')+1 : fn.index(')')].strip()
		if len(before) < 2 or len(after) < 2:
			fn = before + after
		elif len(before) > len(after) > 1:
			fn = after
		elif len(after) > len(before) > 1:
			fn = before
	if len(fn) > 20:
		fn2 = ''.join(cap for cap in fn if cap.isupper())
		if fn2:
			fn = fn2
		else:
			fn2 = ''.join(word[0] for word in fn.replace('-', ' ').split())
			if fn2:
				fn = fn2
	fn = fn.lower()
	for c in ' _-':
		fn = fn.replace(c, '')
	for p in {'τ':'tau', 'µ':'mu', 'é':'e', '+':'plus', '*':'star'}.items():
		fn = fn.replace(p[0], p[1])
	fn = fn.replace('τ', 'tau').replace('é', 'e')
	return fn

def clickable(http):
	if http.find('http') > -1:
		before = http[:http.index('http')]
		if before.endswith('"'):
			# we're messing with an already HTML-ified URI!
			return http
		after = http[http.index('http'):]
		link = after.split(' ')[0]
		rest = after[len(link):].strip()
		if rest.startswith('(') and rest.endswith(')'):
			rest = rest[1:-1]
		return before + make_link(link, f'<code>{link}</code>', why=rest)
	else:
		return http

def h3(x):
	return f'<h3>{x}</h3>'

def li(x):
	return f'<li>{my_md_converter(x)}</li>'

def ul(items):
	if not items:
		return ''
	cuis = [i.strip() for i in items if i]
	if len(cuis) == 1:
		return my_md_converter(cuis[0])
	if all([i.startswith('- ') for i in cuis]):
		cuis = [i[1:].strip() for i in cuis]
	return '<ul>' + '\n'.join([li(i) for i in cuis]) + '</ul>'

def make_link(where, what, hover='', why=''):
	if hover:
		s = f'<a href="{where}" title="{hover}">{what}</a>'
	else:
		s = f'<a href="{where}">{what}</a>'
	if why:
		s += f' ({why})'
	return s

def gentle_latex2mathml(x):
	if x.find('$') < 0:
		# no need to go through the trouble
		return x
	if x.startswith('$'):
		x = ' ' + x
	if x.endswith('$'):
		x = x + ' '
	xs = x.split('$')
	for i in range(0,len(xs)//2):
		xs[2*i+1] = latex2mathml.converter.convert(xs[2*i+1])
	return ''.join(xs).strip()

LINK_PARSER_NORMAL = 1
LINK_PARSER_PERHAPS_LINK = 2
LINK_PARSER_IMPLICIT = 3
LINK_PARSER_IMPLICIT_PRIME = 4
LINK_PARSER_EXPLICIT = 5
LINK_PARSER_EXPLICIT_PRIME = 6
LINK_PARSER_TARGET = 7
LINK_PARSER_FIG_HOPE = 8
LINK_PARSER_FIG_ALMOST = 9
LINK_PARSER_FIG = 10
LINK_PARSER_FIG_PRIME = 11
def link2link(x):
	r = ''
	i = 0
	state = LINK_PARSER_NORMAL
	while i < len(x):
		if state == LINK_PARSER_NORMAL:
			if x[i] == '[':
				state = LINK_PARSER_PERHAPS_LINK
			elif x[i] == '!':
				state = LINK_PARSER_FIG_HOPE
			else:
				r += x[i]
		elif state == LINK_PARSER_PERHAPS_LINK:
			if x[i] == '[':
				where = ''
				state = LINK_PARSER_IMPLICIT
			else:
				where = x[i]
				state = LINK_PARSER_EXPLICIT
		elif state == LINK_PARSER_IMPLICIT:
			if x[i] == ']':
				state = LINK_PARSER_IMPLICIT_PRIME
			else:
				where += x[i]
		elif state == LINK_PARSER_IMPLICIT_PRIME:
			if x[i] == ']':
				r += f'<a href="{get_key(where)}.html">{where}</a>'
				state = LINK_PARSER_NORMAL
			else:
				# ERROR: unmatched [[...], roll back to normal brackets
				r += f'[[{where}]{x[i]}'
				state = LINK_PARSER_NORMAL
		elif state == LINK_PARSER_EXPLICIT:
			if x[i] == ']':
				state = LINK_PARSER_EXPLICIT_PRIME
			else:
				where += x[i]
		elif state == LINK_PARSER_EXPLICIT_PRIME:
			if x[i] == '(':
				target = ''
				state = LINK_PARSER_TARGET
			else:
				# ERROR: no target follows [...], roll back to normal brackets
				r += f'[{where}]{x[i]}'
				state = LINK_PARSER_NORMAL
		elif state == LINK_PARSER_TARGET:
			if x[i] == ')':
				r += f'<a href="{get_key(where)}.html">{where}</a>'
				state = LINK_PARSER_NORMAL
			else:
				target += x[i]
		elif state == LINK_PARSER_FIG_HOPE:
			if x[i] == '[':
				state = LINK_PARSER_FIG_ALMOST
			else:
				r += '!' + x[i]
				state = LINK_PARSER_NORMAL
		elif state == LINK_PARSER_FIG_ALMOST:
			if x[i] == '[':
				where = ''
				state = LINK_PARSER_FIG
			else:
				r += '![' + x[i]
				state = LINK_PARSER_NORMAL
		elif state == LINK_PARSER_FIG:
			if x[i] == ']':
				state = LINK_PARSER_FIG_PRIME
			else:
				where += x[i]
		elif state == LINK_PARSER_FIG_PRIME:
			if x[i] == ']':
				r += f'<br/><img src="{where}" alt="{where}"/><br/>'
				state = LINK_PARSER_NORMAL
			else:
				r += f'![[{where}]' + x[i]
				state = LINK_PARSER_NORMAL
		else:
				print(f'ERROR IN LINK: {x} --- lost parser state')
				state = LINK_PARSER_NORMAL
		i += 1
	# check if we're in the final state
	if state == LINK_PARSER_PERHAPS_LINK:
		r += '['
	elif state == LINK_PARSER_IMPLICIT:
		r += f'[[{where}'
	elif state == LINK_PARSER_IMPLICIT_PRIME:
		r += f'[[{where}]'
	elif state == LINK_PARSER_EXPLICIT:
		r += f'[{where}'
	elif state == LINK_PARSER_EXPLICIT_PRIME:
		r += f'[{where}]'
	elif state == LINK_PARSER_TARGET:
		r += f'[{where}]({target}'
	elif state == LINK_PARSER_FIG_HOPE:
		r += f'!'
	elif state == LINK_PARSER_FIG_ALMOST:
		r += f'!['
	elif state == LINK_PARSER_FIG:
		r += f'![[{where}'
	elif state == LINK_PARSER_FIG_PRIME:
		r += f'![[{where}]'
	return r

TEXT_PARSER_NORMAL = 100
TEXT_PARSER_TICK   = 101        
TEXT_PARSER_TICK_T = 102          
TEXT_PARSER_U      = 103           # _
TEXT_PARSER_US     = 104           # _*
TEXT_PARSER_USS    = 105           # _**
TEXT_PARSER_USST   = 106           # _**a
TEXT_PARSER_USSTS  = 107           # _**a*
TEXT_PARSER_UU     = 108           # __
TEXT_PARSER_UUS    = 109           # __*
TEXT_PARSER_UUSU   = 110           # __*_
TEXT_PARSER_UUST   = 111           # __*a
TEXT_PARSER_UUSTU  = 112           # __*a_
TEXT_PARSER_UUT    = 113           # __a
TEXT_PARSER_UUTS   = 114           # __a*
TEXT_PARSER_UUTSU  = 115           # __a*_
TEXT_PARSER_UUTST  = 116           # __a*b
TEXT_PARSER_UUTSTU = 117           # __a*b_
TEXT_PARSER_UUTU   = 118           # __a_
TEXT_PARSER_UT     = 119           # _a
TEXT_PARSER_UTS    = 120           # _a*
TEXT_PARSER_UTSS   = 121           # _a**
TEXT_PARSER_UTSST  = 122           # _a**b
TEXT_PARSER_UTSSTS = 123           # _a**b*
TEXT_PARSER_S      = 124           # *
TEXT_PARSER_SU     = 125           # *_
TEXT_PARSER_SUU    = 126           # *__
TEXT_PARSER_SUUT   = 127           # *__a
TEXT_PARSER_SUUTU  = 128           # *__a_
TEXT_PARSER_SS     = 129           # **
TEXT_PARSER_SSU    = 130           # **_
TEXT_PARSER_SSUS   = 131           # **_*
TEXT_PARSER_SSUT   = 132           # **_a
TEXT_PARSER_SSUTS  = 133           # **_a*
TEXT_PARSER_SST    = 134           # **a
TEXT_PARSER_SSTU   = 135           # **a_
TEXT_PARSER_SSTUS  = 136           # **a_*
TEXT_PARSER_SSTUT  = 137           # **a_b
TEXT_PARSER_SSTUTS = 138           # **a_b*
TEXT_PARSER_SSTS   = 139           # **a*
TEXT_PARSER_ST     = 140           # *a
TEXT_PARSER_STU    = 141           # *a_
TEXT_PARSER_STUU   = 142           # *a__
TEXT_PARSER_STUUT  = 143           # *a__b
TEXT_PARSER_STUUTU = 144           # *a__b_
def text2text(x):
	r = ''
	i = 0
	state = TEXT_PARSER_NORMAL
	content = ''
	while i < len(x):
		# print(f'[+] TEXT_PARSER_{state}: "{x[:i]}•{x[i:]}" -> "{r}"')
		if x[i:].startswith('<a href="'):
			j = x.find('</a>', i)
			if j > i:
				r += x[i:j+4]
				i = j+4
				continue
		if state == TEXT_PARSER_NORMAL:
			if x[i] == '`':
				state = TEXT_PARSER_TICK
			elif x[i] == '_':
				state = TEXT_PARSER_U
			elif x[i] == '*':
				state = TEXT_PARSER_S
			else:
				r += x[i]
		elif state == TEXT_PARSER_TICK:
			if x[i] == '`':
				r += '``'
				state = TEXT_PARSER_NORMAL
			else:
				content = x[i]
				state = TEXT_PARSER_TICK_T
		elif state == TEXT_PARSER_TICK_T:
			if x[i] == '`':
				r += f'<code>{content}</code>'
				state = TEXT_PARSER_NORMAL
			else:
				# inside ticks everything is verbatim
				content += x[i]

		elif state == TEXT_PARSER_U:      # _
			if x[i] == '_':
				state = TEXT_PARSER_UU
			elif x[i] == '*':
				state = TEXT_PARSER_US
			else:
				content = x[i]
				state = TEXT_PARSER_UT
		elif state == TEXT_PARSER_US:     # _*
			if x[i] == '_':
				r += '<em>*</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				state = TEXT_PARSER_USS
			else:
				content = '*'+x[i]
				state = TEXT_PARSER_UT
		elif state == TEXT_PARSER_USS:    # _**
			if x[i] == '_':
				r += '<em>**</em>'
			elif x[i] == '*':
				content = '*'
				state = TEXT_PARSER_UTSS
			else:
				content = x[i]
				state = TEXT_PARSER_USST
		elif state == TEXT_PARSER_USST:   # _**a
			if x[i] == '_':
				r += f'<em>**{content}</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				state = TEXT_PARSER_USSTS
			else:
				content += x[i]
		elif state == TEXT_PARSER_USSTS:  # _**a*
			if x[i] == '_':
				r += f'<em>**{content}*</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				content = f'<strong>{content}</strong>'
				state = TEXT_PARSER_UT
			else:
				content += '*'+x[i]
				state = TEXT_PARSER_USST
		elif state == TEXT_PARSER_UU:     # __
			if x[i] == '_':
				r += '_'
			elif x[i] == '*':
				state = TEXT_PARSER_UUS
			else:
				content = x[i]
				state = TEXT_PARSER_UUT
		elif state == TEXT_PARSER_UUS:    # __*
			if x[i] == '_':
				state = TEXT_PARSER_UUSU
			elif x[i] == '*':
				content = '**'
				state = TEXT_PARSER_UUT
			else:
				content = x[i]
				state = TEXT_PARSER_UUST
		elif state == TEXT_PARSER_UUSU:   # __*_
			if x[i] == '_':
				r += '<strong>*</strong>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				content = '<em>_</em>'
				state = TEXT_PARSER_UUT
			else:
				content = '_'+x[i]
				state = TEXT_PARSER_UUST
		elif state == TEXT_PARSER_UUST:   # __*a
			if x[i] == '_':
				state = TEXT_PARSER_UUSTU
			elif x[i] == '*':
				content = f'<em>{content}</em>'
				state = TEXT_PARSER_UUT
			else:
				content += x[i]
		elif state == TEXT_PARSER_UUSTU:  # __*a_
			if x[i] == '_':
				r += f'<strong>*{content}</strong>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				content = f'<em>{content}_</em>'
				state = TEXT_PARSER_UUT
			else:
				content += '_'+x[i]
				state = TEXT_PARSER_UUST
		elif state == TEXT_PARSER_UUT:    # __a
			if x[i] == '_':
				state = TEXT_PARSER_UUTU
			elif x[i] == '*':
				state = TEXT_PARSER_UUTS
			else:
				content += x[i]
		elif state == TEXT_PARSER_UUTS:   # __a*
			if x[i] == '_':
				state = TEXT_PARSER_UUTSU
			elif x[i] == '*':
				content += '**'
				state = TEXT_PARSER_UUT
			else:
				content2 = x[i]
				state = TEXT_PARSER_UUTST
		elif state == TEXT_PARSER_UUTSU:  # __a*_
			if x[i] == '_':
				r += f'<strong>{content}*</strong>'
			elif x[i] == '*':
				content += '<em>_</em>'
				state = TEXT_PARSER_UUT
			else:
				content2 = '_'+x[i]
				state = TEXT_PARSER_UUTST
		elif state == TEXT_PARSER_UUTST:  # __a*b
			if x[i] == '_':
				state = TEXT_PARSER_UUTSTU
			elif x[i] == '*':
				content += f'<em>{content2}</em>'
				state = TEXT_PARSER_UUT
			else:
				content2 += x[i]
		elif state == TEXT_PARSER_UUTSTU: # __a*b_
			if x[i] == '_':
				r += f'<strong>{content}*{content2}</strong>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				content += f'<em>{content2}_</em>'
			else:
				content2 ++ '_'+x[i]
				state = TEXT_PARSER_UUTST
		elif state == TEXT_PARSER_UUTU:   # __a_
			if x[i] == '_':
				r += f'<strong>{content}</strong>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				content += '_'
				state = TEXT_PARSER_UUTS
			else:
				content += '_'+x[i]
				state = TEXT_PARSER_UUT
		elif state == TEXT_PARSER_UT:     # _a
			if x[i] == '_':
				r += f'<em>{content}</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				state = TEXT_PARSER_UTS
			else:
				content += x[i]
		elif state == TEXT_PARSER_UTS:    # _a*
			if x[i] == '_':
				r += f'<em>{content}*</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				state = TEXT_PARSER_UTSS
			else:
				content += '*'+x[i]
				state = TEXT_PARSER_UT
		elif state == TEXT_PARSER_UTSS:   # _a**
			if x[i] == '_':
				r += f'<em>{content}**</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				content += '*'
			else:
				content2 = x[i]
				state = TEXT_PARSER_UTSST
		elif state == TEXT_PARSER_UTSST:  # _a**b
			if x[i] == '_':
				r += f'<em>{content}**{content2}</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				state = TEXT_PARSER_UTSSTS
			else:
				content2 += x[i]
		elif state == TEXT_PARSER_UTSSTS: # _a**b*
			if x[i] == '_':
				r += f'<em>{content}**{content2}*</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '*':
				content += f'<strong>{content2}</strong>'
				state = TEXT_PARSER_UT
			else:
				content2 += '*'+x[i]
				state = TEXT_PARSER_UTSST

		elif state == TEXT_PARSER_S:      # *
			if x[i] == '*':
				state = TEXT_PARSER_SS
			elif x[i] == '_':
				state = TEXT_PARSER_SU
			else:
				content = x[i]
				state = TEXT_PARSER_ST
		elif state == TEXT_PARSER_SU:     # *_
			if x[i] == '*':
				r += '<em>_</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				state = TEXT_PARSER_SUU
			else:
				content = '_'+x[i]
				state = TEXT_PARSER_ST
		elif state == TEXT_PARSER_SUU:    # *__
			if x[i] == '*':
				r += '<em>__</em>'
			elif x[i] == '_':
				content = '_'
				state = TEXT_PARSER_STUU
			else:
				content = x[i]
				state = TEXT_PARSER_SUUT
		elif state == TEXT_PARSER_SUUT:   # *__a
			if x[i] == '*':
				r += f'<em>__{content}</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				state = TEXT_PARSER_SUUTU
			else:
				content += x[i]
		elif state == TEXT_PARSER_SUUTU:  # *__a_
			if x[i] == '*':
				r += f'<em>__{content}_</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				content = f'<strong>{content}</strong>'
				state = TEXT_PARSER_ST
			else:
				content += '_'+x[i]
				state = TEXT_PARSER_SUUT
		elif state == TEXT_PARSER_SS:     # **
			if x[i] == '*':
				r += '*'
			elif x[i] == '_':
				state = TEXT_PARSER_SSU
			else:
				content = x[i]
				state = TEXT_PARSER_SST
		elif state == TEXT_PARSER_SSU:    # **_
			if x[i] == '*':
				state = TEXT_PARSER_SSUS
			elif x[i] == '_':
				content = '__'
				state = TEXT_PARSER_SST
			else:
				content = x[i]
				state = TEXT_PARSER_SSUT
		elif state == TEXT_PARSER_SSUS:   # **_*
			if x[i] == '*':
				r += '<strong>_</strong>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				content = '<em>*</em>'
				state = TEXT_PARSER_SST
			else:
				content = '*'+x[i]
				state = TEXT_PARSER_SSUT
		elif state == TEXT_PARSER_SSUT:   # **_a
			if x[i] == '*':
				state = TEXT_PARSER_SSUTS
			elif x[i] == '_':
				content = f'<em>{content}</em>'
				state = TEXT_PARSER_SST
			else:
				content += x[i]
		elif state == TEXT_PARSER_SSUTS:  # **_a*
			if x[i] == '*':
				r += f'<strong>_{content}</strong>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				content = f'<em>{content}*</em>'
				state = TEXT_PARSER_SST
			else:
				content += '*'+x[i]
				state = TEXT_PARSER_SSUT
		elif state == TEXT_PARSER_SST:    # **a
			if x[i] == '*':
				state = TEXT_PARSER_SSTS
			elif x[i] == '_':
				state = TEXT_PARSER_SSTU
			else:
				content += x[i]
		elif state == TEXT_PARSER_SSTU:   # **a_
			if x[i] == '*':
				state = TEXT_PARSER_SSTUS
			elif x[i] == '_':
				content += '__'
				state = TEXT_PARSER_SST
			else:
				content2 = x[i]
				state = TEXT_PARSER_SSTUT
		elif state == TEXT_PARSER_SSTUS:  # **a_*
			if x[i] == '*':
				r += f'<strong>{content}_</strong>'
			elif x[i] == '_':
				content += '<em>*</em>'
				state = TEXT_PARSER_SST
			else:
				content2 = '*'+x[i]
				state = TEXT_PARSER_SSTUT
		elif state == TEXT_PARSER_SSTUT:  # **a_b
			if x[i] == '*':
				state = TEXT_PARSER_SSTUTS
			elif x[i] == '_':
				content += f'<em>{content2}</em>'
				state = TEXT_PARSER_SST
			else:
				content2 += x[i]
		elif state == TEXT_PARSER_SSTUTS: # **a_b*
			if x[i] == '*':
				r += f'<strong>{content}_{content2}</strong>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				content += f'<em>{content2}*</em>'
			else:
				content2 ++ '*'+x[i]
				state = TEXT_PARSER_SSTUT
		elif state == TEXT_PARSER_SSTS:   # **a*
			if x[i] == '*':
				r += f'<strong>{content}</strong>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				content += '*'
				state = TEXT_PARSER_SSTU
			else:
				content += '*'+x[i]
				state = TEXT_PARSER_SST
		elif state == TEXT_PARSER_ST:     # *a
			if x[i] == '*':
				r += f'<em>{content}</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				state = TEXT_PARSER_STU
			else:
				content += x[i]
		elif state == TEXT_PARSER_STU:    # *a_
			if x[i] == '*':
				r += f'<em>{content}_</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				state = TEXT_PARSER_STUU
			else:
				content += '_'+x[i]
				state = TEXT_PARSER_ST
		elif state == TEXT_PARSER_STUU:   # *a__
			if x[i] == '*':
				r += f'<em>{content}__</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				content += '_'
			else:
				content2 = x[i]
				state = TEXT_PARSER_STUUT
		elif state == TEXT_PARSER_STUUT:  # *a__b
			if x[i] == '*':
				r += f'<em>{content}__{content2}</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				state = TEXT_PARSER_STUUTU
			else:
				content2 += x[i]
		elif state == TEXT_PARSER_STUUTU: # *a__b_
			if x[i] == '*':
				r += f'<em>{content}__{content2}_</em>'
				state = TEXT_PARSER_NORMAL
			elif x[i] == '_':
				content += f'<strong>{content2}</strong>'
				state = TEXT_PARSER_ST
			else:
				content2 += '_'+x[i]
				state = TEXT_PARSER_STUUT

		else:
			print('[!] ERROR: Wrong text2text parser state!')
			# should be empty
			r += x[i]
		i += 1
	# print(f'[*] TEXT_PARSER_{state}: "{x[:i]}•{x[i:]}"')
	# aftermath
	if state == TEXT_PARSER_NORMAL: 
		pass
	elif state == TEXT_PARSER_TICK:           
		r += '`'
	elif state == TEXT_PARSER_TICK_T:           
		r += f'`{content}'
	elif state == TEXT_PARSER_U:      # _
		r += '_'
	elif state == TEXT_PARSER_US:     # _*
		r += '_*'
	elif state == TEXT_PARSER_USS:    # _**
		r += '_**'
	elif state == TEXT_PARSER_USST:   # _**a
		r += f'_**{content}'
	elif state == TEXT_PARSER_USSTS:  # _**a*
		# slightly nontrivial
		r += f'_*<em>{content}</em>'
	elif state == TEXT_PARSER_UU:     # __
		r += '__'
	elif state == TEXT_PARSER_UUS:    # __*
		r += '__*'
	elif state == TEXT_PARSER_UUSU:   # __*_
		# slightly nontrivial
		r += '_<em>*</em>'
	elif state == TEXT_PARSER_UUST:   # __*a
		r += f'__*{content}'
	elif state == TEXT_PARSER_UUSTU:  # __*a_
		# slightly nontrivial
		r += f'_<em>*{content}</em>'
	elif state == TEXT_PARSER_UUT:    # __a
		r += f'__{content}'
	elif state == TEXT_PARSER_UUTS:   # __a*
		r += f'__{content}*'
	elif state == TEXT_PARSER_UUTSU:  # __a*_
		# slightly nontrivial
		r += f'_<em>{content}*</em>'
	elif state == TEXT_PARSER_UUTST:  # __a*b
		r += f'__{content}*{content2}'
	elif state == TEXT_PARSER_UUTSTU: # __a*b_
		# slightly nontrivial
		r += f'_<em>{content}*{content2}</em>'
	elif state == TEXT_PARSER_UUTU:   # __a_
		# slightly nontrivial
		r += f'_<em>{content}</em>'
	elif state == TEXT_PARSER_UT:     # _a
		r += f'_{content}'
	elif state == TEXT_PARSER_UTS:    # _a*
		r += f'_{content}*'
	elif state == TEXT_PARSER_UTSS:   # _a**
		r += f'_{content}**'
	elif state == TEXT_PARSER_UTSST:  # _a**b
		r += f'_{content}**{content2}'
	elif state == TEXT_PARSER_UTSSTS: # _a**b*
		# slightly nontrivial
		r += f'_{content}*<em>{content2}</em>'
	elif state == TEXT_PARSER_S:      # *
		r += '*'
	elif state == TEXT_PARSER_SU:     # *_
		r += '*_'
	elif state == TEXT_PARSER_SUU:    # *__
		r += '*__'
	elif state == TEXT_PARSER_SUUT:   # *__a
		r += f'*__{content}'
	elif state == TEXT_PARSER_SUUTU:  # *__a_
		# slightly nontrivial
		r += f'*_<em>{content}</em>'
	elif state == TEXT_PARSER_SS:     # **
		r += '**'
	elif state == TEXT_PARSER_SSU:    # **_
		r += '**_'
	elif state == TEXT_PARSER_SSUS:   # **_*
		# slightly nontrivial
		r += '*<em>_<em>'
	elif state == TEXT_PARSER_SSUT:   # **_a
		r += f'**_{content}'
	elif state == TEXT_PARSER_SSUTS:  # **_a*
		# slightly nontrivial
		r += f'*<em>_{content}</em>'
	elif state == TEXT_PARSER_SST:    # **a
		r += f'**{content}'
	elif state == TEXT_PARSER_SSTU:   # **a_
		r += f'**{content}_'
	elif state == TEXT_PARSER_SSTUS:  # **a_*
		# slightly nontrivial
		r += f'*<em>{content}_</em>'
	elif state == TEXT_PARSER_SSTUT:  # **a_b
		r += f'**{content}_{content2}'
	elif state == TEXT_PARSER_SSTUTS: # **a_b*
		# slightly nontrivial
		r += f'*<em>{content}_{content2}</em>'
	elif state == TEXT_PARSER_SSTS:   # **a*
		# slightly nontrivial
		r += f'*<em>{content}</em>'
	elif state == TEXT_PARSER_ST:     # *a
		r += f'*{content}'
	elif state == TEXT_PARSER_STU:    # *a_
		r += f'*{content}_'
	elif state == TEXT_PARSER_STUU:   # *a__
		r += f'*{content}__'
	elif state == TEXT_PARSER_STUUT:  # *a__b
		r += f'*{content}__{content2}'
	elif state == TEXT_PARSER_STUUTU: # *a__b_
		# slightly nontrivial
		r += f'*{content}_<em>{content2}</em>'

	return r.\
		replace('</em><em>','').\
		replace('<em></em>','').\
		replace('</code><code>','').\
		replace('<code></code>','').\
		replace('</strong><strong>','').\
		replace('<strong></strong>','')
