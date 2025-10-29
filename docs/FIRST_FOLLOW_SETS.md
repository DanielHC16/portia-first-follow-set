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

**The FIRST set of a non-terminal contains all terminals that can appear as the first symbol of any string derived from that non-terminal.**

> **Notation:** Sets are displayed using curly braces `{ }`. `ε` represents epsilon (empty/null production).


| Non-Terminal | → | FIRST Set |
|--------------|---|-----------|
| `program` | → | { `//`, `/*`, `bool`, `char`, `double`, `float`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `s_comment` | → | { `//`, `ε` } |
| `m_comment` | → | { `/*`, `ε` } |
| `main_func` | → | { `int` } |
| `main_body` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `using`, `whole_lit` } |
| `global_dec` | → | { `ε`, `bool`, `char`, `double`, `float`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `mutability` | → | { `const`, `var` } |
| `multi_dec` | → | { `,`, `ε` } |
| `dtype` | → | { `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `value` | → | { `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `size` | → | { `intlit` } |
| `arr_1D` | → | { `ε`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `arr_1D_init` | → | { `ε`, `{` } |
| `arr_value_1D` | → | { `,`, `ε`, `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `arr_1D_cont` | → | { `ε`, `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `arr_1D_cont_val` | → | { `,`, `ε` } |
| `arr_2D` | → | { `ε`, `[` } |
| `arr_2D_init` | → | { `ε`, `{` } |
| `arr_value_2D` | → | { `{` } |
| `arr_value_2D_cont` | → | { `,`, `ε` } |
| `weave_def` | → | { `weave` } |
| `field_list` | → | { `ε`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `field_dec` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `field_dec_cont` | → | { `,`, `ε` } |
| `array_spec_opt` | → | { `ε`, `[` } |
| `field_type` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `weave_id` | → | { `id` } |
| `function` | → | { `ε`, `func` } |
| `function_def` | → | { `func` } |
| `ret_type` | → | { `bool`, `char`, `double`, `float`, `int`, `long`, `string`, `void` } |
| `param` | → | { `ε`, `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `param_cont` | → | { `,`, `ε` } |
| `function_body` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` } |
| `import_block` | → | { `ε`, `using` } |
| `import_stmt` | → | { `using` } |
| `import_cont` | → | { `,`, `ε` } |
| `local_block` | → | { `ε`, `local` } |
| `local_dec` | → | { `local` } |
| `initializer` | → | { `ε`, `id`, `local` } |
| `statement_list` | → | { `(`, `++`, `-`, `--`, `ε`, `do`, `for`, `frac_lit`, `id`, `if`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `statement` | → | { `(`, `++`, `-`, `--`, `ε`, `do`, `for`, `frac_lit`, `id`, `if`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `expression` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `expression1` | → | { `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `string_lit`, `stringlit` } |
| `logical_expr` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `logical_expr_cont` | → | { `&&`, `||`, `ε` } |
| `rel_expr` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `rel_expr_cont` | → | { `!=`, `<`, `=`, `>`, `ε` } |
| `arith_expr` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `term` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `factor` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `numeric_factor` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `cast_val` | → | { `bool`, `boollit`, `char`, `charlit`, `double`, `doublelit`, `float`, `floatlit`, `int`, `intlit`, `long`, `longlit`, `string`, `stringlit` } |
| `numeric_atom` | → | { `++`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `num_lit_type` | → | { `frac_lit`, `whole_lit` } |
| `I_O_stmt` | → | { `thread`, `trap` } |
| `input_stmt` | → | { `trap` } |
| `output_stmt` | → | { `thread` } |
| `function_call` | → | { `id` } |
| `arg` | → | { `ε`, `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `multi_arg` | → | { `,`, `ε` } |
| `assign_stmt` | → | { `id` } |
| `assign_stmt_op` | → | { `%=`, `*=`, `+=`, `-=`, `/=`, `=` } |
| `conditional_stmt` | → | { `ε`, `if`, `switch` } |
| `if_stmt` | → | { `if` } |
| `condition` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `ctrl_body` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `local`, `thread`, `trap`, `whole_lit` } |
| `else_if_ei_stmt` | → | { `ε`, `else` } |
| `else_stmt` | → | { `if`, `{` } |
| `switch_stmt` | → | { `switch` } |
| `switch_val` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `intlit`, `stringlit`, `whole_lit` } |
| `case_stmt` | → | { `case` } |
| `case_stmt_cont` | → | { `ε`, `case` } |
| `case_val` | → | { `id` } |
| `default_stmt` | → | { `ε`, `default` } |
| `loop_stmt` | → | { `do`, `for`, `while` } |
| `while_stmt` | → | { `while` } |
| `do_stmt` | → | { `do` } |
| `for_stmt` | → | { `for` } |
| `update` | → | { `++`, `--`, `ε`, `id` } |
| `up_post` | → | { `++`, `--` } |
| `ret_stmt` | → | { `return` } |
| `ret_value` | → | { `(`, `++`, `-`, `--`, `ε`, `boollit`, `charlit`, `doublelit`, `floatlit`, `frac_lit`, `id`, `intlit`, `longlit`, `stringlit`, `whole_lit` } |
| `string_expr` | → | { `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `stringlit` } |
| `string_value` | → | { `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `stringlit` } |
| `typecast_expr` | → | { `(` } |
| `equal_sym` | → | { `=`, `ε` } |
| `iden` | → | { `id` } |
| `iden1` | → | { `id` } |
| `iden1_cont` | → | { `,`, `ε` } |
| `iden_val` | → | { `.`, `ε`, `[` } |
| `add_min_cont` | → | { `+`, `-`, `ε` } |
| `mult_div_modulo_cont` | → | { `*`, `/`, `ε` } |
| `arr_1D_UD` | → | { `ε`, `id` } |
| `arr_2_2D` | → | { `[` } |
| `ctrl_struct` | → | { `ε`, `do`, `for`, `if`, `switch`, `while` } |
| `data_type` | → | { `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `isize` | → | { `ε`, `[` } |

---

## FOLLOW Sets

**The FOLLOW set of a non-terminal contains all terminals that can appear immediately to the right of that non-terminal in some sentential form.**

> **Notation:** Sets are displayed using curly braces `{ }`. `$` represents the end-of-input marker.

| Non-Terminal | → | FOLLOW Set |
|--------------|--|------------|
| `program` | → | { `$` } |
| `s_comment` | → | { `$`, `/*`, `//`, `;`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `m_comment` | → | { `$`, `/*`, `//`, `;`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `main_func` | → | { `$`, `/*`, `//` } |
| `main_body` | → | { `}` } |
| `global_dec` | → | { `/*`, `//`, `func`, `int` } |
| `mutability` | → | { `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `multi_dec` | → | { `;` } |
| `dtype` | → | { `)`, `id` } |
| `value` | → | { `)`, `,`, `..`, `;`, `break`, `do`, `for`, `if`, `return`, `switch`, `while`, `}` } |
| `size` | → | { `]` } |
| `arr_1D` | → | { `;` } |
| `arr_1D_init` | → | { `;`, `[`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `arr_value_1D` | → | { `}` } |
| `arr_1D_cont` | → | { `}` } |
| `arr_1D_cont_val` | → | { `}` } |
| `arr_2D` | → | { `;`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `arr_2D_init` | → | { `;`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `arr_value_2D` | → | { `}` } |
| `arr_value_2D_cont` | → | { `}` } |
| `weave_def` | → | { `/*`, `//`, `;`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `field_list` | → | { `}` } |
| `field_dec` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string`, `}` } |
| `field_dec_cont` | → | { `;` } |
| `array_spec_opt` | → | { `%=`, `*=`, `+=`, `,`, `-=`, `/=`, `;`, `=` } |
| `field_type` | → | { `id` } |
| `weave_id` | → | { `id` } |
| `function` | → | { `/*`, `//`, `int` } |
| `function_def` | → | { `/*`, `//`, `func`, `int` } |
| `ret_type` | → | { `id` } |
| `param` | → | { `)` } |
| `param_cont` | → | { `)` } |
| `function_body` | → | { `}` } |
| `import_block` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `import_stmt` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` } |
| `import_cont` | → | { `;` } |
| `local_block` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `local_dec` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `initializer` | → | { `;` } |
| `statement_list` | → | { `return` } |
| `statement` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `expression` | → | { `)`, `..`, `;`, `trap` } |
| `expression1` | → | { `)` } |
| `logical_expr` | → | { `)`, `..`, `;`, `trap` } |
| `logical_expr_cont` | → | { `)`, `..`, `;`, `trap` } |
| `rel_expr` | → | { `&&`, `||`, `)`, `..`, `;`, `trap` } |
| `rel_expr_cont` | → | { `&&`, `||`, `)`, `..`, `;`, `trap` } |
| `arith_expr` | → | { `!=`, `&&`, `<`, `=`, `>`, `||`, `)`, `..`, `;`, `trap` } |
| `term` | → | { `!=`, `&&`, `+`, `-`, `<`, `=`, `>`, `||`, `)`, `..`, `;`, `trap` } |
| `factor` | → | { `!=`, `&&`, `*`, `+`, `-`, `/`, `<`, `=`, `>`, `||`, `)`, `..`, `;`, `trap` } |
| `numeric_factor` | → | { `!=`, `&&`, `*`, `+`, `-`, `/`, `<`, `=`, `>`, `||`, `)`, `..`, `;`, `trap` } |
| `numeric_atom` | → | { `!=`, `&&`, `*`, `+`, `-`, `/`, `<`, `=`, `>`, `||`, `)`, `..`, `;`, `trap` } |
| `num_lit_type` | → | { `!=`, `&&`, `*`, `+`, `-`, `/`, `<`, `=`, `>`, `||`, `)`, `..`, `;`, `trap` } |
| `I_O_stmt` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `input_stmt` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `output_stmt` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `function_call` | → | { `!=`, `&&`, `*`, `+`, `-`, `/`, `<`, `=`, `>`, `||`, `)`, `..`, `;`, `trap` } |
| `arg` | → | { `)`, `,` } |
| `multi_arg` | → | { `)` } |
| `assign_stmt` | → | { `;`, `break`, `do`, `for`, `if`, `return`, `switch`, `while`, `}` } |
| `assign_stmt_op` | → | { `;`, `break`, `do`, `for`, `if`, `return`, `switch`, `while`, `}` } |
| `conditional_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `if_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `condition` | → | { `)`, `;` } |
| `ctrl_body` | → | { `break`, `return`, `}` } |
| `else_if_ei_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `else_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `switch_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `switch_val` | → | { `)` } |
| `case_stmt` | → | { `case`, `default`, `}` } |
| `case_stmt_cont` | → | { `case`, `default`, `}` } |
| `case_val` | → | { `:` } |
| `default_stmt` | → | { `}` } |
| `loop_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `while_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `do_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `for_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `update` | → | { `)` } |
| `up_post` | → | { `)` } |
| `ret_stmt` | → | { `}` } |
| `ret_value` | → | { `;` } |
| `string_expr` | → | { `)`, `..` } |
| `string_value` | → | { `)`, `..` } |
| `typecast_expr` | → | { `)`, `..` } |
| `equal_sym` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `expr1_cont` | → | { `)` } |
| `iden` | → | { `)` } |
| `iden1` | → | { `)` } |
| `iden1_cont` | → | { `)` } |
| `iden_val` | → | { `)` } |
| `add_min_cont` | → | { `!=`, `&&`, `<`, `=`, `>`, `||`, `)`, `..`, `;`, `trap` } |
| `mult_div_modulo_cont` | → | { `!=`, `&&`, `+`, `-`, `<`, `=`, `>`, `||`, `)`, `..`, `;`, `trap` } |
| `arr_1D_UD` | → | { `;` } |
| `arr_2_2D` | → | { `;`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `cast_val` | → | { `!=`, `&&`, `*`, `+`, `-`, `/`, `<`, `=`, `>`, `||`, `)`, `..`, `;`, `trap` } |
| `ctrl_struct` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `equal_sym` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `isize` | → | { `)` } |

---
| `mutability` | → | { `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `function_def` | → | { `/*`, `//`, `func`, `int` } |
| `function_body` | → | { `}` } |
| `param` | → | { `)` } |
| `param_cont` | → | { `)` } |
| `weave_def` | → | { `/*`, `//`, `;`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `field_list` | → | { `}` } |
| `field_dec` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string`, `}` } |
| `arg` | → | { `)`, `,` } |
| `arith_expr` | → | { `!=`, `&&`, `(`, `)`, `++`, `-`, `--`, `..`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` } |
| `arr_1D` | → | { `;` } |
| `arr_1D_UD` | → | { `;` } |
| `arr_1D_cont` | → | { `}` } |
| `arr_1D_cont_val` | → | { `}` } |
| `arr_1D_init` | → | { `;`, `[`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `arr_2D` | → | { `;`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `arr_2D_init` | → | { `;`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `arr_2_2D` | → | { `;`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `arr_value_1D` | → | { `}` } |
| `arr_value_2D` | → | { `}` } |
| `arr_value_2D_cont` | → | { `}` } |
| `array_spec_opt` | → | { `%=`, `*=`, `+=`, `,`, `-=`, `/=`, `;`, `=` } |
| `assign_stmt` | → | { `;`, `break`, `do`, `for`, `if`, `return`, `switch`, `while`, `}` } |
| `assign_stmt_op` | → | { `;`, `break`, `do`, `for`, `if`, `return`, `switch`, `while`, `}` } |
| `case_stmt` | → | { `case`, `default`, `}` } |
| `case_stmt_cont` | → | { `case`, `default`, `}` } |
| `case_val` | → | { `:` } |
| `cast_val` | → | { `)` } |
| `condition` | → | { `)`, `;` } |
| `conditional_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `ctrl_body` | → | { `break`, `return`, `}` } |
| `ctrl_struct` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `data_type` | → | { `)` } |
| `default_stmt` | → | { `}` } |
| `do_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `dtype` | → | { `)`, `id` } |
| `else_if_ei_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `else_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `equal_sym` | → | { `(`, `++`, `-`, `--`, `frac_lit`, `id`, `whole_lit` } |
| `expr1_cont` | → | { `)` } |
| `expression` | → | { `)`, `..`, `;`, `trap` } |
| `expression1` | → | { `)` } |
| `factor` | → | { `!=`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` } |
| `field_dec` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string`, `}` } |
| `field_dec_cont` | → | { `;` } |
| `field_list` | → | { `}` } |
| `field_type` | → | { `id` } |
| `for_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `function` | → | { `/*`, `//`, `int` } |
| `function_body` | → | { `}` } |
| `function_call` | → | { `!=`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` } |
| `function_def` | → | { `/*`, `//`, `func`, `int` } |
| `global_dec` | → | { `/*`, `//`, `func`, `int` } |
| `iden` | → | { `)` } |
| `iden1` | → | { `)` } |
| `iden1_cont` | → | { `)` } |
| `iden_val` | → | { `)` } |
| `if_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `import_block` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `import_cont` | → | { `;` } |
| `import_stmt` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` } |
| `initializer` | → | { `;` } |
| `input_stmt` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `isize` | → | { `)` } |
| `local_block` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `local_dec` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `local`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `logical_expr` | → | { `)`, `..`, `;`, `trap` } |
| `logical_expr_cont` | → | { `)`, `..`, `;`, `trap` } |
| `loop_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `m_comment` | → | { `$`, `/*`, `//`, `;`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `main_body` | → | { `}` } |
| `main_func` | → | { `$`, `/*`, `//` } |
| `mult_div_modulo_cont` | → | { `!=`, `&&`, `(`, `)`, `+`, `++`, `-`, `--`, `..`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` } |
| `multi_arg` | → | { `)` } |
| `multi_dec` | → | { `;` } |
| `mutability` | → | { `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `num_lit_type` | → | { `!=`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` } |
| `numeric_atom` | → | { `!=`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` } |
| `numeric_factor` | → | { `!=`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` } |
| `output_stmt` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `param` | → | { `)` } |
| `param_cont` | → | { `)` } |
| `program` | → | { `$` } |
| `rel_expr` | → | { `&&`, `(`, `)`, `++`, `-`, `--`, `..`, `;`, `frac_lit`, `id`, `trap`, `whole_lit` } |
| `rel_expr_cont` | → | { `&&`, `(`, `)`, `++`, `-`, `--`, `..`, `;`, `frac_lit`, `id`, `trap`, `whole_lit` } |
| `ret_stmt` | → | { `}` } |
| `ret_type` | → | { `id` } |
| `ret_value` | → | { `;` } |
| `s_comment` | → | { `$`, `/*`, `//`, `;`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `size` | → | { `]` } |
| `statement` | → | { `(`, `++`, `-`, `--`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `statement_list` | → | { `return` } |
| `string_expr` | → | { `)`, `..` } |
| `string_value` | → | { `)`, `..` } |
| `switch_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `switch_val` | → | { `)` } |
| `term` | → | { `!=`, `&&`, `(`, `)`, `+`, `++`, `-`, `--`, `..`, `;`, `<`, `=`, `>`, `frac_lit`, `id`, `trap`, `whole_lit` } |
| `typecast_expr` | → | { `)`, `..` } |
| `up_post` | → | { `)` } |
| `update` | → | { `)` } |
| `value` | → | { `)`, `,`, `..`, `;`, `break`, `do`, `for`, `if`, `return`, `switch`, `while`, `}` } |
| `weave_def` | → | { `/*`, `//`, `;`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `weave_id` | → | { `id` } |
| `while_stmt` | → | { `(`, `++`, `-`, `--`, `break`, `do`, `for`, `frac_lit`, `id`, `if`, `return`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |

---

## Summary Statistics

### FIRST Sets

- **Average FIRST set size**: 4.53
- **Largest FIRST set**: `function_body` with 17 elements
- **Non-terminals with ε**: 43

### FOLLOW Sets

- **Average FOLLOW set size**: 7.21
- **Largest FOLLOW set**: `factor` with 19 elements

---

**Legend:**
- `EPSILON` or `ε`: Represents empty/null production
- `$`: End-of-input marker
