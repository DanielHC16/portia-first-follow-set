# PORTIA First & Follow Sets

> **Generated from PORTIA CFG** | EBNF Grammar Specification

---

## 📋 Contents

- [Overview](#overview)
- [FIRST Sets](#first-sets)
- [FOLLOW Sets](#follow-sets)
- [Summary Statistics](#summary-statistics)

---

## Overview

This document contains the computed FIRST and FOLLOW sets for the PORTIA programming language grammar.

- **Total Non-terminals**: 98
- **Total Terminals**: 71
- **Start Symbol**: `program`

---

## FIRST Sets

The FIRST set of a non-terminal contains all terminals that can appear as the first symbol of any string derived from that non-terminal.

| Non-Terminal | FIRST Set |
|--------------|----------|
| `I_O_stmt` | `thread`, `trap` |
| `add_min_cont` | `+`, `-`, `EPSILON` |
| `arg` | `EPSILON`, `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` |
| `arith_expr` | `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` |
| `arr_1D` | `EPSILON`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` |
| `arr_1D_UD` | `EPSILON`, `id` |
| `arr_1D_cont` | `EPSILON`, `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` |
| `arr_1D_cont_val` | `,`, `EPSILON` |
| `arr_1D_init` | `EPSILON`, `{` |
| `arr_2D` | `EPSILON`, `[` |
| `arr_2D_init` | `EPSILON`, `{` |
| `arr_2_2D` | `[` |
| `arr_value_1D` | `,`, `EPSILON`, `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` |
| `arr_value_2D` | `{` |
| `arr_value_2D_cont` | `,`, `EPSILON` |
| `array_spec_opt` | `EPSILON`, `[` |
| `assign_stmt` | `id` |
| `assign_stmt_op` | `%=`, `*=`, `+=`, `-=`, `/=`, `=` |
| `case_stmt` | `case` |
| `case_stmt_cont` | `EPSILON`, `case` |
| `case_val` | `id` |
| `cast_val` | `bool`, `boollit`, `char`, `charlit`, `double`, `doublelit`, `float`, `floatlit`, `int`, `intlit`, `long`, `longlit`, `string`, `stringlit` |
| `condition` | `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` |
| `conditional_stmt` | `EPSILON`, `if`, `switch` |
| `ctrl_body` | `local` |
| `ctrl_struct` | `EPSILON`, `do`, `for`, `if`, `switch`, `while` |
| `data_type` | `bool`, `char`, `double`, `float`, `int`, `long`, `string` |
| `default_stmt` | `EPSILON`, `default` |
| `do_stmt` | `do` |
| `dtype` | `bool`, `char`, `double`, `float`, `int`, `long`, `string` |
| `else_if_ei_stmt` | `EPSILON`, `else` |
| `else_stmt` | `if`, `{` |
| `equal_sym` | `=`, `EPSILON` |
| `expr1_cont` | `,`, `EPSILON` |
| `expression` | `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` |
| `expression1` | `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `string_lit`, `stringlit` |
| `factor` | `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` |
| `field_dec` | `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` |
| `field_dec_cont` | `,`, `EPSILON` |
| `field_list` | `EPSILON`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` |
| `field_type` | `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` |
| `for_stmt` | `for` |
| `function` | `EPSILON`, `func` |
| `function_body` | `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` |
| `function_call` | `id` |
| `function_def` | `func` |
| `global_dec` | `;`, `EPSILON`, `bool`, `char`, `double`, `float`, `global`, `id`, `int`, `long`, `string`, `weave` |
| `iden` | `id` |
| `iden1` | `id` |
| `iden1_cont` | `,`, `EPSILON` |
| `iden_val` | `.`, `EPSILON`, `[` |
| `if_stmt` | `if` |
| `import_block` | `EPSILON`, `using` |
| `import_cont` | `,`, `EPSILON` |
| `import_stmt` | `using` |
| `initializer` | `EPSILON`, `id`, `local` |
| `input_stmt` | `trap` |
| `isize` | `EPSILON`, `[` |
| `local_block` | `EPSILON`, `local` |
| `local_dec` | `local` |
| `logical_expr` | `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` |
| `logical_expr_cont` | `&&`, `(`, `++`, `-`, `--`, `EPSILON`, `frac_lit`, `id`, `whole_lit` |
| `loop_stmt` | `do`, `for`, `while` |
| `m_comment` | `/*`, `EPSILON` |
| `main_body` | `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` |
| `main_func` | `int` |
| `mult_div_modulo_cont` | `*`, `/`, `EPSILON` |
| `multi_arg` | `,`, `EPSILON` |
| `multi_dec` | `,`, `EPSILON` |
| `mutability` | `const`, `var` |
| `num_lit_type` | `frac_lit`, `whole_lit` |
| `numeric_atom` | `++`, `--`, `frac_lit`, `id`, `whole_lit` |
| `numeric_factor` | `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` |
| `output_stmt` | `thread` |
| `param` | `EPSILON`, `bool`, `char`, `double`, `float`, `int`, `long`, `string` |
| `param_cont` | `,`, `EPSILON` |
| `program` | `/*`, `//`, `;`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` |
| `rel_expr` | `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` |
| `rel_expr_cont` | `!=`, `<`, `=`, `>`, `EPSILON` |
| `ret_stmt` | `return` |
| `ret_type` | `bool`, `char`, `double`, `float`, `int`, `long`, `string`, `void` |
| `ret_value` | `(`, `++`, `-`, `--`, `EPSILON`, `boollit`, `charlit`, `doublelit`, `floatlit`, `frac_lit`, `id`, `intlit`, `longlit`, `stringlit`, `whole_lit` |
| `s_comment` | `//`, `EPSILON` |
| `size` | `intlit` |
| `statement` | `(`, `++`, `-`, `--`, `EPSILON`, `do`, `for`, `frac_lit`, `id`, `if`, `switch`, `thread`, `trap`, `while`, `whole_lit` |
| `statement_list` | `(`, `++`, `-`, `--`, `EPSILON`, `do`, `for`, `frac_lit`, `id`, `if`, `switch`, `thread`, `trap`, `while`, `whole_lit` |
| `string_expr` | `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `stringlit` |
| `string_value` | `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `stringlit` |
| `switch_stmt` | `switch` |
| `switch_val` | `(`, `++`, `-`, `--`, `frac_lit`, `id`, `intlit`, `stringlit`, `whole_lit` |
| `term` | `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` |
| `typecast_expr` | `(` |
| `up_post` | `++`, `--` |
| `update` | `++`, `--`, `EPSILON`, `id` |
| `value` | `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` |
| `weave_def` | `weave` |
| `weave_id` | `id` |
| `while_stmt` | `while` |

---

## FOLLOW Sets

The FOLLOW set of a non-terminal contains all terminals that can appear immediately to the right of that non-terminal in some sentential form.

| Non-Terminal | FOLLOW Set |
|--------------|----------|
| `I_O_stmt` | `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` |
| `add_min_cont` | `!=`, `&&`, `(`, `)`, `++`, `-`, `--`, `..`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` |
| `arg` | `)`, `,` |
| `arith_expr` | `!=`, `&&`, `(`, `)`, `++`, `-`, `--`, `..`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` |
| `arr_1D` | `;` |
| `arr_1D_UD` | `;` |
| `arr_1D_cont` | `}` |
| `arr_1D_cont_val` | `}` |
| `arr_1D_init` | `;`, `[`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` |
| `arr_2D` | `;`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` |
| `arr_2D_init` | `;`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` |
| `arr_2_2D` | `;`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` |
| `arr_value_1D` | `}` |
| `arr_value_2D` | `}` |
| `arr_value_2D_cont` | `}` |
| `array_spec_opt` | `%=`, `*=`, `+=`, `,`, `-=`, `/=`, `;`, `=` |
| `assign_stmt` | `;`, `break`, `do`, `for`, `if`, `return`, `switch`, `while`, `}` |
| `assign_stmt_op` | `;`, `break`, `do`, `for`, `if`, `return`, `switch`, `while`, `}` |
| `case_stmt` | `case`, `default`, `}` |
| `case_stmt_cont` | `case`, `default`, `}` |
| `case_val` | `:` |
| `cast_val` | `)` |
| `condition` | `)`, `;` |
| `conditional_stmt` | `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` |
| `ctrl_body` | `break`, `return`, `}` |
| `ctrl_struct` | `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` |
| `data_type` | `)` |
| `default_stmt` | `}` |
| `do_stmt` | `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` |
| `dtype` | `)`, `id` |
| `else_if_ei_stmt` | `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` |
| `else_stmt` | `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` |
| `equal_sym` | `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` |
| `expr1_cont` | `)` |
| `expression` | `)`, `..`, `;`, `trap` |
| `expression1` | `)` |
| `factor` | `!=`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` |
| `field_dec` | `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string`, `}` |
| `field_dec_cont` | `;` |
| `field_list` | `}` |
| `field_type` | `id` |
| `for_stmt` | `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` |
| `function` | `/*`, `//`, `int` |
| `function_body` | `}` |
| `function_call` | `!=`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` |
| `function_def` | `/*`, `//`, `func`, `int` |
| `global_dec` | `/*`, `//`, `func`, `int` |
| `iden` | `)` |
| `iden1` | `)` |
| `iden1_cont` | `)` |
| `iden_val` | `)` |
| `if_stmt` | `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` |
| `import_block` | `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` |
| `import_cont` | `;` |
| `import_stmt` | `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` |
| `initializer` | `;` |
| `input_stmt` | `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` |
| `isize` | `)` |
| `local_block` | `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` |
| `local_dec` | `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` |
| `logical_expr` | `)`, `..`, `;`, `trap` |
| `logical_expr_cont` | `)`, `..`, `;`, `trap` |
| `loop_stmt` | `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` |
| `m_comment` | `$`, `/*`, `//`, `;`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` |
| `main_body` | `}` |
| `main_func` | `$`, `/*`, `//` |
| `mult_div_modulo_cont` | `!=`, `&&`, `(`, `)`, `+`, `++`, `-`, `--`, `..`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` |
| `multi_arg` | `)` |
| `multi_dec` | `;` |
| `mutability` | `bool`, `char`, `double`, `float`, `int`, `long`, `string` |
| `num_lit_type` | `!=`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` |
| `numeric_atom` | `!=`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` |
| `numeric_factor` | `!=`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` |
| `output_stmt` | `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` |
| `param` | `)` |
| `param_cont` | `)` |
| `program` | `$` |
| `rel_expr` | `&&`, `(`, `)`, `++`, `-`, `--`, `..`, `;`, `frac_lit`, `id`, `trap`, `whole_lit` |
| `rel_expr_cont` | `&&`, `(`, `)`, `++`, `-`, `--`, `..`, `;`, `frac_lit`, `id`, `trap`, `whole_lit` |
| `ret_stmt` | `}` |
| `ret_type` | `id` |
| `ret_value` | `;` |
| `s_comment` | `$`, `/*`, `//`, `;`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` |
| `size` | `]` |
| `statement` | `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` |
| `statement_list` | `return` |
| `string_expr` | `)`, `..` |
| `string_value` | `)`, `..` |
| `switch_stmt` | `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` |
| `switch_val` | `)` |
| `term` | `!=`, `&&`, `(`, `)`, `+`, `++`, `-`, `--`, `..`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` |
| `typecast_expr` | `)`, `..` |
| `up_post` | `)` |
| `update` | `)` |
| `value` | `)`, `,`, `..`, `;`, `break`, `do`, `for`, `if`, `return`, `switch`, `while`, `}` |
| `weave_def` | `/*`, `//`, `;`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` |
| `weave_id` | `id` |
| `while_stmt` | `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` |

---

## Summary Statistics

### FIRST Sets

- **Average FIRST set size**: 4.53
- **Largest FIRST set**: `main_body` with 17 elements
- **Non-terminals with ε**: 43

### FOLLOW Sets

- **Average FOLLOW set size**: 7.21
- **Largest FOLLOW set**: `numeric_factor` with 19 elements

---

**Legend:**
- `EPSILON` or `ε`: Represents empty/null production
- `$`: End-of-input marker
