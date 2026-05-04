'''
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

#5
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
cand5 = 0
cand6 = 0
for i in range(1,100+1) :
    voto = int(input('1 á 4 para Candidatos,5 para nulos e 6 para voto em branco\n---------------\nInsira seu voto: '))
    if voto == 1 :
        cand1 += 1
    elif voto == 2 :
        cand2 += 1
    elif voto == 3 :
        cand3 += 1
    elif voto == 4 :
        cand4 += 1
    elif voto == 5 :
        cand5 += 1
    elif voto == 6 :
        cand6 += 1
    else :
        print('Valor invalido!')

print('Apuração do voto\n------------------------')

print(f'Candidato 1: {cand1}\nCandidato 2: {cand2}\nCandidato 3: {cand3}\nCandidato 4: {cand4}\nNulos: {cand5}\nBranco: {cand6}')
#6  

nome = input('Digite seu nome: ')
tamanho =  len(nome)
contador = 0

for letra in nome :
    contador+=1

print(f'Forma len: Seu nome tem {tamanho} letras. ')   
print(f'Percorrendo lista: Seu nome tem {contador} letras. ')   


#7
nome = input('Digite seu nome: ')
print(f'Vertical:')

for letra in nome :
    print(letra)


print(f'Horizontal - {nome}')
'''
