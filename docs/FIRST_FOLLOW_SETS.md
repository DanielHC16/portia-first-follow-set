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
| `program` | → | { `/*`, `//`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `s_comment` | → | { `//`, `ε` } |
| `m_comment` | → | { `/*`, `ε` } |
| `global_dec` | → | { `ε`, `bool`, `char`, `double`, `float`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `mutability` | → | { `const`, `var` } |
| `multi_dec` | → | { `,`, `ε` } |
| `dtype` | → | { `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `value` | → | { `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `arr_1D` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `arr_dtype` | → | { `ε`, `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `arr_1D_tail` | → | { `=`, `ε`, `[` } |
| `arr_1D_init` | → | { `=` } |
| `elem_1D_list` | → | { `ε`, `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `elem_1D_list_tail` | → | { `,`, `ε` } |
| `arr_2D` | → | { `[` } |
| `arr_2D_init` | → | { `=`, `ε` } |
| `arr_2D_UD` | → | { `=`, `ε` } |
| `elem_2D_list` | → | { `ε`, `{` } |
| `elem_2D_list_tail` | → | { `,`, `ε` } |
| `weave_def` | → | { `weave` } |
| `field_list` | → | { `ε`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `field_dec` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `field_dec_cont` | → | { `,`, `ε` } |
| `field_array_spec_opt` | → | { `ε`, `[` } |
| `field_type` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `weave_id` | → | { `id` } |
| `size` | → | { `intlit` } |
| `function` | → | { `ε`, `func` } |
| `function_def` | → | { `func` } |
| `ret_type` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string`, `void` } |
| `ret_struct` | → | { `.`, `ε`, `[` } |
| `ret_2D` | → | { `ε`, `[` } |
| `param` | → | { `ε`, `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `param_type` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string` } |
| `param_struct` | → | { `ε`, `[` } |
| `param_2D` | → | { `ε`, `[` } |
| `param_cont` | → | { `,`, `ε` } |
| `function_body` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` } |
| `import_block` | → | { `ε`, `using` } |
| `import_stmt` | → | { `using` } |
| `import_cont` | → | { `,`, `ε` } |
| `local_block` | → | { `ε`, `local` } |
| `local_dec` | → | { `local` } |
| `statement_list` | → | { `(`, `++`, `-`, `--`, `ε`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `statement` | → | { `(`, `++`, `-`, `--`, `ε`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `expression` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `logical_expr` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `logical_expr_cont` | → | { `&&`, `(`, `++`, `-`, `--`, `ε`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `rel_expr` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `rel_expr_cont` | → | { `!=`, `<`, `=`, `>`, `ε` } |
| `equal_sym` | → | { `=`, `ε` } |
| `arith_expr` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `add_min_cont` | → | { `+`, `-`, `ε` } |
| `term` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `mult_div_modulo_cont` | → | { `%`, `*`, `/`, `ε` } |
| `factor` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `primary` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `cast_val` | → | { `(` } |
| `atom` | → | { `++`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `num_lit_type` | → | { `frac_lit`, `whole_lit` } |
| `I_O_stmt` | → | { `thread`, `trap` } |
| `input_stmt` | → | { `trap` } |
| `iden` | → | { `id` } |
| `iden_val` | → | { `.`, `ε`, `[` } |
| `isize` | → | { `ε`, `[` } |
| `output_stmt` | → | { `thread` } |
| `expression1` | → | { `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `string_lit`, `stringlit` } |
| `expr1_cont` | → | { `,`, `ε` } |
| `string_expr` | → | { `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `stringlit` } |
| `string_value` | → | { `(`, `boollit`, `charlit`, `doublelit`, `floatlit`, `id`, `intlit`, `longlit`, `stringlit` } |
| `typecast_expr` | → | { `(` } |
| `function_call` | → | { `id` } |
| `arg` | → | { `ε`, `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `multi_arg` | → | { `,`, `ε` } |
| `iden1` | → | { `id` } |
| `iden1_weave` | → | { `.`, `[` } |
| `iden1_tail` | → | { `ε`, `[` } |
| `iden1_cont` | → | { `,`, `ε` } |
| `assign_stmt` | → | { `id` } |
| `array_spec_opt` | → | { `ε`, `[` } |
| `array_spec_2D` | → | { `ε`, `[` } |
| `assign_stmt_op` | → | { `%=`, `*=`, `+=`, `-=`, `/=`, `=` } |
| `ctrl_struct` | → | { `do`, `for`, `if`, `switch`, `while` } |
| `conditional_stmt` | → | { `if`, `switch` } |
| `if_stmt` | → | { `if` } |
| `condition` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `else_if_ei_stmt` | → | { `ε`, `else` } |
| `else_stmt` | → | { `if`, `{` } |
| `switch_stmt` | → | { `switch` } |
| `switch_val` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `intlit`, `stringlit`, `whole_lit` } |
| `case_stmt` | → | { `case` } |
| `case_stmt_cont` | → | { `ε`, `case` } |
| `case_val` | → | { `boollit`, `charlit`, `doublelit`, `floatlit`, `intlit`, `longlit`, `stringlit` } |
| `ctrl_body` | → | { `(`, `++`, `-`, `--`, `ε`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `ret_ctrl_body` | → | { `ε`, `return` } |
| `default_stmt` | → | { `ε`, `default` } |
| `loop_stmt` | → | { `do`, `for`, `while` } |
| `for_stmt` | → | { `for` } |
| `initializer` | → | { `ε`, `id`, `local` } |
| `update` | → | { `++`, `--`, `ε`, `id` } |
| `up_post` | → | { `++`, `--` } |
| `while_stmt` | → | { `while` } |
| `do_stmt` | → | { `do` } |
| `ret_stmt` | → | { `return` } |
| `ret_value` | → | { `(`, `++`, `-`, `--`, `ε`, `boollit`, `charlit`, `doublelit`, `floatlit`, `frac_lit`, `id`, `intlit`, `longlit`, `stringlit`, `whole_lit` } |
| `main_func` | → | { `int` } |
| `main_body` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` } |

---

## FOLLOW Sets

**The FOLLOW set of a non-terminal contains all terminals that can appear immediately to the right of that non-terminal in some sentential form.**

> **Notation:** Sets are displayed using curly braces `{ }`. `$` represents the end-of-input marker.

| Non-Terminal | → | FOLLOW Set |
|--------------|--|------------|
| `program` | → | { `$` } |
| `s_comment` | → | { `$`, `/*`, `//`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `m_comment` | → | { `$`, `/*`, `//`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `global_dec` | → | { `/*`, `//`, `func`, `int` } |
| `mutability` | → | { `bool`, `char`, `double`, `float`, `int`, `long`, `string` } |
| `multi_dec` | → | { `;` } |
| `dtype` | → | { `)`, `id` } |
| `value` | → | { `)`, `,`, `..`, `:`, `;`, `}` } |
| `arr_1D` | → | { `;` } |
| `arr_dtype` | → | { `id` } |
| `arr_1D_tail` | → | { `;` } |
| `arr_1D_init` | → | { `;` } |
| `elem_1D_list` | → | { `}` } |
| `elem_1D_list_tail` | → | { `}` } |
| `arr_2D` | → | { `;` } |
| `arr_2D_init` | → | { `;`, `=` } |
| `arr_2D_UD` | → | { `;` } |
| `elem_2D_list` | → | { `}` } |
| `elem_2D_list_tail` | → | { `}` } |
| `weave_def` | → | { `/*`, `//`, `bool`, `char`, `double`, `float`, `func`, `global`, `id`, `int`, `long`, `string`, `weave` } |
| `field_list` | → | { `}` } |
| `field_dec` | → | { `bool`, `char`, `double`, `float`, `id`, `int`, `long`, `string`, `}` } |
| `field_dec_cont` | → | { `;` } |
| `field_array_spec_opt` | → | { `,`, `;` } |
| `field_type` | → | { `id` } |
| `weave_id` | → | { `id` } |
| `size` | → | { `]` } |
| `function` | → | { `/*`, `//`, `int` } |
| `function_def` | → | { `/*`, `//`, `func`, `int` } |
| `ret_type` | → | { `id` } |
| `ret_struct` | → | { `id` } |
| `ret_2D` | → | { `id` } |
| `param` | → | { `)` } |
| `param_type` | → | { `id` } |
| `param_struct` | → | { `)`, `,`, `id` } |
| `param_2D` | → | { `)`, `,`, `id` } |
| `param_cont` | → | { `)` } |
| `function_body` | → | { `}` } |
| `import_block` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit` } |
| `import_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `using`, `while`, `whole_lit` } |
| `import_cont` | → | { `;` } |
| `local_block` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `local_dec` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `local`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `statement_list` | → | { `break`, `return`, `}` } |
| `statement` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `expression` | → | { `;` } |
| `logical_expr` | → | { `)`, `;` } |
| `logical_expr_cont` | → | { `)`, `;` } |
| `rel_expr` | → | { `&&`, `(`, `)`, `++`, `-`, `--`, `;`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `rel_expr_cont` | → | { `&&`, `(`, `)`, `++`, `-`, `--`, `;`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `equal_sym` | → | { `(`, `++`, `-`, `--`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `arith_expr` | → | { `!=`, `&&`, `(`, `)`, `++`, `-`, `--`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `add_min_cont` | → | { `!=`, `&&`, `(`, `)`, `++`, `-`, `--`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `term` | → | { `!=`, `&&`, `(`, `)`, `+`, `++`, `-`, `--`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `mult_div_modulo_cont` | → | { `!=`, `&&`, `(`, `)`, `+`, `++`, `-`, `--`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `factor` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `primary` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `cast_val` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `atom` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `num_lit_type` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `I_O_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `input_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `iden` | → | { `)` } |
| `iden_val` | → | { `)` } |
| `isize` | → | { `)` } |
| `output_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `expression1` | → | { `)` } |
| `expr1_cont` | → | { `)` } |
| `string_expr` | → | { `)`, `..` } |
| `string_value` | → | { `)`, `..` } |
| `typecast_expr` | → | { `)`, `..` } |
| `function_call` | → | { `!=`, `%`, `&&`, `(`, `)`, `*`, `+`, `++`, `-`, `--`, `..`, `/`, `;`, `<`, `=`, `>`, `boollit`, `charlit`, `frac_lit`, `id`, `stringlit`, `whole_lit` } |
| `arg` | → | { `)`, `,` } |
| `multi_arg` | → | { `)` } |
| `iden1` | → | { `)` } |
| `iden1_weave` | → | { `)` } |
| `iden1_tail` | → | { `)` } |
| `iden1_cont` | → | { `)` } |
| `assign_stmt` | → | { `;` } |
| `array_spec_opt` | → | { `%=`, `*=`, `+=`, `-=`, `/=`, `=` } |
| `array_spec_2D` | → | { `%=`, `*=`, `+=`, `-=`, `/=`, `=` } |
| `assign_stmt_op` | → | { `;` } |
| `ctrl_struct` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `conditional_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `if_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `condition` | → | { `)`, `;` } |
| `else_if_ei_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `else_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `switch_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `switch_val` | → | { `)` } |
| `case_stmt` | → | { `case`, `default`, `}` } |
| `case_stmt_cont` | → | { `case`, `default`, `}` } |
| `case_val` | → | { `:` } |
| `ctrl_body` | → | { `break`, `return`, `}` } |
| `ret_ctrl_body` | → | { `break`, `return`, `}` } |
| `default_stmt` | → | { `}` } |
| `loop_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `for_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `initializer` | → | { `;` } |
| `update` | → | { `)` } |
| `up_post` | → | { `)` } |
| `while_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `do_stmt` | → | { `(`, `++`, `-`, `--`, `bool`, `boollit`, `break`, `char`, `charlit`, `do`, `double`, `float`, `for`, `frac_lit`, `id`, `if`, `int`, `long`, `return`, `string`, `stringlit`, `switch`, `thread`, `trap`, `while`, `whole_lit`, `}` } |
| `ret_stmt` | → | { `break`, `return`, `}` } |
| `ret_value` | → | { `;` } |
| `main_func` | → | { `$`, `/*`, `//` } |
| `main_body` | → | { `}` } |

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
