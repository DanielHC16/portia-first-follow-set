# First & Follow Set Calculator - Implementation Guide

## Algorithm Overview

### FIRST Set Computation

The FIRST set of a symbol α (terminal or non-terminal) is the set of terminals that can appear as the first symbol of strings derived from α.

**Rules:**
1. If X is a terminal, then FIRST(X) = {X}
2. If X is a non-terminal and X → ε is a production, then add ε to FIRST(X)
3. If X → Y₁Y₂...Yₖ is a production:
   - Add FIRST(Y₁) - {ε} to FIRST(X)
   - If ε is in FIRST(Y₁), add FIRST(Y₂) - {ε} to FIRST(X)
   - Continue for Y₃, Y₄, ... as long as ε is in FIRST of previous symbols
   - If ε is in FIRST of all Yᵢ, add ε to FIRST(X)

### FOLLOW Set Computation

The FOLLOW set of a non-terminal A is the set of terminals that can appear immediately to the right of A in some sentential form.

**Rules:**
1. Place $ (end marker) in FOLLOW(S) where S is the start symbol
2. If A → αBβ is a production:
   - Add FIRST(β) - {ε} to FOLLOW(B)
   - If ε is in FIRST(β), add FOLLOW(A) to FOLLOW(B)
3. If A → αB is a production:
   - Add FOLLOW(A) to FOLLOW(B)

## Implementation Steps

1. **Parse Grammar**: Read and parse the EBNF grammar from CFG.txt
2. **Identify Symbols**: Separate terminals from non-terminals
3. **Build Production Map**: Create data structure mapping non-terminals to their productions
4. **Compute FIRST Sets**: Iteratively compute FIRST sets until no changes occur
5. **Compute FOLLOW Sets**: Iteratively compute FOLLOW sets until no changes occur
6. **Output Results**: Format and display the results

## Example

For the production:
```
A -> B C | d
B -> e | EPSILON
C -> f
```

**FIRST Sets:**
- FIRST(A) = {e, d, f}
- FIRST(B) = {e, ε}
- FIRST(C) = {f}

**FOLLOW Sets:**
- FOLLOW(A) = {$}
- FOLLOW(B) = {f}
- FOLLOW(C) = {FOLLOW(A)} = {$}

## Data Structures

```python
# Example structure (pseudocode)
grammar = {
    'A': [['B', 'C'], ['d']],
    'B': [['e'], ['EPSILON']],
    'C': [['f']]
}

first = {
    'A': set(),
    'B': set(),
    'C': set()
}

follow = {
    'A': set(),
    'B': set(),
    'C': set()
}
```
