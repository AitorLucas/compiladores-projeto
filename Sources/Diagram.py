# Lexical and Syntactic Analyzer for Custom RPN Language
# Group: 4
# Author: Aitor Eler Lucas

import os
from pathlib import Path
import graphviz

def generate_images_from_dot(dot_dir="Output/Dot", img_dir="Output/Image"):
    print("\n∴ Generating Diagrams...")

    dot_path = Path(dot_dir)
    img_path = Path(img_dir)
    img_path.mkdir(parents=True, exist_ok=True)

    dot_files = list(dot_path.glob("*.dot"))
    if not dot_files:
        print(f"\nNo .dot files found in {dot_path}")
        return

    for dot_file in dot_files:
        try:
            img_file = img_path / (dot_file.stem + ".png")
            with open(dot_file, "r", encoding="utf-8") as f:
                dot_source = f.read()
            graph = graphviz.Source(dot_source)
            graph.format = "png"
            graph.render(filename=img_file.with_suffix('').as_posix(), cleanup=True)
        except Exception as e:
            print(f"\nError generating image for {dot_file}: {e}")

    print("\nImages generated")

if __name__ == "__main__":
    generate_images_from_dot()
