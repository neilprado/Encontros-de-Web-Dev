# Question 1

print("Hello World!")

# Question 2

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print("A soma dos dois números é:", a + b)

# Question 3
import math

PI = 3.14159
raio = float(input("Digite o raio:"))
print("A área do círculo é:{:.4f}".format(math.pow(raio, 2) * PI))

# Question 4
idade_em_dias = int(input("Digite a idade em dias: "))

anos = idade_em_dias // 365
idade_em_dias %= 365

meses = idade_em_dias // 30
idade_em_dias %= 30

dias = idade_em_dias

print(f"{anos} ano(s), {meses} mes(es) e {dias} dia(s)")

# Question 5
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

PROD = valor1 * valor2

print(f"O produto entre {valor1} e {valor2} é igual a {PROD}")

# Question 6
A = float(input("Digite a primeira nota: "))
B = float(input("Digite a segunda nota: "))
C = float(input("Digite a terceira nota: "))

MEDIA = ((A * 2) + (B * 3) + (C * 5)) / 10

print(f"A média do aluno é {MEDIA:.1f}")

# Question 7
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

DIFERENCA = (A * B) - (C * D)

print(f"A diferença do produto de A e B pelo produto de C e D é {DIFERENCA}")

#Question 8
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor que o funcionário recebe por hora: "))

salario = horas_trabalhadas * valor_hora

print(f"O funcionário de número {numero_funcionario} receberá um salário de R${salario:.2f}")

#Question 9
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor que o funcionário recebe por hora: "))

salario = horas_trabalhadas * valor_hora

print(f"O funcionário de número {numero_funcionario} receberá um salário de R${salario:.2f}")

#Question 10
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

pi = 3.14159

area_tri_ret = (A * C) / 2
area_circ = pi * C ** 2
area_trap = ((A + B) * C) / 2
area_quad = B ** 2
area_ret = A * B

print(f"Área do triângulo retângulo: {area_tri_ret:.3f}")
print(f"Área do círculo: {area_circ:.3f}")
print(f"Área do trapézio: {area_trap:.3f}")
print(f"Área do quadrado: {area_quad:.3f}")
print(f"Área do retângulo: {area_ret:.3f}")


