#include <stdio.h>

int main() {

    char letras[5];

    int i;

    for (i = 0; i < 5; i++) {
        printf("Digite a letra %d: ", i);
        scanf(" %c", &letras[i]);
    }   

    printf("\nLetras digitadas:\n");

    for (i = 0; i < 5; i++) {

        printf("letras[%d] = %c\n", i, letras[i]);

    }

    return 0;

}