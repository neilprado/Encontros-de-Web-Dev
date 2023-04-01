# Estruturas em Python

### Estruturas de decisão

Em Python, as estruturas de decisão permitem que você controle o fluxo de execução de um programa com base em condições específicas. Existem duas principais estruturas de decisão em Python: if e else.

Aqui está a sintaxe básica do if em Python:

```python
if condição:
    # Executa se a condição for verdadeira
```

Se a condição for verdadeira, o código dentro do bloco if será executado. Caso contrário, o bloco if será ignorado e o programa continuará executando o código após o bloco if.

Exemplo: 

```python
x = 5

if x > 0:
    print("x é positivo")
```

Agora vamos adicionar a estrutura else. A sintaxe básica é:

```python
if condição:
    # Executa se a condição for verdadeira
else:
    # Executa se a condição for falsa
```

Se a condição no if for verdadeira, o bloco de código dentro do if será executado. Caso contrário, o bloco de código dentro do else será executado. Aqui está um exemplo:

```python
x = -2

if x > 0:
    print("x é positivo")
else:
    print("x é negativo ou zero")
```

Neste exemplo, o programa verifica se x é maior que 0. Se a condição for verdadeira, ele imprimirá "x é positivo" na tela. Caso contrário, ele imprimirá "x é negativo ou zero".

Você também pode adicionar a estrutura elif para testar condições adicionais. A sintaxe básica é:

```python
if condição1:
    # Executa se a condição1 for verdadeira
elif condição2:
    # Executa se a condição1 for falsa e a condição2 for verdadeira
else:
    # Executa se todas as condições anteriores forem falsas
```

Se a primeira condição for verdadeira, o bloco de código dentro do primeiro if será executado. Caso contrário, o programa testará a segunda condição no bloco elif. Se a segunda condição for verdadeira, o bloco de código dentro do segundo if será executado. Caso contrário, o programa executará o bloco de código dentro do else.

Aqui está um exemplo com if, elif e else:

```python
x = 0

if x > 0:
    print("x é positivo")
elif x == 0:
    print("x é zero")
else:
    print("x é negativo")
```

Neste exemplo, o programa verifica se x é maior que 0. Se a condição for verdadeira, ele imprimirá "x é positivo" na tela. Se a primeira condição for falsa, ele verificará se x é igual a 0. Se essa condição for verdadeira, ele imprimirá "x é zero" na tela. Caso contrário, ele imprimirá "x é negativo".