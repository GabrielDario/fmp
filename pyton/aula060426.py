''''
#exercicio 3
sexo = input("Digite f para feminino ou m para masculino: \n")
altura = float(input("Qual sua altura: \n"))

pesoIdeal = None

if sexo == 'f' or sexo == 'F': 
    pesoIdeal = (62.7 * altura) - 44.7
    print(f'Seu peso: {altura} peso ideal: {pesoIdeal}')
elif  sexo == 'm' or sexo == 'M':
      pesoIdeal = (72.7 * altura) - 58
      print(f'Peso ideal: {round(pesoIdeal,2)}')
else: 
      print(f'Sexo não encontrado')

#exercicio 4

saldoMedio = float(input("Qual seu saldo médio: \n"))
valorCredito = None

if saldoMedio >= 0 and saldoMedio <= 200 :
    print(f'SEM CRÉDITO ESPECIAL')
elif saldoMedio > 200 and saldoMedio <= 400 :
    valorCredito = saldoMedio * 0.2 
    print(f'Valor do crédito: {valorCredito}')
elif saldoMedio > 400 and saldoMedio <= 600 :
    valorCredito = saldoMedio * 0.3 
    print(f'Valor do crédito: {valorCredito}')
elif saldoMedio > 600 :
    valorCredito = saldoMedio * 0.4
    print(f'Valor do crédito: {valorCredito}')
else : 
      print(f'Valor incorreto')

#Exercício 5
n1 = float(input("Nota da 1º prova: \n"))
n2 = float(input("Nota da 2º prova \n"))
n3 = float(input("Nota da 3º prova \n"))

aritmetica = (n1 + n2 + n3) / 3
ponderada =  (n1 * 3) + (n2 * 3) + (n3 * 4)
ponderada = ponderada / 10
print(f'Nota aritmética: {round(aritmetica,2)}')
print(f'Nota ponderada: {round(ponderada,2)}')

#Exercício 1

idadeh1 = int(input("Qual idade do homem(1): \n"))
idadeh2 = int(input("Qual idade do homem(2): \n"))
idadem1 = int(input("Qual idade da mulher(1): \n"))
idadem2 = int(input("Qual idade da mulher(2): \n"))
maiorH = None
menorH = None
maiorM = None
menorM = None

if idadeh1 > idadeh2 : 
    maiorH = idadeh1
    menorH = idadeh2
else :
    maiorH = idadeh2
    menorH = idadeh1

if idadem1 > idadem2 : 
    maiorM = idadem1
    menorM = idadem2
else :
    maiorM = idadem2
    menorM = idadem1

calculoSomar = maiorH + menorM
calculoProduto = menorH * maiorM
print(f'Somar idade do homem mais velho com a mulher mais nova: {calculoSomar}')
print(f'Produto das idades do homem mais novo com a mulher mais velha: {calculoProduto}')

#Exercício 2

nome = input("Qual o nome do produto:  \n")
qnt = int(input("Quantos produtos adquiridos: \n"))
preco = float(input("Qual o valor desse protudo : \n"))

total = qnt * preco
print(f'Total {total}')
if qnt <= 5 :
    total = total - (total * 0.02)
elif qnt > 5 and qnt <= 10 :
    total = total - (total * 0.03)
elif qnt > 10 :
    total = total - (total * 0.05)
else : 
 print(f'Algo invalido!')

print(f'Total a pagar: {total} do produto {nome}')

#Exercício 3

caes = int(input("Quantos cães foram atendidos: \n"))

if caes < 20 :
    print(f'O petshop ficou ocioso.')
elif caes >= 20 and caes <= 30 :
    print(f'Normal')
elif caes > 30 :
    print(f'Pet Shop lotada.')
else :
    print(f'Valor inválido.')

#Exercício 4

n1 = int(input('Informa um número: '))
n2 = int(input('Informa outro número: '))
dif = None

if n1 > n2 :
    dif = n1 - n2
    print(f'Diferente entre os número são de: {dif}')
elif n1< n2 :
       dif = n2 - n1
       print(f'Diferente entre os número são de: {dif}')
else :
      print('Valores inválidos')


#Exercício 5

print('Qual o nível do professor : nível 1,nível 2 e nível 3.')
nivel = input('Digite 1,2 ou 3: \n')
horas = int(input('Quantos horas foram dadas: '))
salario = None
if nivel == '1' :
     salario = horas * 12
elif  nivel == '2' :
      salario = horas * 17
elif  nivel == '3' : 
      salario = horas * 25
else :
      print('Valores inválidos')
      exit()

print(f'Salário do professor: R$ {round(salario,2)}')

'''
#CONTINUAR AULA 08