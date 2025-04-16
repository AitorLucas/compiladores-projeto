# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

from TokenType import TokenType

class Parser:
    """Validates syntax according to language rules"""

    def __init__(self, tokens):
        """
        Initialize a new parser
        
        Args:
            tokens (list[Token]): List of tokens to parse
        """
        self.tokens = tokens
        self.current_token = None
        self.token_index = -1
        self.errors = []
        self.line_breaks = self._find_line_breaks()
        self.advance()
    
    def _find_line_breaks(self):
        """Finds all newline positions for accurate line counting"""
        breaks = [0]
        for i, token in enumerate(self.tokens):
            if token.type == TokenType.NEWLINE:
                breaks.append(token.position + 1)
        return breaks
    
    def get_line_number(self, position):
        """Returns correct line number for a given position"""
        for line_num, line_pos in enumerate(self.line_breaks):
            if position < line_pos:
                return line_num
        return len(self.line_breaks)
    
    def advance(self):
        """Move to next token"""
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None
    
    def add_error(self, message, position):
        """Records an error with line number"""
        line = self.get_line_number(position)
        self.errors.append(f"Line {line+1}: {message} (position {position})")
    
    def parse(self):
        """Main parsing method"""
        try:
            while self.current_token is not None:
                if self.current_token.type == TokenType.PAREN_OPEN:
                    start_pos = self.current_token.position
                    self.advance()
                    self.parse_expression(start_pos)
                    if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                        self.add_error("Missing closing parenthesis", start_pos)
                        # Skip ahead to recover
                        while self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                            self.advance()
                    if self.current_token:
                        self.advance()
                else:
                    self.add_error(f"Unexpected token '{self.current_token.value}'", 
                                 self.current_token.position)
                    self.advance()
            
            if self.errors:
                print("\nSYNTAX ERRORS FOUND:")
                for error in self.errors:
                    print(error)
                return False
            return True
            
        except Exception as e:
            pos = self.current_token.position if self.current_token else 0
            self.add_error(str(e), pos)
            return False
    
    def parse_expression(self, start_pos):
        """Parses individual expressions"""
        try:
            components = []
            while self.current_token is not None and self.current_token.type != TokenType.PAREN_CLOSE:
                if self.current_token.type == TokenType.PAREN_OPEN:
                    inner_pos = self.current_token.position
                    self.advance()
                    self.parse_expression(inner_pos)
                    if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                        self.add_error("Missing closing parenthesis in nested expression", inner_pos)
                        while self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                            self.advance()
                    if self.current_token:
                        self.advance()
                    components.append(('expr', inner_pos))
                
                elif self.current_token.type in [TokenType.NUMBER, TokenType.OPERATOR, 
                                              TokenType.MEM, TokenType.RES]:
                    components.append((self.current_token.type.name.lower(), 
                                    self.current_token.position))
                    self.advance()
                
                else:
                    self.add_error(f"Unexpected token '{self.current_token.value}' in expression", 
                                 self.current_token.position)
                    self.advance()
            
            # Validate RPN structure
            if self.current_token and self.current_token.type == TokenType.PAREN_CLOSE:
                stack = []
                for comp in components:
                    if comp[0] in ['number', 'expr', 'mem', 'res']:
                        stack.append(comp)
                    elif comp[0] == 'operator':
                        if len(stack) < 2:
                            self.add_error("Not enough operands for operator", comp[1])
                            break
                        stack.pop()
                        stack.pop()
                        stack.append(('result', comp[1]))
                
                if len(stack) != 1:
                    self.add_error("Invalid expression structure", start_pos)
            
        except Exception as e:
            pos = self.current_token.position if self.current_token else 0
            self.add_error(str(e), pos)