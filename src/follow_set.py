"""
Follow Set Calculator Module
Computes FOLLOW sets for all non-terminals in the grammar
"""

class FollowSetCalculator:
    """
    Calculates FOLLOW sets for non-terminals
    """
    
    def __init__(self, grammar_parser, first_calculator):
        """
        Initialize with parsed grammar and FIRST sets
        
        Args:
            grammar_parser: GrammarParser instance
            first_calculator: FirstSetCalculator instance
        """
        self.parser = grammar_parser
        self.first_calc = first_calculator
        self.follow_sets = {}
    
    def compute_follow_sets(self):
        """
        Compute FOLLOW sets for all non-terminals
        
        Returns:
            dict: Dictionary mapping non-terminals to their FOLLOW sets
        """
        # Initialize FOLLOW sets
        for non_terminal in self.parser.non_terminals:
            self.follow_sets[non_terminal] = set()
        
        # Add $ to FOLLOW of start symbol
        if self.parser.start_symbol:
            self.follow_sets[self.parser.start_symbol].add('$')
        
        # Iteratively compute FOLLOW sets until no changes
        changed = True
        while changed:
            changed = False
            for non_terminal in self.parser.non_terminals:
                old_size = len(self.follow_sets[non_terminal])
                self._compute_follow(non_terminal)
                if len(self.follow_sets[non_terminal]) > old_size:
                    changed = True
        
        return self.follow_sets
    
    def _compute_follow(self, non_terminal):
        """
        Compute FOLLOW set for a single non-terminal
        
        Args:
            non_terminal (str): The non-terminal to compute FOLLOW set for
        """
        # TODO: Implement FOLLOW set computation logic
        # For each production A -> αBβ
        # Add FIRST(β) - {epsilon} to FOLLOW(B)
        # If epsilon in FIRST(β), add FOLLOW(A) to FOLLOW(B)
        # For production A -> αB, add FOLLOW(A) to FOLLOW(B)
        pass
    
    def get_follow(self, non_terminal):
        """
        Get FOLLOW set for a non-terminal
        
        Args:
            non_terminal (str): The non-terminal
            
        Returns:
            set: FOLLOW set of the non-terminal
        """
        return self.follow_sets.get(non_terminal, set())
