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
        # Initialize FIRST sets for terminals
        for terminal in self.parser.terminals:
            self.first_sets[terminal] = {terminal}
        
        # Initialize FIRST sets for non-terminals
        for non_terminal in self.parser.non_terminals:
            self.first_sets[non_terminal] = set()
        
        # Add EPSILON to FIRST sets
        self.first_sets['EPSILON'] = {'EPSILON'}
        
        # Iteratively compute FIRST sets until no changes
        changed = True
        iterations = 0
        while changed:
            changed = False
            iterations += 1
            
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
        # Get all productions for this non-terminal
        productions = self.parser.get_productions(symbol)
        
        for production in productions:
            # For each production symbol -> Y1 Y2 ... Yk
            self._add_first_of_production(symbol, production)
    
    def _add_first_of_production(self, lhs, production):
        """
        Add FIRST set of a production to the LHS symbol
        
        Args:
            lhs (str): Left-hand side non-terminal
            production (list): List of symbols in the production
        """
        if not production or production == ['EPSILON']:
            # Empty production or epsilon
            self.first_sets[lhs].add('EPSILON')
            return
        
        # For Y1 Y2 ... Yk
        for i, symbol in enumerate(production):
            if symbol == 'EPSILON':
                self.first_sets[lhs].add('EPSILON')
                break
            
            # Get FIRST of current symbol
            first_of_symbol = self.first_sets.get(symbol, set())
            
            # Add FIRST(Yi) - {EPSILON} to FIRST(LHS)
            self.first_sets[lhs].update(first_of_symbol - {'EPSILON'})
            
            # If EPSILON not in FIRST(Yi), stop
            if 'EPSILON' not in first_of_symbol:
                break
            
            # If this is the last symbol and all previous had EPSILON
            if i == len(production) - 1:
                self.first_sets[lhs].add('EPSILON')
    
    def get_first(self, symbol):
        """
        Get FIRST set for a symbol
        
        Args:
            symbol (str): The symbol
            
        Returns:
            set: FIRST set of the symbol
        """
        return self.first_sets.get(symbol, set())
    
    def get_first_of_sequence(self, symbols):
        """
        Get FIRST set of a sequence of symbols
        
        Args:
            symbols (list): List of symbols
            
        Returns:
            set: FIRST set of the sequence
        """
        result = set()
        
        if not symbols:
            result.add('EPSILON')
            return result
        
        for i, symbol in enumerate(symbols):
            first_of_symbol = self.get_first(symbol)
            result.update(first_of_symbol - {'EPSILON'})
            
            if 'EPSILON' not in first_of_symbol:
                break
            
            if i == len(symbols) - 1:
                result.add('EPSILON')
        
        return result
