#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#define MAX_ALUNOS 100

// ============================================================
// PROTÓTIPOS DAS FUNÇÕES
// ============================================================

// Funções de validação e entrada
void limparBuffer();
int validarNome(char nome[]);
void cadastrarAluno(char nomes[][100], float notas[], int *quantidade);

// Funções de exibição
void listarAlunos(char nomes[][100], float notas[], int quantidade);
void mediaGeral(float notas[], int quantidade);
void maiorMenorNota(char nomes[][100], float notas[], int quantidade);
void alunosAprovados(char nomes[][100], float notas[], int quantidade);

// Submenu
void submenu(char nomes[][100], float notas[], int quantidade);
void ordemAlfabetica(char nomes[][100], float notas[], int quantidade);
void ordemDecrescente(char nomes[][100], float notas[], int quantidade);
void ordemCrescente(char nomes[][100], float notas[], int quantidade);
void alunosReprovados(char nomes[][100], float notas[], int quantidade);
void notasEntreXeY(char nomes[][100], float notas[], int quantidade);
void desvioAluno(char nomes[][100], float notas[], int quantidade);

// Funções auxiliares
float calcularMedia(float notas[], int quantidade);

// Funções recursivas
void listarRecursivo(char nomes[][100], float notas[], int quantidade, int indice);
float somaRecursiva(float notas[], int quantidade);


// ============================================================
// FUNÇÃO PRINCIPAL
// ============================================================

int main() {

    // Vetores paralelos
    char nomes[MAX_ALUNOS][100];
    float notas[MAX_ALUNOS];

    int quantidade = 0;
    int opcao;

    do {

        printf("\n========================================\n");
        printf("       GERENCIAMENTO DE ALUNOS\n");
        printf("========================================\n");
        printf("1 - Cadastrar alunos e notas\n");
        printf("2 - Listagem alunos com notas\n");
        printf("3 - Calcular e exibir media geral da turma\n");
        printf("4 - Maior e menor nota registrada\n");
        printf("5 - Mostrar alunos aprovados (media >= 7)\n");
        printf("6 - Abrir submenu\n");
        printf("0 - Encerrar aplicacao\n");
        printf("========================================\n");
        printf("Digite uma opcao: ");

        scanf("%d", &opcao);
        limparBuffer();

        switch (opcao) {

            case 1:
                cadastrarAluno(nomes, notas, &quantidade);
                break;

            case 2:
                listarAlunos(nomes, notas, quantidade);
                break;

            case 3:
                mediaGeral(notas, quantidade);
                break;

            case 4:
                maiorMenorNota(nomes, notas, quantidade);
                break;

            case 5:
                alunosAprovados(nomes, notas, quantidade);
                break;

            case 6:
                submenu(nomes, notas, quantidade);
                break;

            case 0:
                printf("\nAplicacao encerrada.\n");
                break;

            default:
                printf("\nOpcao invalida!\n");
        }

    } while (opcao != 0);

    return 0;
}


// ============================================================
// LIMPAR BUFFER
// ============================================================

void limparBuffer() {

    int c;

    while ((c = getchar()) != '\n' && c != EOF);
}


// ============================================================
// VALIDAR NOME
// Aceita letras e espacos.
// ============================================================

int validarNome(char nome[]) {

    int i;

    // Não permite nome vazio
    if (strlen(nome) == 0) {
        return 0;
    }

    for (i = 0; nome[i] != '\0'; i++) {

        // Permite letras e espacos
        if (!isalpha((unsigned char)nome[i]) && nome[i] != ' ') {
            return 0;
        }
    }

    return 1;
}


// ============================================================
// CADASTRAR ALUNOS
// ============================================================

void cadastrarAluno(char nomes[][100], float notas[], int *quantidade) {

    int continuar = 1;

    if (*quantidade >= MAX_ALUNOS) {

        printf("\nLimite maximo de alunos atingido!\n");
        return;
    }

    while (continuar == 1 && *quantidade < MAX_ALUNOS) {

        printf("\n========== CADASTRO ==========\n");

        // ----------------------------------------
        // Cadastro do nome
        // ----------------------------------------

        do {

            printf("Digite o nome do aluno: ");
            fgets(nomes[*quantidade], 100, stdin);

            // Remove o \n do final
            nomes[*quantidade][strcspn(nomes[*quantidade], "\n")] = '\0';

            if (!validarNome(nomes[*quantidade])) {
                printf("Nome invalido! Digite somente letras.\n");
            }

        } while (!validarNome(nomes[*quantidade]));


        // ----------------------------------------
        // Cadastro da nota
        // ----------------------------------------

        do {

            printf("Digite a nota (0 a 10): ");

            if (scanf("%f", &notas[*quantidade]) != 1) {

                printf("Nota invalida! Digite um numero.\n");

                limparBuffer();
                notas[*quantidade] = -1;

            } else {

                limparBuffer();

                if (notas[*quantidade] < 0 ||
                    notas[*quantidade] > 10) {

                    printf("Nota invalida! Digite uma nota entre 0 e 10.\n");
                }
            }

        } while (notas[*quantidade] < 0 ||
                 notas[*quantidade] > 10);


        (*quantidade)++;

        printf("\nAluno cadastrado com sucesso!\n");

        // ----------------------------------------
        // Pergunta se deseja cadastrar outro
        // ----------------------------------------

        do {

            printf("\nDeseja cadastrar outro aluno?\n");
            printf("1 - Sim\n");
            printf("0 - Nao\n");
            printf("Opcao: ");

            scanf("%d", &continuar);
            limparBuffer();

            if (continuar != 0 && continuar != 1) {
                printf("Opcao invalida!\n");
            }

        } while (continuar != 0 && continuar != 1);
    }
}


// ============================================================
// LISTAR ALUNOS
// Utiliza uma funcao recursiva.
// ============================================================

void listarAlunos(char nomes[][100], float notas[], int quantidade) {

    if (quantidade == 0) {
        printf("\nNenhum aluno cadastrado.\n");
        return;
    }

    printf("\n========== LISTA DE ALUNOS ==========\n");

    listarRecursivo(nomes, notas, quantidade, 0);
}


// ============================================================
// FUNCAO RECURSIVA 1
// Lista os alunos um por um.
// ============================================================

void listarRecursivo(char nomes[][100], float notas[], int quantidade, int indice) {

    // Caso base
    if (indice >= quantidade) {
        return;
    }

    printf("%d - %-30s Nota: %.2f\n",
           indice + 1,
           nomes[indice],
           notas[indice]);

    // Chamada recursiva
    listarRecursivo(nomes, notas, quantidade, indice + 1);
}


// ============================================================
// CALCULAR MEDIA
// ============================================================

float calcularMedia(float notas[], int quantidade) {

    if (quantidade == 0) {
        return 0;
    }

    return somaRecursiva(notas, quantidade) / quantidade;
}


// ============================================================
// FUNCAO RECURSIVA 2
// Soma todas as notas.
// ============================================================

float somaRecursiva(float notas[], int quantidade) {

    // Caso base
    if (quantidade == 0) {
        return 0;
    }

    // Soma a ultima nota e chama novamente
    return notas[quantidade - 1] +
           somaRecursiva(notas, quantidade - 1);
}


// ============================================================
// MEDIA GERAL
// ============================================================

void mediaGeral(float notas[], int quantidade) {

    float media;

    if (quantidade == 0) {
        printf("\nNenhum aluno cadastrado.\n");
        return;
    }

    media = calcularMedia(notas, quantidade);

    printf("\nMedia geral da turma: %.2f\n", media);
}


// ============================================================
// MAIOR E MENOR NOTA
// ============================================================

void maiorMenorNota(char nomes[][100],
                    float notas[],
                    int quantidade) {

    int i;
    int posMaior = 0;
    int posMenor = 0;

    if (quantidade == 0) {
        printf("\nNenhum aluno cadastrado.\n");
        return;
    }

    for (i = 1; i < quantidade; i++) {

        if (notas[i] > notas[posMaior]) {
            posMaior = i;
        }

        if (notas[i] < notas[posMenor]) {
            posMenor = i;
        }
    }

    printf("\n========== MAIOR E MENOR NOTA ==========\n");

    printf("Maior nota: %.2f - %s\n",
           notas[posMaior],
           nomes[posMaior]);

    printf("Menor nota: %.2f - %s\n",
           notas[posMenor],
           nomes[posMenor]);
}


// ============================================================
// ALUNOS APROVADOS
// Media >= 7
// ============================================================

void alunosAprovados(char nomes[][100],
                     float notas[],
                     int quantidade) {

    int i;
    int encontrou = 0;

    if (quantidade == 0) {
        printf("\nNenhum aluno cadastrado.\n");
        return;
    }

    printf("\n========== ALUNOS APROVADOS ==========\n");

    for (i = 0; i < quantidade; i++) {

        if (notas[i] >= 7) {

            printf("%-30s Nota: %.2f\n",
                   nomes[i],
                   notas[i]);

            encontrou = 1;
        }
    }

    if (!encontrou) {
        printf("Nenhum aluno aprovado.\n");
    }
}


// ============================================================
// SUBMENU
// ============================================================

void submenu(char nomes[][100],
             float notas[],
             int quantidade) {

    int opcao;

    do {

        printf("\n========================================\n");
        printf("             SUBMENU\n");
        printf("========================================\n");
        printf("1 - Mostrar turma em ordem alfabetica\n");
        printf("2 - Mostrar turma em ordem decrescente de notas\n");
        printf("3 - Mostrar turma em ordem crescente de notas\n");
        printf("4 - Mostrar alunos reprovados (nota < 7)\n");
        printf("5 - Listar alunos com notas de X a Y\n");
        printf("6 - Desvio da nota de um aluno em relacao a media\n");
        printf("0 - Voltar ao menu principal\n");
        printf("========================================\n");
        printf("Digite uma opcao: ");

        scanf("%d", &opcao);
        limparBuffer();

        switch (opcao) {

            case 1:
                ordemAlfabetica(nomes, notas, quantidade);
                break;

            case 2:
                ordemDecrescente(nomes, notas, quantidade);
                break;

            case 3:
                ordemCrescente(nomes, notas, quantidade);
                break;

            case 4:
                alunosReprovados(nomes, notas, quantidade);
                break;

            case 5:
                notasEntreXeY(nomes, notas, quantidade);
                break;

            case 6:
                desvioAluno(nomes, notas, quantidade);
                break;

            case 0:
                printf("\nVoltando ao menu principal...\n");
                break;

            default:
                printf("\nOpcao invalida!\n");
        }

    } while (opcao != 0);
}


// ============================================================
// ORDEM ALFABETICA
// ============================================================

void ordemAlfabetica(char nomes[][100],
                     float notas[],
                     int quantidade) {

    char nomesTemp[MAX_ALUNOS][100];
    float notasTemp[MAX_ALUNOS];

    int i, j;

    if (quantidade == 0) {
        printf("\nNenhum aluno cadastrado.\n");
        return;
    }

    // Copia os vetores originais
    for (i = 0; i < quantidade; i++) {

        strcpy(nomesTemp[i], nomes[i]);
        notasTemp[i] = notas[i];
    }

    // Ordenacao usando Bubble Sort
    for (i = 0; i < quantidade - 1; i++) {

        for (j = 0; j < quantidade - i - 1; j++) {

            if (strcmp(nomesTemp[j], nomesTemp[j + 1]) > 0) {

                char nomeAux[100];
                float notaAux;

                strcpy(nomeAux, nomesTemp[j]);
                strcpy(nomesTemp[j], nomesTemp[j + 1]);
                strcpy(nomesTemp[j + 1], nomeAux);

                notaAux = notasTemp[j];
                notasTemp[j] = notasTemp[j + 1];
                notasTemp[j + 1] = notaAux;
            }
        }
    }

    printf("\n========== ORDEM ALFABETICA ==========\n");

    for (i = 0; i < quantidade; i++) {

        printf("%-30s Nota: %.2f\n",
               nomesTemp[i],
               notasTemp[i]);
    }
}


// ============================================================
// ORDEM DECRESCENTE DE NOTAS
// ============================================================

void ordemDecrescente(char nomes[][100],
                      float notas[],
                      int quantidade) {

    char nomesTemp[MAX_ALUNOS][100];
    float notasTemp[MAX_ALUNOS];

    int i, j;

    if (quantidade == 0) {
        printf("\nNenhum aluno cadastrado.\n");
        return;
    }

    for (i = 0; i < quantidade; i++) {

        strcpy(nomesTemp[i], nomes[i]);
        notasTemp[i] = notas[i];
    }

    // Bubble Sort
    for (i = 0; i < quantidade - 1; i++) {

        for (j = 0; j < quantidade - i - 1; j++) {

            if (notasTemp[j] < notasTemp[j + 1]) {

                float notaAux;
                char nomeAux[100];

                notaAux = notasTemp[j];
                notasTemp[j] = notasTemp[j + 1];
                notasTemp[j + 1] = notaAux;

                strcpy(nomeAux, nomesTemp[j]);
                strcpy(nomesTemp[j], nomesTemp[j + 1]);
                strcpy(nomesTemp[j + 1], nomeAux);
            }
        }
    }

    printf("\n========== NOTAS DECRESCENTES ==========\n");

    for (i = 0; i < quantidade; i++) {

        printf("%-30s Nota: %.2f\n",
               nomesTemp[i],
               notasTemp[i]);
    }
}


// ============================================================
// ORDEM CRESCENTE DE NOTAS
// ============================================================

void ordemCrescente(char nomes[][100],
                    float notas[],
                    int quantidade) {

    char nomesTemp[MAX_ALUNOS][100];
    float notasTemp[MAX_ALUNOS];

    int i, j;

    if (quantidade == 0) {
        printf("\nNenhum aluno cadastrado.\n");
        return;
    }

    for (i = 0; i < quantidade; i++) {

        strcpy(nomesTemp[i], nomes[i]);
        notasTemp[i] = notas[i];
    }

    // Bubble Sort
    for (i = 0; i < quantidade - 1; i++) {

        for (j = 0; j < quantidade - i - 1; j++) {

            if (notasTemp[j] > notasTemp[j + 1]) {

                float notaAux;
                char nomeAux[100];

                notaAux = notasTemp[j];
                notasTemp[j] = notasTemp[j + 1];
                notasTemp[j + 1] = notaAux;

                strcpy(nomeAux, nomesTemp[j]);
                strcpy(nomesTemp[j], nomesTemp[j + 1]);
                strcpy(nomesTemp[j + 1], nomeAux);
            }
        }
    }

    printf("\n========== NOTAS CRESCENTES ==========\n");

    for (i = 0; i < quantidade; i++) {

        printf("%-30s Nota: %.2f\n",
               nomesTemp[i],
               notasTemp[i]);
    }
}


// ============================================================
// ALUNOS REPROVADOS
// Nota < 7
// ============================================================

void alunosReprovados(char nomes[][100],
                      float notas[],
                      int quantidade) {

    int i;
    int encontrou = 0;

    if (quantidade == 0) {
        printf("\nNenhum aluno cadastrado.\n");
        return;
    }

    printf("\n========== ALUNOS REPROVADOS ==========\n");

    for (i = 0; i < quantidade; i++) {

        if (notas[i] < 7) {

            printf("%-30s Nota: %.2f\n",
                   nomes[i],
                   notas[i]);

            encontrou = 1;
        }
    }

    if (!encontrou) {
        printf("Nenhum aluno reprovado.\n");
    }
}


// ============================================================
// ALUNOS COM NOTAS ENTRE X E Y
// ============================================================

void notasEntreXeY(char nomes[][100],
                   float notas[],
                   int quantidade) {

    float x, y;
    int i;
    int encontrou = 0;

    if (quantidade == 0) {
        printf("\nNenhum aluno cadastrado.\n");
        return;
    }

    printf("\nDigite a menor nota: ");
    scanf("%f", &x);

    printf("Digite a maior nota: ");
    scanf("%f", &y);

    limparBuffer();

    if (x > y) {

        printf("\nIntervalo invalido!\n");
        printf("A primeira nota deve ser menor que a segunda.\n");

        return;
    }

    if (x < 0 || y > 10) {

        printf("\nAs notas devem estar entre 0 e 10.\n");
        return;
    }

    printf("\n========== ALUNOS ENTRE %.2f E %.2f ==========\n",
           x, y);

    for (i = 0; i < quantidade; i++) {

        if (notas[i] >= x && notas[i] <= y) {

            printf("%-30s Nota: %.2f\n",
                   nomes[i],
                   notas[i]);

            encontrou = 1;
        }
    }

    if (!encontrou) {
        printf("Nenhum aluno encontrado nesse intervalo.\n");
    }
}


// ============================================================
// DESVIO DA NOTA DO ALUNO EM RELACAO A MEDIA
// Exemplo:
// Media = 7
// Nota do aluno = 6
// Desvio = 6 - 7 = -1
// ============================================================

void desvioAluno(char nomes[][100],
                 float notas[],
                 int quantidade) {

    char nomeBusca[100];
    float media;
    int i;
    int encontrado = 0;

    if (quantidade == 0) {
        printf("\nNenhum aluno cadastrado.\n");
        return;
    }

    media = calcularMedia(notas, quantidade);

    printf("\nDigite o nome do aluno: ");
    fgets(nomeBusca, 100, stdin);

    nomeBusca[strcspn(nomeBusca, "\n")] = '\0';

    for (i = 0; i < quantidade; i++) {

        if (strcasecmp(nomes[i], nomeBusca) == 0) {

            float desvio;

            desvio = notas[i] - media;

            printf("\n========== DESVIO ==========\n");
            printf("Aluno: %s\n", nomes[i]);
            printf("Nota: %.2f\n", notas[i]);
            printf("Media da turma: %.2f\n", media);
            printf("Desvio: %.2f\n", desvio);

            if (desvio > 0) {

                printf("O aluno esta %.2f pontos acima da media.\n",
                       desvio);

            } else if (desvio < 0) {

                printf("O aluno esta %.2f pontos abaixo da media.\n",
                       fabs(desvio));

            } else {

                printf("O aluno esta exatamente na media.\n");
            }

            encontrado = 1;
            break;
        }
    }

    if (!encontrado) {
        printf("\nAluno nao encontrado.\n");
    }
}
