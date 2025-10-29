# PORTIA First & Follow Sets

> **Internal Tool for PORTIA Programming Language Development Team**

This repository contains the FIRST and FOLLOW sets generated from the PORTIA programming language grammar. These sets are essential for parser construction and will be integrated into the main PORTIA compiler.

## � Quick Start - Using the Calculator

### When you update the grammar (`grammar/CFG.txt`):

1. **Edit the grammar file**
   ```bash
   # Open and modify grammar/CFG.txt with your changes
   ```

2. **Run the generator**
   ```bash
   cd src
   python main.py
   ```

3. **Check the updated outputs**
   - `output/FIRST_FOLLOW_RAW.txt` - Updated raw sets
   - `docs/FIRST_FOLLOW_SETS.md` - Updated visualized sets

4. **Verify the changes**
   - Review the generated sets for correctness
   - Check for any new conflicts or ambiguities
   - Ensure all non-terminals have valid FIRST/FOLLOW sets

### Output Files Updated Automatically:
✅ `output/FIRST_FOLLOW_RAW.txt` - Machine-readable format  
✅ `docs/FIRST_FOLLOW_SETS.md` - Human-readable tables with statistics

> **Note**: The calculator automatically handles epsilon productions, computes sets iteratively until fixpoint, and validates the grammar structure.

---

## �📋 Purpose

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
│   └── CFG.txt                     # PORTIA language grammar (EBNF format)
├── docs/
│   ├── CFG_Visualization.md        # Human-readable grammar reference
│   ├── ALGORITHM.md                # FIRST/FOLLOW computation explanation
│   ├── PROJECT_STRUCTURE.md        # Repository organization
│   └── FIRST_FOLLOW_SETS.md        # ✨ Generated sets (visualized tables)
├── output/
│   └── FIRST_FOLLOW_RAW.txt        # ✨ Generated sets (raw text format)
├── src/
│   ├── main.py                     # Generator script
│   ├── grammar_parser.py           # CFG parser
│   ├── first_set.py                # FIRST set calculator
│   └── follow_set.py               # FOLLOW set calculator
└── README.md
```

## 📊 Generated Files

### Raw Format (`output/FIRST_FOLLOW_RAW.txt`)
Plain text format with FIRST and FOLLOW sets for all non-terminals. Easy to parse programmatically.

**Example:**
```
FIRST(program) = { /*, //, ;, bool, char, double, float, func, global, id, int, long, string, weave }
FOLLOW(program) = { $ }
```

### Visualized Format (`docs/FIRST_FOLLOW_SETS.md`)
Markdown tables with formatted FIRST and FOLLOW sets, including statistics and summary information.

**Features:**
- Organized tables for easy reference
- Summary statistics (average set sizes, largest sets, etc.)
- Non-terminals with epsilon productions highlighted
- Total of **98 non-terminals** and **72 terminals**

## 📖 Grammar Specification

The PORTIA grammar is defined in [`grammar/CFG.txt`](grammar/CFG.txt) using EBNF notation with the following conventions:

- **`->`** : Defines a production rule
- **`|`** : Denotes alternation (choice between productions)
- **`EPSILON`** : Represents empty/null productions (ε or λ)
- **Terminals**: Symbols that don't appear on the left-hand side of any production
- **Non-terminals**: Production rule names that can be further derived

### Example Productions

```ebnf
program -> s_comment m_comment global_dec s_comment m_comment function s_comment m_comment main_func s_comment m_comment
s_comment -> // comment | EPSILON
m_comment -> /* comments */ | EPSILON
dtype -> int | long | float | double | char | string | bool
global_dec -> global mutability dtype id = value multi_dec ; global_dec | EPSILON
main_func -> int main ( ) { main_body }
```

**Important**: Place spaces between symbols you don't want read as one symbol. For example:
- `( A )` is three symbols: `(`, `A`, `)`
- `(A)` is one symbol: `(A)`

## 📖 PORTIA Language Features

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

## � Reference Documentation

**Grammar Visualization**: Open [`docs/CFG_Visualization.md`](docs/CFG_Visualization.md) for the complete human-readable grammar documentation with organized sections.

**Algorithm Details**: See [`docs/ALGORITHM.md`](docs/ALGORITHM.md) for the FIRST/FOLLOW computation algorithms and implementation details.

**Generated Sets**: 
- [`output/FIRST_FOLLOW_RAW.txt`](output/FIRST_FOLLOW_RAW.txt) - Machine-readable format
- [`docs/FIRST_FOLLOW_SETS.md`](docs/FIRST_FOLLOW_SETS.md) - Human-readable tables with statistics

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
