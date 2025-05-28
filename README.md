# Analisador Léxico e Sintático para Linguagem RPN Personalizada

Este projeto implementa um analisador léxico e sintático para uma linguagem baseada em Notação Polonesa Reversa (Reverse Polish Notation - RPN), com suporte a estruturas condicionais (`if-then-else`), de repetição (`for`) e de recuperação de dados (`RES e MEM`). 

---

## 📁 Estrutura do Projeto

```
├── Docs
│   ├── DFA
│   │   └── *
│   ├── FirstFollow
│   │   ├── First_Follow.md
│   │   └── First_Follow.txt
│   ├── Gramatica
│   │   └── Gramatica.txt
│   ├── Tabela_LL1
│   │   ├── Tabela_LL1.md
│   │   └── Tabela_LL1.txt
│   └── *.pdf
├── Input
│   └── *.txt
├── Output
│   ├── Dot
│   │   └── *.dot
│   ├── Txt
│   │   └── *.txt
│   └── Image
│       └── *.png
├── Sources
│   ├── ASTNode.py
│   ├── Calc.py
│   ├── Diagram.py
│   ├── Lexer.py
│   ├── Parser.py
│   ├── Token.py
│   └── TokenType.py
├── LICENSE
└── README.md
```

• SOURCES

- `ASTNode`: Estrutura de nó para a Árvore Sintática Abstrata (AST).
- `Calc`: Ponto de entrada do programa, que executa o lexer e o parser com um arquivo de entrada.
- `Diagram`: Gera diagramas das árvores sintáticas em formato gráfico.
- `Lexer`: Classe responsável por transformar o código-fonte em tokens.
- `Parser`: Classe que verifica a estrutura sintática dos tokens.
- `TokenType`: Enumeração com todos os tipos de tokens.
- `Token`: Classe que representa um token com tipo, valor e posição no código.

• DOCS
- `Gramática`: Descreve a gramática da linguagem em EBNF.
- `FirstFollow`: Tabelas dos conjuntos FIRST e FOLLOW para cada não-terminal.
- `Tabela_LL1`: Tabela de análise sintática LL(1) baseada na gramática.

---

## 📜 Descrição

O analisador realiza:

1. **Análise Léxica**  
   Converte o código-fonte em uma sequência de tokens reconhecíveis, como números, operadores, identificadores, palavras-chave, etc.

2. **Análise Sintática**  
   Verifica se os tokens seguem a gramática da linguagem, suportando expressões RPN, condicionais e loops `for`.

---


## 🖥️ Como Usar

### Pré-requisitos

- Python 3.x instalado.

### Execução

```bash
python Sources/Calc.py <arquivo_entrada>
```

#### Exemplo: 

```bash
python Sources/Calc.py Input/test1.txt
```

---

## 📘 Sintaxe Suportada

- Operadores Aritméticos: +, -, *, /, %, ^, |
- Operadores de Comparação: >, <, >=, <=, ==, !=
- Palavras-chave: if, then, else, for, MEM, RES
- Parênteses: Usados para delimitar expressões
- Identificadores: Nomes de variáveis válidas
- Expressões Condicionais:
    - (if (x y 'condicional') then (...) else (...))

```
Tal que: 
    x, y são números reais
    'condicional' é um operador de comparação
    ... são blocos de expressões quaisquer
```

- Loops `for`:
    - (for (start end) (...))
```
Tal que:
    start é um número inteiro do início do loop
    end é um número inteiro do final do loop
    ... é um bloco de expressão onde está disponível a 'variavel'
```

---

## 📤 Saída

- Tokens gerados são exibidos com tipo, valor, linha e posição.
- Validação sintática imprime se há ou não erros.

---

## ⚠️ Tratamento de Erros

- Tokens inválidos são classificados como `ERROR`.
- Parênteses não balanceados ou estruturas incompletas são sinalizadas.
- Erros sintáticos exibem número da linha e posição.

---

## 📁 Exemplo de Arquivo de Entrada

Arquivos de teste incluídos no repositório:

- `test1.txt`
- `test2.txt`
- `test3.txt`
---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

---

## 👤 Autor
**Aitor Eler Lucas**  