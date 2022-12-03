#!/Users/grammarware/opt/anaconda3/bin/python

SECTION_MET = 'Meta'
SECTION_GEN = 'General'
SECTION_ADF = 'Application domain/field'
SECTION_TOT = 'Type of tool (e.g. model checker, test generator)'
SECTION_TOT_= 'Type of tool'
SECTION_EIT = 'Expected input thing'
SECTION_EIF = 'Expected input format'
SECTION_FMT = 'Format'
SECTION_EI_ = 'Expected input'
SECTION_EO_ = 'Expected output'
SECTION_ITU = 'Internals (tools used, frameworks, techniques, paradigms, ...)'
SECTION_I__ = 'Internals'
SECTION_COM = 'Comments'
SECTION_URI = 'URIs (github, websites, etc.)'
SECTION_URI_= 'Links'
SECTION_LCD = 'Last commit date'
SECTION_LPD = 'Last publication date'
SECTION_JRP = 'Related papers'
SECTION_LRP = 'List of related papers'
SECTION_RTT = 'Related tools (tools mentioned or compared to in the paper)'
SECTION_RT_ = 'Related tools'
SECTION_T__ = 'Tools'

REASON = 'Reason for this entry: '
DS22_PAPER     = 'https://doi.org/10.1145/3550355.3552426'
DS22_ARTEFACT  = 'https://doi.org/10.4121/20347950.v1'
DS22_CONTAINED = f'Contained in the ProVerB22 dataset (<a href="{DS22_PAPER}">paper</a> + <a href="{DS22_ARTEFACT}">artefact</a>)'

KNOWN_VENUES = {
	'https://doi.org/10.1007/978-3-319-63387-9': 'CAV 2017',
	'https://doi.org/10.1007/978-3-319-63390-9': 'CAV 2017',
	'https://doi.org/10.1007/978-3-319-96142-2': 'CAV 2018',
	'https://doi.org/10.1007/978-3-319-96145-3': 'CAV 2018',
	'https://doi.org/10.1007/978-3-030-25540-4': 'CAV 2019',
	'https://doi.org/10.1007/978-3-030-25543-5': 'CAV 2019',
	'https://doi.org/10.1007/978-3-030-53288-8': 'CAV 2020',
	'https://doi.org/10.1007/978-3-030-53291-8': 'CAV 2020',
	'https://doi.org/10.1007/978-3-030-81685-8': 'CAV 2021',
	'https://doi.org/10.1007/978-3-030-81688-9': 'CAV 2021',
	'https://doi.org/10.1007/978-3-031-13185-1': 'CAV 2022',
	'https://doi.org/10.1007/978-3-642-36742-7': 'TACAS 2013',
	'https://doi.org/10.1007/978-3-642-54862-8': 'TACAS 2014',
	'https://doi.org/10.1007/978-3-662-46681-0': 'TACAS 2015',
	'https://doi.org/10.1007/978-3-662-49674-9': 'TACAS 2016',
	'https://doi.org/10.1007/978-3-662-54577-5': 'TACAS 2017',
	'https://doi.org/10.1007/978-3-662-54580-5': 'TACAS 2017',
	'https://doi.org/10.1007/978-3-319-89960-2': 'TACAS 2018',
	'https://doi.org/10.1007/978-3-319-89963-3': 'TACAS 2018',
	'https://doi.org/10.1007/978-3-030-17462-0': 'TACAS 2019',
	'https://doi.org/10.1007/978-3-030-45237-7': 'TACAS 2020',
	'https://doi.org/10.1007/978-3-030-72013-1': 'TACAS 2021',
	'https://doi.org/10.1007/978-3-030-72016-2': 'TACAS 2021',
	'https://doi.org/10.1007/978-3-030-99524-9': 'TACAS 2022',
}

