# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

import os
from pathlib import Path

class ASTNode:
    def __init__(self, type_, value=None, children=None):
        self.type = type_
        self.value = value
        self.children = children if children else []

    def _format_tree(self, prefix="", is_last=True):
        connector = "└── " if is_last else "├── "
        line = f"{prefix}{connector}{self.type}: {self.value}\n"
        prefix += "    " if is_last else "│   "
        for i, child in enumerate(self.children):
            line += child._format_tree(prefix, i == len(self.children) - 1)
        return line

    def __str__(self):
        # Usado pelo print()
        return self._format_tree("", True)

    __repr__ = __str__  # Para usar no console ou debug

    def save_as_text(self, index, directory="Output/Txt"):
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        filepath = directory / f"ast_linha{index}.txt"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self._format_tree("", True))

    def save_as_dot(self, index, directory="Output/Dot"):
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        filepath = directory / f"ast_linha{index}.dot"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("digraph AST {\n")
            node_count = [0]

            def escape(s):
                return str(s).replace('"', '\\"')

            def write_node(node, parent_id=None):
                current_id = node_count[0]
                label = f"{node.type}\\n{escape(node.value)}" if node.value else node.type
                f.write(f'  node{current_id} [label="{label}"];\n')
                if parent_id is not None:
                    f.write(f'  node{parent_id} -> node{current_id};\n')
                node_count[0] += 1
                my_id = current_id
                for child in node.children:
                    write_node(child, my_id)

            write_node(self)
            f.write("}\n")
