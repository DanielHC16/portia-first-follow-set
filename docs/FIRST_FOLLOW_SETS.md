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

- **Total Non-terminals**: 107
- **Total Terminals**: 72
- **Start Symbol**: `program`

---

## FIRST Sets

**The FIRST set of a non-terminal contains all terminals that can appear as the first symbol of any string derived from that non-terminal.**

> **Notation:** Sets are displayed using curly braces `{ }`. `ε` represents epsilon (empty/null production).

| Non-Terminal | → | FIRST Set |
|--------------|---|-----------|
| `I_O_stmt` | → | { `thread`, `trap` } |
| `add_min_cont` | → | { `+`, `-`, `ε` } |
| `arg` | → | { `ε`, `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `arith_expr` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `arr_1D` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `arr_1D_init` | → | { `=` } |
| `arr_1D_tail` | → | { `=`, `ε`, `[` } |
| `arr_2D` | → | { `[` } |
| `arr_2D_UD` | → | { `=`, `ε` } |
| `arr_2D_init` | → | { `=`, `ε` } |
| `arr_dtype` | → | { `ε`, `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `array_spec_2D` | → | { `ε`, `[` } |
| `array_spec_opt` | → | { `ε`, `[` } |
| `assign_stmt` | → | { `id` } |
| `assign_stmt_op` | → | { `%=`, `*=`, `+=`, `-=`, `/=`, `=` } |
| `atom` | → | { `++`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `case_stmt` | → | { `case` } |
| `case_stmt_cont` | → | { `ε`, `case` } |
| `case_val` | → | { `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `cast_val` | → | { `(` } |
| `condition` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `conditional_stmt` | → | { `if`, `switch` } |
| `ctrl_body` | → | { `(`, `++`, `-`, `--`, `ε`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `ctrl_struct` | → | { `do`, `for`, `if`, `switch`, `while` } |
| `default_stmt` | → | { `ε`, `default` } |
| `do_stmt` | → | { `do` } |
| `dtype` | → | { `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `elem_1D_list` | → | { `ε`, `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `elem_1D_list_tail` | → | { `,`, `ε` } |
| `elem_2D_list` | → | { `ε`, `{` } |
| `elem_2D_list_tail` | → | { `,`, `ε` } |
| `else_if_ei_stmt` | → | { `ε`, `else` } |
| `else_stmt` | → | { `if`, `{` } |
| `equal_sym` | → | { `=`, `ε` } |
| `expr1_cont` | → | { `,`, `ε` } |
| `expression` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `expression1` | → | { `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `string_lit`, `stringlit` } |
| `factor` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `field_array_spec_opt` | → | { `ε`, `[` } |
| `field_dec` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `field_dec_cont` | → | { `,`, `ε` } |
| `field_list` | → | { `ε`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `field_type` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `for_stmt` | → | { `for` } |
| `function` | → | { `ε`, `func` } |
| `function_body` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` } |
| `function_call` | → | { `id` } |
| `function_def` | → | { `func` } |
| `global_dec` | → | { `ε`, `bool`, `char`, `double`, `float`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `iden` | → | { `id` } |
| `iden1` | → | { `id` } |
| `iden1_cont` | → | { `,`, `ε` } |
| `iden1_tail` | → | { `ε`, `[` } |
| `iden1_weave` | → | { `.`, `[` } |
| `iden_val` | → | { `.`, `ε`, `[` } |
| `if_stmt` | → | { `if` } |
| `import_block` | → | { `ε`, `using` } |
| `import_cont` | → | { `,`, `ε` } |
| `import_stmt` | → | { `using` } |
| `initializer` | → | { `ε`, `id`, `local` } |
| `input_stmt` | → | { `trap` } |
| `isize` | → | { `ε`, `[` } |
| `local_block` | → | { `ε`, `local` } |
| `local_dec` | → | { `local` } |
| `logical_expr` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `logical_expr_cont` | → | { `&&`, `(`, `++`, `-`, `--`, `ε`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `loop_stmt` | → | { `do`, `for`, `while` } |
| `m_comment` | → | { `/*`, `ε` } |
| `main_body` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` } |
| `main_func` | → | { `int` } |
| `mult_div_modulo_cont` | → | { `%`, `*`, `/`, `ε` } |
| `multi_arg` | → | { `,`, `ε` } |
| `multi_dec` | → | { `,`, `ε` } |
| `mutability` | → | { `const`, `var` } |
| `num_lit_type` | → | { `frac_lit`, `whole_lit` } |
| `output_stmt` | → | { `thread` } |
| `param` | → | { `ε`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `param_2D` | → | { `ε`, `[` } |
| `param_cont` | → | { `,`, `ε` } |
| `param_struct` | → | { `ε`, `[` } |
| `param_type` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `primary` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `program` | → | { `/*`, `//`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `rel_expr` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `rel_expr_cont` | → | { `!=`, `<`, `=`, `>`, `ε` } |
| `ret_2D` | → | { `ε`, `[` } |
| `ret_ctrl_body` | → | { `ε`, `return` } |
| `ret_stmt` | → | { `return` } |
| `ret_struct` | → | { `.`, `ε`, `[` } |
| `ret_type` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string`, `void` } |
| `ret_value` | → | { `(`, `++`, `-`, `--`, `ε`, `boollit`, `charlit`, `doublelit`, `floatlit`, `frac_lit`, `id`, `intlit`, `longlit`, `stringlit`, `whole_lit` } |
| `s_comment` | → | { `//`, `ε` } |
| `size` | → | { `intlit` } |
| `statement` | → | { `(`, `++`, `-`, `--`, `ε`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `statement_list` | → | { `(`, `++`, `-`, `--`, `ε`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `string_expr` | → | { `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `stringlit` } |
| `string_value` | → | { `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `stringlit` } |
| `switch_stmt` | → | { `switch` } |
| `switch_val` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `intlit`, `stringlit`, `whole_lit` } |
| `term` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `typecast_expr` | → | { `(` } |
| `up_post` | → | { `++`, `--` } |
| `update` | → | { `++`, `--`, `ε`, `id` } |
| `value` | → | { `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `weave_def` | → | { `weave` } |
| `weave_id` | → | { `id` } |
| `while_stmt` | → | { `while` } |

---

## FOLLOW Sets

**The FOLLOW set of a non-terminal contains all terminals that can appear immediately to the right of that non-terminal in some sentential form.**

> **Notation:** Sets are displayed using curly braces `{ }`. `$` represents the end-of-input marker.

| Non-Terminal | → | FOLLOW Set |
|--------------|--|------------|
| `I_O_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `add_min_cont` | → | { `!=`, `&&`, `(`, `)`, `++`, `-`, `--`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `arg` | → | { `)`, `,` } |
| `arith_expr` | → | { `!=`, `&&`, `(`, `)`, `++`, `-`, `--`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `arr_1D` | → | { `;` } |
| `arr_1D_init` | → | { `;` } |
| `arr_1D_tail` | → | { `;` } |
| `arr_2D` | → | { `;` } |
| `arr_2D_UD` | → | { `;` } |
| `arr_2D_init` | → | { `;`, `=` } |
| `arr_dtype` | → | { `id` } |
| `array_spec_2D` | → | { `%=`, `*=`, `+=`, `-=`, `/=`, `=` } |
| `array_spec_opt` | → | { `%=`, `*=`, `+=`, `-=`, `/=`, `=` } |
| `assign_stmt` | → | { `;` } |
| `assign_stmt_op` | → | { `;` } |
| `atom` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `case_stmt` | → | { `case`, `default`, `}` } |
| `case_stmt_cont` | → | { `case`, `default`, `}` } |
| `case_val` | → | { `:` } |
| `cast_val` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `condition` | → | { `)`, `;` } |
| `conditional_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `ctrl_body` | → | { `break`, `return`, `}` } |
| `ctrl_struct` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `default_stmt` | → | { `}` } |
| `do_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `dtype` | → | { `)`, `id` } |
| `elem_1D_list` | → | { `}` } |
| `elem_1D_list_tail` | → | { `}` } |
| `elem_2D_list` | → | { `}` } |
| `elem_2D_list_tail` | → | { `}` } |
| `else_if_ei_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `else_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `equal_sym` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `expr1_cont` | → | { `)` } |
| `expression` | → | { `;` } |
| `expression1` | → | { `)` } |
| `factor` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `field_array_spec_opt` | → | { `,`, `;` } |
| `field_dec` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string`, `}` } |
| `field_dec_cont` | → | { `;` } |
| `field_list` | → | { `}` } |
| `field_type` | → | { `id` } |
| `for_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `function` | → | { `/*`, `//`, `int` } |
| `function_body` | → | { `}` } |
| `function_call` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `function_def` | → | { `/*`, `//`, `func`, `int` } |
| `global_dec` | → | { `/*`, `//`, `func`, `int` } |
| `iden` | → | { `)` } |
| `iden1` | → | { `)` } |
| `iden1_cont` | → | { `)` } |
| `iden1_tail` | → | { `)` } |
| `iden1_weave` | → | { `)` } |
| `iden_val` | → | { `)` } |
| `if_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `import_block` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `import_cont` | → | { `;` } |
| `import_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` } |
| `initializer` | → | { `;` } |
| `input_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `isize` | → | { `)` } |
| `local_block` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `local_dec` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `logical_expr` | → | { `)`, `;` } |
| `logical_expr_cont` | → | { `)`, `;` } |
| `loop_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `m_comment` | → | { `$`, `/*`, `//`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `main_body` | → | { `}` } |
| `main_func` | → | { `$`, `/*`, `//` } |
| `mult_div_modulo_cont` | → | { `!=`, `&&`, `(`, `)`, `+`, `++`, `-`, `--`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `multi_arg` | → | { `)` } |
| `multi_dec` | → | { `;` } |
| `mutability` | → | { `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `num_lit_type` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `output_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `param` | → | { `)` } |
| `param_2D` | → | { `)`, `,`, `id` } |
| `param_cont` | → | { `)` } |
| `param_struct` | → | { `)`, `,`, `id` } |
| `param_type` | → | { `id` } |
| `primary` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `program` | → | { `$` } |
| `rel_expr` | → | { `&&`, `(`, `)`, `++`, `-`, `--`, `;`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `rel_expr_cont` | → | { `&&`, `(`, `)`, `++`, `-`, `--`, `;`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `ret_2D` | → | { `id` } |
| `ret_ctrl_body` | → | { `break`, `return`, `}` } |
| `ret_stmt` | → | { `break`, `return`, `}` } |
| `ret_struct` | → | { `id` } |
| `ret_type` | → | { `id` } |
| `ret_value` | → | { `;` } |
| `s_comment` | → | { `$`, `/*`, `//`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `size` | → | { `]` } |
| `statement` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `statement_list` | → | { `break`, `return`, `}` } |
| `string_expr` | → | { `)`, `..` } |
| `string_value` | → | { `)`, `..` } |
| `switch_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `switch_val` | → | { `)` } |
| `term` | → | { `!=`, `&&`, `(`, `)`, `+`, `++`, `-`, `--`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `typecast_expr` | → | { `)`, `..` } |
| `up_post` | → | { `)` } |
| `update` | → | { `)` } |
| `value` | → | { `)`, `,`, `..`, `:`, `;`, `}` } |
| `weave_def` | → | { `/*`, `//`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `weave_id` | → | { `id` } |
| `while_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |

---

## Summary Statistics

### FIRST Sets

- **Average FIRST set size**: 5.17
- **Largest FIRST set**: `function_body` with 27 elements
- **Non-terminals with ε**: 49

### FOLLOW Sets

- **Average FOLLOW set size**: 8.39
- **Largest FOLLOW set**: `local_dec` with 28 elements

---

**Legend:**
- `EPSILON` or `ε`: Represents empty/null production
- `$`: End-of-input marker
