from graphviz import Source

Source.from_file("dfa.dot").render("dfa", format="png")