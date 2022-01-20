#!/Users/grammarware/opt/anaconda3/bin/python

import markdown2

def md2html_generic(md_lines):
	return markdown2.markdown('\n'.join(md_lines))

def md2html(md_lines):
	ret_lines = []
	IN_LIST = False
	for line in md_lines:
		if IN_LIST:
			if line.startswith('- ') or line.startswith('* '):
				ret_lines.append(li(line[2:].strip()))
			else:
				ret_lines.append('</ul>')
				ret_lines.append(my_md_converter(line.strip()))
				IN_LIST = False
		else:
			if line.startswith('- ') or line.startswith('* '):
				ret_lines.append('<ul>')
				ret_lines.append(li(line[2:].strip()))
				IN_LIST = True
			else:
				ret_lines.append(my_md_converter(line.strip()))
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
	return x

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
				r += f'<a href="{get_key(where)}.html">{where}</a>'
				state = LINK_PARSER_IMPLICIT_PRIME
			else:
				where += x[i]
		elif state == LINK_PARSER_IMPLICIT_PRIME:
			if x[i] == ']':
				state = LINK_PARSER_NORMAL
			else:
				print(f'ERROR IN LINK: {x} --- unmatched [[')
				return x
		elif state == LINK_PARSER_EXPLICIT:
			if x[i] == ']':
				state = LINK_PARSER_EXPLICIT_PRIME
			else:
				where += x[i]
		elif state == LINK_PARSER_EXPLICIT_PRIME:
			if x[i] == '(':
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
				# theoretically we could collect targets for verification, but we don't need this data
				pass
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
				return x
		i += 1
	return r