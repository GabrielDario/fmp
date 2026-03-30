'''
nome = input("Qual seu nome? ")

notaUm = float(input("Qual a nota da 1º prova? "))
notaDois = float(input("Qual a nota da 2º prova? "))

media = (notaUm + notaDois) / 2

aprovado = media >= 6
recuperacao = media >= 4 and media <6
reprovado = media < 4 and media >= 0
invalidos = notaUm < 0 or notaDois < 0 or notaUm > 10 or notaDois > 10
pInvalido = 'Dados inválidos!'
if invalidos : print(pInvalido)
elif aprovado :  print(f'Parabéns,você foi aprovado com {media}')
elif recuperacao : print(f'Recuperação com  {media}')
elif reprovado : print(f'Reprovado com  {media}')
else : print(pInvalido)


print('Calculo do IMC')

peso = float(input("Qual seu peso: "))
altura = float(input("Qual altura: "))

imc = peso / (altura ** 2)
imc = round(imc,2)

abaixoPeso = imc <18.5
pesoNormal = imc >= 18.5 and imc < 25
acimaDoPeso = imc >= 25 and imc < 30
obesidade = imc >= 30 

pesoInlivado = peso <= 0
pInvalido = 'Dados inválidos!'

if abaixoPeso : print(f'IMC = {imc} = Abaixo do peso')
elif pesoInlivado :  print(f'Não existe peso negativo!')
elif pesoNormal :  print(f'IMC = {imc} = Peso normal')
elif acimaDoPeso :  print(f'IMC = {imc} = Acima do peso')
elif obesidade :  print(f'IMC = {imc} = Obesidade')
else : print(pInvalido)

#Exercicio 2
numero = int(input("Informe um número inteiro: "))

if numero % 2 == 0 : print(f'{numero} é par')
else : print(f"{numero} é impar")

if numero > 0 : print(f'{numero} é positivo')
elif numero == 0 : print(f'{numero} é neutro')
else : print(f"{numero} é negativo")

#Exercicio 1
idade = int(input("Informe a idade: "))

if idade >= 5 and idade <= 7 : print(f'Infantil A')
elif idade >= 8 and idade <= 10 :  print(f'Infantil B')
elif idade >= 11 and idade <= 13 :  print(f'Juvenil A')
elif idade >= 14 and idade <= 17 :  print(f'Juvenil B')
else : print(f"{idade} = idade invalida")

#Exercicio 3

altura = float(input('Informe a sua altura: '))
sexo = input('Informe F para feminino ou M para masculino: ')
pesoIdeal = None

if sexo == "f" or sexo == 'F' : pesoIdeal = (62.1 * altura) - 44.7
elif sexo == "m" or sexo == 'M' : pesoIdeal = (72.7 * altura) - 58
else : print('Informação inválida') 

print(f'Peso ideal para você: {round(pesoIdeal,2 )}')
'''
#Exercicio 3
litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()

# Preços por litro
preco_alcool = 4.89
preco_gasolina = 6.89

# Cálculo
if tipo == "A":
    preco = preco_alcool
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

elif tipo == "G":
    preco = preco_gasolina
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

else:
    print("Tipo de combustível inválido!")
    exit()

# Valor bruto
valor_bruto = litros * preco

# Valor com desconto
valor_final = valor_bruto * (1 - desconto)

# Saída
print(f"Valor a pagar: R$ {valor_final:.2f}")