# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

class Token:
    """Class representing a lexical token with type, value, and position"""
    
    def __init__(self, type, value, position):
        """
        Initialize a new token
        
        Args:
            type (TokenType): The type of the token
            value (str): The actual text value of the token
            position (int): Position in the source code
        """
        self.type = type
        self.value = value
        self.position = position
    
    def __str__(self):
        """String representation of the token for debugging"""
        return f"Token({self.type}, '{self.value}', pos={self.position})"