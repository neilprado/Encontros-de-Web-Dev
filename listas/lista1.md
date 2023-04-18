# Lista de Exercícios 1

### Questão 1 - O seu primeiro programa em qualquer linguagem de programação normalmente é o "**Hello World!**". Neste primeiro problema tudo o que você precisa fazer é imprimir esta mensagem na tela.

**Entrada**

Este problema não possui nenhuma entrada.

**Saída**

Você deve imprimir a mensagem "**Hello World!**" e em seguida o final de linha, conforme o exemplo abaixo.

| Exemplo de entrada  | Exemplo de saída    |
| ------------------- |:-------------------:|
|                     | Hello World!        |


### Questão 2 - Leia 2 valores inteiros e armazene-os nas variáveis **A** e **B**. Efetue a soma de **A** e **B** atribuindo o seu resultado na variável **X**. Imprima **X** conforme exemplo apresentado abaixo.

**Entrada**

A entrada contém 2 valores inteiros.

**Saída**

Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável **X** e pelo final de linha. Cuide para que tenha um espaço antes e depois do sinal de igualdade, conforme o exemplo abaixo.

| Exemplo de entrada  | Exemplo de saída    |
| ------------------- |:-------------------:|
| 10 9                | X = 19              |
| -10 4               | X = -6              |
| 15 -7               | X = 8               |


### Questão 3 - Considerando para este problema que π = 3.14159: Efetue o cálculo da área, elevando o valor de **raio** ao quadrado e multiplicando por π.

A fórmula para calcular a área de uma circunferência é: area = π . raio<sup>2</sup>.

**Entrada**

A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável **raio**.

**Saída**

Apresentar a mensagem abaixo seguido pelo valor da variável **area**, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double).

| Exemplo de entrada  | Exemplo de saída    |
| ------------------- |:-------------------:|
| 2.00                | A = 12.5664         |
| 100.64              | A = 31819.3103      |
| 150.00              | A = 70685.7750      |

### Questão 4 -  Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

:exclamation:Apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

**Entrada**

O arquivo de entrada contém um valor inteiro.

**Saída**

Imprima a saída conforme exemplo fornecido.

| Exemplo de entrada  | Exemplo de saída             |
| ------------------- |:----------------------------:|
| 400                 | 1 ano(s) 1 mes(es) 5 dia(s)  |
| 800                 | 2 ano(s) 2 mes(es) 10 dia(s) |
| 30                  | 0 ano(s) 1 mes(es) 0 dia(s)  |

### Questão 5 -  Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável **PROD**. Aseguir mostre a variável **PROD** com mensagem correspondente.

**Entrada**

O arquivo de entrada contém 2 valores inteiros.

**Saída**

Imprima a mensagem "PROD" e a variável **PROD** conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

| Exemplo de entrada  | Exemplo de saída    |
| ------------------- |:-------------------:|
| 3 9                 | PROD = 27           |
| -30 10              | PROD = -300         |
| 0 9                 | PROD = 0            |

### Questão 6 -  Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

**Entrada**

O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão.

**Saída**

Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade.

| Exemplo de entrada  | Exemplo de saída    |
| ------------------- |:-------------------:|
| 5.0 6.0 7.0         | MEDIA = 6.3         |
| 5.0 10.0 10.0       | MEDIA = 9.0         |
| 10.0 10.0 5.0       | MEDIA = 7.5         |

### Questão 7 - Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula:DIFERENCA= (A\* B-C\* D).

**Entrada**

O arquivo de entrada contém 4 valores inteiros.

**Saída**

Imprima a mensagem **DIFERENCA** com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

| Exemplo de entrada  | Exemplo de saída    |
| ------------------- |:-------------------:|
| 5 6 7 8             | DIFERENCA = -26     |
| 0 0 7 8             | DIFERENCA = -56     |
| 5 6 -7 8            | DIFERENCA = 86      |

### Questão 8 - Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

**Entrada**

O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

**Saída**

Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.

| Exemplo de entrada  | Exemplo de saída               |
| ------------------- |:------------------------------:|
| 25 100 5.50         | NUMBER = 25 SALARY = U$ 550.00 |
| 1 200 20.50         | NUMBER = 1 SALARY = U$ 4100.00 |
| 6 145 15.55         | NUMBER = 6 SALARY = U$ 2254.75 |

### Questão 9 - Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

**Entrada**

O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

**Saída**

A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

| Exemplo de entrada     | Exemplo de saída         |
| --------------------- |:-------------------------:|
| 12 1 5.30 16 2 5.10   | VALOR A PAGAR = R$ 15.50  |
| 13 2 15.30 161 4 5.20 | VALOR A PAGAR = R$ 51.40  |
| 1 1 15.10 2 1 15.10   | VALOR A PAGAR = R$ 30.20  |

### Questão 10 -  Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
  - a área do triângulo retângulo que tem A por base e C por altura.
  - a área do círculo de raio C. (pi= 3.14159)
  - a área do trapézio que tem A e B por bases e C por altura.
  - a área do quadrado que tem lado B.
  - a área do retângulo que tem lados A e B.

**Entrada**

O arquivo de entrada contém três valores com um dígito após o ponto decimal.

**Saída**

O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

| Exemplo de entrada     | Exemplo de saída                                                                               |
| --------------------- |:-----------------------------------------------------------------------------------------------:|
| 3.0 4.0 5.2           | TRIANGULO = 7.800 CIRCULO = 84.949 TRAPEZIO = 18.200 QUADRADO = 16.000 RETANGULO = 12.000       |
| 12.7 10.4 15.2        | TRIANGULO = 96.520 CIRCULO = 725.833 TRAPEZIO = 175.560 QUADRADO = 108.160 RETANGULO = 132.080  |
