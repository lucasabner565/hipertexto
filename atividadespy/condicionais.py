#questão1

idade = int (input("Digite sua idade: "))
if idade < 18:
    print ("Você é menor de idade.")
elif idade >= 18 and idade < 60:
    print ("Você é maior de idade.")
else:
    print ("Você é idoso.")

#questão2

numero = int (input("Digite um número: "))
if numero > 0:
    print ("O número é positivo.")
elif numero < 0:
    print ("O número é negativo.")
else:
    print ("O número é zero.")
if numero % 2 == 0:
        print ("O número é par.")
else:
        print ("O número é ímpar.")

#questão3

num1 = int (input("Digite o primeiro número: "))
num2 = int (input("Digite o segundo número: "))
num3 = int (input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
     print ("O maior número é: ", num1)
elif num2 > num1 and num2 > num3:
     print ("O maior número é: ", num2)
else:
     print ("O maior número é: ", num3)

#questão4

num1 = int (input("Digite o primeiro número: "))
num2 = int (input("Digite o segundo número: "))
if num1 == num2 * 2:
     print ("O primeiro número é múltiplo do segundo número.")
else:
        print ("O primeiro número não é múltiplo do segundo número.")

#questão5

nota = int (input("Digite a nota do aluno: "))
if nota >= 7:
    print ("O aluno está aprovado.")
elif nota >= 5 and nota < 7:
     print ("O aluno está de recuperação.")
else:
     print ("O aluno está reprovado.")

#questão6

num = int (input("Digite um número: "))
if num >= 50 and num <= 100:
     print ("O número está no intervalo de 50 a 100.")
else:
        print ("O número não está no intervalo de 50 a 100.")

#questão7

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caractere = input("Digite um caractere: ").lower()
if caractere in vogais:
    print ("O caractere é uma vogal.")
elif caractere in consoantes:
    print ("O caractere é uma consoante.")
elif caractere in numeros:
    print ("O caractere é um número.")
else:
    print ("O caractere é um símbolo.")

#questão8

num1 = int (input("Digite o primeiro número: "))
num2 = int (input("Digite o segundo número: "))
if num1 > num2:
    print (num2, num1)
else:
    print (num1, num2)

#questão9

nascimento = int (input("Digite o ano de nascimento: "))
ano_atual = 2026
if ano_atual - nascimento >= 16:
    print ("Você pode votar.")
else:
    print ("Você não pode votar.")

#questão10

peso = float (input("Digite seu peso em kg: "))
altura = float (input("Digite sua altura em metros: "))
imc = peso / (altura * altura)
if imc < 18.5:
     print ("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
        print ("Você está com o peso normal.")
elif imc >= 25 and imc < 30:
        print ("Você está com sobrepeso.")
else:
        print ("Você está com obesidade.")

#questão11

lado1 = int (input("Digite o primeiro número: "))
lado2 = int (input("Digite o segundo número: "))
lado3 = int (input("Digite o terceiro número: "))
if lado1 != 0 and lado2 != 0 and lado3 != 0:
    print ("Os números podem formar um triângulo.")
else:
    print ("Os números não podem formar um triângulo.")
if lado1 == lado2 and lado2 == lado3:
    print ("O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print ("O triângulo é isósceles.")
else:
    print ("O triângulo é escaleno.")

#questão12

horario1 = float (input("Digite o primeiro horário em horas e minutos (ex: 14.30): "))
horario2 = float (input("Digite o segundo horário em horas e minutos (ex: 14.30): "))
if horario1 < horario2:
    print ("O primeiro horário acontece antes do segundo horário.")
elif horario1 > horario2:
    print ("O segundo horario acontece antes do primeiro horário.")
else:
    print ("Os horários são iguais.")

#questão13

num = int (input("Digite um número: "))
if num % 3 == 0:
    print ("O número é divisível por 3.")
elif num % 5 == 0:
    print ("O número é divisível por 5.")
elif num % 3 == 0 and num % 5 == 0:
    print ("O número é divisível por 3 e por 5.")
else:
    print ("O número não é divisível por 3 nem por 5.")

#questão14
salario = float (input("Digite o salário do funcionário: "))
if salario <= 1500:
    aumento = salario * 20/100
elif salario > 1500 and salario <= 3000:
    aumento = salario * 15/100
else:
    aumento = salario * 10/100

#questão15
mes = int (input("Digite o número do mês (1 a 12): "))
if mes == 1:
    print ("Janeiro")
elif mes == 2:
    print ("Fevereiro")
elif mes == 3:
    print ("Março")
elif mes == 4:
    print ("Abril")
elif mes == 5:
    print ("Maio")
elif mes == 6:
    print ("Junho")
elif mes == 7:
    print ("Julho")
elif mes == 8:
    print ("Agosto")
elif mes == 9:
    print ("Setembro")
elif mes == 10:
    print ("Outubro")
elif mes == 11:
    print ("Novembro")
elif mes == 12:
    print ("Dezembro")
else:
    print ("Mês inválido.")

#questão16
num1 = int (input("Digite o primeiro número: "))
num2 = int (input("Digite o segundo número: "))
num3 = int (input("Digite o terceiro número: "))
if num3 ** 2 == num1 ** 2 + num2 ** 2:
    print ("Os números podem formar um triângulo retângulo.")
else:
    print ("Os números não podem formar um triângulo retângulo.")

#questão17
num = int (input("Digite um número: "))
if num != 2 and num != 3 and num != 5 and num != 7:
    print ("O número não é primo.")
else:
    print ("O número é primo.")

#questão18
from datetime import date

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

try:
    data = date(ano, mes, dia)
    print("Data válida")
except ValueError:
    print("Data inválida")

#questão19
horario = float(input("Digite o horário em horas e minutos (ex: 14.30): "))
if horario >= 08.00 and horario < 18.00:
    print("É horário comercial.")
else:
    print("Não é horário comercial.")

#questão20
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))
peso1 = 2
peso2 = 3
peso3 = 5
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
if media_ponderada >= 7:
    print("O aluno está aprovado.")
elif media_ponderada >= 5 and media_ponderada < 7:
    print("O aluno está de recuperação.")
else:
    print("O aluno está reprovado.")

#questão21
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
if n1 > 0 and (n1 ** 0.5) == int(n1 ** 0.5):
    print("Existe um quadrado perfeito.")
elif n2 > 0 and (n2 ** 0.5) == int(n2 ** 0.5):
    print("Existe um quadrado perfeito.")
elif n3 > 0 and (n3 ** 0.5) == int(n3 ** 0.5):
    print("Existe um quadrado perfeito.")
elif n4 > 0 and (n4 ** 0.5) == int(n4 ** 0.5):
    print("Existe um quadrado perfeito.")
else:
    print("Não existe um quadrado perfeito.")

#questão22
x1 = int (input("Digite o x do primeiro ponto: "))
y1 = int (input("Digite o y do primeiro ponto: "))
x2 = int (input("Digite o x do segundo ponto: "))
y2 = int (input("Digite o y do segundo ponto: "))
x3 = int (input("Digite o x do terceiro ponto: "))
y3 = int (input("Digite o y do terceiro ponto: "))
if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
    print("Os pontos são colineares, isto é, estão alinhados.")
else:
    print("Os pontos não são colineares, isto é, não estão alinhados.")

#questão23
n = int(input("Digite um número de cinco dígitos: "))

if 10000 <= n <= 99999:
    d1 = n // 10000
    d2 = (n // 1000) % 10
    d4 = (n // 10) % 10
    d5 = n % 10

    if d1 == d5 and d2 == d4:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")
else:
    print("O número não tem cinco dígitos")

#questão24
horario1= float(input("Digite o primeiro horário em horas, minutos e segundos (ex: 14.30.45): "))
horario2= float(input("Digite o segundo horário em horas, minutos e segundos (ex: 14.30.45): "))
segundos1 = int(horario1 * 3600)
segundos2 = int(horario2 * 3600)
if segundos1 > segundos2:
    print("O primeiro horário é maior em segundos")
elif segundos2 > segundos1:
    print("O segundo horário é maior em segundos.")
else:
    print("Os horários são iguais.")

#questão25
idade= int(input("Digite uma idade: "))
contribuicao= int(input("Digite o tempo de contribuição: "))
if idade >= 65 or contribuicao >= 35:
    print("Você pode se aposentar.")
else:
    print("Você não pode se aposentar.")

#questão26
num= float(input("Digite um número: "))
inteira= int(num)
decimal= num - inteira
if decimal > inteira:
    print("A parte decimal é maior que a parte inteira.")
else:
    print("A parte inteira é maior que a parte decimal.")

#questão27
n1= int(input("Digite o primeiro número: "))
n2= int(input("Digite o segundo número: "))
n3= int(input("Digite o terceiro número: "))
if n1 > 0 and n2 > 0 and n3 > 0:
    print("Os números podem formar um triângulo.")
else:
    print("Os números não podem formar um triângulo.")
if n1 == n2 and n2 == n3:
    print("O triângulo é equilátero.")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("O triângulo é isósceles.")
elif n3 ** 2 == n1 ** 2 + n2 ** 2 or n2 ** 2 == n1 ** 2 + n3 ** 2 or n1 ** 2 == n2 ** 2 + n3 ** 2:
    print("O triângulo é retângulo.")
else:
    print("O triângulo é escaleno.")

#questão28
caractere= input("Digite um caractere: ")

if len(caractere) == 1:
    codigo = ord(caractere)

    if 65 <= codigo <= 90:
        print("Letra maiúscula")
    elif 97 <= codigo <= 122:
        print("Letra minúscula")
    elif 48 <= codigo <= 57:
        print("Número")
    else:
        print("Outro símbolo")
else:
    print("Digite apenas um caractere")
#questão29
media= float(input("Digite a média do aluno: "))
faltas= int(input("Digite o número de faltas do aluno: "))
if media >= 7 and faltas <= 10:
    print("O aluno está aprovado.")
elif media >= 5 and media < 7 and faltas <= 10:
    print("O aluno está de recuperação.")
else:
    print("O aluno está reprovado.")

#questão30
nota1= float(input("Digite a nota da primeira prova: "))
nota2= float(input("Digite a nota da segunda prova: "))
nota3= float(input("Digite a nota da terceira prova: "))
nota4= float(input("Digite a nota da quarta prova: "))
if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    menor= nota1
elif nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    menor= nota2
elif nota3 < nota1 and nota3 < nota2 and nota3 < nota4:
    menor= nota3
else:
    menor= nota4
if nota1 > nota2 and nota1 > nota3 and nota1 > nota4:
    maior= nota1
elif nota2 > nota1 and nota2 > nota3 and nota2 > nota4:
    maior= nota2
elif nota3 > nota1 and nota3 > nota2 and nota3 > nota4: 
    maior= nota3
else:                       
    maior= nota4
media= (nota1 + nota2 + nota3 + nota4 - menor - maior)/2
print("A média do aluno, desconsiderando a menor e a maior nota, é:", media)
if media >= 7:
    print("O aluno está aprovado.")
elif media >= 5 and media < 7:
    print("O aluno está de recuperação.")
else:
    print("O aluno está reprovado.")
    
#fim_atividade



