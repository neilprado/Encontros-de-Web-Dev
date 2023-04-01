# História do Python e primeiros comandos

### História

Python é uma linguagem de programação de alto nível que foi desenvolvida por Guido van Rossum nos anos 1980, enquanto ele trabalhava no Centro para Matemática e Informática (CWI) na Holanda. A ideia original de Van Rossum era criar uma linguagem que fosse fácil de aprender e de ler, com uma sintaxe simples e clara que permitisse aos programadores escrever código de maneira rápida e eficiente. O nome Python foi escolhido como uma homenagem ao grupo de comédia britânico Monty Python, do qual Van Rossum era fã.

Desde o seu lançamento em 1991, Python tem crescido em popularidade e se tornou uma das linguagens de programação mais usadas em todo o mundo. Ela é conhecida por sua facilidade de uso e versatilidade, sendo utilizada em diversas áreas, desde desenvolvimento web até ciência de dados e inteligência artificial. A comunidade de desenvolvedores Python é bastante ativa, e existem inúmeras bibliotecas e frameworks disponíveis para tornar o desenvolvimento em Python ainda mais fácil e eficiente.

### Usos principais do Python

Python é uma linguagem de programação versátil que pode ser usada em diversas áreas e para diferentes propósitos. Alguns dos usos mais comuns para Python incluem:

1. Desenvolvimento Web: Python é frequentemente usado para o desenvolvimento web, graças a frameworks populares como o Django e Flask.
2. Ciência de Dados: Python é uma das principais linguagens de programação usadas na análise de dados e na ciência de dados, graças a bibliotecas populares como NumPy, Pandas, Matplotlib e Scikit-learn.
3. Automação e Scripting: Python é uma escolha popular para automação de tarefas e scripting em sistemas operacionais como Linux, macOS e Windows.
4. Inteligência Artificial e Aprendizado de Máquina: Python é amplamente utilizado em projetos de inteligência artificial e aprendizado de máquina, graças a bibliotecas populares como TensorFlow, Keras e PyTorch.
5. Jogos e Gráficos: Python é usado em jogos e gráficos 3D, graças a bibliotecas populares como Pygame, PyOpenGL e Panda3D.

Esses são apenas alguns exemplos do amplo uso de Python na indústria e na comunidade de desenvolvedores. Sua flexibilidade e facilidade de uso tornam Python uma escolha popular para uma variedade de projetos e aplicações.

### Função Print
**print(*objects, sep=' ', end='\n', file=None, flush=False)**

O método print() é usado para imprimir valores na tela do console ou em um arquivo. Ele tem os seguintes parâmetros:

*objects: representa os objetos que se deseja imprimir na tela. Pode haver zero ou mais objetos, e eles serão impressos separados por um espaço, a menos que o parâmetro sep seja especificado.
sep: é o separador que será usado para separar os objetos passados como argumentos. O padrão é um espaço em branco.
end: é a string que será adicionada no final da saída. O padrão é uma nova linha ('\n').
file: é o objeto de arquivo para o qual a saída deve ser enviada. O padrão é a saída padrão do console.
flush: um booleano que indica se o buffer deve ser limpo após a impressão. O padrão é False, o que significa que o buffer não será limpo.

```python
# Imprime a string 'Hello, World!' na tela
print('Hello, World!')

# Imprime dois números separados por um traço
a, b = 10, 20
print(a, '-', b, sep='')

# Imprime uma mensagem sem adicionar uma nova linha no final
print('Continua', end=' ')

# Imprime em um arquivo especificado
with open('saida.txt', 'w') as f:
    print('Isto vai para um arquivo!', file=f)
```
:exclamation: Copie o código para a sua IDE favorita para executar o código.

Para formatar um texto com python: 
```python
nome = "João"
idade = 25
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))
```

### Função Input
**input(prompt)**

Em Python, o método input() é usado para receber uma entrada de dados do usuário. Ele permite que o usuário insira dados do teclado e, em seguida, esses dados podem ser processados e usados pelo programa. O método input() retorna uma string que contém a entrada do usuário.

A sintaxe básica do método input() é a seguinte:

```python
variavel = input("Digite uma mensagem: ")
```

Aqui, a função input() recebe uma mensagem de entrada opcional (entre aspas) que é exibida ao usuário para indicar que tipo de entrada é esperada. Quando o usuário insere a entrada, ela é armazenada em uma variável, nesse caso chamada de "variavel".

Por exemplo, o seguinte código solicita ao usuário que insira o nome e a idade, em seguida, armazena essas informações em variáveis:

```python
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

print("Seu nome é " + nome + " e você tem " + idade + " anos.")
```

Ao executar esse código, a mensagem "Digite o seu nome:" será exibida na tela. O usuário poderá inserir o nome, seguido pela idade, que serão armazenados nas variáveis "nome" e "idade". O programa então exibirá uma mensagem que combina essas informações na tela.

É importante observar que o método input() retorna uma string, mesmo que o usuário insira um número. Se o programa precisar usar esse valor como um número, será necessário convertê-lo usando uma função como int() ou float().

Exemplos:

```python
idade = int(input("Digite a sua idade: "))
print("No próximo ano, você terá " + str(idade + 1) + " anos.")
```

```python
altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite o seu peso em quilogramas: "))

imc = peso / (altura ** 2)
print("O seu IMC é " + str(imc) + ".")
```

### Tipos de dados em Python

1. Números:
  - Inteiros: 10, -7, 0
  - Ponto flutuante: 3.14, -2.5, 1.0
  - Números complexos: 2 + 3j, -4j, 1 - 2j
2. Sequências:
  - Listas: [1, 2, 3], ["apple", "banana", "orange"]
  - Tuplas: (1, 2, 3), ("apple", "banana", "orange")
  - Strings: "Hello", 'world', "Python is fun!"
3. Mapeamentos:
  - Dicionários: {"name": "John", "age": 30}, {"fruit": "apple", "color": "red"}
4. Conjuntos:
  - Conjuntos: {1, 2, 3}, {"apple", "banana", "orange"}
  - Conjuntos imutáveis: frozenset([1, 2, 3]), frozenset(["apple", "banana", "orange"])
5. Booleanos:
  - Verdadeiro: True
  - Falso: False
6. Tipos de dados binários:
  - Bytes: b'hello', b'\x00\x01\x02'
  - Bytearray: bytearray(b'hello')
7. Tipos de dados nulos:
  - None

### Variáveis

Em Python, uma variável é um objeto que armazena um valor. Ela é um nome que se refere a um valor específico e é usada para armazenar dados que podem ser usados ​​posteriormente em um programa. A variável em si não possui um tipo de dado fixo, pois seu tipo é determinado pelo valor que ela armazena.

Para criar uma variável em Python, basta atribuir um valor a ela usando o operador de atribuição "=":

Exemplo:

```python
nome = "Maria"
idade = 25
altura = 1.70
```

Nesse exemplo, a variável "nome" armazena uma string "Maria", a variável "idade" armazena um número inteiro 25 e a variável "altura" armazena um número de ponto flutuante 1.70.

As variáveis em Python podem ser usadas em expressões e instruções, podendo ser atualizadas com novos valores a qualquer momento, conforme necessário. Também é possível usar operações aritméticas e outras operações com as variáveis em Python, o que as torna muito flexíveis e poderosas para o desenvolvimento de programas.
