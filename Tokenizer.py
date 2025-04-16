# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

from TokenType import TokenType
from Token import Token

class Tokenizer:
    """Converts source code into a sequence of tokens using the same initialization pattern as Parser"""
    
    def __init__(self, code):
        """
        Initialize the tokenizer with source code
        
        Args:
            code (str): The source code to tokenize
        """
        self.code = code
        self.position = 0
        self.current_char = None
        self.code_length = len(code)
        self.advance()  # Initialize first character
    
    def advance(self):
        """Move to the next character in the source code"""
        if self.position < self.code_length:
            self.current_char = self.code[self.position]
            self.position += 1
        else:
            self.current_char = None
    
    def tokenize(self):
        """
        Convert source code into tokens
        
        Returns:
            list[Token]: List of tokens generated from the code
        """
        tokens = []
        
        while self.current_char is not None:
            # Skip whitespace
            if self.current_char.isspace():
                self.advance()
                continue
                
            # Handle parentheses
            if self.current_char == '(':
                tokens.append(Token(TokenType.PAREN_OPEN, '(', self.position-1))
                self.advance()
                continue
                
            if self.current_char == ')':
                tokens.append(Token(TokenType.PAREN_CLOSE, ')', self.position-1))
                self.advance()
                continue
                
            # Handle numbers (both integer and float)
            if self.current_char.isdigit() or self.current_char == '.':
                start_pos = self.position-1
                num_str = ''
                
                while (self.current_char is not None and 
                       (self.current_char.isdigit() or self.current_char == '.')):
                    num_str += self.current_char
                    self.advance()
                    
                tokens.append(Token(TokenType.NUMBER, num_str, start_pos))
                continue
                
            # Handle operators
            if self.current_char in '+-*/%^|':
                tokens.append(Token(TokenType.OPERATOR, self.current_char, self.position-1))
                self.advance()
                continue
                
            # Handle identifiers and keywords
            if self.current_char.isalpha():
                start_pos = self.position-1
                ident_str = ''
                
                while (self.current_char is not None and 
                       self.current_char.isalpha()):
                    ident_str += self.current_char
                    self.advance()
                    
                # Check for reserved keywords
                if ident_str == 'RES':
                    tokens.append(Token(TokenType.RES, ident_str, start_pos))
                elif ident_str == 'MEM':
                    tokens.append(Token(TokenType.MEM, ident_str, start_pos))
                elif ident_str == 'if':
                    tokens.append(Token(TokenType.IF, ident_str, start_pos))
                elif ident_str == 'then':
                    tokens.append(Token(TokenType.THEN, ident_str, start_pos))
                elif ident_str == 'else':
                    tokens.append(Token(TokenType.ELSE, ident_str, start_pos))
                elif ident_str == 'for':
                    tokens.append(Token(TokenType.FOR, ident_str, start_pos))
                else:
                    tokens.append(Token(TokenType.IDENTIFIER, ident_str, start_pos))
                continue
                
            self.advance()  # Skip unrecognized characters
        
        return tokens