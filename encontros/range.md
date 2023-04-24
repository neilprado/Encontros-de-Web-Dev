# Percorrendo intervalos de 0 a N

### Range

Foi possível observar como percorrer listas com tamanhos definidos, porém, ainda não foi visto como percorrer intervalos de 0 a N, como temos em linguagens como Java, JavaScript, C, Go:

```js
for(i = 0; i < n; i++) {
  // instruções a serem seguidas
}
```
No Python, apesar de não haver esta complexidade de estrutura de uma iteração, mas temos um método chamado *range*, cujo retorno é compatível com o for, porém não é uma lista, é algo como um objeto iterável. Sua sintaxe é:

```python
for i in range(10):
  print(i)
```

No exemplo acima, é possível visualizar, ao executar o código, que a iteração ocorre e é impresso até o valor passado via parâmetro menos uma unidade, já que é preciso lembrar que o primeiro índice da lista é o 0. 

Dentro do método range, também é possível inserir valores de início e o incremento de forma opcional. Portanto, o único parâmetro obrigatório do método é seu momento de parada. Considerando o método range com seus parâmetros opcionais, a declaração do método é:

**range(start, stop, step)**

- start: (opcional) O valor inicial (ou 0 se não for explicitado)
- stop: O valor de parada
- step: O valor de "saltos" de um valor para o outro (ou 1 se não for explicitado)

### Enumerate

Muitas vezes, quando é preciso enumerar elementos em uma coleção. Ou seja, além do valor do elemento, é preciso obter o índice. Iterando com for e o método enumerate, isso ficaria do seguinte modo:

```python
frutas = ["laranja", "manga", "melancia"]
for i, fruta in enumerate(frutas):
  print(i, fruta)
```