# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

from enum import Enum

class TokenType(Enum):
    """Enumeration of all possible token types in our language"""
    NUMBER = 'NUMBER'           # Numeric literals (both integer and float)
    OPERATOR = 'OPERATOR'       # Arithmetic operators: +, -, *, /, %, ^, |
    PAREN_OPEN = 'PAREN_OPEN'   # Opening parenthesis '('
    PAREN_CLOSE = 'PAREN_CLOSE' # Closing parenthesis ')'
    MEMORY = 'MEMORY'           # Memory operations
    RES = 'RES'                 # Result reference operation
    MEM = 'MEM'                 # Memory operation
    COMMAND = 'COMMAND'         # Special commands
    IDENTIFIER = 'IDENTIFIER'   # Variable identifiers
    IF = 'IF'                   # If conditional
    THEN = 'THEN'               # Then clause
    ELSE = 'ELSE'               # Else clause
    FOR = 'FOR'                 # For loop
    NEWLINE = 'NEWLINE'         # Line breaking