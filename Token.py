# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

class Token:
    """Class representing a lexical token with type, value, and position"""
    
    def __init__(self, type, value, position, line):
        """
        Initialize a new token
        
        Args:
            type (TokenType): The type of the token
            value (str): The actual text value of the token
            position (int): Position in the source code
            line (int): Line in the source code
        """
        self.type = type
        self.value = value
        self.position = position
        self.line = line
    
    def __str__(self):
        """String representation of the token for debugging"""
        return f"║ {str(self.type):<24} │ {repr(self.value):<9} │ {self.line:>3} │ {self.position:>4} ║"