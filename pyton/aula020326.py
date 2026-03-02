'''
 #Exercício 1

x = int (input("Digite um valor: "))    
y = int (input("Digite outro valor: "))    

soma = x + y
sub = x-y
mult = x*y
div = x/y

print(f'Seus numeros: {x} e {y} \n-------------\nSoma: {soma}\nSubtração: {sub}\nMultiplicacao: {mult}\nDivisão: {div}')

------------------------------------------
#Exercicio 2 
cavalos = int(input("Digite quantos cavalos você comprou: "))    
ferraduras = cavalos * 4

print(f'Você precisa comprar {ferraduras} ferraduras para sua haras.')

------------------------------------------
#Exercício3

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade: '))

diasVividos = idade * 365
print(f'{nome}, você já viveu {diasVividos} dias.')



#   Exercício4
------------------------------------------
pao = int(input("Digite quantos pãozinhos foram vendidos: ")) #0,12
broa = int(input("Digite quantas broas foram vendidos: ")) #1,5

paoVendido = float(pao * 0.12)
broaVendido = float(pao * 1.5)

totalVendidos = paoVendido + broaVendido

poupanca = totalVendidos * 0.1

print(f"Foram arrecadados {totalVendidos} com os pãos juntos.")

print(f"Deve se guardado {poupanca} que é 10% do total")

------------------------------------------
#Exercício 5    

pesoPrato = float(input("Qual o peso do seu prato em gramas: "))

valorPrato = float(pesoPrato * 0.012)
print(f"Seu prato irá custar {valorPrato} Reais")
------------------------------------------
#Exercício 6

dias = int(input("Digite um dia: "))
mes = int(input("Digite um mês (EM DOIS DÍGITOS:)"))

diasTotais = ((mes - 1) * 30 ) + dias 
print(f"Já se passaram {diasTotais}")
'''

