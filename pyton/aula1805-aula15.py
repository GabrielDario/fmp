# LISTA 3
#1
mS = 0
mF = 0
maiorS =0
pS = 0
p = 1
per = 0
s = None
f = None
o = None
while o != 0:
    o = int(input(f'Digite 0 para encerrar ou 1 para continuar: '))
    if o == 0: 
        break
    

    
    s = int(input(f'Qual salário da pessoa {p}: '))
    f = int(input(f'Quantos filhos a pessoa {p} tem: '))
    
    if s > maiorS:
        maiorS = s
    
    if s <= 100:
        per = per + 1
        
    mS = s + mS
    mF = f + mF
    print(f'Pessoa {p}: Ganha R${s} com {f} filhos.')
    p = p+1
    print('-------------------------')


mS = mS / (p-1)
mF = mF / (p-1)
per = (per / (p-1)) * 100

print('--------------------------------')
print('ESTATISTICAS :')
print(f'Média de salário: R${mS}')
print(f'Média de filhos {round(mF,2)}')
print(f'Maior salário: R$ {round(maiorS,2)}')
print(f'Percentual de pessoas com salário até R$ 100,00: {per} %')