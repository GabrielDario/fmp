import timeit

# Trecho do seu código executado repetidas vezes (por padrão, 1.000.000 de vezes)
test_code = ""
temperatura = []
for i in range(7):
    temperatura.append(25.5 + i)

soma = 0
for i in range(7):
    soma += temperatura[i]


# Executa 10.000 vezes para medir um tempo estável
repeticoes = 10000
tempo_total = timeit.timeit(stmt=test_code, number=repeticoes)

print(f"Tempo total ({repeticoes} execucoes): {tempo_total:.6f} s")
print(f"Tempo medio por execucao: {tempo_total / repeticoes:.8f} s")