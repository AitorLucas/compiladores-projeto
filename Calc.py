# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

import sys
from Tokenizer import Tokenizer
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
    print("Tokenizing input file...")
    tokenizer = Tokenizer(code)
    tokens = tokenizer.tokenize()
    
    print("\nGenerated tokens:")
    for token in tokens:
        print(token)
    
    # Syntax analysis
    print("\nValidating syntax...")
    parser = Parser(tokens)
    is_valid = parser.parse()
    
    if is_valid:
        print("\nSYNTAX VALIDATION: Input file syntax is correct")
    else:
        print("\nSYNTAX VALIDATION: Input file contains syntax errors")

if __name__ == "__main__":
    main()