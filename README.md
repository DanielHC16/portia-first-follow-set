# PORTIA First & Follow Sets

> **Internal Tool for PORTIA Programming Language Development Team**

This repository contains the FIRST and FOLLOW sets generated from the PORTIA programming language grammar. These sets are essential for parser construction and will be integrated into the main PORTIA compiler.

## 📋 Purpose

FIRST and FOLLOW sets are used for:
- **LL(1) Parser Construction**: Verifying the grammar is suitable for predictive parsing
- **Parse Table Generation**: Building the predictive parsing table
- **Conflict Detection**: Identifying grammar ambiguities
- **Parser Development**: Reference for the PORTIA compiler team

## 📊 What's Included

- **Grammar Definition**: PORTIA CFG in EBNF format
- **FIRST Sets**: Complete FIRST sets for all grammar symbols
- **FOLLOW Sets**: Complete FOLLOW sets for all non-terminals
- **Documentation**: Grammar visualization and reference materials

## 📁 Repository Structure

```
first-follow-set/
├── grammar/
│   └── CFG.txt                 # PORTIA language grammar (EBNF format)
├── docs/
│   ├── CFG_Visualization.md    # Human-readable grammar reference
│   ├── ALGORITHM.md            # FIRST/FOLLOW computation explanation
│   ├── PROJECT_STRUCTURE.md    # Repository organization
│   ├── FIRST_SETS.md           # Generated FIRST sets (to be added)
│   └── FOLLOW_SETS.md          # Generated FOLLOW sets (to be added)
├── src/
│   └── (Helper scripts for set generation)
└── README.md
```

## 📖 Grammar Specification

The PORTIA grammar is defined in [`grammar/CFG.txt`](grammar/CFG.txt) using EBNF notation with the following conventions:

- **`->`** : Defines a production rule
- **`|`** : Denotes alternation (choice between productions)
- **`EPSILON`** : Represents empty/null productions (ε or λ)
- **Terminals**: Symbols that don't appear on the left-hand side of any production
- **Non-terminals**: Production rule names that can be further derived

### Example Productions

```ebnf
program -> s_comment m_comment global_dec s_comment m_comment function s_comment m_comment main s_comment m_comment
dtype -> int | long | float | double | char | string | bool
global_dec -> global mutability dtype id = value multi_dec ; global_dec | EPSILON
```

**Important**: Place spaces between symbols you don't want read as one symbol. For example:
- `( A )` is three symbols: `(`, `A`, `)`
- `(A)` is one symbol: `(A)`

## � PORTIA Language Features

The PORTIA grammar includes:

- **Data Types**: `int`, `long`, `float`, `double`, `char`, `string`, `bool`
- **Variables**: Mutable (`var`) and immutable (`const`) declarations
- **Arrays**: 1D and 2D array support
- **Structures**: Custom types using `weave` keyword
- **Functions**: Full function support with parameters and return types
- **Control Flow**: `if`/`else`, `switch`, `for`, `while`, `do-while`
- **I/O Operations**: `trap()` for input, `thread()` for output
- **Operators**: Arithmetic, relational, logical, and compound assignment
- **Comments**: Single-line (`//`) and multi-line (`/* */`)

## 🔗 Integration with PORTIA Compiler

This repository will be linked to the main PORTIA compiler as a reference for:
- Parser implementation
- Syntax analysis
- Grammar validation
- Development documentation

## 👥 Team

Internal tool for the PORTIA development team.

---

**Note**: This is a development resource for the PORTIA compiler project.
