#!/Users/grammarware/opt/anaconda3/bin/python
import os
from collections import OrderedDict
from pathlib import Path
import proverb

def cleanup(s,c):
	return s[len(c):].strip() if s.startswith(c) else s

def red(x):
	return f'[\033[31m{x}\033[39m]'
def green(x):
	return f'[\033[32m{x}\033[39m]'
def blue(x):
	return f'[\033[34m{x}\033[39m]'
def yellow(x):
	return f'[\033[33m{x}\033[39m]'
def message(x, y):
	return f'\033[1m{x}\033[22m {y}\033[0m'

def warning(msg):
	print(message(yellow('WARN'), msg))

def info(msg):
	print(message(blue('INFO'), msg))

def error(msg):
	print(message(red('FAIL'), msg))

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

class Item(object):
	def __init__(self, name):
		super(Item, self).__init__()
		self.sections = OrderedDict()
		self.tags = {}
		self.title = ''
		self.subtitle = ''
		self.name = Path(name).stem
		self.rank = 0 # default, rewrite with a fact
		cx_subsections = cx_lines = 0
		with open(name, 'r', encoding='utf-8') as file:
			cur_section = 'General'
			self.sections[cur_section] = []
			for line in file.readlines():
				line = line.strip()
				if line.startswith('#### '):
					cur_section = line[5:].strip()
					if cur_section.endswith(':'):
						cur_section = cur_section[:-1]
					if cur_section in self.sections.keys():
						error(f'Duplicate section titled {cur_section}')
					self.sections[cur_section] = []
					continue
				self.sections[cur_section].append(line.strip())
		for key in list(self.sections.keys()):
			if not self.sections[key]:
				del self.sections[key]
		if 'Name' not in self.sections:
			# error(f'I find the lack of name disturbing')
			self.sections['Name'] = [self.name]
		# info(f'{name} titled "{self.title}"; {cx_subsections} sections; {cx_lines} lines')
		# NB: type elevation
		# for section in self.sections.keys():
		# 	self.sections[section] = Items(self.sections[section])
	def add_tag(self, key, tag, desc):
		self.tags[key] = (tag, desc)
	def dump_to(self, filename):
		# info(f'{filename} with {self.sections.keys()} being dumped...')
		with open(filename, 'w', encoding='utf-8') as file:
			p = proverb.ToolPage(\
					self.name, \
					self.sections['Name'][0], \
					self.subtitle, \
					self.rank, \
					self.tags, \
					'TEST', 'TEST2')
			file.write(p.dump())
		# info(f'{self.name} dumped')

def traverse_dir(d, by_key, by_name):
	for filename in os.listdir(d):
		if filename.startswith('README') or filename.startswith('.DS_Store'):
			continue
		if filename.endswith(".md"):
			key = get_key(filename)
			if key in by_key.keys():
				# NB: only works with duplicates, but not with 'triplicates' etc
				by_key[key + '1'] = by_key[key]
				del by_key[key]
				key = key + '2'
				error(f'Key {key} forked')
			by_key[key] = Item(os.path.join(d, filename))
			by_name[by_key[key].name] = by_key[key]
			info(f'Processed {key} from {filename}')
			continue
		elif os.path.isdir(os.path.join(d, filename)):
			warning(f'--> Descend into {filename}')
			traverse_dir(os.path.join(d, filename), by_key, by_name)
			warning(f'<-- Back from {filename}')
		else:
			warning('Not traversed ' + filename)
			continue

def make_link(where, what, why=''):
	s = f'<a href="{where}.html">{what}</a>'
	if why:
		s += f' ({why})'
	return s

item_by_key = {}
item_by_name = {}
traverse_dir('Tools', item_by_key, item_by_name)

indices = {}
name_by_index = {}

indices['index'] = []
name_by_index['index'] = 'All tools'
indices['tags'] = []
name_by_index['tags'] = 'All tags'
for i in range(0,6):
	indices[f'pv{i}'] = []
	name_by_index[f'pv{i}'] = f'PV{i} tools'

cx = 0
with open('facts.lst', 'r', encoding='utf-8') as file:
	for line in file.readlines():
		triple = [part.strip() for part in line.split('::')]
		if len(triple) == 3:
			name, tag, desc = triple
		elif len(triple) == 2:
			name, tag = triple
			desc = ''
		else:
			warning(f'Skipped fact {line}')
			continue
		cx += 1
		# deal with all kinds of tags
		if tag.startswith('PV'):
			rank = int(tag[2])
			item_by_name[name].rank = rank
			item_by_name[name].subtitle = desc
			indices[tag.lower()].append(make_link(get_key(name), name, desc))
			continue
		tag_key = get_key(tag)
		item_by_name[name].add_tag(tag_key, tag, desc)
		if tag_key not in indices:
			indices[tag_key] = []
			name_by_index[tag_key] = tag
			indices['tags'].append(make_link(tag_key, tag))
		indices[tag_key].append(make_link(get_key(name), name, desc))

info(f'{cx} facts are known!')

for f in item_by_key:
	item_by_key[f].dump_to(os.path.join('www', f + '.html'))
	indices['index'].append(make_link(f, item_by_key[f].name))

for index in indices:
	with open(os.path.join('www', index + '.html'), 'w', encoding='utf-8') as file:
		lst = [f'<li>{item}</li>' for item in sorted(indices[index])]
		file.write(proverb.IndexPage(name_by_index[index], '<ul>' + '\n'.join(lst) + '</ul>').dump())
info(f'{len(indices)} indices generated!')