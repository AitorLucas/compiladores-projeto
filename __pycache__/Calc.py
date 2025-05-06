# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

import sys
from Lexer import Lexer
from Parser import Parser

def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python Calc.py <input_file>")
        return

    input_file = sys.argv[1]
    
    try:
        with open(input_file, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"ERROR: Input file '{input_file}' not found")
        return
    
    # Lexical analysis
    print("\n∴ Tokenizing input file...")
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    print("\nGENERATED TOKENS:")
    print("╔══════════════════════════╤═══════════╤═════╤══════╗")
    print("║        TOKEN TYPE        │   VALUE   │ LIN │ POSI ║")
    print("╟──────────────────────────┼───────────┼─────┼──────╢")
    for token in tokens:
        print(token)
    print("╚══════════════════════════╧═══════════╧═════╧══════╝")

    # Syntax analysis
    print("\n∴ Validating syntax...")
    parser = Parser(tokens)
    is_valid = parser.parse()
    
    print("\nSYNTAX VALIDATION:")
    if is_valid:
        print("Input file syntax is correct\n")
    else:
        print("Input file contains syntax errors\n")

if __name__ == "__main__":
    main()