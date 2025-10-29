"""
PORTIA First & Follow Set Calculator
Main entry point for the application
"""

import os
from grammar_parser import GrammarParser
from first_set import FirstSetCalculator
from follow_set import FollowSetCalculator


def main():
    """
    Main function to run the First & Follow set calculator
    """
    print("=" * 70)
    print(" " * 15 + "PORTIA First & Follow Set Generator")
    print("=" * 70)
    print()
    
    # Get the grammar file path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    grammar_file = os.path.join(project_dir, 'grammar', 'CFG.txt')
    
    print(f"Reading grammar from: {grammar_file}")
    print()
    
    # Parse the grammar
    print("Parsing grammar...")
    parser = GrammarParser(grammar_file)
    parser.parse()
    print(f"✓ Found {len(parser.non_terminals)} non-terminals")
    print(f"✓ Found {len(parser.terminals)} terminals")
    print(f"✓ Start symbol: {parser.start_symbol}")
    print()
    
    # Compute FIRST sets
    print("Computing FIRST sets...")
    first_calc = FirstSetCalculator(parser)
    first_sets = first_calc.compute_first_sets()
    print(f"✓ FIRST sets computed for {len([k for k in first_sets.keys() if k in parser.non_terminals])} non-terminals")
    print()
    
    # Compute FOLLOW sets
    print("Computing FOLLOW sets...")
    follow_calc = FollowSetCalculator(parser, first_calc)
    follow_sets = follow_calc.compute_follow_sets()
    print(f"✓ FOLLOW sets computed for {len(follow_sets)} non-terminals")
    print()
    
    # Save raw output
    raw_output_file = os.path.join(project_dir, 'output', 'FIRST_FOLLOW_RAW.txt')
    os.makedirs(os.path.dirname(raw_output_file), exist_ok=True)
    
    print("Generating output files...")
    save_raw_output(parser, first_sets, follow_sets, raw_output_file)
    print(f"✓ Raw output saved to: output/FIRST_FOLLOW_RAW.txt")
    
    # Save visualized output
    viz_output_file = os.path.join(project_dir, 'docs', 'FIRST_FOLLOW_SETS.md')
    save_visualized_output(parser, first_sets, follow_sets, viz_output_file)
    print(f"✓ Visualized output saved to: docs/FIRST_FOLLOW_SETS.md")
    
    print()
    print("=" * 70)
    print(" " * 25 + "Generation Complete!")
    print("=" * 70)


def save_raw_output(parser, first_sets, follow_sets, output_file):
    """
    Save FIRST and FOLLOW sets in raw format
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("PORTIA FIRST AND FOLLOW SETS (RAW FORMAT)\n")
        f.write("=" * 70 + "\n\n")
        
        # FIRST sets
        f.write("FIRST SETS\n")
        f.write("-" * 70 + "\n\n")
        
        # Sort non-terminals for consistent output
        non_terminals = sorted(parser.non_terminals)
        
        for nt in non_terminals:
            first_set = sorted(first_sets.get(nt, set()))
            f.write(f"FIRST({nt}) = {{ {', '.join(first_set)} }}\n")
        
        f.write("\n" + "=" * 70 + "\n\n")
        
        # FOLLOW sets
        f.write("FOLLOW SETS\n")
        f.write("-" * 70 + "\n\n")
        
        for nt in non_terminals:
            follow_set = sorted(follow_sets.get(nt, set()))
            f.write(f"FOLLOW({nt}) = {{ {', '.join(follow_set)} }}\n")


def save_visualized_output(parser, first_sets, follow_sets, output_file):
    """
    Save FIRST and FOLLOW sets in visualized Markdown format
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# PORTIA First & Follow Sets\n\n")
        f.write("> **Generated from PORTIA CFG** | EBNF Grammar Specification\n\n")
        f.write("---\n\n")
        
        # Table of contents
        f.write("## 📋 Contents\n\n")
        f.write("- [Overview](#overview)\n")
        f.write("- [FIRST Sets](#first-sets)\n")
        f.write("- [FOLLOW Sets](#follow-sets)\n")
        f.write("- [Summary Statistics](#summary-statistics)\n\n")
        f.write("---\n\n")
        
        # Overview
        f.write("## Overview\n\n")
        f.write("This document contains the computed FIRST and FOLLOW sets for the PORTIA programming language grammar.\n\n")
        f.write(f"- **Total Non-terminals**: {len(parser.non_terminals)}\n")
        f.write(f"- **Total Terminals**: {len(parser.terminals) - 1}\n")  # Exclude $
        f.write(f"- **Start Symbol**: `{parser.start_symbol}`\n\n")
        
        # FIRST sets
        f.write("---\n\n")
        f.write("## FIRST Sets\n\n")
        f.write("**The FIRST set of a non-terminal contains all terminals that can appear as the first symbol of any string derived from that non-terminal.**\n\n")
        f.write("> **Notation:** Sets are displayed using curly braces `{ }`. `ε` represents epsilon (empty/null production).\n\n")
        
        # Create table
        f.write("| Non-Terminal | → | FIRST Set |\n")
        f.write("|--------------|--||-----------|\n")
        
        non_terminals = sorted(parser.non_terminals)
        for nt in non_terminals:
            first_set = sorted(first_sets.get(nt, set()))
            # Replace EPSILON with ε for better visualization
            first_set_display = [s.replace('EPSILON', 'ε') for s in first_set]
            first_str = ', '.join([f'`{s}`' for s in first_set_display])
            f.write(f"| `{nt}` | → | {{ {first_str} }} |\n")
        
        # FOLLOW sets
        f.write("\n---\n\n")
        f.write("## FOLLOW Sets\n\n")
        f.write("**The FOLLOW set of a non-terminal contains all terminals that can appear immediately to the right of that non-terminal in some sentential form.**\n\n")
        f.write("> **Notation:** Sets are displayed using curly braces `{ }`. `$` represents the end-of-input marker.\n\n")
        
        # Create table
        f.write("| Non-Terminal | → | FOLLOW Set |\n")
        f.write("|--------------|--|------------|\n")
        
        for nt in non_terminals:
            follow_set = sorted(follow_sets.get(nt, set()))
            follow_str = ', '.join([f'`{s}`' for s in follow_set])
            f.write(f"| `{nt}` | → | {{ {follow_str} }} |\n")
        
        # Statistics
        f.write("\n---\n\n")
        f.write("## Summary Statistics\n\n")
        
        # FIRST set statistics
        avg_first = sum(len(first_sets.get(nt, set())) for nt in parser.non_terminals) / len(parser.non_terminals)
        max_first_nt = max(parser.non_terminals, key=lambda nt: len(first_sets.get(nt, set())))
        max_first_size = len(first_sets.get(max_first_nt, set()))
        
        f.write("### FIRST Sets\n\n")
        f.write(f"- **Average FIRST set size**: {avg_first:.2f}\n")
        f.write(f"- **Largest FIRST set**: `{max_first_nt}` with {max_first_size} elements\n")
        f.write(f"- **Non-terminals with ε**: {sum(1 for nt in parser.non_terminals if 'EPSILON' in first_sets.get(nt, set()))}\n\n")
        
        # FOLLOW set statistics
        avg_follow = sum(len(follow_sets.get(nt, set())) for nt in parser.non_terminals) / len(parser.non_terminals)
        max_follow_nt = max(parser.non_terminals, key=lambda nt: len(follow_sets.get(nt, set())))
        max_follow_size = len(follow_sets.get(max_follow_nt, set()))
        
        f.write("### FOLLOW Sets\n\n")
        f.write(f"- **Average FOLLOW set size**: {avg_follow:.2f}\n")
        f.write(f"- **Largest FOLLOW set**: `{max_follow_nt}` with {max_follow_size} elements\n\n")
        
        f.write("---\n\n")
        f.write("**Legend:**\n")
        f.write("- `EPSILON` or `ε`: Represents empty/null production\n")
        f.write("- `$`: End-of-input marker\n")


if __name__ == "__main__":
    main()
