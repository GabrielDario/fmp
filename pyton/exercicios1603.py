'''
#exercicio 1
moedasde1 = int(input("Quantas moedas de 1 centavo você tem: "))
moedasde5 = int(input("Quantas moedas de 5 centavos você tem: "))
moedasde10 = int(input("Quantas moedas de 10 centavos você tem: "))
moedasde25 = int(input("Quantas moedas de 25 centavos você tem: "))
moedasde50 = int(input("Quantas moedas de 50 centavos você tem: "))
moedasde1Real = int(input("Quantas moedas de Um real você tem:  "))

dinheiro = (0.01 * moedasde1) + (0.05 * moedasde5) + (0.1 * moedasde10) + (0.25 * moedasde25) + (0.5 * moedasde50)+ (moedasde1Real * 1)

print(f'Você tem R$ {round(dinheiro,2)} Reais.')

#Exercicio2
refrescoTotal = float(input("Quantos litros de refresco você quer? \n"))

agua = round(refrescoTotal * 0.8, 2)
suco = round(refrescoTotal  * 0.2,2)
print(f'Você precisa de {agua} litros de água para fazer esse refresco.')
print(f'Você precisa de {suco} litros de suco para fazer esse refresco.')

#Exercicio3

precoProduto = float(input("Qual o preco do produto? \n"))

precoDescontado = precoProduto - (precoProduto * 0.1)
print(f'O preco desse produto com desconto sairá R$ {precoDescontado} reais.')

#Exercicio4
salarioFixo = float(input("Qual seu salário fixo? \n"))
valorDasvendas = float(input("Quantos você vendeu? \n"))

valorBruto = salarioFixo + (valorDasvendas * 0.04)
print(f'Você vai receber um total de {valorBruto}')

#Exercicio5

peso = float(input("Qual o seu peso? \n"))

engordar = peso + (peso * 0.15)
emagrecer = peso - (peso * 0.2)
print(f'Seu peso se engordar 15%: {engordar}')
print(f'Seu peso se emagrecer 20%: {emagrecer}')

#Exercicio6
salarioMinino = float(input("Qual o salário mínimo? \n"))
salarioFuncionario = float(input("Qual seu salário ? \n"))

quantidade = salarioFuncionario/salarioMinino
print(f'Você recebe {round(quantidade, 2)} salário(s) mínimo')

#Exercicio7
numero = int(input("Digite um número: \n"))


print(f'Tabuada do {numero}')
print("------------")
print(f'{numero} x 1 = {numero*1}')
print(f'{numero} x 2 = {numero*2}')
print(f'{numero} x 3 = {numero*3}')
print(f'{numero} x 4 = {numero*4}')
print(f'{numero} x 5 = {numero*5}')
print(f'{numero} x 6 = {numero*6}')
print(f'{numero} x 7 = {numero*7}')
print(f'{numero} x 8 = {numero*8}')
print(f'{numero} x 9 = {numero*9}')
print(f'{numero} x 10 = {numero*10}')
print("------------")

#Exercicio 8
anoNascimento = int(input("Digite o ano do seu nascimento: \n"))
anoAtual = int(input("Digite o ano atual: \n"))

idadeAnos = anoAtual - anoNascimento
idadeMeses = idadeAnos * 12
idadeDias = idadeAnos * 365
idadeSemanas = idadeAnos * 48
print(f'Sua idade é anos será {idadeAnos}')
print(f'Sua idade em meses será {idadeMeses}')
print(f'Sua idade em dias será {idadeDias}')
print(f'Sua idade em semanas será {idadeSemanas}')

#Exercicio 8

salario = 1200 
conta1 = 200
conta2 = 120
desconto = (conta1 + (conta1 * 0.02)) + (conta2 + (conta2 * 0.02))
restou = salario - (desconto)

print('Com salário de 1200 e com contas de R$ 200 e outra conta de R$ 120 com\n'
      'multa de 2%, restará R$ ', restou , ' do seu salário.')
'''