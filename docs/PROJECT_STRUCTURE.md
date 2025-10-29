# Project Structure Reference

## 📁 Complete Directory Layout

```
portia-first-follow-set/
│
├── 📄 README.md                    # Project overview and purpose
├── 📄 .gitignore                   # Git ignore rules
│
├── 📂 grammar/
│   └── 📄 CFG.txt                  # PORTIA grammar in EBNF format
│
├── 📂 docs/
│   ├── 📄 CFG_Visualization.md     # Human-readable grammar documentation
│   ├── 📄 ALGORITHM.md             # FIRST/FOLLOW algorithm explanation
│   ├── 📄 PROJECT_STRUCTURE.md     # This file
│   ├── 📄 FIRST_SETS.md            # Generated FIRST sets (to be added)
│   └── 📄 FOLLOW_SETS.md           # Generated FOLLOW sets (to be added)
│
└── 📂 src/
    ├── 📄 __init__.py              # Package initialization
    ├── 📄 main.py                  # Main entry point
    ├── 📄 parser.py                # Grammar parser module
    ├── 📄 first_set.py             # FIRST set calculator
    └── 📄 follow_set.py            # FOLLOW set calculator
```

## 📋 File Descriptions

### Root Level

| File | Purpose |
|------|---------|
| `README.md` | Project overview and purpose for the team |
| `.gitignore` | Specifies files and directories to ignore in Git |

### Grammar Directory

| File | Purpose |
|------|---------|
| `CFG.txt` | PORTIA language grammar in EBNF format - source of truth |

### Documentation Directory

| File | Purpose |
|------|---------|
| `CFG_Visualization.md` | Human-readable formatted grammar with sections |
| `ALGORITHM.md` | Explanation of FIRST and FOLLOW set computation algorithms |
| `PROJECT_STRUCTURE.md` | This file - repository organization reference |
| `FIRST_SETS.md` | Generated FIRST sets for all grammar symbols (to be added) |
| `FOLLOW_SETS.md` | Generated FOLLOW sets for all non-terminals (to be added) |

### Source Directory

| File | Purpose |
|------|---------|
| `__init__.py` | Makes src a Python package, exports main classes |
| `main.py` | Entry point for generating FIRST and FOLLOW sets |
| `parser.py` | Parses EBNF grammar from CFG.txt |
| `first_set.py` | Computes FIRST sets for all symbols |
| `follow_set.py` | Computes FOLLOW sets for all non-terminals |

## 🔄 Workflow

1. **Grammar Definition** (`grammar/CFG.txt`)
   - Contains the formal EBNF grammar for PORTIA
   - Single source of truth for language syntax

2. **Generate Sets** (via `src/main.py`)
   - Parse grammar from CFG.txt
   - Compute FIRST sets for all symbols
   - Compute FOLLOW sets for all non-terminals
   - Output results to documentation

3. **Use in Parser Development**
   - Reference FIRST and FOLLOW sets
   - Build predictive parsing table
   - Integrate with PORTIA compiler

## 🎯 Purpose

This repository serves as a **reference and documentation tool** for the PORTIA development team:

- Maintains the formal grammar specification
- Generates and documents FIRST/FOLLOW sets
- Provides grammar visualization
- Supports parser development

## 🔗 Integration with PORTIA

This repository will be linked to the main PORTIA compiler:

- Grammar specification reference
- Parser construction aid
- Development documentation
- Team resource
