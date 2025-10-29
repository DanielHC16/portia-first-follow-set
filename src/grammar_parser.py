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
        with open(self.grammar_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Split by "->"
            if '->' not in line:
                continue
            
            parts = line.split('->')
            lhs = parts[0].strip()
            rhs = parts[1].strip()
            
            # Set start symbol as first production
            if self.start_symbol is None:
                self.start_symbol = lhs
            
            # Add to non-terminals
            self.non_terminals.add(lhs)
            
            # Split RHS by "|" for alternatives
            alternatives = [alt.strip() for alt in rhs.split('|')]
            
            # Tokenize each alternative
            if lhs not in self.productions:
                self.productions[lhs] = []
            
            for alt in alternatives:
                # Split by whitespace to get symbols
                symbols = alt.split()
                self.productions[lhs].append(symbols)
        
        # Identify terminals
        self.identify_symbols()
        
        return self.productions
    
    def identify_symbols(self):
        """
        Identify terminals and non-terminals from parsed grammar
        """
        # Collect all symbols that appear in RHS
        all_symbols = set()
        for prods in self.productions.values():
            for prod in prods:
                for symbol in prod:
                    if symbol != 'EPSILON':
                        all_symbols.add(symbol)
        
        # Terminals are symbols that don't appear on LHS
        self.terminals = all_symbols - self.non_terminals
        
        # Add end marker
        self.terminals.add('$')
    
    def get_productions(self, non_terminal):
        """
        Get all productions for a given non-terminal
        
        Args:
            non_terminal (str): The non-terminal symbol
            
        Returns:
            list: List of productions
        """
        return self.productions.get(non_terminal, [])
