import os

## Em Python, não usamos ponteiros manuais (como *inicio ou NULL) nem precisamos declarar variáveis no topo antes de usar. A alocação de memória é
## automática e o equivalente ao NULL do C++ é o None.
# Equivalente à 'struct Lista' do C++

class No:
    def __init__(self, numero):
        self.numero = numero
        self.prox = None  # Equivalente ao ponteiro *prox (inicia apontando para NULL)

class ListaEncadeada:

    def __init__(self):
        # Equivalente às variáveis globais/controle de ponteiros:
        self.inicio = None  # Lista *inicio = NULL
        self.fim = None     # Lista *fim = NULL

    def inserir_inicio(self, numero):
        novo = No(numero)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.prox = self.inicio
            self.inicio = novo
        print(f"\nNúmero {numero} inserido no INÍCIO com sucesso!")

    def inserir_fim(self, numero):
        novo = No(numero)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.prox = novo
            self.fim = novo
        print(f"\nNúmero {numero} inserido no FIM com sucesso!")

    def consultar(self):
        if self.inicio is None:
            print("\nLista vazia!")
            return

        print("\n--- Elementos da Lista ---")
        aux = self.inicio  # aux = inicio
        posicao = 1
        while aux is not None:
            print(f"Posição {posicao}: {aux.numero}")
            aux = aux.prox  # Percorre elemento por elemento
            posicao += 1

    def remover(self, numero):
        if self.inicio is None:
            print("\nLista vazia! Nenhum elemento para remover.")
            return

        aux = self.inicio  # aux para percorrer
        ant = None         # anterior para reencadear os ponteiros
        achou = False

        # Busca o elemento na lista
        while aux is not None:
            if aux.numero == numero:
                achou = True
                break
            ant = aux
            aux = aux.prox

        if not achou:
            print(f"\nNúmero {numero} não encontrado na lista!")
        else:
            # Caso 1: O nó a remover é o PRIMEIRO
            if aux == self.inicio:
                self.inicio = self.inicio.prox
                if self.inicio is None:  # Se a lista tinha apenas 1 elemento
                    self.fim = None

            # Caso 2: O nó está no MEIO ou FIM
            else:
                ant.prox = aux.prox
                if aux == self.fim:  # Se era o último elemento
                    self.fim = ant

            # No Python, o Garbage Collector descarta 'aux' da memória automaticamente
            print(f"\nNúmero {numero} removido com sucesso!")

    def esvaziar(self):
        if self.inicio is None:
            print("\nA lista já está vazia!")
        else:
            # Em Python, basta apontar inicio e fim para None
            self.inicio = None
            self.fim = None
            print("\nLista esvaziada com sucesso!")

    def limpar_tela(self):
     os.system('cls' if os.name == 'nt' else 'clear')
     
# --- MENU DE OPÇÕES ---
def main():
    lista = ListaEncadeada()

    while True:
        lista.limpar_tela() 
        print("\n===============================")
        print("        MENU DE OPÇÕES         ")
        print("===============================")
        print(" 1 - Inserir inicio da lista")
        print(" 2 - Inserir fim da lista")
        print(" 3 - Consultar toda a lista")
        print(" 4 - Remover da lista")
        print(" 5 - Esvaziar a lista")
        print(" 6 - Sair do Sistema")
        
        try:
            opcao = int(input("\nDigite a opção: "))
        except ValueError:
            print("\nPor favor, digite um número válido!")
            continue

        if opcao == 1:
            num = int(input("\nDigite o número para inserir no INÍCIO: "))
            lista.inserir_inicio(num)
            input("\nPressione Enter para continuar...")

        elif opcao == 2:
            num = int(input("\nDigite o número para inserir no FIM: "))
            lista.inserir_fim(num)
            input("\nPressione Enter para continuar...")

        elif opcao == 3:
            lista.consultar()
            input("\nPressione Enter para continuar...")

        elif opcao == 4:
            num = int(input("\nDigite o número que deseja remover: "))
            lista.remover(num)
            input("\nPressione Enter para continuar...")

        elif opcao == 5:
            lista.esvaziar()
            input("\nPressione Enter para continuar...")

        elif opcao == 6:
            print("\nSaindo do sistema...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()