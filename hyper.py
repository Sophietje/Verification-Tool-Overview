#!/Users/grammarware/opt/anaconda3/bin/python

import markdown2

def clickable(http):
	if http.find('http') > -1:
		before = http[:http.index('http')]
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
	return f'<li>{clickable(x)}</li>'

def ul(items):
	if not items:
		return ''
	cuis = [i.strip() for i in items if i]
	if len(cuis) == 1:
		return clickable(cuis[0])
	if all([i.startswith('- ') for i in cuis]):
		cuis = [i[1:].strip() for i in cuis]
	return '<ul>' + '\n'.join([li(i) for i in cuis]) + '</ul>'

def md2html(md_lines):
	return markdown2.markdown('\n'.join(md_lines))

def make_link(where, what, hover='', why=''):
	if hover:
		s = f'<a href="{where}.html" title="{hover}">{what}</a>'
	else:
		s = f'<a href="{where}.html">{what}</a>'
	if why:
		s += f' ({why})'
	return s
