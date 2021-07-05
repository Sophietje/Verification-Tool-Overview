#!/Users/grammarware/opt/anaconda3/bin/python
import os
from collections import OrderedDict

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

class Conference(object):
	def __init__(self, name):
		super(Conference, self).__init__()
		self.sections = OrderedDict()
		self.title = ''
		seen_title = False
		cur_subtitle = ''
		cx_subsections = cx_lines = 0
		with open(name, 'r', encoding='utf-8') as file:
			for line in file.readlines():
				line = line.strip()
				if not line:
					continue
				if line.startswith('## '):
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
	def dump_to(self, name):
		with open(name, 'w', encoding='utf-8') as file:
			file.write(f'## {self.title}\n')
			file.write('---\n')
			for section in self.sections.keys():
				if section:
					file.write(f'### {section}\n')
				for line in self.sections[section]:
					file.write(line + '\n')
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