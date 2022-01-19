#!/Users/grammarware/opt/anaconda3/bin/python

from collections import OrderedDict
from hyper import *

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
					<span class="tag"><a href="pv0.html">PV0</a></span>
					<span class="tag"><a href="pv1.html">PV1</a></span>
					<span class="tag"><a href="pv2.html">PV2</a></span>
					<span class="tag"><a href="pv3.html">PV3</a></span>
					<span class="tag"><a href="pv4.html">PV4</a></span>
					<span class="tag"><a href="pv5.html">PV5</a></span>
				</h1>
			</div>
		</div>
		<div class="left">
			<img src="proverb.png" alt="ProVerB"/>
			<h1>ProVerB:</h1>
			<h2>Program<br/>Verification<br/>Book</h2>

			<p>
				<a href="index.html">Top</a><br/>
				<a href="tags.html">Tags</a><br/>
				<a href="index.html">Search</a><br/>
				<br/>
				<a href="index.html">Frameworks</a><br/>
				<a href="index.html">Checkers</a><br/>
				<a href="index.html">Provers</a><br/>
				<br/>
				<a href="index.html">Related</a><br/>
				<a href="index.html">Links here</a><br/>
				<a href="index.html">Edit source</a><br/>
				<br/>
				<a href="index.html">Help</a><br/>
			</p>
		</div>
		<div class="main">
		<div class="tabber">
			{tabs}
		</div>
		<br/><hr/>
		<div class="f">
			<!-- FMT logo? -->
			The page is maintained by <a href="http://grammarware.github.io/">Dr. Vadim Zaytsev</a> a.k.a. @<a href="http://grammarware.net">grammarware</a> from University of Twente.<br/>
			The tabber code used on this page, is derivative from <a href="http://www.kean.edu/~gkolodiy/5223/tabber.html">the one made by Patrick Fitzgerald</a> and distributed under <a href="https://opensource.org/licenses/mit-license.php">the MIT license</a>.<br/>
			The open book logo is by <a href="https://commons.wikimedia.org/wiki/File:Open_Book_icon.svg">Icon Lauk</a> from the <a href="https://thenounproject.com/icon/open-book-2238057/">Noun Project</a>, CC-BY 2018.<br/>
			All other referenced works of art, science and engineering, are subject to their own individual copyrights.<br/>
			Last updated: <strong>January 2022</strong>.
		</div>
	</div>
	</body>
</html>
'''

# TODO
EDITLINK = '''
				<ul>
					<li><a href="https://github.com/Sophietje/Verification-Tool-Overview/">View/edit source</a> (Markdown)</li>
				</ul>
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
		return TEMPLATE.format(title=self.title, tabs=tabber)

class ToolPage(Page):
	def __init__(self, t, ft, st, rank, tags, c1, c2):
		super(ToolPage, self).__init__(t)
		# construct the title
		FULL_TITLE = f'<h1 class="fbs"><span class="pv"><a href="pv{rank}.html">PV{rank}</a> ⊧</span> {ft}'
		if st:
			FULL_TITLE += f'<span class="subtitle">{st}</span>'
		FULL_TITLE += '</h1>'
		# construct tag links
		TAGS = '<div>' + '\n'.join([f'<span class="tag">{make_link(t, tags[t][0], hover=tags[t][1])}</span>'\
				for t in tags]) + '</div>'
		self.tabs['Tool'] = TAGS + FULL_TITLE + c1
		self.tabs['Meta'] = TAGS + c2 + EDITLINK

class IndexPage(Page):
	def __init__(self, cat, lst):
		super(IndexPage, self).__init__('Index')
		FULL_TITLE = f'<h1 class="fbs">{cat} in ProVerB</h1>'
		self.tabs['Index'] = FULL_TITLE + lst
