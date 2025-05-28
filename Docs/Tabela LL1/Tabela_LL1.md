# Tabela LL(1) - Analisador Sintático LL(1)

## 1. `<program>`

| Lookahead | Produção                          |
|-----------|------------------------------------|
| `(`       | `<program> → <expression> NEWLINE <program>` |
| `EOF`     | `<program> → ε`                    |

---

## 2. `<expression>`

| Lookahead | Produção               |
|-----------|------------------------|
| `(`       | `<expression> → ( <expr_body> )` |

---

## 3. `<expr_body>`

| Lookahead   | Produção         |
|-------------|------------------|
| `IF`        | `<expr_body> → <if_expr>` |
| `FOR`       | `<expr_body> → <for_expr>` |
| `MEM`       | `<expr_body> → <rpn_expr>` |
| `NUMBER`    | `<expr_body> → <rpn_expr>` |
| `IDENTIFIER`| `<expr_body> → <rpn_expr>` |
| `(`         | `<expr_body> → <rpn_expr>` |

---

## 4. `<rpn_expr>`

| Lookahead   | Produção                            |
|-------------|-------------------------------------|
| `MEM`       | `<rpn_expr> → MEM`                 |
| `NUMBER`    | `<rpn_expr> → <term> <term> <operator>` |
| `IDENTIFIER`| `<rpn_expr> → <term> <term> <operator>` |
| `(`         | `<rpn_expr> → <term> <term> <operator>` |

---

## 5. `<term>`

| Lookahead   | Produção             |
|-------------|----------------------|
| `NUMBER`    | `<term> → NUMBER`    |
| `IDENTIFIER`| `<term> → IDENTIFIER`|
| `(`         | `<term> → <expression>` |

---

## 6. `<operator>`

| Lookahead | Produção             |
|-----------|----------------------|
| `+`       | `<operator> → +`     |
| `-`       | `<operator> → -`     |
| `*`       | `<operator> → *`     |
| `/`       | `<operator> → /`     |
| `%`       | `<operator> → %`     |
| `|`       | `<operator> → |`     |
| `^`       | `<operator> → ^`     |
| `==`      | `<operator> → ==`    |
| `!=`      | `<operator> → !=`    |
| `<`       | `<operator> → <`     |
| `>`       | `<operator> → >`     |
| `<=`      | `<operator> → <=`    |
| `>=`      | `<operator> → >=`    |

---

## 7. `<if_expr>`

| Lookahead | Produção                                        |
|-----------|-------------------------------------------------|
| `IF`      | `<if_expr> → IF <expression> THEN <expression> [ELSE <expression>]` |

---

## 8. `<for_expr>`

| Lookahead | Produção                                        |
|-----------|-------------------------------------------------|
| `FOR`     | `<for_expr> → FOR ( IDENTIFIER NUMBER NUMBER ) <expression>` |
