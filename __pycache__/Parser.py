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
        self.advance()

    def advance(self):
        """Move to next token"""
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None
    
    def add_error(self, message, token):
        """Records an error with line number"""
        self.errors.append(f"Line {token.line}: {message} (line: {token.line} | position: {token.position})")
    
    def parse(self):
        """Main parsing method"""
        try:
            while self.current_token is not None:
                if self.current_token.type == TokenType.PAREN_OPEN:
                    self.advance()

                    if self.current_token and self.current_token.type == TokenType.IF:
                        self.parse_if_expression()
                    elif self.current_token and self.current_token.type == TokenType.FOR:
                        self.parse_for_expression()
                    else:
                        self.parse_expression()

                    if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                        self.add_error("Missing closing parenthesis", self.current_token)
                        # Skip ahead to recover
                        while self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                            self.advance()
                    if self.current_token:
                        self.advance()
                elif self.current_token.type == TokenType.NEWLINE:
                    self.advance()
                else:
                    self.add_error(f"Unexpected token '{self.current_token.value}'", self.current_token)
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
    
    def parse_expression(self, allow_identifiers=False):
        """Parses individual expressions"""
        try:
            if self.current_token.type == TokenType.IF:
                self.parse_if_expression()
                return
            elif self.current_token.type == TokenType.FOR:
                self.parse_for_expression()
                return

            components = []
            while self.current_token is not None and self.current_token.type != TokenType.PAREN_CLOSE:
                valid_tokens = [
                    TokenType.NUMBER,
                    TokenType.ARITHMETIC_OP,
                    TokenType.COMPARISON_OP,
                    TokenType.MEM,
                    TokenType.RES,
                ]
                if allow_identifiers:
                    valid_tokens.append(TokenType.IDENTIFIER)
                
                if self.current_token.type == TokenType.PAREN_OPEN:
                    inner_pos = self.current_token.position
                    self.advance()
                    self.parse_expression()
                    if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                        self.add_error("Missing closing parenthesis in nested expression", self.current_token)
                        while self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                            self.advance()
                    if self.current_token:
                        self.advance()
                    components.append(('expr', inner_pos))
                
                elif self.current_token.type in valid_tokens:
                    components.append((self.current_token.type.name.lower(), self.current_token.position))
                    self.advance()
                
                else:
                    self.add_error(f"Unexpected token '{self.current_token.value}' in expression", self.current_token)
                    self.advance()

            # Special handling for (MEM), (n MEM), (n RES)
            if len(components) == 1 and components[0][0] == 'mem':
                return  # valid: (MEM)
            elif len(components) == 2:
                if components[0][0] == 'number' and components[1][0] in ['mem', 'res']:
                    return  # valid: (n MEM) or (n RES)
            
            # Validate RPN structure
            if self.current_token and self.current_token.type == TokenType.PAREN_CLOSE:
                stack = []
                for comp in components:
                    valid_components = ['number', 'expr']
                    if allow_identifiers:
                        valid_components.append('identifier')
                    if comp[0] in valid_components:
                        stack.append(comp)
                    elif comp[0] in ['arithmetic_op', 'comparison_op']:
                        if len(stack) < 2:
                            self.add_error("Not enough operands for operator", self.current_token)
                            break
                        stack.pop()
                        stack.pop()
                        stack.append(('result', comp[1]))

                if len(stack) != 1:
                    self.add_error("Invalid expression structure", self.current_token)
            
        except Exception as e:
            pos = self.current_token.position if self.current_token else 0
            self.add_error(str(e), pos)
    
    def parse_if_expression(self):
        """Parses an if-then-else statement"""
        self.advance() # Consume 'if'
        # Condition block
        if self.current_token and self.current_token.type == TokenType.PAREN_OPEN:
            self.advance()
            self.parse_expression()
            if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                self.add_error("Missing closing parenthesis in if condition", self.current_token)
            if self.current_token:
                self.advance()
        else:
            self.add_error("Expected '(' after 'if'", self.current_token)

        if not (self.current_token and self.current_token.type == TokenType.THEN):
            self.add_error("Expected 'then' after 'if' condition", self.current_token)
            return
        self.advance()

        # 'then' block
        if self.current_token and self.current_token.type == TokenType.PAREN_OPEN:
            self.advance()
            self.parse_expression()
            if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                self.add_error("Missing closing parenthesis in 'then' block", self.current_token)
            if self.current_token:
                self.advance()
        else:
            self.add_error("Expected '(' after 'then'", self.current_token)

        # Optional 'else' block
        if self.current_token and self.current_token.type == TokenType.ELSE:
            self.advance()
            if self.current_token and self.current_token.type == TokenType.PAREN_OPEN:
                self.advance()
                self.parse_expression()
                if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                    self.add_error("Missing closing parenthesis in 'else' block", self.current_token)
                if self.current_token:
                    self.advance()
            else:
                self.add_error("Expected '(' after 'else'", self.current_token)

        # Ensure closing parenthesis for entire if expression
        if self.current_token is None or self.current_token.type != TokenType.PAREN_CLOSE:
            self.add_error("Missing closing parenthesis for 'if' expression", self.current_token or self.tokens[-1])

    def parse_for_expression(self):
        """Parses a for loop"""
        self.advance() # Consume 'for'
        # Loop header block
        if self.current_token and self.current_token.type == TokenType.PAREN_OPEN:
            self.advance()
            # Expect: (var start end)
            if self.current_token.type != TokenType.IDENTIFIER:
                self.add_error("Expected variable name in for-loop", self.current_token)
            self.advance()

            for _ in range(2):  # expect two numbers: start, end
                if self.current_token.type != TokenType.NUMBER:
                    self.add_error("Expected number in for-loop range", self.current_token)
                self.advance()

            if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                self.add_error("Missing closing parenthesis in for-loop header", self.current_token)
            if self.current_token:
                self.advance()
        else:
            self.add_error("Expected '(' after 'for'", self.current_token)

        # Loop body block
        if self.current_token and self.current_token.type == TokenType.PAREN_OPEN:
            self.advance()
            self.parse_expression(allow_identifiers=True)
            if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                self.add_error("Missing closing parenthesis in for-loop body", self.current_token)
            if self.current_token:
                self.advance()
        else:
            self.add_error("Expected '(' to start for-loop body", self.current_token)

        # Ensure closing parenthesis for entire for expression
        if self.current_token is None or self.current_token.type != TokenType.PAREN_CLOSE:
            self.add_error("Missing closing parenthesis for 'for' expression", self.current_token or self.tokens[-1])
