# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

from enum import Enum

class TokenType(Enum):
    """Enumeration of all possible token types in our language"""
    NUMBER = 'NUMBER'                   # Numeric literals (both integer and float)
    ARITHMETIC_OP = 'ARITHMETIC_OP'     # Arithmetic operators: +, -, *, /, %, ^, |
    COMPARISON_OP = 'COMPARISON_OP'     # Comparison operators: >, <, >=, <=, ==, !=
    PAREN_OPEN = 'PAREN_OPEN'           # Opening parenthesis '('
    PAREN_CLOSE = 'PAREN_CLOSE'         # Closing parenthesis ')'
    RES = 'RES'                         # Result reference operation
    MEM = 'MEM'                         # Memory operation
    IF = 'IF'                           # If conditional
    THEN = 'THEN'                       # Then clause
    ELSE = 'ELSE'                       # Else clause
    FOR = 'FOR'                         # For loop
    NEWLINE = 'NEWLINE'                 # Line breaking
    ERROR = 'ERROR'                     # Invalid characters