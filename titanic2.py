#!/usr/local/bin/python3
import os
from collections import OrderedDict
from pathlib import Path
import proverb
from hyper import *
import sys
from terminology import *

cx = 0

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
		self.source = []
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
					elif len(tmp) >= 3 and tmp[1].strip().lower() == 'source':
						self.source.extend([make_link_from_source(part.strip()) for part in tmp[2:]])
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
						indices[tag.lower()].add(make_link(get_key(self.name)+'.html', self.name, why=desc))
						continue
					# other tags
					tag_key = get_key(tag)
					self.add_tag(tag_key, tag, desc)
					if tag_key not in indices:
						indices[tag_key] = set()
						name_by_index[tag_key] = tag
						tag_to_add = make_link(tag_key+'.html', tag)
						if tag_key in tag_by_key:
							if tag_by_key[tag_key].check_for('Name'):
								tag_to_add += ' — ' + tag_by_key[tag_key].sections['Name'][0]
						indices['tags'].add(tag_to_add)
					indices[tag_key].add(make_link(get_key(self.name)+'.html', self.name, why=desc))
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
					self._markdown_to_html1(), \
					self._markdown_to_html2(), \
					self.source)
			file.write(p.dump())
		# info(f'{self.name} dumped')
	def check_for(self, section_name):
		return section_name in self.sections \
			and len(self.sections[section_name]) > 0 \
			and self.sections[section_name][0]!='?' \
			and self.sections[section_name][0]!='-' \
			and self.sections[section_name][0]!=''
	def _markdown_to_html1(self):
		lines = []
		if self.check_for(SECTION_GEN):
			# usually the only one, for unfilled templates
			self._h3_md(lines, '', SECTION_GEN)
		if self.check_for(SECTION_ADF):
			self._h3_ul(lines, SECTION_ADF, SECTION_ADF)
		if self.check_for(SECTION_TOT):
			self._h3_ul(lines, SECTION_TOT_, SECTION_TOT)
		if self.check_for(SECTION_EIT) or self.check_for(SECTION_EIF):
			lines.append(h3(SECTION_EI_))
			if self.check_for(SECTION_EIT):
				lines.append(md2html(self.sections[SECTION_EIT]))
			if self.check_for(SECTION_EIF):
				lines.append(f'<p>{SECTION_FMT}:</p>')
				lines.append(md2html(self.sections[SECTION_EIF]))
		if self.check_for(SECTION_EO_):
			self._h3_md(lines, SECTION_EO_, SECTION_EO_)
		if self.check_for(SECTION_ITU):
			self._h3_md(lines, SECTION_I__, SECTION_ITU)
		if self.check_for(SECTION_COM):
			self._h3_md(lines, SECTION_COM, SECTION_COM)
		return '\n'.join(lines)
	def _markdown_to_html2(self):
		lines = []
		if self.check_for(SECTION_URI):
			self._h4_ul(lines, SECTION_URI_, SECTION_URI)
		if self.check_for(SECTION_LCD):
			self._h4_ul(lines, SECTION_LCD, SECTION_LCD)
		if self.check_for(SECTION_LRP):
			self._h4_ul(lines, SECTION_JRP, SECTION_LRP)
		if self.check_for(SECTION_LPD):
			self._h4_ul(lines, SECTION_LPD, SECTION_LPD)
		if self.check_for(SECTION_RTT):
			self._h4_ul(lines, SECTION_RT_, SECTION_RTT)
		return '\n'.join(lines)
	def _h4_ul(self, lines, key1, key2):
		LIST = ul(self.sections[key2])
		lines.append(h4(key1, 'hasul' if LIST.startswith('<ul>') else ''))
		lines.append(LIST)
	def _h3_ul(self, lines, key1, key2):
		if key1:
			lines.append(h3(key1))
		lines.append(ul(self.sections[key2]))
	def _h3_md(self, lines, key1, key2):
			if key1:
				lines.append(h3(key1))
			lines.append(md2html(self.sections[key2]))

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

indices['all'] = set()
name_by_index['all'] = 'All tools'
indices['tags'] = set()
name_by_index['tags'] = 'All tags'
for i in range(0,7):
	indices[f'pv{i}'] = set()
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
	indices['all'].add(make_link(f+'.html', item_by_key[f].name))
	if item_by_key[f].rank == 0 and not item_by_key[f].subtitle:
		indices['pv0'].add(make_link(f+'.html', item_by_key[f].name))

for index in indices:
	with open(os.path.join(sys.argv[1], index + '.html'), 'w', encoding='utf-8') as file:
		lst = [f'<li>{item}</li>' for item in sorted(indices[index])]
		text = ''
		title = name_by_index[index]
		if index in tag_by_key:
			title += '<span class="subtitle">' + tag_by_key[index].sections['Name'][0] + '</span>'
			if tag_by_key[index].check_for(SECTION_GEN):
				text += '\n'.join(tag_by_key[index].sections[SECTION_GEN])
			if tag_by_key[index].check_for(SECTION_URI):
				text += '\n' + h4(SECTION_URI_)
				text += '\n' + ul(tag_by_key[index].sections[SECTION_URI])
				text += '\n' + h3(SECTION_T__)
		text += '<ul>\n' + '\n'.join(lst) + '\n</ul>'
		file.write(proverb.IndexPage(title, len(lst), text).dump())
info(f'{len(indices)} indices generated!')

with open('index.html', 'r', encoding='utf-8') as ifile:
	with open(os.path.join(sys.argv[1], 'index.html'), 'w', encoding='utf-8') as ofile:
		for line in ifile.readlines():
			if line.startswith('<<PV_TEXT$'):
				PV_text = tag_by_key[f'pv{int(line.split("$")[1])}'].sections[SECTION_GEN]
				ofile.write('\n'.join(PV_text)[4:] + '\n')
			else:
				ofile.write(line)
