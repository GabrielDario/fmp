'''
#1 e #2
i = 0
soma = 0
somaImpares = 0
somaPares = 0

while i < 11 :
    soma = soma + i
    if i % 2 == 0 :
        somaPares = somaPares + i
    else : 
        somaImpares = somaImpares + i
    i = i + 1 

print(f'Soma total: {soma}')
print(f'Soma pares: {somaPares}')
print(f'Soma impares: {somaImpares}')

#3
inicial = int(input('Digite um número inicial: '))
final = int(input('Digite um número final: '))

somaMultiplos = 0
while inicial < final+1:
    if inicial % 3 == 0:
        print(f'{inicial} é multiplo. ')
        somaMultiplos = somaMultiplos + inicial

    inicial = inicial + 1

print(f'Soma multiplicos de 3: {somaMultiplos}')
#4

t = int(input('Digite um número para mostrar tabuada do: '))
i = 1
while i < 11:
    print(f'{t} x {i} = {t*i}')
    i = i+1
 
#5
t = int(input('Tabuada desejada: '))
i = int(input('Tabuada inicia no: '))
f = int(input('Tabuada termina:  '))

while i < f+1:
    r = t*i
    print(f'{t} x {i} = {r}')
    i = i+1

#LISTA DE REPETIÇÃO 2

#1
nF = int(input('Quantos fatoriais voce quer fazer: '))
count = 0
while nF > 0:
    f = int(input('Fatorial de que numero: '))
    count = 0

    for i in range(f,1, -1) :
        if(i == f) :
            count = i * (i-1)
        else: 
            count = count * (i-1)

    print(f'Fatorial de {f}! é {count}')
    nF = nF-1
#2
n = int(input('Quantos números  deve ser lido: '))

int1 = 0;
int2 = 0;
int3 = 0;
int4 = 0;

while n > 0:
    nI = int(input('informe um número: '))
    
    if nI >= 0 and nI <= 25 :
        int1 = int1 +1
    elif nI > 25 and nI <= 50 :
         int2 = int2 +1
    elif nI > 50 and nI <= 75 :
          int3 = int3 +1
    elif nI > 75 and nI <= 100 :
          int4 = int4 +1 
    else : 
         print('Número fora do intervalo ou inválido!')

    n = n-1
print(f'Números no intervalo de [0...25] = {int1}')
print(f'Números no intervalo de [26...50] = {int2}')
print(f'Números no intervalo de [51...75] = {int3}')
print(f'Números no intervalo de [76...10] = {int4}')

#3
i = 1;
somatorioNegativo = 0;
while i < 11 :
       n = int(input(f'informe o {i}º número: '))
       if n < 0:
              somatorioNegativo = somatorioNegativo + n
       i = i+1
print(f'Somatório dos negativos total = {somatorioNegativo}')

#4
chico = 1.5 #2 cm por ano
juca = 1.10 #3cm por ano
ano = 0
while chico > juca :
    chico = chico + 0.02
    juca = juca + 0.03
    difereca = chico - juca
    print(f'Altura do chico: {round(chico,2)} m e do juca {round(juca,2)}m, faltam {round(difereca,2)} m')
    ano= ano +1

print(f'Serão necessário {ano} anos para Juca ser mais alto que o Chico')

#5

intervalo = 0
n = None

while n != 0:
    n = int(input(f'Informe um número: '))
    
    if(n > 0 and n <= 100):
        intervalo = intervalo + 1

print(f'Foi informado {intervalo} número(s) de 0 á 100.')
#6
nTabuleiro = 1 #64 casas
graos = 1

while nTabuleiro <= 64:
    graos = graos * 2
    print(f'Quadrado {nTabuleiro}: {graos} grãos.')
    nTabuleiro = nTabuleiro+1

print(f'Foi pago no total de {graos} grãos para o monge.')

#7
    nMaior = 0
    n = None

    while n != -1:
        n = int(input(f'Informe um número: '))
        if(n > nMaior):
            nMaior = n

    print(f'O maior número foi {nMaior}.')
'''