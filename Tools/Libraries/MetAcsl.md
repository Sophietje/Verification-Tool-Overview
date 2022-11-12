a [[Frama-C]] plugin for specification and verification of high-level properties. Quoting their website:
<blockquote>
	MetAcsl is a plug-in dedicated to specifying and verifying high-level ACSL requirements (HILARE), that is, properties that are supposed to be checked at many points of the code base under analysis, so that writing the corresponding ACSL annotations manually would be extremely tedious and error-prone.
</blockquote>

#### Name:
MetAcsl

#### Application domain/field:

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:
- a target: the set of functions where the HILARE should hold;
- a context: the kind of program points that are concerned by the HILARE;
- the property itself: an ACSL predicate, possibly enriched with meta-variables

#### Expected input format:

#### Expected output:

#### Internals (tools used, frameworks, techniques, paradigms, ...):

#### Comments:

#### URIs (github, websites, etc.):
https://frama-c.com/fc-plugins/metacsl.html
https://git.frama-c.com/pub/meta

#### Last commit date:
11 May 2022

#### Last publication date:

#### List of related papers:
[MetAcsl: Specification and Verification of High-Level Properties](https://doi.org/10.1007/978-3-030-17462-0_22) (TACAS 2019)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV4 :: checks high-level ACSL requirements by propagating them across the codebase
:: Source :: https://doi.org/10.1145/3550355.3552426
