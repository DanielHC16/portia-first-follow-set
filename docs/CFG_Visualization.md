# Context-Free Grammar (CFG) - Visualization

> **Note:** ε represents epsilon (empty/null production)

---

## 📋 Table of Contents

- [Program Structure](#program-structure)
- [Comments](#comments)
- [Global Declarations](#global-declarations)
- [Data Types & Values](#data-types--values)
- [Array Declarations](#array-declarations)
- [Weave (Struct) Definitions](#weave-struct-definitions)
- [Function Definitions](#function-definitions)
- [Imports & Local Declarations](#imports--local-declarations)
- [Statements](#statements)
- [Expressions](#expressions)
- [Input/Output Statements](#inputoutput-statements)
- [Function Calls](#function-calls)
- [Assignment Statements](#assignment-statements)
- [Control Structures](#control-structures)
- [Return Statements](#return-statements)

---

## Program Structure

```
program         → s_comment m_comment global_dec s_comment m_comment 
                  function s_comment m_comment main_func s_comment m_comment

main_func       → int main ( ) { main_body }

main_body       → import_block local_block statement_list return intlit ;
```

---

## Comments

**Note**: Comment productions are placed early in the grammar (productions 2-3) to establish proper structure.

```
s_comment       → // comment
                | ε

m_comment       → /* comments */
                | ε
```

---

## Global Declarations

```
global_dec      → global mutability dtype id = value multi_dec ; global_dec
                | arr_1D ; global_dec
                | weave_def global_dec
                | ε

mutability      → var
                | const

multi_dec       → , id = value multi_dec
                | ε
```

---

## Data Types & Values

```
dtype           → int | long | float | double | char | string | bool

value           → intlit | longlit | floatlit | doublelit 
                | charlit | stringlit | boollit

size            → intlit

data_type       → dtype
```

---

## Array Declarations

### 1D Arrays

```
arr_1D          → dtype id [ size ] arr_1D_init arr_2D arr_1D
                | arr_1D_UD
                | ε

arr_1D_init     → { arr_value_1D }
                | ε

arr_value_1D    → arr_1D_cont
                | arr_1D_cont_val

arr_1D_cont     → value arr_1D_cont_val }
                | ε

arr_1D_cont_val → , value arr_1D_cont_val
                | ε

arr_1D_UD       → id [ size ] = value ; arr_1D_UD
                | ε
```

### 2D Arrays

```
arr_2D          → arr_2_2D
                | ε

arr_2_2D        → [ size ] arr_2D_init

arr_2D_init     → ε
                | { arr_value_2D }

arr_value_2D    → { arr_1D_cont } arr_value_2D_cont

arr_value_2D_cont → , { arr_1D_cont } arr_value_2D_cont
                  | ε
```

---

## Weave (Struct) Definitions

```
weave_def       → weave id { field_list }

field_list      → field_dec field_list
                | ε

field_dec       → field_type id array_spec_opt field_dec_cont ;

field_dec_cont  → , id field_dec_cont
                | ε

array_spec_opt  → [ size ]
                | ε

field_type      → dtype
                | weave_id

weave_id        → id
```

---

## Function Definitions

```
function        → function_def function
                | ε

function_def    → func ret_type id ( param ) { function_body }

ret_type        → dtype
                | void

param           → dtype id param_cont
                | ε

param_cont      → , dtype id param_cont
                | ε

function_body   → import_block local_block statement_list ret_stmt
```

---

## Imports & Local Declarations

### Imports

```
import_block    → import_stmt import_block
                | ε

import_stmt     → using id import_cont ;

import_cont     → , id import_cont
                | ε
```

### Local Declarations

```
local_block     → local_dec local_block
                | ε

local_dec       → local mutability dtype id = value multi_dec ;
```

---

## Statements

```
statement_list  → statement statement_list
                | ε

statement       → expression ;
                | I_O_stmt
                | assign_stmt ;
                | ctrl_struct
```

---

## Expressions

### Logical Expressions

```
expression      → logical_expr

logical_expr    → rel_expr logical_expr_cont

logical_expr_cont → && rel_expr logical_expr_cont
                  | || rel_expr logical_expr_cont
                  | ε
```

### Relational Expressions

```
rel_expr        → arith_expr rel_expr_cont

rel_expr_cont   → = equal_sym arith_expr rel_expr_cont
                | != arith_expr rel_expr_cont
                | > equal_sym arith_expr rel_expr_cont
                | < equal_sym arith_expr rel_expr_cont
                | ε

equal_sym       → =
                | ε
```

### Arithmetic Expressions

```
arith_expr      → term add_min_cont

add_min_cont    → + term add_min_cont
                | - term add_min_cont
                | ε

term            → factor mult_div_modulo_cont

mult_div_modulo_cont → * factor mult_div_modulo_cont
                     | / factor mult_div_modulo_cont
                     | ε
```

### Factors

```
factor          → numeric_factor

numeric_factor  → - numeric_factor
                | ( cast_val )
                | numeric_atom
                | ( arith_expr )

cast_val        → data_type ) factor
                | value )

numeric_atom    → num_lit_type
                | function_call
                | -- id
                | ++ id

num_lit_type    → whole_lit
                | frac_lit

typecast_expr   → ( data_type ) expression
```

---

## Input/Output Statements

### Input

```
I_O_stmt        → input_stmt
                | output_stmt

input_stmt      → trap ( iden ) ;

iden            → id iden_val

iden_val        → isize
                | . id
                | ε

isize           → [ size ]
                | ε
```

### Output

```
output_stmt     → thread ( expression1 ) ;

expression1     → id expr1_cont
                | value
                | string_expr
                | string_lit
                | iden1

expr1_cont      → , id expr1_cont
                | ε

string_expr     → string_value .. string_value

string_value    → stringlit
                | string_expr
                | typecast_expr
                | function_call
                | value
```

---

## Function Calls

```
function_call   → id ( arg multi_arg )

arg             → value
                | ε

multi_arg       → , id ( arg ) multi_arg
                | ε

iden1           → id [ size ]
                | id . id iden1_cont

iden1_cont      → , id . id iden1_cont
                | ε
```

---

## Assignment Statements

```
assign_stmt     → id array_spec_opt assign_stmt_op

assign_stmt_op  → = value
                | += value
                | -= value
                | *= value
                | /= value
                | %= value
```

---

## Control Structures

### Control Body

```
ctrl_struct     → conditional_stmt
                | loop_stmt
                | ε

ctrl_body       → local_dec expression input_stmt output_stmt 
                  assign_stmt ctrl_struct
```

### Conditional Statements

```
conditional_stmt → if_stmt
                 | switch_stmt
                 | ε

if_stmt         → if ( condition ) { ctrl_body ret_stmt } else_if_ei_stmt

condition       → logical_expr

else_if_ei_stmt → else else_stmt
                | ε

else_stmt       → if_stmt
                | { ctrl_body ret_stmt }
```

### Switch Statement

```
switch_stmt     → switch ( switch_val ) { case_stmt default_stmt }

switch_val      → id
                | intlit
                | stringlit
                | arith_expr

case_stmt       → case case_val : ctrl_body break ; case_stmt_cont

case_stmt_cont  → case_stmt case_stmt_cont
                | ε

case_val        → id

default_stmt    → default ctrl_body
                | ε
```

### Loop Statements

```
loop_stmt       → for_stmt
                | while_stmt
                | do_stmt

for_stmt        → for ( initializer ; condition ; update ) { ctrl_body }

initializer     → local var dtype id = value multi_dec
                | assign_stmt
                | ε

update          → ++ id
                | -- id
                | id up_post
                | ε

up_post         → ++
                | --

while_stmt      → while ( condition ) { ctrl_body }

do_stmt         → do { ctrl_body } while ( condition ) ;
```

---

## Return Statements

```
ret_stmt        → return ret_value ;

ret_value       → value
                | id
                | logical_expr
                | ε
```

---

## Production Summary

| Category | Non-Terminals |
|----------|---------------|
| **Program** | program, main_func, main_body |
| **Comments** | s_comment, m_comment |
| **Declarations** | global_dec, local_dec, mutability, multi_dec |
| **Data Types** | dtype, value, size, data_type |
| **Arrays** | arr_1D, arr_2D, arr_1D_init, arr_2D_init, arr_value_1D, arr_value_2D |
| **Structs** | weave_def, field_list, field_dec, field_type, weave_id |
| **Functions** | function, function_def, ret_type, param, function_body |
| **Imports** | import_block, import_stmt |
| **Statements** | statement, statement_list |
| **Expressions** | expression, logical_expr, rel_expr, arith_expr, term, factor |
| **I/O** | I_O_stmt, input_stmt, output_stmt |
| **Assignment** | assign_stmt, assign_stmt_op |
| **Control Flow** | ctrl_struct, conditional_stmt, loop_stmt, if_stmt, switch_stmt, for_stmt, while_stmt, do_stmt |
| **Return** | ret_stmt, ret_value |

---

**Legend:**
- `→` : Production rule (derives to)
- `|` : Alternative production (or)
- `ε` : Epsilon (empty/null production)
- **Terminals** are lowercase or special symbols (e.g., `int`, `+`, `{`, etc.)
- **Non-terminals** are production rule names (e.g., `expr`, `stmt`, etc.)
