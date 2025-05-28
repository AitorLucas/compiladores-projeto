# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

import sys
from pathlib import Path
from Lexer import Lexer
from Parser import Parser

def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python Calc.py <input_file>")
        return

    input_file = sys.argv[1]

    input_path = Path(input_file)
    if not input_path.exists():
        tests_dir = Path(__file__).parent.parent / "Input"
        possible_path = tests_dir / input_file
        if possible_path.exists():
            input_path = possible_path
        else:
            print(f"ERROR: Input file '{input_file}' not found (also checked in {tests_dir})")
            return

    try:
        code = input_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"ERROR: Input file '{input_file}' not found")
        return
    
    clean_output_folder()

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
    asts = parser.parse()

    if asts:
        for i, ast in enumerate(asts, 1):
            print(f"\n🌳 AST da linha {i}:")
            print(ast)
            ast.save_as_text(i)
            ast.save_as_dot(i)

def clean_output_folder():
    for folder_name in ["Output/Dot", "Output/Txt"]:
        folder_path = Path(folder_name)
        if folder_path.exists() and folder_path.is_dir():
            for file_path in folder_path.iterdir():
                try:
                    if file_path.is_file():
                        file_path.unlink()
                except Exception as e:
                    print(f"Erro ao deletar {file_path}: {e}")
        else:
            # Cria a pasta se não existir
            folder_path.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    main()