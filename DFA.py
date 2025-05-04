from graphviz import Digraph

# Define DFA structure for the lexical analyzer based on your language
dfa = Digraph(format='png')
dfa.attr(rankdir='LR', size='8,5')
dfa.attr('node', shape='circle')

# States
states = {
    "start": "Start",
    "number": "Number",
    "decimal": "Decimal",
    "identifier": "Identifier",
    "operator": "Operator",
    "whitespace": "Whitespace",
    "paren_open": "ParenOpen",
    "paren_close": "ParenClose",
    "end": "End"
}

# Final states (accepting)
final_states = {"number", "decimal", "identifier", "operator", "paren_open", "paren_close"}

# Add states to graph
for state_key, label in states.items():
    if state_key in final_states:
        dfa.node(state_key, label, shape="doublecircle")
    else:
        dfa.node(state_key, label)

# Transitions
transitions = [
    ("start", "number", "digit"),
    ("number", "number", "digit"),
    ("number", "decimal", "."),
    ("decimal", "decimal", "digit"),
    ("start", "identifier", "letter"),
    ("identifier", "identifier", "letter/digit"),
    ("start", "operator", "+ - * / % ^ < > = !"),
    ("start", "paren_open", "("),
    ("start", "paren_close", ")"),
    ("start", "whitespace", "whitespace"),
    ("whitespace", "start", "whitespace")
]

# Add transitions to graph
for from_state, to_state, label in transitions:
    dfa.edge(from_state, to_state, label)

dfa.render("/mnt/data/dfa_lexer", cleanup=False)
"/mnt/data/dfa_lexer.png"
