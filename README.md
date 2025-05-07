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

## Representação Simplificada

[DFA]([https://automatonsimulator.com/#%7B%22type%22%3A%22DFA%22%2C%22dfa%22%3A%7B%22transitions%22%3A%7B%22start%22%3A%7B%220%22%3A%22s3%22%2C%221%22%3A%22s3%22%2C%22(%22%3A%22s0%22%2C%22)%22%3A%22s1%22%2C%22%2B%22%3A%22s2%22%2C%22%20%22%3A%22s4%22%2C%22a%22%3A%22s5%22%7D%2C%22s3%22%3A%7B%220%22%3A%22s3%22%2C%221%22%3A%22s3%22%7D%2C%22s5%22%3A%7B%220%22%3A%22s5%22%2C%221%22%3A%22s5%22%2C%22a%22%3A%22s5%22%7D%7D%2C%22startState%22%3A%22start%22%2C%22acceptStates%22%3A%5B%22s0%22%2C%22s1%22%2C%22s2%22%2C%22s3%22%2C%22s4%22%2C%22s5%22%5D%7D%2C%22states%22%3A%7B%22start%22%3A%7B%7D%2C%22s3%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A513%2C%22left%22%3A401%2C%22displayId%22%3A%22num%22%7D%2C%22s0%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A255%2C%22left%22%3A230%2C%22displayId%22%3A%22open_par%22%7D%2C%22s1%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A329%2C%22left%22%3A241%2C%22displayId%22%3A%22close_par%22%7D%2C%22s2%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A405%2C%22left%22%3A250%2C%22displayId%22%3A%22art_op%22%7D%2C%22s4%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A637%2C%22left%22%3A229%2C%22displayId%22%3A%22space%22%7D%2C%22s5%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A755%2C%22left%22%3A178%2C%22displayId%22%3A%22ident%22%7D%7D%2C%22transitions%22%3A%5B%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%220%22%2C%22stateB%22%3A%22s3%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%221%22%2C%22stateB%22%3A%22s3%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%22(%22%2C%22stateB%22%3A%22s0%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%22)%22%2C%22stateB%22%3A%22s1%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%22%2B%22%2C%22stateB%22%3A%22s2%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%22%20%22%2C%22stateB%22%3A%22s4%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%22a%22%2C%22stateB%22%3A%22s5%22%7D%2C%7B%22stateA%22%3A%22s3%22%2C%22label%22%3A%220%22%2C%22stateB%22%3A%22s3%22%7D%2C%7B%22stateA%22%3A%22s3%22%2C%22label%22%3A%221%22%2C%22stateB%22%3A%22s3%22%7D%2C%7B%22stateA%22%3A%22s5%22%2C%22label%22%3A%220%22%2C%22stateB%22%3A%22s5%22%7D%2C%7B%22stateA%22%3A%22s5%22%2C%22label%22%3A%221%22%2C%22stateB%22%3A%22s5%22%7D%2C%7B%22stateA%22%3A%22s5%22%2C%22label%22%3A%22a%22%2C%22stateB%22%3A%22s5%22%7D%5D%2C%22bulkTests%22%3A%7B%22accept%22%3A%22%20%5Cn(%5Cn)%5Cn1%5Cn0%5Cn101%5Cn0111%5Cna%5Cna0a%5Cnaaa%22%2C%22reject%22%3A%22%2B000%5Cn0aa%5Cn%3F%5Cn%22%7D%7D](https://automatonsimulator.com/#%7B%22type%22%3A%22DFA%22%2C%22dfa%22%3A%7B%22transitions%22%3A%7B%22start%22%3A%7B%220%22%3A%22s3%22%2C%221%22%3A%22s3%22%2C%22(%22%3A%22s0%22%2C%22)%22%3A%22s1%22%2C%22%2B%22%3A%22s2%22%2C%22%20%22%3A%22s4%22%2C%22a%22%3A%22s5%22%2C%22%3E%22%3A%22s6%22%7D%2C%22s3%22%3A%7B%220%22%3A%22s3%22%2C%221%22%3A%22s3%22%7D%2C%22s5%22%3A%7B%220%22%3A%22s5%22%2C%221%22%3A%22s5%22%2C%22a%22%3A%22s5%22%7D%2C%22s6%22%3A%7B%22%3D%22%3A%22s6%22%7D%7D%2C%22startState%22%3A%22start%22%2C%22acceptStates%22%3A%5B%22s0%22%2C%22s1%22%2C%22s2%22%2C%22s3%22%2C%22s4%22%2C%22s5%22%2C%22s6%22%5D%7D%2C%22states%22%3A%7B%22start%22%3A%7B%7D%2C%22s3%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A474%2C%22left%22%3A401%2C%22displayId%22%3A%22num%22%7D%2C%22s0%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A216%2C%22left%22%3A230%2C%22displayId%22%3A%22open_par%22%7D%2C%22s1%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A290%2C%22left%22%3A241%2C%22displayId%22%3A%22close_par%22%7D%2C%22s2%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A366%2C%22left%22%3A250%2C%22displayId%22%3A%22art_op%22%7D%2C%22s4%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A579%2C%22left%22%3A450%2C%22displayId%22%3A%22space%22%7D%2C%22s5%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A697%2C%22left%22%3A455%2C%22displayId%22%3A%22ident%22%7D%2C%22s6%22%3A%7B%22isAccept%22%3Atrue%2C%22top%22%3A842%2C%22left%22%3A346%2C%22displayId%22%3A%22com_op%22%7D%7D%2C%22transitions%22%3A%5B%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%220%22%2C%22stateB%22%3A%22s3%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%221%22%2C%22stateB%22%3A%22s3%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%22(%22%2C%22stateB%22%3A%22s0%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%22)%22%2C%22stateB%22%3A%22s1%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%22%2B%22%2C%22stateB%22%3A%22s2%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%22%20%22%2C%22stateB%22%3A%22s4%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%22a%22%2C%22stateB%22%3A%22s5%22%7D%2C%7B%22stateA%22%3A%22start%22%2C%22label%22%3A%22%3E%22%2C%22stateB%22%3A%22s6%22%7D%2C%7B%22stateA%22%3A%22s3%22%2C%22label%22%3A%220%22%2C%22stateB%22%3A%22s3%22%7D%2C%7B%22stateA%22%3A%22s3%22%2C%22label%22%3A%221%22%2C%22stateB%22%3A%22s3%22%7D%2C%7B%22stateA%22%3A%22s5%22%2C%22label%22%3A%220%22%2C%22stateB%22%3A%22s5%22%7D%2C%7B%22stateA%22%3A%22s5%22%2C%22label%22%3A%221%22%2C%22stateB%22%3A%22s5%22%7D%2C%7B%22stateA%22%3A%22s5%22%2C%22label%22%3A%22a%22%2C%22stateB%22%3A%22s5%22%7D%2C%7B%22stateA%22%3A%22s6%22%2C%22label%22%3A%22%3D%22%2C%22stateB%22%3A%22s6%22%7D%5D%2C%22bulkTests%22%3A%7B%22accept%22%3A%22%20%5Cn(%5Cn)%5Cn1%5Cn0%5Cn101%5Cn0111%5Cna%5Cna0a%5Cnaaa%5Cn%3E%5Cn%3E%3D%22%2C%22reject%22%3A%22%2B000%5Cn0aa%5Cn%3F%5Cn%3D%5Cn%3E%3E%5Cn%3D%3E%22%7D%7D))

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

---

## 👤 Autor
**Aitor Eler Lucas**  
