"""
First Set Calculator Module
Computes FIRST sets for all symbols in the grammar
"""

class FirstSetCalculator:
    """
    Calculates FIRST sets for grammar symbols
    """
    
    def __init__(self, grammar_parser):
        """
        Initialize with parsed grammar
        
        Args:
            grammar_parser: GrammarParser instance
        """
        self.parser = grammar_parser
        self.first_sets = {}
    
    def compute_first_sets(self):
        """
        Compute FIRST sets for all non-terminals
        
        Returns:
            dict: Dictionary mapping symbols to their FIRST sets
        """
        # Initialize FIRST sets
        for terminal in self.parser.terminals:
            self.first_sets[terminal] = {terminal}
        
        for non_terminal in self.parser.non_terminals:
            self.first_sets[non_terminal] = set()
        
        # Iteratively compute FIRST sets until no changes
        changed = True
        while changed:
            changed = False
            for non_terminal in self.parser.non_terminals:
                old_size = len(self.first_sets[non_terminal])
                self._compute_first(non_terminal)
                if len(self.first_sets[non_terminal]) > old_size:
                    changed = True
        
        return self.first_sets
    
    def _compute_first(self, symbol):
        """
        Compute FIRST set for a single symbol
        
        Args:
            symbol (str): The symbol to compute FIRST set for
        """
        # TODO: Implement FIRST set computation logic
        # For each production X -> Y1 Y2 ... Yk
        # Add FIRST(Y1) - {epsilon} to FIRST(X)
        # If epsilon in FIRST(Y1), add FIRST(Y2) - {epsilon}, etc.
        pass
    
    def get_first(self, symbol):
        """
        Get FIRST set for a symbol
        
        Args:
            symbol (str): The symbol
            
        Returns:
            set: FIRST set of the symbol
        """
        return self.first_sets.get(symbol, set())
