Tyrolean Termination Tool 2 is a tool for automatically proving and disproving termination of rewrite systems.

#### Name:
TTT2: Tyrolean Termination Tool 2

#### Application domain/field:
Term rewriting
Termination
Term rewrite system (TRSs)

#### Type of tool (e.g. model checker, test generator):
Termination analyzer

#### Expected input thing:
Term rewrite system

#### Expected input format:
[TPDB](../Formats/TPDB.md) format

#### Expected output:
Whether the term rewrite system terminates or not (`YES`, `NO`, `MAYBE`)

It also shows the following:
- Term rewrite system/problem
- Proof of termination
- Time it took to find the proof

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [MiniSat](Solvers/SAT/MiniSat.md) and [Yices](Solvers/SMT/Yices.md).

#### Comments:
Also spellt as $T_TT_2$.

License: GNU LGPL V3.0?

#### URIs (github, websites, etc.):
Project page: http://cl-informatik.uibk.ac.at/ttt2/index.php#news
Repository: http://cl2-informatik.uibk.ac.at/mercurial.cgi/ttt2/

#### Last commit date:
5 July 2021

#### Last publication date:
2009

#### List of related papers:
[Tyrolean Termination Tool 2](https://doi.org/10.1007/978-3-642-02348-4_21) (RTA '09)

#### Related tools (tools mentioned or compared to in the paper):
Successor of $T_TT$
Other automated termination analyzers: [AProVE](AProVE.md), [[JamBox]]
$T_TT_2$ is used by the following tools: [[CaT]], [[ConCon]], [[KBCV]], [[mkbTT]], [TcT](TcT.md), [[Wanda]]

#### Meta
:: Termination
:: PV1 :: produces a proof of termination for a term rewrite system
:: Source :: compared to [[nonreach]] :: https://doi.org/10.1145/3550355.3552426
