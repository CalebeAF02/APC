# Questão 12

## Enunciado

Desenvolva uma função lógica que receba quatro variáveis booleanas (`p`, `q`, `r` e `s`) e retorne o resultado de uma expressão lógica composta.

A função deverá calcular o valor da seguinte expressão:

```txt
((p OR q) AND r) AND (p OR (q AND r))
```

O programa deve utilizar operadores lógicos para realizar o cálculo da expressão booleana.

### Exemplo

Entrada:
```txt
p = True
q = False
r = True
s = False
```

Saída:
```txt
True
```