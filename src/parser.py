"""
Grammar Parser Module
Parses EBNF grammar from CFG.txt file
"""

class GrammarParser:
    """
    Parses EBNF grammar specification
    """
    
    def __init__(self, grammar_file):
        """
        Initialize parser with grammar file path
        
        Args:
            grammar_file (str): Path to the grammar file
        """
        self.grammar_file = grammar_file
        self.productions = {}
        self.terminals = set()
        self.non_terminals = set()
        self.start_symbol = None
    
    def parse(self):
        """
        Parse the grammar file and extract productions
        
        Returns:
            dict: Dictionary mapping non-terminals to list of productions
        """
        # TODO: Implement grammar parsing logic
        # Read file line by line
        # Split by "->" to get LHS and RHS
        # Split RHS by "|" to get alternative productions
        # Tokenize each production
        pass
    
    def identify_symbols(self):
        """
        Identify terminals and non-terminals from parsed grammar
        """
        # TODO: Non-terminals appear on LHS
        # TODO: Terminals don't appear on LHS
        pass
    
    def get_productions(self, non_terminal):
        """
        Get all productions for a given non-terminal
        
        Args:
            non_terminal (str): The non-terminal symbol
            
        Returns:
            list: List of productions
        """
        return self.productions.get(non_terminal, [])
