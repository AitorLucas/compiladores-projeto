# Analisador Léxico e Sintático para Linguagem RPN Personalizada

Este projeto implementa um analisador léxico e sintático para uma linguagem baseada em Notação Polonesa Reversa (Reverse Polish Notation - RPN), com suporte a estruturas condicionais (`if-then-else`) e de repetição (`for`). 

---

## 📜 Descrição

O analisador realiza:

1. **Análise Léxica**  
   Converte o código-fonte em uma sequência de tokens reconhecíveis, como números, operadores, identificadores, palavras-chave, etc.

2. **Análise Sintática**  
   Verifica se os tokens seguem a gramática da linguagem, suportando expressões RPN, condicionais e loops `for`.

---

## 🧱 Estrutura do Projeto

- `TokenType`: Enumeração com todos os tipos de tokens.
- `Token`: Classe que representa um token com tipo, valor e posição no código.
- `Lexer`: Classe responsável por transformar o código-fonte em tokens.
- `Parser`: Classe que verifica a estrutura sintática dos tokens.
- `main()`: Ponto de entrada do programa, que executa o lexer e o parser com um arquivo de entrada.

---

## 🖥️ Como Usar

### Pré-requisitos

- Python 3.x instalado.

### Execução

```bash
python Calc.py <arquivo_entrada>
```

#### Exemplo: 

```bash
python Calc.py test1.txt
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
    - (for (variavel start end) (...))
```
Tal que:
    'variavel' é o nome da variavel que será utilizada dentro do loop
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

Uso educacional apenas.

---

## 👤 Autor
**Aitor Eler Lucas**  