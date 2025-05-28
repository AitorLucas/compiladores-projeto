# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

from TokenType import TokenType
from Token import Token
from ASTNode import ASTNode

class Parser:
    """Validates syntax according to language rules"""

    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.token_index = -1
        self.errors = []
        self.advance()

    def advance(self):
        """Move to the next token."""
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None

    def add_error(self, message, token):
        """Record a syntax error with token position info."""
        self.errors.append(f"Line {token.line}: {message} (line: {token.line} | position: {token.position})")

    def parse(self):
        """Parse the token stream into AST nodes, validating syntax."""
        program_nodes = []

        try:
            while self.current_token is not None:
                if self.current_token.type == TokenType.NEWLINE:
                    self.advance()
                    continue

                if self.current_token.type == TokenType.PAREN_OPEN:
                    self.advance()
                    if self.current_token and self.current_token.type == TokenType.IF:
                        node = self.parse_if_expression()
                    elif self.current_token and self.current_token.type == TokenType.FOR:
                        node = self.parse_for_expression()
                    else:
                        node = self.parse_expression()

                    if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                        self.add_error("Missing closing parenthesis", self.current_token)
                        while self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                            self.advance()
                    if self.current_token and self.current_token.type == TokenType.PAREN_CLOSE:
                        self.advance()

                    program_nodes.append(node)

                while self.current_token and self.current_token.type != TokenType.NEWLINE:
                    if self.current_token.type in [TokenType.MEM, TokenType.RES]: # Outside parentheses, MEM and RES tokens are invalid
                        self.add_error(f"'{self.current_token.value}' can only be used inside parentheses", self.current_token)
                    self.advance()
                if self.current_token and self.current_token.type == TokenType.NEWLINE:
                    self.advance()

            if self.errors:
                print("\nSYNTAX ERRORS FOUND:")
                for error in self.errors:
                    print(error)
                return []

            return program_nodes

        except Exception as e:
            self.add_error(str(e), self.current_token)
            return []

    def parse_expression(self):
        """
        Parse expressions recursively, handling nested parentheses,
        special tokens MEM and RES, and RPN operator application.
        """
        try:
            if self.current_token.type == TokenType.IF:
                return self.parse_if_expression()
            elif self.current_token.type == TokenType.FOR:
                return self.parse_for_expression()

            components = []

            while self.current_token is not None and self.current_token.type != TokenType.PAREN_CLOSE:
                if self.current_token.type == TokenType.PAREN_OPEN:
                    self.advance()
                    sub_expr = self.parse_expression()
                    if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                        self.add_error("Missing closing parenthesis in nested expression", self.current_token)
                        while self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                            self.advance()
                    if self.current_token:
                        self.advance()
                    components.append(sub_expr)
                elif self.current_token.type in [
                    TokenType.NUMBER,
                    TokenType.ARITHMETIC_OP,
                    TokenType.COMPARISON_OP,
                    TokenType.MEM,
                    TokenType.RES,
                ]:
                    components.append(ASTNode(self.current_token))
                    self.advance()
                else:
                    self.add_error(f"Unexpected token '{self.current_token.value}' in expression", self.current_token)
                    self.advance()
            
            # MEM
            if len(components) == 1:
                if components[0].token.type == TokenType.MEM:
                    return ASTNode(components[0].token)
                if components[0].token.type == TokenType.RES:
                    self.add_error("RES cannot be used alone", components[0].token)
                    return ASTNode(Token(TokenType.ERROR, "Invalid use of RES", components[0].token.position, components[0].token.line))

            # V MEM or N RES
            if len(components) == 2:
                left, right = components
                if right.token.type == TokenType.MEM:
                    return ASTNode(right.token, [left])
                elif right.token.type == TokenType.RES:
                    return ASTNode(right.token, [left])
                else:
                    if left.token.type in [TokenType.MEM, TokenType.RES] or right.token.type in [TokenType.MEM, TokenType.RES]:
                        self.add_error("Invalid use of MEM or RES", right.token)
                        return ASTNode(Token(TokenType.ERROR, "Invalid use of MEM or RES", right.token.position, right.token.line))

            # RPN Stack
            stack = []
            for node in components:
                stack.append(node)

            result_stack = []
            for node in stack:
                if isinstance(node, ASTNode) and node.token.type in [
                    TokenType.NUMBER, TokenType.MEM, TokenType.RES
                ] or (isinstance(node, ASTNode) and node.children):
                    result_stack.append(node)
                elif node.token.type in [TokenType.ARITHMETIC_OP, TokenType.COMPARISON_OP]:
                    if len(result_stack) < 2:
                        self.add_error("Not enough operands for operator", node.token)
                        return ASTNode(Token(TokenType.ERROR, "Not enough operands for operator", node.token.position, node.token.line))
                    right = result_stack.pop()
                    left = result_stack.pop()
                    result_stack.append(ASTNode(node.token, [left, right]))
                else:
                    self.add_error(f"Unexpected node type in expression: {node.token.type}", node.token)
                    return ASTNode(Token(TokenType.ERROR, f"Unexpected node type in expression: {node.token.type}", node.token.position, node.token.line))

            if len(result_stack) != 1:
                self.add_error("Invalid expression structure", self.current_token)
                return ASTNode(Token(TokenType.ERROR, "Invalid expression structure", self.current_token.position, self.current_token.line))

            return result_stack[0]

        except Exception as e:
            self.add_error(str(e), self.current_token)
            return ASTNode(Token(TokenType.ERROR, str(e), self.current_token.position, self.current_token.line))

    def parse_if_expression(self):
        """Parse if expression with condition, then and optional else branches."""
        self.advance()  # consume 'if'
        if_token = Token(TokenType.IF, "if", self.current_token.position, self.current_token.line)
        if_node = ASTNode(if_token)

        if self.current_token and self.current_token.type == TokenType.PAREN_OPEN:
            self.advance()
            condition = self.parse_expression()
            if_node.children.append(condition)
            if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                self.add_error("Missing closing parenthesis in if condition", self.current_token)
            if self.current_token:
                self.advance()
        else:
            self.add_error("Expected '(' after 'if'", self.current_token)

        if not (self.current_token and self.current_token.type == TokenType.THEN):
            self.add_error("Expected 'then' after 'if' condition", self.current_token)
            return if_node
        self.advance()

        if self.current_token and self.current_token.type == TokenType.PAREN_OPEN:
            self.advance()
            then_expr = self.parse_expression()
            if_node.children.append(then_expr)
            if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                self.add_error("Missing closing parenthesis in 'then' block", self.current_token)
            if self.current_token:
                self.advance()
        else:
            self.add_error("Expected '(' after 'then'", self.current_token)

        if self.current_token and self.current_token.type == TokenType.ELSE:
            self.advance()
            if self.current_token and self.current_token.type == TokenType.PAREN_OPEN:
                self.advance()
                else_expr = self.parse_expression()
                if_node.children.append(else_expr)
                if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                    self.add_error("Missing closing parenthesis in 'else' block", self.current_token)
                if self.current_token:
                    self.advance()
            else:
                self.add_error("Expected '(' after 'else'", self.current_token)

        return if_node

    def parse_for_expression(self):
        """Parse for-loop expression with start and end numbers and loop body."""
        self.advance()  # consume 'for'
        for_token = Token(TokenType.FOR, "for", self.current_token.position, self.current_token.line)
        for_node = ASTNode(for_token)

        if self.current_token and self.current_token.type == TokenType.PAREN_OPEN:
            self.advance()
            if self.current_token.type != TokenType.NUMBER:
                self.add_error("Expected start number in for-loop", self.current_token)
                return ASTNode(Token(TokenType.ERROR, "Expected start number in for-loop", self.current_token.position, self.current_token.line))
            start_node = ASTNode(self.current_token)
            self.advance()

            if self.current_token.type != TokenType.NUMBER:
                self.add_error("Expected end number in for-loop", self.current_token)
                return ASTNode(Token(TokenType.ERROR, "Expected end number in for-loop", self.current_token.position, self.current_token.line))
            end_node = ASTNode(self.current_token)
            self.advance()

            for_node.children.extend([start_node, end_node])

            if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                self.add_error("Missing closing parenthesis in for-loop header", self.current_token)
            if self.current_token:
                self.advance()
        else:
            self.add_error("Expected '(' after 'for'", self.current_token)
            return ASTNode(Token(TokenType.ERROR, "Expected '(' after 'for'", self.current_token.position, self.current_token.line))

        if self.current_token and self.current_token.type == TokenType.PAREN_OPEN:
            self.advance()
            body_expr = self.parse_expression()
            for_node.children.append(body_expr)
            if self.current_token and self.current_token.type != TokenType.PAREN_CLOSE:
                self.add_error("Missing closing parenthesis in for-loop body", self.current_token)
            if self.current_token:
                self.advance()
        else:
            self.add_error("Expected '(' to start for-loop body", self.current_token)
            return ASTNode(Token(TokenType.ERROR, "Expected '(' to start for-loop body", self.current_token.position, self.current_token.line))

        return for_node