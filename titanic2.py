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
	for p in {'τ':'tau', 'é':'e', '+':'plus', '*':'star'}.items():
		fn = fn.replace(p[0], p[1])
	fn = fn.replace('τ', 'tau').replace('é', 'e')
	return fn

class Item(object):
	def __init__(self, name):
		super(Item, self).__init__()
		self.sections = OrderedDict()
		self.tags = []
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
	def dump_to(self, filename):
		# info(f'{filename} with {self.sections.keys()} being dumped...')
		with open(filename, 'w', encoding='utf-8') as file:
			p = proverb.ToolPage(self.name, self.sections['Name'][0], self.subtitle, self.rank,\
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

item_by_key = {}
item_by_name = {}
traverse_dir('Tools', item_by_key, item_by_name)

PV = [[],[],[],[],[],[]]
explanations = {} # overengineered?
with open('facts.lst', 'r', encoding='utf-8') as file:
	for line in file.readlines():
		if line.find('|=') > -1:
			name = line[line.index('|=')+2:line.index('{')].strip()
			rank = int(line[2])
			tmp = line.split('{')
			xpln = tmp[1].split('}')[0].strip()
			# expressway
			item_by_name[name].rank = rank
			item_by_name[name].subtitle = xpln
			# long term overengineered storage
			PV[rank].append(name)
			explanations[tmp[0].strip()] = xpln
		else:
			warning(f'Skipped fact {line}')
info(f'{len(explanations)} facts are known!')

full_list = []
for f in item_by_key:
	item_by_key[f].dump_to(os.path.join('www', f + '.html'))
	full_list.append(f'<a href="{f}.html">{item_by_key[f].name}</a>')

with open(os.path.join('www', 'index.html'), 'w', encoding='utf-8') as file:
	lst = [f'<li>{item}</li>' for item in sorted(full_list)]
	file.write(proverb.IndexPage('<ul>' + '\n'.join(lst) + '</ul>').dump())
