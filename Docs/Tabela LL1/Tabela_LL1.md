# Tabela LL(1) - Analisador Sintático LL(1)

# Tabela LL(1)

| Não-terminal    | Terminal         | Produção                                      |
|:---------------:|:----------------|:----------------------------------------------|
| `<program>`     | (                | `<expression> NEWLINE <program>`              |
| `<program>`     | EOF              | ε                                             |
| `<expression>`  | (                | `( <expr_body> )`                             |
| `<expr_body>`   | IF               | `<if_expr>`                                   |
| `<expr_body>`   | FOR              | `<for_expr>`                                  |
| `<expr_body>`   | MEM              | `<mem_expr>`                                  |
| `<expr_body>`   | NUMBER           | `<rpn_expr>`                                  |
| `<expr_body>`   | (                | `<rpn_expr>`                                  |
| `<rpn_expr>`    | NUMBER           | `<term> <term> <arith_op>`                    |
| `<rpn_expr>`    | (                | `<term> <term> <arith_op>`                    |
| `<mem_expr>`    | MEM              | MEM                                           |
| `<mem_expr>`    | NUMBER           | `<term> MEM \| <term> RES`                    |
| `<mem_expr>`    | (                | `<term> MEM \| <term> RES`                    |
| `<term>`        | NUMBER           | NUMBER                                        |
| `<term>`        | (                | `( <expression> )`                            |
| `<arith_op>`    | +                | +                                             |
| `<arith_op>`    | -                | -                                             |
| `<arith_op>`    | *                | *                                             |
| `<arith_op>`    | /                | /                                             |
| `<arith_op>`    | %                | %                                             |
| `<arith_op>`    | ^                | ^                                             |
| `<arith_op>`    | \|               | \|                                            |
| `<if_expr>`     | IF               | IF <cond_expr> THEN <expression> [ELSE <expression>] |
| `<cond_expr>`   | (                | ( <term> <term> <comp_op> )                   |
| `<comp_op>`     | ==               | ==                                            |
| `<comp_op>`     | !=               | !=                                            |
| `<comp_op>`     | <                | <                                             |
| `<comp_op>`     | >                | >                                             |
| `<comp_op>`     | <=               | <=                                            |
| `<comp_op>`     | >=               | >=                                            |
| `<for_expr>`    | FOR              | FOR ( <term> <term> ) <expression>            |