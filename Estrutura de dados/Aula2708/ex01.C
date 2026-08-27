#include <stdio.h>

int main() {

    int vetor[5];

    int i;

    // Leitura dos valores

    for (i = 0; i < 5; i++) {

        printf("Digite o valor %d: ", i);

        scanf("%d", &vetor[i]);

    }

    // Impressão dos valores

    printf("\nValores digitados:\n");

    for (i = 0; i < 5; i++) {

        printf("vetor[%d] = %d\n", i, vetor[i]);

    }

    return 0;
}
