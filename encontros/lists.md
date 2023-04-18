# Listas em Python

### Listas

Em Python, uma lista é uma coleção de itens que podem ser de diferentes tipos de dados, como números, strings e até outras listas. As listas são mutáveis, o que significa que é possível adicionar, remover e modificar seus itens após a criação.

Para criar uma lista em Python, você pode usar colchetes [] e separar os itens com vírgulas.

```python
lista = [1, 2, 3, "quatro", "cinco"]
```

Para acessar um item em uma lista, você pode usar o índice correspondente dentro dos colchetes []. Lembre-se de que o índice do primeiro item em uma lista é sempre zero. Aqui está um exemplo:

Exemplo: 

```python
lista = [1, 2, 3, "quatro", "cinco"]
print(lista[0])    # Imprime 1
print(lista[3])    # Imprime "quatro"
```

Você também pode usar índices negativos para acessar itens contando a partir do final da lista. Por exemplo:

```python
lista = [1, 2, 3, "quatro", "cinco"]
print(lista[-1])    # Imprime "cinco"
print(lista[-2])    # Imprime "quatro"
```

Além disso, você pode modificar um item em uma lista atribuindo um novo valor ao seu índice. Por exemplo:

```python
lista = [1, 2, 3, "quatro", "cinco"]
lista[1] = "dois"
print(lista)    # Imprime [1, "dois", 3, "quatro", "cinco"]
```

Para adicionar um novo item ao final de uma lista, você pode usar o método append(). Por exemplo:

```python
lista = [1, 2, 3, "quatro", "cinco"]
lista.append("seis")
print(lista)    # Imprime [1, 2, 3, "quatro", "cinco", "seis"]
```
Para remover um item de uma lista, você pode usar o método remove() passando o valor do item que deseja remover. Por exemplo:

```python
lista = [1, 2, 3, "quatro", "cinco"]
lista.remove(3)
print(lista)    # Imprime [1, 2, "quatro", "cinco"]
```

Neste exemplo, o programa verifica se x é maior que 0. Se a condição for verdadeira, ele imprimirá "x é positivo" na tela. Se a primeira condição for falsa, ele verificará se x é igual a 0. Se essa condição for verdadeira, ele imprimirá "x é zero" na tela. Caso contrário, ele imprimirá "x é negativo".