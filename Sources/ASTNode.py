# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

import os
from pathlib import Path

class ASTNode:
    def __init__(self, token, children=None):
        self.token = token
        self.children = children if children else []

    def _format_tree(self, prefix="", is_last=True):
        connector = "└── " if is_last else "├── "
        type_str = self.token.type.name if hasattr(self.token.type, "name") else str(self.token.type)
        value_str = f": {self.token.value}" if self.token.value is not None else ""
        line = f"{prefix}{connector}{type_str} {value_str}\n"
        prefix += "    " if is_last else "│   "
        for i, child in enumerate(self.children):
            line += child._format_tree(prefix, i == len(self.children) - 1)
        return line

    def __str__(self):
        return self._format_tree("", True)

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
                label = f"{node.token.type}\\n{escape(node.token.value)}" if node.token.value else node.token.type
                f.write(f'  node{current_id} [label="{label}"];\n')
                if parent_id is not None:
                    f.write(f'  node{parent_id} -> node{current_id};\n')
                node_count[0] += 1
                my_id = current_id
                for child in node.children:
                    write_node(child, my_id)

            write_node(self)
            f.write("}\n")
