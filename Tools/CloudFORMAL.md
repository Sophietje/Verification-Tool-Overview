#### Name:
CloudFORMAL

#### Application domain/field:
Infrastructure as Code (IaC)
Security analysis
Configuration files
Cloud infrastructure

#### Type of tool (e.g. model checker, test generator):
Security analyser?

#### Expected input thing:
cfn (CloudFormation) configuration file

#### Expected input format:
`.json` file

#### Expected output:
`.owl` file that can be opened, navigated and queried in Protégé.
The models are automatically checked against common security best-practices. For each of these properties it will determine whether it is `TRUE`, `FALSE` or `UNKNOWN`. These results are outputted in a `.csv` file.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Encodes AWS CloudFormation templates into Description Logic models.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/claudiacauli/CloudFORMAL

#### Last commit date:
25 February 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_36 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Security
:: PV3 :: checks common security best-practices and user-specified queries of a cloud configuration