#!/Users/grammarware/opt/anaconda3/bin/python
import os
from collections import OrderedDict
from pathlib import Path
import proverb
from hyper import *

def check_for(sections, section_name):
	return section_name in sections \
		and len(sections[section_name]) > 0 \
		and sections[section_name][0]!='?' \
		and sections[section_name][0]!='-' \
		and sections[section_name][0]!=''

SECTION_GEN = 'General'
SECTION_ADF = 'Application domain/field'
SECTION_TOT = 'Type of tool (e.g. model checker, test generator)'
SECTION_TOT_= 'Type of tool'
SECTION_EIT = 'Expected input thing'
SECTION_EIF = 'Expected input format'
SECTION_EI_ = 'Expected input'
SECTION_EO_ = 'Expected output'
SECTION_ITU = 'Internals (tools used, frameworks, techniques, paradigms, ...)'
SECTION_I__ = 'Internals'
SECTION_COM = 'Comments'
SECTION_URI = 'URIs (github, websites, etc.)'
SECTION_URI_= 'Links'
SECTION_LCD = 'Last commit date'
SECTION_LPD = 'Last publication date'
SECTION_LRP = 'List of related papers'
SECTION_RTT = 'Related tools (tools mentioned or compared to in the paper)'
SECTION_RT_ = 'Related tools'
def markdown_to_html1(sections):
	lines = []
	if check_for(sections, SECTION_GEN):
		# usually the only one, for unfilled templates
		lines.append(ul(sections[SECTION_GEN]))
	if check_for(sections, SECTION_ADF):
		lines.append(h3(SECTION_ADF))
		lines.append(ul(sections[SECTION_ADF]))
	if check_for(sections, SECTION_TOT):
		lines.append(h3(SECTION_TOT_))
		lines.append(ul(sections[SECTION_TOT]))
	if check_for(sections, SECTION_EIT) or check_for(sections, SECTION_EIF):
		lines.append(h3(SECTION_EI_))
		if check_for(sections, SECTION_EIT):
			lines.append(md2html_generic(sections[SECTION_EIT]))
		if check_for(sections, SECTION_EIF):
			lines.append('Format:')
			lines.append(md2html_generic(sections[SECTION_EIF]))
	if check_for(sections, SECTION_EO_):
		lines.append(h3(SECTION_EO_))
		lines.append(ul(sections[SECTION_EO_]))
	if check_for(sections, SECTION_ITU):
		lines.append(h3(SECTION_I__))
		lines.append(md2html_generic(sections[SECTION_ITU]))
	if check_for(sections, SECTION_COM):
		lines.append(h3(SECTION_COM))
		lines.append(md2html(sections[SECTION_COM]))
	return '\n'.join(lines)

def markdown_to_html2(sections):
	lines = []
	if check_for(sections, SECTION_URI):
		lines.append(h3(SECTION_URI_))
		lines.append(ul(sections[SECTION_URI]))
	if check_for(sections, SECTION_LCD):
		lines.append(h3(SECTION_LCD))
		lines.append(ul(sections[SECTION_LCD]))
	if check_for(sections, SECTION_LPD):
		lines.append(h3(SECTION_LPD))
		lines.append(ul(sections[SECTION_LPD]))
	if check_for(sections, SECTION_LRP):
		lines.append(h3(SECTION_LRP))
		lines.append(ul(sections[SECTION_LRP]))
	if check_for(sections, SECTION_RTT):
		lines.append(h3(SECTION_RT_))
		lines.append(ul(sections[SECTION_RTT]))
	lines.append(h3('ProVerB specific'))
	return '\n'.join(lines)

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

class Item(object):
	def __init__(self, name):
		super(Item, self).__init__()
		self.sections = OrderedDict()
		self.tags = {}
		self.title = ''
		self.subtitle = ''
		self.name = Path(name).stem
		self.filename = name
		self.rank = 0 # default, rewrite with a fact
		cx_subsections = cx_lines = 0
		with open(name, 'r', encoding='utf-8') as file:
			cur_section = SECTION_GEN
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
	def add_tag(self, key, tag, desc):
		self.tags[key] = (tag, desc)
	def dump_to(self, filename):
		# info(f'{filename} with {self.sections.keys()} being dumped...')
		with open(filename, 'w', encoding='utf-8') as file:
			p = proverb.ToolPage(\
					self.filename,
					self.name, \
					self.sections['Name'][0], \
					self.subtitle, \
					self.rank, \
					self.tags, \
					markdown_to_html1(self.sections), \
					markdown_to_html2(self.sections))
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
			indices[tag.lower()].append(make_link(get_key(name)+'.html', name, why=desc))
			continue
		tag_key = get_key(tag)
		item_by_name[name].add_tag(tag_key, tag, desc)
		if tag_key not in indices:
			indices[tag_key] = []
			name_by_index[tag_key] = tag
			indices['tags'].append(make_link(tag_key+'.html', tag))
		indices[tag_key].append(make_link(get_key(name)+'.html', name, why=desc))

info(f'{cx} facts are known!')

for f in item_by_key:
	item_by_key[f].dump_to(os.path.join('www', f + '.html'))
	indices['index'].append(make_link(f+'.html', item_by_key[f].name))
	if item_by_key[f].rank == 0:
		indices['pv0'].append(make_link(f+'.html', item_by_key[f].name))

for index in indices:
	with open(os.path.join('www', index + '.html'), 'w', encoding='utf-8') as file:
		lst = [f'<li>{item}</li>' for item in sorted(indices[index])]
		file.write(proverb.IndexPage(name_by_index[index], len(lst), '<ul>' + '\n'.join(lst) + '</ul>').dump())
info(f'{len(indices)} indices generated!')