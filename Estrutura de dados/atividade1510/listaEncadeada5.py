class Entrega:
    def __init__(self, codigo, cliente, endereco, status, distancia_km):
        self.codigo = codigo
        self.cliente = cliente
        self.endereco = endereco
        self.status = status  # 'Pendente', 'Em rota' ou 'Entregue'
        self.distancia_km = distancia_km
        self.proximo = None

    def __str__(self):
        return (f"Código: {self.codigo} | Cliente: {self.cliente} | "
                f"Endereço: {self.endereco} | Status: {self.status} | "
                f"Distância: {self.distancia_km:.1f} km")


class ListaEntregas:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def cadastrar_no_final(self, codigo, cliente, endereco, status, distancia_km):
        if self.buscar(codigo) is not None:
            print(f"\n[ERRO] Já existe uma entrega com o código {codigo}.")
            return False

        nova_entrega = Entrega(codigo, cliente, endereco, status, distancia_km)
        
        if self.inicio is None:
            self.inicio = nova_entrega
            self.fim = nova_entrega
        else:
            self.fim.proximo = nova_entrega
            self.fim = nova_entrega

        print(f"\n[OK] Entrega {codigo} cadastrada com sucesso!")
        return True

    def listar(self):
        if self.inicio is None:
            print("\n-------------------------------------------")
            print("         LISTA DE ENTREGAS VAZIA           ")
            print("-------------------------------------------")
            return

        print("\n===========================================")
        print("            LISTA DE ENTREGAS              ")
        print("===========================================")
        atual = self.inicio
        while atual is not None:
            print(atual)
            atual = atual.proximo
        print("===========================================")

    def buscar(self, codigo):
        atual = self.inicio
        while atual is not None:
            if atual.codigo == codigo:
                return atual
            atual = atual.proximo
        return None

    def alterar_status(self, codigo, novo_status):
        entrega = self.buscar(codigo)
        if entrega:
            entrega.status = novo_status
            print(f"\n[OK] Status da entrega {codigo} alterado para '{novo_status}'.")
        else:
            print(f"\n[ERRO] Entrega com código {codigo} não encontrada.")

    def contar_pendentes(self):
        contador = 0
        atual = self.inicio
        while atual is not None:
            if atual.status == "Pendente":
                contador += 1
            atual = atual.proximo
        return contador

    def calcular_distancia_total(self):
        distancia_total = 0.0
        atual = self.inicio
        while atual is not None:
            distancia_total += atual.distancia_km
            atual = atual.proximo
        return distancia_total

    def remover_entregues(self):
        atual = self.inicio
        anterior = None
        removidos = 0

        while atual is not None:
            if atual.status == "Entregue":
                proximo_no = atual.proximo

                if anterior is None:
                    self.inicio = proximo_no
                else:
                    anterior.proximo = proximo_no

                if atual == self.fim:
                    self.fim = anterior

                removidos += 1
                atual = proximo_no
            else:
                anterior = atual
                atual = atual.proximo

        print(f"\n[OK] Removidas {removidos} entrega(s) concluída(s) ('Entregue').")

    def esvaziar(self):
        self.inicio = None
        self.fim = None
        print("\n[OK] Lista de entregas esvaziada.")


def ler_status():
    print("\nEscolha o status:")
    print("1 - Pendente")
    print("2 - Em rota")
    print("3 - Entregue")
    while True:
        opcao = input("Opção de status: ").strip()
        if opcao == "1":
            return "Pendente"
        elif opcao == "2":
            return "Em rota"
        elif opcao == "3":
            return "Entregue"
        else:
            print("Opção inválida! Digite 1, 2 ou 3.")


def menu():
    sistema = ListaEntregas()

    while True:
        print("\n" + "="*45)
        print("    SISTEMA DE ENTREGAS - TRANSPORTADORA   ")
        print("="*45)
        print("1. Cadastrar entrega no final")
        print("2. Listar todas as entregas")
        print("3. Buscar entrega pelo código")
        print("4. Alterar estado de uma entrega")
        print("5. Contar entregas pendentes")
        print("6. Calcular distância total")
        print("7. Remover entregas com estado 'Entregue'")
        print("8. Esvaziar a lista")
        print("9. Encerrar o sistema")
        print("="*45)

        opcao = input("Digite a opção desejada (1-9): ").strip()

        if opcao == "1":
            try:
                codigo = int(input("Código da entrega: "))
                cliente = input("Nome do cliente: ").strip()
                endereco = input("Endereço: ").strip()
                status = ler_status()
                distancia = float(input("Distância (em km): "))
                sistema.cadastrar_no_final(codigo, cliente, endereco, status, distancia)
            except ValueError:
                print("\n[ERRO] Código e Distância devem ser valores numéricos válidos.")

        elif opcao == "2":
            sistema.listar()

        elif opcao == "3":
            try:
                codigo = int(input("Digite o código da entrega para busca: "))
                entrega = sistema.buscar(codigo)
                if entrega:
                    print(f"\n[ENCONTRADA] {entrega}")
                else:
                    print(f"\n[ERRO] Entrega com código {codigo} não foi encontrada.")
            except ValueError:
                print("\n[ERRO] O código precisa ser um número inteiro.")

        elif opcao == "4":
            try:
                codigo = int(input("Digite o código da entrega: "))
                if sistema.buscar(codigo):
                    novo_status = ler_status()
                    sistema.alterar_status(codigo, novo_status)
                else:
                    print(f"\n[ERRO] Entrega {codigo} não encontrada.")
            except ValueError:
                print("\n[ERRO] O código precisa ser um número inteiro.")

        elif opcao == "5":
            pendentes = sistema.contar_pendentes()
            print(f"\n[INFO] Total de entregas pendentes: {pendentes}")

        elif opcao == "6":
            total_km = sistema.calcular_distancia_total()
            print(f"\n[INFO] Distância total percorrida/planejada: {total_km:.2f} km")

        elif opcao == "7":
            sistema.remover_entregues()

        elif opcao == "8":
            confirma = input("Tem certeza que deseja esvaziar a lista? (s/n): ").strip().lower()
            if confirma == 's':
                sistema.esvaziar()

        elif opcao == "9":
            sistema.esvaziar()
            print("\nSaindo do sistema... Até logo!\n")
            break

        else:
            print("\n[ERRO] Opção inválida. Escolha um número de 1 a 9.")


if __name__ == "__main__":
    menu()