# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

from TokenType import TokenType
from Token import Token

class Lexer:
    """Converts source code into a sequence of tokens using the same initialization pattern as Parser"""
    
    def __init__(self, code):
        """
        Initialize the lexer with source code
        
        Args:
            code (str): The source code to tokenize
        """
        self.code = code
        self.position = 0
        self.line = 1
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
            # Handle newlines explicitly for line tracking
            if self.current_char == '\n':
                tokens.append(Token(TokenType.NEWLINE, '\n', self.position-1, self.line))
                self.line += 1
                self.advance()
                continue

            # Skip whitespace
            if self.current_char.isspace():
                self.advance()
                continue
            
            if self.current_char == '#':
                # Comment: skip until end of line
                while self.current_char and self.current_char != '\n':
                    self.advance()
                continue

            # Handle parentheses
            if self.current_char == '(':
                tokens.append(Token(TokenType.PAREN_OPEN, '(', self.position-1, self.line))
                self.advance()
                continue
                
            if self.current_char == ')':
                tokens.append(Token(TokenType.PAREN_CLOSE, ')', self.position-1, self.line))
                self.advance()
                continue

            # Handle numbers (both integer and float and negatives)
            if (self.current_char.isdigit() or 
                self.current_char == '.' or 
                (self.current_char == '-' and self.peek_next() and (self.peek_next().isdigit() or self.peek_next() == '.'))):

                start_pos = self.position - 1
                num_str = ''
                dot_count = 0

                if self.current_char == '-':
                    num_str += self.current_char
                    self.advance()
                
                if self.current_char == '.':
                    dot_count += 1
                    num_str += self.current_char
                    self.advance()
                
                while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
                    if self.current_char == '.':
                        dot_count += 1
                        if dot_count > 1:
                            break  # More than one dot = invalid number
                    num_str += self.current_char
                    self.advance()

                if not num_str[-1].isdigit():
                    tokens.append(Token(TokenType.ERROR, num_str, start_pos, self.line))
                else:
                    tokens.append(Token(TokenType.NUMBER, num_str, start_pos, self.line))
                continue
            
            # Handle comparison operators
            if self.current_char in "<>!=":
                start_pos = self.position - 1
                op = self.current_char
                self.advance()
                if self.current_char == '=':
                    op += self.current_char
                    self.advance()
                
                if op in ['<', '>', '<=', '>=', '==', '!=']:
                    tokens.append(Token(TokenType.COMPARISON_OP, op, start_pos, self.line))
                else:
                    tokens.append(Token(TokenType.ERROR, op, start_pos, self.line))
                continue

            # Handle arithmetic operators
            if self.current_char in '+-*/%^|':
                tokens.append(Token(TokenType.ARITHMETIC_OP, self.current_char, self.position-1, self.line))
                self.advance()
                continue
                
            # Handle identifiers and keywords
            if self.current_char.isalpha():
                start_pos = self.position-1
                ident_str = ''
                
                while (self.current_char is not None and 
                       (self.current_char.isalnum() or self.current_char == '_')):
                    ident_str += self.current_char
                    self.advance()
                    
                # Check for reserved keywords
                keywords_map = {
                    'if': TokenType.IF,
                    'then': TokenType.THEN,
                    'else': TokenType.ELSE,
                    'for': TokenType.FOR,
                    'MEM': TokenType.MEM,
                    'RES': TokenType.RES
                }

                token_type = keywords_map.get(ident_str, TokenType.IDENTIFIER) # default: Identifier
                tokens.append(Token(token_type, ident_str, start_pos, self.line))
                continue

            tokens.append(Token(TokenType.ERROR, self.current_char, self.position - 1, self.line))
            self.advance()
        
        return tokens
    
    def peek_next(self): 
        """Look at next character without consuming it"""
        return self.code[self.position] if self.position < self.code_length else None