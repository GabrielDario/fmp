'''
#Exercicio 5
celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = float((1.8 * celsius) + 32)
print('Temperatura em Fahrenheit :' , fahrenheit , '°')


#Exercicio 6

horasTrabalhadas = int(input("Digite as horas trabalhadas: "))
horasExtras = int(input("Digite as horas extras: "))

salarioBruto = (horasTrabalhadas * 10) + (horasExtras * 15)
salarioLiquido = salarioBruto - (salarioBruto * 0.1)
print(f"Salário Bruto: R$ {salarioBruto} Reais.")
print(f"Salário Líquido: R$ {salarioLiquido} Reais.")

#Exercicio 7

print("Quantos litros você tomou?\n--------------------")

lata = int(input("Quantos latas de 350ml você tomou: "))
garrafa = int(input("Quantos garrafas de 600ml você tomou: "))
litrao = int(input("Quantos litrão de 2L você tomou: "))

litrosTotal = ((lata * 350) + (garrafa * 600) + (litrao * 2000)) / 1000
print(f"Você Comprou : {litrosTotal} litros.")


#Exercicio 8

import math
contaTotal = float(input("Quanto deu a conta total para dividir em 3: "))

valorSemCentavo = math.floor(contaTotal / 3)
valorComCentavos = round( contaTotal - valorSemCentavo - valorSemCentavo , 2 )
print(f"Carlos e André pagaram: R$ {valorSemCentavo} e André R$ {valorComCentavos}")

'''
