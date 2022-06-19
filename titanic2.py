#!/usr/local/bin/python3
import os
from collections import OrderedDict
from pathlib import Path
import proverb
from hyper import *
import sys

cx = 0


SECTION_MET = 'Meta'
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
		global cx
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
				# line = line.strip()
				if line.startswith('#### '):
					cur_section = line[5:].strip()
					if cur_section.endswith(':'):
						cur_section = cur_section[:-1]
					if cur_section in self.sections.keys():
						error(f'Duplicate section titled {cur_section}')
					if cur_section != SECTION_MET:
						self.sections[cur_section] = []
					continue
				if cur_section == SECTION_MET:
					if not line.strip():
						continue
					tmp = line.split('::')
					if len(tmp) == 2:
						tag = tmp[1].strip()
						desc = ''
					elif len(tmp) == 3:
						tag = tmp[1].strip()
						desc = tmp[2].strip()
					else:
						error(f'Unintelligible meta entry {line}')
					# deal with all kinds of tags
					cx += 1
					if tag.lower() == 'no pv':
						# beyond PV-classification
						self.rank = -1
						continue
					if tag.startswith('PV'):
						# PV level
						self.rank = int(tag[2])
						self.subtitle = desc
						indices[tag.lower()].append(make_link(get_key(self.name)+'.html', self.name, why=desc))
						continue
					# other tags
					tag_key = get_key(tag)
					self.add_tag(tag_key, tag, desc)
					if tag_key not in indices:
						indices[tag_key] = []
						name_by_index[tag_key] = tag
						indices['tags'].append(make_link(tag_key+'.html', tag))
						if tag_key in tag_by_key:
							if tag_by_key[tag_key].check_for('Name'):
								indices['tags'][-1] += ' — ' + tag_by_key[tag_key].sections['Name'][0]
					indices[tag_key].append(make_link(get_key(self.name)+'.html', self.name, why=desc))
					continue
				self.sections[cur_section].append(line.rstrip())
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
					tag_by_key, \
					self.markdown_to_html1(), \
					self.markdown_to_html2())
			file.write(p.dump())
		# info(f'{self.name} dumped')
	def check_for(self, section_name):
		return section_name in self.sections \
			and len(self.sections[section_name]) > 0 \
			and self.sections[section_name][0]!='?' \
			and self.sections[section_name][0]!='-' \
			and self.sections[section_name][0]!=''
	def markdown_to_html1(self):
		lines = []
		if self.check_for(SECTION_GEN):
			# usually the only one, for unfilled templates
			lines.append(md2html(self.sections[SECTION_GEN]))
		if self.check_for(SECTION_ADF):
			lines.append(h3(SECTION_ADF))
			lines.append(ul(self.sections[SECTION_ADF]))
		if self.check_for(SECTION_TOT):
			lines.append(h3(SECTION_TOT_))
			lines.append(ul(self.sections[SECTION_TOT]))
		if self.check_for(SECTION_EIT) or self.check_for(SECTION_EIF):
			lines.append(h3(SECTION_EI_))
			if self.check_for(SECTION_EIT):
				lines.append(md2html(self.sections[SECTION_EIT]))
			if self.check_for(SECTION_EIF):
				lines.append('<p>Format:</p>')
				lines.append(md2html(self.sections[SECTION_EIF]))
		if self.check_for(SECTION_EO_):
			lines.append(h3(SECTION_EO_))
			lines.append(md2html(self.sections[SECTION_EO_]))
		if self.check_for(SECTION_ITU):
			lines.append(h3(SECTION_I__))
			lines.append(md2html(self.sections[SECTION_ITU]))
		if self.check_for(SECTION_COM):
			lines.append(h3(SECTION_COM))
			lines.append(md2html(self.sections[SECTION_COM]))
		return '\n'.join(lines)
	def markdown_to_html2(self):
		lines = []
		if self.check_for(SECTION_URI):
			lines.append(h4(SECTION_URI_))
			lines.append(ul(self.sections[SECTION_URI]))
		if self.check_for(SECTION_LCD):
			lines.append(h4(SECTION_LCD))
			lines.append(ul(self.sections[SECTION_LCD]))
		if self.check_for(SECTION_LRP):
			lines.append(h4("Related papers"))
			lines.append(ul(self.sections[SECTION_LRP]))
		if self.check_for(SECTION_LPD):
			lines.append(h4(SECTION_LPD))
			lines.append(ul(self.sections[SECTION_LPD]))
		if self.check_for(SECTION_RTT):
			lines.append(h4(SECTION_RT_))
			lines.append(ul(self.sections[SECTION_RTT]))
		lines.append(h4('ProVerB specific'))
		return '\n'.join(lines)

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
tag_by_key = {}
tag_by_name = {}
indices = {}
name_by_index = {}

indices['all'] = []
name_by_index['all'] = 'All tools'
indices['tags'] = []
name_by_index['tags'] = 'All tags'
for i in range(0,7):
	indices[f'pv{i}'] = []
	name_by_index[f'pv{i}'] = f'PV{i} tools'

for filename in os.listdir(sys.argv[1]):
	if filename.endswith(".html"):
		EXISTENCE.add(filename)

traverse_dir('Tags', tag_by_key, tag_by_name)
traverse_dir('Tools', item_by_key, item_by_name)
traverse_dir('Formats', item_by_key, item_by_name)

info(f'{cx} facts are known!')

for f in item_by_key:
	item_by_key[f].dump_to(os.path.join(sys.argv[1], f + '.html'))
	indices['all'].append(make_link(f+'.html', item_by_key[f].name))
	if item_by_key[f].rank == 0 and not item_by_key[f].subtitle:
		indices['pv0'].append(make_link(f+'.html', item_by_key[f].name))

for index in indices:
	with open(os.path.join(sys.argv[1], index + '.html'), 'w', encoding='utf-8') as file:
		lst = [f'<li>{item}</li>' for item in sorted(indices[index])]
		text = ''
		if index in tag_by_key:
			if tag_by_key[index].check_for(SECTION_GEN):
				text += '\n'.join(tag_by_key[index].sections[SECTION_GEN])
			if tag_by_key[index].check_for(SECTION_URI):
				text += '\n' + h4(SECTION_URI_)
				text += '\n' + ul(tag_by_key[index].sections[SECTION_URI])
				text += '\n' + h3('Tools')
		text += '<ul>\n' + '\n'.join(lst) + '\n</ul>'
		file.write(proverb.IndexPage(name_by_index[index], len(lst), text).dump())
info(f'{len(indices)} indices generated!')

with open('index.html', 'r', encoding='utf-8') as ifile:
	with open(os.path.join(sys.argv[1], 'index.html'), 'w', encoding='utf-8') as ofile:
		for line in ifile.readlines():
			if line.startswith('<<PV_TEXT$'):
				PV_text = tag_by_key[f'pv{int(line.split("$")[1])}'].sections[SECTION_GEN]
				ofile.write('\n'.join(PV_text)[4:] + '\n')
			else:
				ofile.write(line)
