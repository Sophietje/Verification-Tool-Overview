#!/Users/grammarware/opt/anaconda3/bin/python

import markdown2

def md2html_generic(md_lines):
	return markdown2.markdown('\n'.join(md_lines))

def is_ul_item(line):
	return line.startswith('- ') or line.startswith('* ')

def is_ol_item(line):
	return len(line) > 3 and line[0].isdigit() and line[1] == '.' and line[2] == ' '

IN_NO_LIST = 0
IN_UL_LIST = 1
IN_OL_LIST = 2
def md2html(md_lines):
	ret_lines = []
	stack = [IN_NO_LIST]
	i = 0
	while i < len(md_lines):
		line = md_lines[i]
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
	# if not x:
	# 	return '<br/>'
	return matched2code(clickable(link2link(x)))

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

def matched2code(x):
	for pair in (('`','code'), ('**','strong'), ('__','strong'), ('*','em'), ('_','em')):
		x = matched2tag(pair[0], pair[1], x) 
	return latex2mathml(x)

def matched2tag(symbol, tag, x):
	if x.find(symbol) < 0:
		# no need to go through the trouble
		return x
	xs = x.split(symbol)
	if len(xs) == 2:
		# we consider this too few
		return x
	if len(xs) % 2 != 0:
		xs.append('')
	r = ''
	for i in range(0, len(xs) // 2):
		r += f'{xs[2*i]}<{tag}>{xs[2*i+1]}</{tag}>'
	return r.replace(f'<{tag}></{tag}>', '').replace(f'</{tag}><{tag}>', '')

def latex2mathml(x):
	if x.find('$') < 0:
		# no need to go through the trouble
		return x
	if x.startswith('$'):
		x = ' ' + x
	if x.endswith('$'):
		x = x + ' '
	xs = x.split('$')
	if len(xs) == 3:
		return f'{xs[0]}<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mi>{xs[1]}</mi></mrow></math>{xs[2]}'.strip()
	elif len(xs) == 5:
		return f'''{xs[0]}
		<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mi>{xs[1]}</mi></mrow></math>
		{xs[2]}
		<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mi>{xs[3]}</mi></mrow></math>
		{xs[4]}'''.strip()
	else:
		# too complex
		return x


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

TEXT_PARSER_NORMAL = 1
TEXT_PARSER_STAR = 2
TEXT_PARSER_STAR_STAR = 3
TEXT_PARSER_STAR_STAR_TEXT = 4
TEXT_PARSER_STAR_STAR_TEXT_STAR = 5
TEXT_PARSER_STAR_TEXT = 6
TEXT_PARSER_STAR_UNDER = 7
TEXT_PARSER_TICK = 8
TEXT_PARSER_UNDER = 9
TEXT_PARSER_UNDER_STAR = 10
TEXT_PARSER_UNDER_STAR_STAR = 11
TEXT_PARSER_UNDER_TEXT = 12
TEXT_PARSER_UNDER_UNDER = 13
TEXT_PARSER_UNDER_UNDER_STAR = 14
TEXT_PARSER_UNDER_UNDER_TEXT = 15
TEXT_PARSER_UNDER_UNDER_TEXT_UNDER = 16
TEXT_PARSER_UNDER_UNDER_UNDER  = 17
TEXT_PARSER_UNDER_UNDER_UNDER_TEXT  = 18
TEXT_PARSER_UNDER_UNDER_UNDER_TEXT_U  = 19
TEXT_PARSER_UNDER_UNDER_UNDER_TEXT_UU  = 20
def text2text(x):
	r = ''
	i = 0
	state = TEXT_PARSER_NORMAL
	content = ''
	while i < len(x):
		# print(f'[+] TEXT_PARSER_{state}: "{x[:i]}•{x[i:]}"')
		if state == TEXT_PARSER_NORMAL:
			if x[i] == '`':
				content = ''
				state = TEXT_PARSER_TICK
			elif x[i] == '_':
				content = ''
				state = TEXT_PARSER_UNDER
			elif x[i] == '*':
				content = ''
				state = TEXT_PARSER_STAR
			else:
				r += x[i]
		elif state == TEXT_PARSER_TICK:
			if x[i] == '`':
				r += f'<code>{content}</code>'
				state = LINK_PARSER_NORMAL
			else:
				# inside ticks everything is verbatim
				content += x[i]
		elif state == TEXT_PARSER_UNDER:
			if x[i] == '_':
				state = TEXT_PARSER_UNDER_UNDER
			elif x[i] == '*':
				state = TEXT_PARSER_UNDER_STAR
			else:
				content = x[i]
				state = TEXT_PARSER_UNDER_TEXT
		elif state == TEXT_PARSER_UNDER_TEXT:
			# normal _xxx_
			if x[i] == '_':
				r += f'<em>{content}</em>'
				state = LINK_PARSER_NORMAL
			else:
				content += x[i]
		elif state == TEXT_PARSER_STAR_TEXT:
			# normal *xxx*
			if x[i] == '*':
				r += f'<em>{content}</em>'
				state = LINK_PARSER_NORMAL
			else:
				content += x[i]
		elif state == TEXT_PARSER_UNDER_UNDER_TEXT:
			# normal __xxx__
			if x[i] == '_':
				state = TEXT_PARSER_UNDER_UNDER_TEXT_UNDER
			else:
				content += x[i]
		elif state == TEXT_PARSER_UNDER_UNDER_TEXT_UNDER:
			if x[i] == '_':
				r += f'<strong>{content}</strong>'
				state = TEXT_PARSER_NORMAL
			else:
				r += f'_<em>{content}</em>'
				state = TEXT_PARSER_NORMAL
				continue
		elif state == TEXT_PARSER_STAR_STAR_TEXT:
			# normal **xxx**
			if x[i] == '*':
				state = TEXT_PARSER_STAR_STAR_TEXT_STAR
			else:
				content += x[i]
		elif state == TEXT_PARSER_STAR_STAR_TEXT_STAR:
			if x[i] == '*':
				r += f'<strong>{content}</strong>'
				state = TEXT_PARSER_NORMAL
			else:
				r += f'*<em>{content}</em>'
				state = TEXT_PARSER_NORMAL
				continue
		elif state == TEXT_PARSER_UNDER_UNDER:
			if x[i] == '_':
				state = TEXT_PARSER_UNDER_UNDER_UNDER
			elif x[i] == '*':
				state = TEXT_PARSER_UNDER_UNDER_STAR
			else:
				content = x[i]
				state = TEXT_PARSER_UNDER_UNDER_TEXT
		elif state == TEXT_PARSER_UNDER_STAR:
			if x[i] == '*':
				state = TEXT_PARSER_UNDER_STAR_STAR
			else:
				# _*x - we give up
				r += '_'
				state = TEXT_PARSER_STAR
				continue
		elif state == TEXT_PARSER_STAR:
			if x[i] == '*':
				state = TEXT_PARSER_STAR_STAR
			elif x[i] == '_':
				state = TEXT_PARSER_STAR_UNDER
			else:
				content += x[i]
				state = TEXT_PARSER_STAR_TEXT
		elif state == TEXT_PARSER_UNDER_UNDER_UNDER:
			if x[i] == '_':
				# give up the first underscore, keep at three
				r += '_'
			else:
				content = x[i]
				state = TEXT_PARSER_UNDER_UNDER_UNDER_TEXT
		elif state == TEXT_PARSER_UNDER_UNDER_UNDER_TEXT:
			if x[i] == '_':
				state = TEXT_PARSER_UNDER_UNDER_UNDER_TEXT_U
			else:
				content += x[i]
		elif state == TEXT_PARSER_UNDER_UNDER_UNDER_TEXT_U:
			if x[i] == '_':
				state = TEXT_PARSER_UNDER_UNDER_UNDER_TEXT_UU
			else:
				r += f'__<em>{content}</em>'
				state = TEXT_PARSER_NORMAL
				continue
		elif state == TEXT_PARSER_UNDER_UNDER_UNDER_TEXT_UU:
			if x[i] == '_':
				r += f'<strong><em>{content}</em></strong>'
				state = TEXT_PARSER_NORMAL
			else:
				r += f'_<strong>{content}</strong>'
				state = TEXT_PARSER_NORMAL
				continue
		else:
			# should be empty
			r += x[i]
		i += 1
	# print(f'[*] TEXT_PARSER_{state}: "{x[:i]}•{x[i:]}"')
	# aftermath
	if state == TEXT_PARSER_STAR:
		r += '*'
	elif state == TEXT_PARSER_STAR_STAR:
		r += '**'
	elif state == TEXT_PARSER_STAR_STAR_TEXT:
		r += f'**{content}'
	elif state == TEXT_PARSER_STAR_STAR_TEXT_STAR:
		r += f'*<em>{content}</em>'
	elif state == TEXT_PARSER_STAR_TEXT:
		r += f'*{content}'
	elif state == TEXT_PARSER_STAR_UNDER:
		r += '*_'
	elif state == TEXT_PARSER_TICK:
		r += f'`{content}'
	elif state == TEXT_PARSER_UNDER:
		r += '_'
	elif state == TEXT_PARSER_UNDER_STAR:
		r += '_*'
	elif state == TEXT_PARSER_UNDER_STAR_STAR:
		r += '_**'
	elif state == TEXT_PARSER_UNDER_TEXT:
		r += f'_{content}'
	elif state == TEXT_PARSER_UNDER_UNDER:
		r += '__'
	elif state == TEXT_PARSER_UNDER_UNDER_STAR:
		r += '__*'
	elif state == TEXT_PARSER_UNDER_UNDER_TEXT:
		r += f'__{content}'
	elif state == TEXT_PARSER_UNDER_UNDER_TEXT_UNDER:
		r += f'_<em>{content}</em>'
	elif state == TEXT_PARSER_UNDER_UNDER_UNDER:
		r += '___'
	elif state == TEXT_PARSER_UNDER_UNDER_UNDER_TEXT:
		r += f'___{content}'
	elif state == TEXT_PARSER_UNDER_UNDER_UNDER_TEXT_U:
		r += f'__<em>{content}</em>'
	elif state == TEXT_PARSER_UNDER_UNDER_UNDER_TEXT_UU:
		r += f'_<strong>{content}</strong>'
	return r
