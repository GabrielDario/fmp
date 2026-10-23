class Jogador:
    def __init__(self, identificador, nome):
        self.id = identificador
        self.nome = nome
        self.pontos = 0
        self.proximo = None


class TurnosJogo:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.atual = None

    # 1. Adicionar jogador ao final do ciclo
    def adicionar_jogador(self, identificador, nome):
        # Verifica se ID já existe
        if self._buscar_por_id(identificador) is not None:
            print(f"Erro: Jogador com ID {identificador} já existe.")
            return False

        novo = Jogador(identificador, nome)

        # Caso A: Lista Vazia
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            novo.proximo = novo  # Aponta para si mesmo
            self.atual = novo
        else:
            # Caso B: Adicionar ao final da lista circular
            self.fim.proximo = novo
            novo.proximo = self.inicio
            self.fim = novo

        return True

    def _buscar_por_id(self, identificador):
        if self.inicio is None:
            return None

        aux = self.inicio
        while True:
            if aux.id == identificador:
                return aux
            aux = aux.proximo
            if aux == self.inicio:
                break
        return None

    # 2. Listar todos os jogadores exatamente uma vez
    def listar_jogadores(self):
        if self.inicio is None:
            print("Nenhum jogador cadastrado.")
            return

        print("\n--- JOGADORES NO JOGO ---")
        aux = self.inicio
        while True:
            marcador = " <- (TURNO ATUAL)" if aux == self.atual else ""
            print(f"ID: {aux.id} | Nome: {aux.nome:<12} | Pontos: {aux.pontos}{marcador}")
            aux = aux.proximo
            if aux == self.inicio:
                break
        print("-------------------------")

    # 3. Mostrar o jogador atual
    def mostrar_atual(self):
        if self.atual is None:
            print("Não há jogadores ativos no momento.")
        else:
            print(f"\n[JOGADOR ATUAL] ID: {self.atual.id} | Nome: {self.atual.nome} | Pontos: {self.atual.pontos}")

    # 4. Passar o turno para o próximo
    def passar_turno(self):
        if self.atual is None:
            print("Não há jogadores para passar o turno.")
            return

        self.atual = self.atual.proximo
        print(f"Turno passado para: {self.atual.nome} (ID: {self.atual.id})")

    # 5. Registrar pontos para o jogador atual
    def registrar_pontos(self, pontos):
        if self.atual is None:
            print("Não há jogador atual para receber pontos.")
            return

        self.atual.pontos += pontos
        print(f"{pontos} pontos adicionados para {self.atual.nome}. Total: {self.atual.pontos}")

    # 6. Remover um jogador pelo identificador
    def remover_jogador(self, identificador):
        if self.inicio is None:
            print("A lista está vazia.")
            return False

        alvo = self._buscar_por_id(identificador)
        if alvo is None:
            print(f"Jogador com ID {identificador} não encontrado.")
            return False

        # Caso A: Único jogador na lista
        if self.inicio == self.fim and self.inicio == alvo:
            self.inicio = None
            self.fim = None
            self.atual = None
            print(f"Jogador {alvo.nome} removido. A lista ficou vazia.")
            return True

        # Encontra o nó anterior ao alvo
        ant = self.inicio
        while ant.proximo != alvo:
            ant = ant.proximo

        # Atualiza encadeamento ignorando o alvo
        ant.proximo = alvo.proximo

        # Ajusta self.inicio se o primeiro foi removido
        if alvo == self.inicio:
            self.inicio = alvo.proximo
            self.fim.proximo = self.inicio  # Garante invariante do fim

        # Ajusta self.fim se o último foi removido
        if alvo == self.fim:
            self.fim = ant

        # Ajusta self.atual se o jogador do turno atual foi removido
        if alvo == self.atual:
            self.atual = alvo.proximo

        print(f"Jogador {alvo.nome} (ID: {identificador}) removido do jogo.")

        # 7. Encerrar aviso se não houver mais jogadores
        if self.inicio is None:
            print("Não há mais jogadores no jogo.")

        return True


# Suite de testes automatizados obrigatórios
def executar_testes_obrigatorios():
    print("\n=========================================")
    print("   INICIANDO TESTES AUTOMATIZADOS")
    print("=========================================")

    jogo = TurnosJogo()

    print("\n1. Teste: Lista vazia...")
    jogo.listar_jogadores()
    jogo.mostrar_atual()

    print("\n2. Teste: Um único jogador apontando para si...")
    jogo.adicionar_jogador(1, "Alice")
    jogo.listar_jogadores()
    print(f"Inicio aponta para Fim? {jogo.inicio == jogo.fim}")
    print(f"Primeiro.proximo aponta para si mesmo? {jogo.inicio.proximo == jogo.inicio}")

    print("\n3. Teste: Adicionar mais jogadores e rodar mais turnos que a quantidade de jogadores...")
    jogo.adicionar_jogador(2, "Bob")
    jogo.adicionar_jogador(3, "Caio")
    jogo.listar_jogadores()

    print("\nExecutando 5 passagens de turno em uma lista de 3 jogadores:")
    for i in range(1, 6):
        print(f"Passo {i}: ", end="")
        jogo.passar_turno()

    print("\n4. Teste: Remover jogador do meio/atual (Bob - ID 2)...")
    jogo.atual = jogo._buscar_por_id(2)  # Força o turno em Bob
    jogo.mostrar_atual()
    jogo.remover_jogador(2)
    jogo.mostrar_atual()
    jogo.listar_jogadores()

    print("\n5. Teste: Remover o primeiro jogador (Alice - ID 1)...")
    jogo.remover_jogador(1)
    jogo.listar_jogadores()
    print(f"fim.proximo é igual ao novo início? {jogo.fim.proximo == jogo.inicio}")

    print("\n6. Teste: Remover o último jogador restante (Caio - ID 3)...")
    jogo.remover_jogador(3)
    jogo.listar_jogadores()

    print("\n=========================================")
    print("   TESTES CONCLUÍDOS COM SUCESSO")
    print("=========================================\n")


def menu():
    jogo = TurnosJogo()
    opcao = -1

    while opcao != 0:
        print("\n=====================================")
        print("      CONTROLE DE TURNOS DO JOGO     ")
        print("=====================================")
        print("1. Adicionar Jogador")
        print("2. Listar Todos os Jogadores")
        print("3. Mostrar Jogador Atual")
        print("4. Passar Turno")
        print("5. Registrar Pontos para Jogador Atual")
        print("6. Remover Jogador por ID")
        print("7. Executar Testes Automatizados")
        print("0. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue

        if opcao == 1:
            try:
                identificador = int(input("ID do Jogador: "))
                nome = input("Nome do Jogador: ")
                if jogo.adicionar_jogador(identificador, nome):
                    print(f"Jogador {nome} adicionado com sucesso.")
            except ValueError:
                print("ID deve ser um número inteiro.")
        elif opcao == 2:
            jogo.listar_jogadores()
        elif opcao == 3:
            jogo.mostrar_atual()
        elif opcao == 4:
            jogo.passar_turno()
        elif opcao == 5:
            try:
                pts = int(input("Quantidade de pontos a somar: "))
                jogo.registrar_pontos(pts)
            except ValueError:
                print("Valor de pontos deve ser inteiro.")
        elif opcao == 6:
            try:
                identificador = int(input("ID do Jogador a remover: "))
                jogo.remover_jogador(identificador)
            except ValueError:
                print("ID inválido.")
        elif opcao == 7:
            executar_testes_obrigatorios()
        elif opcao == 0:
            print("Encerrando o programa.")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()