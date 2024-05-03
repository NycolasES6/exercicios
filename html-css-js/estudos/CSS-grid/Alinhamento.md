# Grid: Alinhamento
---

Existe 6 propriedades para alinhamento
1. `Justfy-content`
2. `align-content`
3. `justfy-items`
4. `align-items`
5. `justfy-self`
6. `align-self`

Vamos separálo em 2 grupos
1. `justfy` e `align`
2. `content`, `items` e `self`

---

## Justfy e Align
Sabendo que o grid é bidimensional, nós temos o eixo x e o y.

o ***eixo x*** é o posicinamento horizontal, da esquerda para a direita.
o ***eixo y*** é o posicinamento vertical, de cima para baixo.

---

## Content, Items e Self
Juntando o `Justfy` e `Align`, com esses elementos: `content`, `items` e `self`; nós observamos nossas propiedades

### Content
`jsutfy-content` e `align-content` nos permite alinhar o próprio grid, relativo ao espaço fora do grid.
O uso dessas propriedades são im pouco mais raras, pois só é aplicado caso o grid seja menor que a area definida.
(Por exemplo, quando usamos em px o tamanho do grid, poderemos terminar com um grid pequeno, para o tamanho da area do grid)

Podemos usar **7 valores**:
1. start
2. end
3. center
4. stretch
5. space-between
6. space-around
7. space-evenly

---

### Items
`justfy-items` e `align-items` vai permitir alinhar os items do nosso grid, em qualquer espaço disponível, na célula que ele habitar.

Podemos usar **7 valores**:
1. start
2. end
3. center
4. stretch
5. space-between
6. space-around
7. space-evenly

---

### Self
`justfy-self` e `align-self` vai nos permitir alinhar o item em sí.
Faz a mesma coisa que o `justfy-items` e `align-items`, porém, aplicado diretamente no item de um grid.