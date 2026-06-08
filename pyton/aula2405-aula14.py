'''
# LISTA 3 AULA 14
#1
mediaSalarial = 0
mediaFilhos = 0
maiorSalario =0
pessoa = 1
percentualSalario100 = 0
salario = 0
filho = 0

try:
    salario = int(input(f'Qual salário da pessoa {pessoa}: '))
except ValueError:
    print('ERRO! VALOR INVALIDO')
while salario > 0:
    if pessoa == 1 :
        filho = int(input(f'Quantos filhos a pessoa {pessoa} tem: '))
        while filho < 0:
            print("VALOR INVÁLIDO DE FILHOS!")
            filho = int(input(f'Quantos filhos a pessoa {pessoa} tem: '))
            
    else:
        salario = int(input(f'Qual salário da pessoa {pessoa}: '))
        if salario < 0:
            break
        filho = int(input(f'Quantos filhos a pessoa {pessoa} tem: '))
    
    if salario > maiorSalario:
        maiorSalario = salario
    
    if salario <= 100:
        percentualSalario100 = percentualSalario100 + 1
        
    mediaSalarial = salario + mediaSalarial
    mediaFilhos = filho + mediaFilhos
    pessoa = pessoa+1
    print('-------------------------')
   
if mediaSalarial == 0 :
    mediaSalarial = 0
    mediaFilhos = 0
    percentualSalario100 = 0
else:
    mediaSalarial = mediaSalarial / (pessoa-1)
    mediaFilhos = mediaFilhos / (pessoa-1)
    percentualSalario100 = (percentualSalario100 / (pessoa-1)) * 100

print('--------------------------------')
print('ESTATISTICAS :')
print(f'Média de salário: R${mediaSalarial}')
print(f'Média de filhos {round(mediaFilhos,2)}')
print(f'Maior salário: R$ {round(maiorSalario,2)}')
print(f'Percentual de pessoas com salário até R$ 100,00: {percentualSalario100} %')
#2.1 SIMPLES - APENAS NUMERADOR PULANDO DE DOIS EM DOIS
numerador = 1
denominador = 1
soma = 0

for denominador in range(1,50+1):
   soma = soma + (numerador / denominador)
   numerador = numerador + 2
print(f"A soma disso é: {round(soma,2)}")

#2.2 - NÚMERADOR IMPARES E FOR MULTIPLOS DE 3
numerador = 1 #multiplos de 3
denominador = 1 #de 1 em 1
soma = 0

for denominador in range(1, 50 + 1):
    while numerador % 3 != 0:
        numerador = numerador + 1
    soma = soma + (numerador / denominador)
    numerador = numerador + 3

print(f"A soma disso é: {round(soma,2)}")

#3
contador = 1

while contador <= 500:
    print(contador)
    contador = contador + 1

#4
maiorAltura = 0
menorAltura = 0
mulheres = 0
homens = 0
mediaAlturaMulher  =0
mediaAlturaPopulacao = 0
percentualHomens = 0
populacao = 0

altura = None
sexo = None
tem_letra = False

while populacao < 50:
    print(f'Cidadão {populacao+1}:')
    print('--------------------------')
    sexo = int(input(f'Qual sexo:(0)Para masculino ou (1)para feminino: '))

    while sexo != 0 and sexo != 1: 
        print('VALOR INVÁLIDO')
        sexo = int(input(f'Qual sexo: (0)Para masculino ou (1)para feminino: '))

    altura = input("Digite a altura: ")
    for c in altura:
        if c.isalpha():
            tem_letra = True
    while tem_letra:
        print('VALOR INVÁLIDO')
        altura = input("Digite a altura: ")
        for c in altura:
            if c.isalpha():
                tem_letra = True
            else : 
                tem_letra = False

    altura = float(altura)

    if populacao == 0:
        maiorAltura = altura
        menorAltura = altura

    if altura > maiorAltura:
        maiorAltura = altura

    if altura < menorAltura:
        menorAltura = altura

    if sexo == 0 :
        homens = homens + 1
    else : 
            mulheres = mulheres + 1
            mediaAlturaMulher = mediaAlturaMulher + altura
        
    mediaAlturaPopulacao = mediaAlturaPopulacao + altura
    populacao = populacao + 1
    print('-------------------------')
    
percentualHomens = (homens / populacao) * 100

if mediaAlturaMulher == 0:
    mediaAlturaMulher = 0
else :
    mediaAlturaMulher = mediaAlturaMulher / mulheres

mediaAlturaPopulacao = mediaAlturaPopulacao / populacao
print('--------------------------------')
print('ESTATISTICAS :')
print(f'Maior altura {maiorAltura} m')
print(f'Menor altura {menorAltura} m')
print(f'Média altura das mulheres {round(mediaAlturaMulher,2)} m')
print(f'Média altura da população {round(mediaAlturaPopulacao,2)} m')
print(f'Percentual masculino na populacão {round(percentualHomens,2)} %')

#5
limiteInferior = int(input("Limite Inferior: "))
limiteSuperior = int(input("Limite Superior: "))
print("---------------")
inicio = limiteInferior
numeroAtual = None
soma = 0

print(f'Limite inferior: {limiteInferior}')
print(f'Limite superior: {limiteSuperior}')
print(f'Saida: ')
while inicio < limiteSuperior:
    
    if inicio % 2 == 0:
        print(inicio)
        soma = soma + inicio

    inicio = inicio + 1
print(f'Soma:', soma)

#6
qnt = int(input("Quantos números você quer botar: "))
soma = 0
inicio = 0
print("---------------")
while inicio < qnt:
    n = int(input("Informe um número: "))
    
    soma = n + soma
    inicio = inicio +1

print(f'Soma desses números: {soma}')

#7
qnt = int(input("Quantos usuário você quer botar a idade: "))
somaMaiorIdade = 0
mediaMaiorIdade = 0
nMaiorDeIdade = 0
idade = 0
inicio = 0
print("---------------")
while inicio < qnt:
    idade = int(input("Qual sua idade: "))
    if idade >= 18 :
       somaMaiorIdade = somaMaiorIdade + idade
       nMaiorDeIdade = nMaiorDeIdade + 1
    inicio = inicio + 1

mediaMaiorIdade = somaMaiorIdade / nMaiorDeIdade
print(f'Soma dos maiores de idade: {somaMaiorIdade}')
print(f'Média dos maiores de idade: {mediaMaiorIdade}')

#8
numerador = 1
denominador = 1
soma = 0

n = int(input("Digite um número inteiro e positivo: "))

for denominador in range(1,n+1):
   soma = soma + (numerador / denominador)
   denominador = denominador + 1
print(f"A soma disso é: {round(soma,2)}")
'''
