#!/Users/grammarware/opt/anaconda3/bin/python

from collections import OrderedDict
from hyper import *
import datetime

TEMPLATE = '''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html version="-//W3C//DTD XHTML 1.1//EN"
			xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
			xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
			xsi:schemaLocation="http://www.w3.org/1999/xhtml
													http://www.w3.org/MarkUp/SCHEMA/xhtml11.xsd">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta name="viewport" content="initial-scale=1.0"/>
		<title>{title} — ProVerB — SLEBoK</title>
		<link href="main.css" rel="stylesheet" type="text/css" />
		<script type="text/javascript">
			var _gaq = _gaq || [];
			_gaq.push(['_setAccount', 'UA-3743366-7']);
			_gaq.push(['_setDomainName', 'github.io']);
			_gaq.push(['_setAllowLinker', true]);
			_gaq.push(['_trackPageview']);
			(function() {{
				var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
				ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
				var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
			}})();
		</script>
	</head>
	<body>
		<div class="left">
			<div class="logo">
				<a href="index.html"><img src="proverb.png" alt="ProVerB"/></a>
				<h3>Program<br/>Verification<br/>Book</h3>
			</div>
			<nav>
				<ul style="margin: 0;padding: 0;">
					<li>
						<a href="index.html">Homepage</a>
					</li>
					<li>
						<a href="all.html">All tools</a>
					</li>
					<ul>
						
					<li>
							<a href="pv0.html" title="unprocessed/nonverifying">PV0</a>
						</li><li>
							<a href="pv1.html" title="solvers/linters">PV1</a>
						</li><li>
							<a href="pv2.html" title="synthesisers">PV2</a>
						</li><li>
							<a href="pv3.html" title="property checkers">PV3</a>
						</li><li>
							<a href="pv4.html" title="monoverifiers">PV4</a>
						</li><li>
							<a href="pv5.html" title="spec compilers">PV5</a>
						</li><li>
							<a href="pv6.html" title="proof assistants">PV6</a>
						</li><li>
							<a href="framework.html">Frameworks</a>
						</li></ul>
					<li>
							<a href="tags.html">Tags</a>
						</li><li>
							<a href="specificationformat.html">Specification formats</a>
						</li><li>
						<a href="credits.html">About</a>
					</li>
				</ul>
			</nav>
		</div>
		<div class="main">
			{tabs}
		</div>
		<br/><hr/>
		<div class="f">
			<a href="help.html">ProVerB</a> is a part of <a href="https://slebok.github.io/">SLEBoK</a>.
			Last updated: <strong>{last_updated}</strong>.{source}
		</div>
	</body>
</html>
'''

class Page(object):
	def __init__(self, t, src):
		super(Page, self).__init__()
		self.title = t
		self.tabs = OrderedDict()
		self.src = src
	def dump(self):
		tabber = ''
		for tab in self.tabs:
			if (tab == 'Tool'):
				tabber += f'<div class="tool-info">{self.tabs[tab]}</div>'
			elif (tab == 'Meta'):
				tabber += f'<div class="meta-info">{self.tabs[tab]}</div>'
			else:
				tabber += f'<div class="tabbertab">{self.tabs[tab]}</div>'
		return TEMPLATE.format(title=self.title, tabs=tabber, source=self.src,\
			last_updated=datetime.datetime.now().strftime('%B %Y'))

class ToolPage(Page):
	def __init__(self, fn, t, ft, st, rank, tags, tags_by_key, c1, c2, src):
		super(ToolPage, self).__init__(t, src)
		self.filename = fn
		# construct the title
		if rank < 0:
			FULL_TITLE = f'<h1 class="fbs">{ft}'
		else:
			FULL_TITLE = f'<h1 class="fbs"><span class="pv"><a href="pv{rank}.html">PV{rank}</a> ⊧</span> {ft}'
		if st:
			FULL_TITLE += f'<span class="subtitle">{st}</span>'
		FULL_TITLE += '</h1>'
		# construct tag links
		TAGS = '<div>' + '\n'.join([self.format_tag(t, tags, tags_by_key) for t in sorted(tags)]) + '</div>'
		EDITLINK = '<p>' + make_link('https://github.com/Sophietje/Verification-Tool-Overview/blob/main/'+self.filename, 'View/edit source', why='Markdown') + '</p>'
		self.tabs['Tool'] = FULL_TITLE + c1
		self.tabs['Meta'] = TAGS + c2 + EDITLINK
	def format_tag(self, t, tags1, tags2):
		hover = tags1[t][1]
		if not hover and t in tags2 and tags2[t].check_for('Name'):
			hover = tags2[t].sections['Name'][0]
		return f'<span class="tag">{make_link(t+".html", tags1[t][0], hover=hover)}</span>'

class IndexPage(Page):
	def __init__(self, cat, size, lst):
		super(IndexPage, self).__init__('Index', '')
		if cat.endswith('</span>'):
			i = cat.index('<span')
			FULL_TITLE = f'<h1 class="fbs">{cat[:i]} in ProVerB{cat[i:]}</h1>'
		else:
			FULL_TITLE = f'<h1 class="fbs">{cat} in ProVerB</h1>'
		self.tabs['Index'] = FULL_TITLE + lst + f'\n<p>{size} items on this list.</p>'
