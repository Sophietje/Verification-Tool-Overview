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
		<title>{title}</title>
		<link href="main.css" rel="stylesheet" type="text/css" />
		<link href="tabber.css" rel="stylesheet" type="text/css" media="screen" />
		<script type="text/javascript" src="tabber.js" />
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
		<div class="top">
			<div class="pvs">
				<h1>
					<span class="tag"><a href="pv0.html" title="unprocessed">PV0</a></span>
					<span class="tag"><a href="pv1.html" title="solvers/linters">PV1</a></span>
					<span class="tag"><a href="pv2.html" title="property checkers">PV2</a></span>
					<span class="tag"><a href="pv3.html" title="monoverifiers">PV3</a></span>
					<span class="tag"><a href="pv4.html" title="spec compilers">PV4</a></span>
					<span class="tag"><a href="pv5.html" title="proof assistants">PV5</a></span>
				</h1>
			</div>
		</div>
		<div class="left">
			<a href="index.html"><img src="proverb.png" alt="ProVerB"/></a>
			<h1>ProVerB:</h1>
			<h2>Program<br/>Verification<br/>Book</h2>

			<p>
				<a href="index.html">Top</a><br/>
				<a href="tags.html">Tags</a><br/>
				<a href="index.html">Search</a><br/>
				<br/>
				<a href="framework.html">Frameworks</a><br/>
				<a href="format.html">Formats</a><br/>
				<br/>
				<a href="https://github.com/Sophietje/Verification-Tool-Overview/">Backend repo</a><br/>
				<a href="https://github.com/slebok/slebok.github.io/tree/master/proverb">Frontend repo</a><br/>
				<br/>
				<a href="help.html">Help</a><br/>
			</p>
		</div>
		<div class="main">
		<div class="tabber">
			{tabs}
		</div>
		<br/><hr/>
		<div class="f">
			<a href="help.html">ProVerB</a> is a part of <a href="https://slebok.github.io/">SLEBoK</a>.
			Last updated: <strong>{last_updated}</strong>.
		</div>
	</div>
	</body>
</html>
'''

class Page(object):
	def __init__(self, t):
		super(Page, self).__init__()
		self.title = t
		self.tabs = OrderedDict()
	def dump(self):
		tabber = ''
		for tab in self.tabs:
			tabber += f'<div class="tabbertab"><h2>{tab}</h2>{self.tabs[tab]}</div>'
		return TEMPLATE.format(title=self.title, tabs=tabber, last_updated=datetime.datetime.now().strftime('%B %Y'))

class ToolPage(Page):
	def __init__(self, fn, t, ft, st, rank, tags, c1, c2):
		super(ToolPage, self).__init__(t)
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
		TAGS = '<div>' + '\n'.join([f'<span class="tag">{make_link(t+".html", tags[t][0], hover=tags[t][1])}</span>'\
				for t in sorted(tags)]) + '</div>'
		EDITLINK = '<ul><li>' + make_link('https://github.com/Sophietje/Verification-Tool-Overview/blob/main/'+self.filename, 'View/edit source', why='Markdown')+'</li></ul>'
		self.tabs['Tool'] = TAGS + FULL_TITLE + c1
		self.tabs['Meta'] = TAGS + c2 + EDITLINK

class IndexPage(Page):
	def __init__(self, cat, size, lst):
		super(IndexPage, self).__init__('Index')
		FULL_TITLE = f'<h1 class="fbs">{cat} in ProVerB</h1>'
		self.tabs['Index'] = FULL_TITLE + lst + f'<p>{size} tools in this list.</p>'
