#include <stdio.h>
#include <time.h>

int main() {
    float temperatura[7];

    // 1. INÍCIO DA MEDIÇÃO
    clock_t inicio = clock();

    // --- OPERAÇÃO A MEDIR ---
    // Laço 1: Preenchimento automático do vetor
    for (int i = 0; i < 7; i++) {
        temperatura[i] = 25.5f + i; // Simulando valores de temperatura
    }

    // Laço 2: Leitura/Processamento do vetor
    float soma = 0;
    for (int i = 0; i < 7; i++) {
        soma += temperatura[i]; // Processamento leve em memória
    }
    // --- FIM DA OPERAÇÃO A MEDIR ---

    clock_t fim = clock();

    // 2. CÁLCULO E EXIBIÇÃO DO TEMPO
    double tempo_gasto = (double)(fim - inicio) / CLOCKS_PER_SEC;

    printf("Soma das temperaturas: %.2f\n", soma);
    printf("Tempo de execucao: %f segundos\n", tempo_gasto);

    return 0;
}