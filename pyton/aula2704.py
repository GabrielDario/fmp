'''
#1 
nPares = 0
somaPares = 0
for i in range(1,501) :
    if i % 2 == 0 :
        nPares = nPares + 1
        somaPares = somaPares + i
print(f'Existe {nPares} números pares entre 0 e 500.')
print(f'Soma de todos os números pares é {somaPares}.')

#2
somaImpares = 0
for i in range(1,11) :
    if i % 2 != 0 :
        somaImpares = somaImpares + i
print(f'Soma de todos os números ímpares é {somaImpares}.')

#3
nInicial = int(input('Digite valor inicial: '))
nFinal = int(input('Digite valor final: '))
somaFinal = 0
for i in range(nInicial,nFinal+1) :
    if i % 3 == 0 :
        somaFinal = somaFinal + i
print(f'Soma de todos os multiplos de 3 dos valores que você colocou é {somaFinal}.')

#4
t = int(input('Informe a tabuada desejada: '))
for i in range(1,11) :
    r = t * 1
    print(f'{t} x {i} = {r} ')

#5
t = int(input('Qual tabuada você deseja fazer: '))
nInicial = int(input('Digite valor inicial: '))
nFinal = int(input('Digite valor final: '))

for i in range(nInicial,nFinal+1) :
    r = t * i
    print(f'{t} x {i} = {r}')

#OUTRA LISTAAAA
#1
maior = 0
menor = 1000
for i in range(1,6) :
    altura = float(input(f'Digite a altura do individuo {i}: '))
    if altura > maior :
        maior = altura
    if altura < menor :
        menor = altura

print(f'Altura maior do grupo: {maior}')
print(f'Altura menor do grupo: {menor}')

#2
print('Mostrando números ímpares de 100 a 200: ')
for i in range(100,200) :
    if i % 2 == 0 :
        print(i)

#3

f = int(input('Digite um valor: '))
count = 0;
for i in range(f,1, -1) :
    if(i == f) :
        count = i * (i-1)
    else: 
      count = count * (i-1)

print(f'Resultado de {f}! = {count}')

#4
nNegativos = 0
for i in range(1,6) :
    a = int(input("Bote um número: "))
    if a < 0 :
        nNegativos +=1

print(f'Tem {nNegativos} números negativos')
'''
#5