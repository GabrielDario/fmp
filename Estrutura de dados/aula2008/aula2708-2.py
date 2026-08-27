import time

# 1. INÍCIO DA MEDIÇÃO
inicio = time.perf_counter()

# --- INÍCIO DA OPERAÇÃO A MEDIR ---
temperatura = []

# Laço 1: Preenchimento da lista
for i in range(7):
    temp = 25.5 + i  # Simulando a entrada de dados
    temperatura.append(temp)

# Laço 2: Leitura/Processamento da lista
soma = 0
for i in range(7):
    soma += temperatura[i]
# --- FIM DA OPERAÇÃO A MEDIR ---

fim = time.perf_counter()

# 2. EXIBIÇÃO DO TEMPO
tempo_gasto = fim - inicio
print(f"Tempo de execucao: {tempo_gasto:.8f} segundos")