#!/Users/grammarware/opt/anaconda3/bin/python

from collections import OrderedDict
from hyper import *
import datetime

PV_text = (\
	'manipulate given and produced software artefacts with some degree of rigour. Conceptually such artefacts then may correspond to mathematical and formal entities, but this correspondence is mostly a matter of expectations. This category should be reasonably unpopulated since we mostly avoid to include such tools here.',
	'encode the formal expectations about the artefacts that they manipulate, and report back to their users about found inconsistencies. A typical resident of this level could be a linter: a tool that analyses your program and complains about places where your program does not conform to its expectations.',
	'?',
	'allow the end user to control the properties that are being checked. For instance, it could be a tool that analyses user-written assertions in the code and verifies that they are indeed always respected by the program.',
	'operate within a particular paradigm and derive their actions, conclusions and even properties that they need to check, from a built-in formal specification. For example, such a tool can guarantee freedom of deadlocks in a multi-threaded application, or data consistency in a database management system. Either the specification or the property set is fixed for tools of this level.',
	'allow the end user to write their own specifications and “compile” them to fully formal mathematical representations that can be combined with mathematical representations of programs themselves or their desired properties, and verified together. Such a tool can already help someone make claims and guarantees about correctness, complexity or predicted performance of a novel, previously non-existing, garbage collection algorithm. Some of PV4 tools focus on synthesising a software artefact that satisfies the desired conditions, instead of checking an existing one for conformance.',
	'can handle different user-written specifications, encode a wide range of different formulae for properties, and are capable of producing proofs of such properties together with inferring the correctness of such proofs.'
	)

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
              <a href="pv0.html" title="unprocessed">PV0</a>
            </li><li>
              <a href="pv1.html" title="solvers/linters">PV1</a>
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
              <a href="language.html">Languages</a>
            </li><li>
            <a href="credits.html">About</a>
          </li>
        </ul>
      </nav>
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
		self.tabs['Index'] = FULL_TITLE + lst + f'\n<p>{size} items on this list.</p>'
