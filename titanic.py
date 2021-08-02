#!/Users/grammarware/opt/anaconda3/bin/python
import os
from collections import OrderedDict

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

class Items(object):
	def __init__(self, lines):
		super(Items, self).__init__()
		self.items = []
		i = 0
		item_lines = []
		while i < len(lines):
			if lines[i].startswith('-'):
				if item_lines:
					self.items.append(Item(item_lines))
					item_lines = []
			item_lines.append(lines[i])
			i += 1
		if item_lines:
			self.items.append(Item(item_lines))
	def dump_to(self, file):
		for item in self.items:
			item.dump_to(file)

class Item(object):
	# -   [![](https://dblp.uni-trier.de/img/paper-oa.dark.hollow.16x16.png)](https://doi.org/10.1007/978-3-030-53288-8_30) Reachability Analysis Using Message Passing over Tree Decompositions.
	# [Sriram Sankaranarayanan](https://dblp.uni-trier.de/pid/82/1542.html)
	# Implementation of prototype has no name
	# --->
	# - [🔓](https://doi.org/10.1007/978-3-030-72013-1_12) cake\_lpr: Verified Propagation Redundancy Checking in CakeML.
	# [Yong Kiam Tan](https://dblp.org/pid/156/7492.html), [Marijn J. H. Heule](https://dblp.org/pid/h/MarijnHeule.html), [Magnus O. Myreen](https://dblp.org/pid/92/2955.html)
	# ✅ Uses [[cake_lpr]], compares to: [[ACL2]], [[Coq]], [[GRATchks]]
	def __init__(self, lines):
		super(Item, self).__init__()
		self.title = self.authors = ''
		self.lines = []
		for line in lines:
			if line.startswith('-'):
				line = line[1:].strip().replace('dblp.uni-trier.de', 'dblp.org')
			if line.find('doi.org') > -1:
				if self.title:
					warning(f'Duplicate title: "{self.title}" vs "{line}"')
				self.title = line
			elif line.find('/pid/') > -1:
				if self.authors:
					warning(f'Duplicate authors: "{self.authors}" vs "{line}"')
				self.authors = line
			else:
				# NB: looks overengineered, but is not simplifiable if we want unicode support
				line = cleanup(line, '✅')
				line = cleanup(line, '⚙️')
				line = cleanup(line, '❌')
				if not line:
					continue
				self.lines.append(line)
		if not self.title:
			warning('No title!')
		else:
			self.title = self.title.replace('[![](https://dblp.org/img/paper-oa.dark.hollow.16x16.png)]', '[🔓]')
			self.title = self.title.replace('[![](https://dblp.org/img/paper.dark.hollow.16x16.png)]', '[🔓]')
		if not self.authors:
			warning('No authors!')
		else:
			self.authors = self.authors.replace('dblp.uni-trier.de', 'dblp.org')
			while self.authors.find('![](https://dblp.org/img/orcid-mark.12x12.png') > -1:
				# ![](https://dblp.org/img/orcid-mark.12x12.png "0000-0002-5143-9764")
				start = self.authors.index('![](https://dblp.org/img/orcid-mark.12x12.png')
				end = self.authors.index('")', start) + 2
				self.authors = self.authors[:start] + self.authors[end:]
	def dump_to(self, file):
		file.write(f'-\t{self.title}\n')
		file.write(f'\t{self.authors}\n')
		if self.lines:
			for line in self.lines:
				if line == 'None':
					file.write(f'\t❌ {line}\n')
				elif (line.startswith('[[') and line.endswith(']]') and line.find(' ') < 0) \
				  or (line.startswith('Tool: [[') and line.endswith(']]') and line.find(' ', 5) < 0):
					file.write(f'\t✅ Presents {line}\n')
				elif line.startswith('Introduces '):
					file.write(f"\t✅ {line.replace('Introduces', 'Presents')}\n")
				else:
					file.write(f'\t✅ {line}\n')
		else:
			file.write(f'\t⚙️\n')

class Conference(object):
	def __init__(self, name):
		super(Conference, self).__init__()
		self.sections = OrderedDict()
		self.tags = []
		self.title = ''
		seen_title = False
		cur_subtitle = ''
		cx_subsections = cx_lines = 0
		with open(name, 'r', encoding='utf-8') as file:
			for line in file.readlines():
				line = line.strip()
				if not line or line == '---':
					continue
				if len(line) > 2 and line[0] == '#' and line[1] not in ('#', ' '):
					self.tags.append(line)
				elif line.startswith('## '):
					if seen_title:
						warning('Duplicate title in ' + name)
					seen_title = True
					self.title = line[3:].strip()
				elif line.startswith('### '):
					cur_subtitle = line[4:].strip()
					if cur_subtitle in self.sections.keys():
						warning('Duplicate section in ' + name)
					else:
						self.sections[cur_subtitle] = []
						cx_subsections += 1
				else:
					if cur_subtitle not in self.sections.keys():
						warning('Implicit section')
						self.sections[cur_subtitle] = []
					self.sections[cur_subtitle].append(line)
					cx_lines += 1
		info(f'{name} titled "{self.title}"; {cx_subsections} sections; {cx_lines} lines')
		# NB: type elevation
		for section in self.sections.keys():
			self.sections[section] = Items(self.sections[section])
	def dump_to(self, name):
		with open(name, 'w', encoding='utf-8') as file:
			file.write(f'## {self.title}\n')
			for tag in self.tags:
				file.write(tag + '\n')
			file.write('---\n')
			for section in self.sections.keys():
				if section:
					file.write(f'### {section}\n')
				self.sections[section].dump_to(file)
		info(f'{name} dumped')

# https://dblp.org/img/orcid-mark.12x12.png
files = {}
for filename in os.listdir('Conferences.old'):
	if filename.endswith(".md"): 
		files[filename] = Conference(os.path.join('Conferences.old', filename))
		files[filename].dump_to(os.path.join('Conferences', filename))
		continue
	else:
		continue