word-level model checking format for capturing models of hardware and potentially software in a bit-precise manner; a non-backward-compatible extension of [BTOR](BTOR.md), which was tailored towards bit-vectors and one-dimensional bit-vector arrays, BTOR2 has explicit sort declarations and register/memory initialisations; inpired by a new [AIGER](AIGER.md) format

```
<num>     ::= positive unsigned integer (greater than zero)
<uint>    ::= unsigned integer (including zero)
<string>  ::= sequence of whitespace and printable characters without '\n'
<symbol>  ::= sequence of printable characters without '\n'
<comment> ::= ';' <string>
<nid>     ::= <num>
<sid>     ::= <num>
<const>   ::= 'const' <sid> [0-1]+
<constd>  ::= 'constd' <sid> ['-']<uint>
<consth>  ::= 'consth' <sid> [0-9a-fA-F]+
<input>   ::= ( 'input' | 'one' | 'ones' | 'zero' ) <sid> | <const> | <constd> | <consth>
<state>   ::= 'state' <sid>
<bitvec>  ::= 'bitvec' <num>
<array>   ::= 'array' <sid> <sid>
<node>    ::= <sid> 'sort' ( <array> | <bitvec> )
            | <nid> ( <input> | <state> )
            | <nid> <opidx> <sid> <nid> <uint> [<uint>]
            | <nid> <op> <sid> <nid> [<nid> [<nid>]]
            | <nid> ( 'init' | 'next' ) <sid> <nid> <nid>
            | <nid> ( 'bad' | 'constraint' | 'fair' | 'output' ) <nid>
            | <nid> 'justice' <num> ( <nid> )+
<line>    ::= <comment> | <node> [<symbol>] [<comment>]
<btor>    ::= ( <line> '\n' )+ 
```

#### Related tools (tools mentioned or compared to in the paper):
Used by [Boolector](../Solvers/SMT/Boolector.md)

#### List of related papers:
https://doi.org/10.1007/978-3-319-96145-3_32

#### Meta
:: no PV
:: Specification format
:: Source :: https://doi.org/10.1145/3550355.3552426