# Iterações em Python

Em Python, existem duas estruturas de repetição: "for" e "while". Ambas são usadas para executar um conjunto de instruções várias vezes.

### Loop for

O loop "for" é usado para iterar sobre uma sequência (como uma lista, tupla, string, etc.) e executar um conjunto de instruções para cada item na sequência. Aqui está a sintaxe do loop *for* em Python

```python
lista = [0, 1, 2]
for l in lista:
    print(l)
```

Para um exemplo um pouco mais próximo da realidade, temos: 

```python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```

O resultado dessa ação é: 

```python
maçã
banana
laranja
```

### Loop While

O loop "while" é usado para executar um conjunto de instruções enquanto uma condição for verdadeira. A condição é verificada antes de cada iteração do loop. Aqui está um exemplo da sintaxe do loop *while* no Python:

```python
counter = 0
while counter < 5:
    print(counter)
    counter += 1
```

Isso imprimiria os números de 0 a 4 conforme visto a seguir:

```python
0
1
2
3
4
```

Em suma, pode ser usado qualquer uma das opções de loop para os problemas mais variados, porém, é comum que os loops *for* sejam usados quando se sabe exatamente quantas vezes deseja executar um conjunto de instruções, enquanto os loops *while* são usados quando não se sabe quantas vezes será preciso executar um conjunto de instruções.