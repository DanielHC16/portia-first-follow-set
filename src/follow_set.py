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
        iterations = 0
        while changed:
            changed = False
            iterations += 1
            
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
        # For each production A -> alpha B beta
        for lhs, productions in self.parser.productions.items():
            for production in productions:
                # Find all occurrences of non_terminal in this production
                for i, symbol in enumerate(production):
                    if symbol == non_terminal:
                        # Get beta (rest of production after this symbol)
                        beta = production[i + 1:]
                        
                        if beta:
                            # FOLLOW(B) includes FIRST(beta) - {EPSILON}
                            first_of_beta = self.first_calc.get_first_of_sequence(beta)
                            self.follow_sets[non_terminal].update(first_of_beta - {'EPSILON'})
                            
                            # If EPSILON in FIRST(beta), add FOLLOW(A) to FOLLOW(B)
                            if 'EPSILON' in first_of_beta:
                                if lhs in self.follow_sets:
                                    self.follow_sets[non_terminal].update(self.follow_sets[lhs])
                        else:
                            # B is at the end: A -> alpha B
                            # Add FOLLOW(A) to FOLLOW(B)
                            if lhs in self.follow_sets:
                                self.follow_sets[non_terminal].update(self.follow_sets[lhs])
    
    def get_follow(self, non_terminal):
        """
        Get FOLLOW set for a non-terminal
        
        Args:
            non_terminal (str): The non-terminal
            
        Returns:
            set: FOLLOW set of the non-terminal
        """
        return self.follow_sets.get(non_terminal, set())
