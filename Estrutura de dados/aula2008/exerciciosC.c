/*
Exercicio1
#include <stdio.h>

int main(){
    float temperatura[7];

    for( int i = 0; i < 7; i++){
        float temp;

        printf("Digite a temperatura do dia %d: ", i + 1);
        scanf("%f", &temp);

        temperatura[i] = temp;
    }

    for(int i = 0; i < 7; i++){
        printf("Dia %d: %.2f graus\n", i + 1, temperatura[i]);
    }
}

#include <stdio.h>
//Exercício2
int main() {
    int estoque[10];

    for (int i = 0; i < 10; i++) {
        printf("Digite a quantidade em estoque do produto %d: ", i);
        scanf("%d", &estoque[i]);
    }

    printf("\n--- PRODUTOS COM ESTOQUE BAIXO (< 5) ---\n");

    for (int i = 0; i < 10; i++) {
        if (estoque[i] < 5) {
            printf("Produto %d: %d unidades\n", i, estoque[i]);
        }
    }

    return 0;
}
#include <stdio.h>
//Exercício3
int main() {
    float notas[8];
    float soma = 0.0f;
    float media;
    int acima_da_media = 0;

    // Leitura das notas e acúmulo da soma
    for (int i = 0; i < 8; i++) {
        printf("Digite a nota do aluno %d: ", i + 1);
        scanf("%f", &notas[i]);
        soma += notas[i];
    }

    // Cálculo da média
    media = soma / 8.0f;

    // Contagem de alunos acima da média
    for (int i = 0; i < 8; i++) {
        if (notas[i] > media) {
            acima_da_media++;
        }
    }

    // Exibição dos resultados
    printf("\nMedia da turma: %.2f\n", media);
    printf("Alunos acima da media: %d\n", acima_da_media);

    return 0;
}

#include <stdio.h>
//Exercício 4
int main() {
    int codigos[15];
    int busca;
    int posicao = 0;

    for (int i = 0; i < 15; i++) {
        printf("Digite o código do cliente: %d: ", i + 1);
        scanf("%d", &codigos[i]);
    }

    printf("Código para buscar:");
    scanf("%d", &busca);
    printf("\n Verificar existencia cliente: \n");

    for (int i = 0; i < 15; i++){
        if (codigos[i] == busca)   {
            posicao = i+1;
            break;
        }
    }

    if (posicao != 0)  {
        printf("\nCliente encontrado na posicao (indice): %d\n", posicao);
    }
    else
    {
        printf("\nCliente nao encontrado no sistema.\n");
    }

    return 0;
}


#include <stdio.h>
//Exercício 5
int main() {
    float vendas[12];
    int pos_maior = 0;
    int pos_menor = 0;

    for (int i = 0; i < 12; i++) {
        printf("Digite o valor da venda %d: R$ ", i + 1);
        scanf("%f", &vendas[i]);
    }

    float maior = vendas[0];
    float menor = vendas[0];

    for (int i = 1; i < 12; i++) {
        if (vendas[i] > maior) {
            maior = vendas[i];
            pos_maior = i;
        }
        if (vendas[i] < menor) {
            menor = vendas[i];
            pos_menor = i;
        }
    }

    printf("\n--- RELATORIO DE VENDAS ---\n");
    printf("Maior venda: R$ %.2f (Posicao/Indice: %d)\n", maior, pos_maior);
    printf("Menor venda: R$ %.2f (Posicao/Indice: %d)\n", menor, pos_menor);

    return 0;
}
*/
//Exercício 6
#include <stdio.h>

int main() {
    int erros[20];
    int contadores[6] = {0}; 

    for (int i = 0; i < 20; i++) {
        do {
            printf("Digite o codigo do erro %d (1 a 5): ", i + 1);
            scanf("%d", &erros[i]);
            
            if (erros[i] < 1 || erros[i] > 5) {
                printf("Codigo invalido! Digite apenas valores de 1 a 5.\n");
            }
        } while (erros[i] < 1 || erros[i] > 5); 

        contadores[erros[i]]++;
    }

    printf("\n--- RELATORIO DE OCORRENCIAS DE ERRO ---\n");
    for (int tipo = 1; tipo <= 5; tipo++) {
        printf("Tipo de Erro %d: %d ocorrencia(s)\n", tipo, contadores[tipo]);
    }

    return 0;
}