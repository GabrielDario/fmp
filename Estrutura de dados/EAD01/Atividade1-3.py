class Atendimento:
    def __init__(self, codigo, paciente, data, horario):
        self.codigo = codigo
        self.paciente = paciente
        self.data = data        # Formato: AAAA-MM-DD
        self.horario = horario  # Formato: HH:MM
        self.anterior = None
        self.proximo = None


class AgendaAtendimentos:
    def __init__(self):
        self.inicio = None
        self.fim = None

    # 4. Buscar pelo código
    def buscar_por_codigo(self, codigo):
        atual = self.inicio
        while atual is not None:
            if atual.codigo == codigo:
                return atual
            atual = atual.proximo
        return None

    # 2. Impedir dois atendimentos no mesmo horário (conflito)
    def _verificar_conflito(self, data, horario, codigo_ignorado=None):
        atual = self.inicio
        while atual is not None:
            if atual.codigo != codigo_ignorado:
                if atual.data == data and atual.horario == horario:
                    return True
            atual = atual.proximo
        return False

    # 1. Inserir mantendo a ordem cronológica
    def inserir_ordenado(self, novo_no):
        # 2. Impedir código duplicado
        if self.buscar_por_codigo(novo_no.codigo) is not None:
            print(f"Erro: Código {novo_no.codigo} já cadastrado.")
            return False

        # 2. Impedir mesmo horário
        if self._verificar_conflito(novo_no.data, novo_no.horario):
            print(f"Erro: Já existe atendimento em {novo_no.data} às {novo_no.horario}.")
            return False

        # Caso A: Lista Vazia
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
            return True

        # Chave de ordenação cronológica (data + horario)
        chave_novo = (novo_no.data, novo_no.horario)

        # Caso B: Inserir no início
        chave_inicio = (self.inicio.data, self.inicio.horario)
        if chave_novo < chave_inicio:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no
            return True

        # Busca a posição de inserção (meio ou fim)
        atual = self.inicio
        while atual.proximo is not None and (atual.proximo.data, atual.proximo.horario) < chave_novo:
            atual = atual.proximo

        # Caso C: Inserir no fim
        if atual.proximo is None:
            atual.proximo = novo_no
            novo_no.anterior = atual
            self.fim = novo_no
        else:
            # Caso D: Inserir entre dois nós
            novo_no.proximo = atual.proximo
            novo_no.anterior = atual
            atual.proximo.anterior = novo_no
            atual.proximo = novo_no

        return True

    # Desconecta o nó da estrutura mantendo o objeto em memória
    def _desconectar_no(self, codigo):
        no = self.buscar_por_codigo(codigo)
        if no is None:
            return None

        # Se for o único nó
        if no == self.inicio and no == self.fim:
            self.inicio = None
            self.fim = None
        # Se for o primeiro nó
        elif no == self.inicio:
            self.inicio = no.proximo
            self.inicio.anterior = None
        # Se for o último nó
        elif no == self.fim:
            self.fim = no.anterior
            self.fim.proximo = None
        # Se estiver no meio
        else:
            no.anterior.proximo = no.proximo
            no.proximo.anterior = no.anterior

        no.anterior = None
        no.proximo = None
        return no

    # 5. Cancelar um atendimento
    def cancelar(self, codigo):
        no = self._desconectar_no(codigo)
        return no is not None

    # 6. Reagendar removendo o nó e reinserindo-o corretamente
    def reagendar(self, codigo, nova_data, novo_horario):
        no = self.buscar_por_codigo(codigo)
        if no is None:
            print(f"Erro: Atendimento com código {codigo} não encontrado.")
            return False

        if self._verificar_conflito(nova_data, novo_horario, codigo_ignorado=codigo):
            print(f"Erro: Conflito de horário em {nova_data} às {novo_horario}.")
            return False

        # Desconecta da posição atual
        self._desconectar_no(codigo)

        # Atualiza dados
        no.data = nova_data
        no.horario = novo_horario

        # Reinsere na ordem cronológica correta
        return self.inserir_ordenado(no)

    # 3. Listar em ordem cronológica
    def listar_cronologica(self):
        if self.inicio is None:
            print("Agenda vazia.")
            return

        print("\n--- AGENDA DE ATENDIMENTOS (CRONOLÓGICA) ---")
        atual = self.inicio
        while atual is not None:
            print(f"[{atual.codigo}] Paciente: {atual.paciente:<15} | Data: {atual.data} | Horário: {atual.horario}")
            atual = atual.proximo
        print("-------------------------------------------")

    # 3. Listar em ordem inversa
    def listar_inversa(self):
        if self.fim is None:
            print("Agenda vazia.")
            return

        print("\n--- AGENDA DE ATENDIMENTOS (ORDEM INVERSA) ---")
        atual = self.fim
        while atual is not None:
            print(f"[{atual.codigo}] Paciente: {atual.paciente:<15} | Data: {atual.data} | Horário: {atual.horario}")
            atual = atual.anterior
        print("---------------------------------------------")

    # 7. Exibir o primeiro e o último atendimento
    def exibir_primeiro_e_ultimo(self):
        if self.inicio is None:
            print("Agenda vazia.")
            return

        p = self.inicio
        f = self.fim
        print(f"\n[PRIMEIRO ATENDIMENTO] Código: {p.codigo} | Paciente: {p.paciente} | Data: {p.data} | Horário: {p.horario}")
        print(f"[ÚLTIMO ATENDIMENTO]   Código: {f.codigo} | Paciente: {f.paciente} | Data: {f.data} | Horário: {f.horario}")


# Suite de testes automatizados obrigatórios
def executar_testes_obrigatorios():
    print("\n=========================================")
    print("   INICIANDO TESTES AUTOMATIZADOS")
    print("=========================================")

    agenda = AgendaAtendimentos()

    print("\n1. Teste: Inserir entre dois (base)...")
    agenda.inserir_ordenado(Atendimento(10, "Ana Santos", "2026-11-10", "10:00"))
    agenda.inserir_ordenado(Atendimento(30, "Carlos Lima", "2026-11-10", "14:00"))
    agenda.listar_cronologica()

    print("\n2. Teste: Inserir antes de todos (08:00)...")
    agenda.inserir_ordenado(Atendimento(5, "Beatriz Souza", "2026-11-10", "08:00"))
    agenda.listar_cronologica()

    print("\n3. Teste: Inserir depois de todos (16:00)...")
    agenda.inserir_ordenado(Atendimento(40, "Daniel Rocha", "2026-11-10", "16:00"))
    agenda.listar_cronologica()

    print("\n4. Teste: Inserir no meio (11:30)...")
    agenda.inserir_ordenado(Atendimento(20, "Eduardo Paes", "2026-11-10", "11:30"))
    agenda.listar_cronologica()

    print("\n5. Teste: Verificar conflito de horário (10:00)...")
    agenda.inserir_ordenado(Atendimento(99, "Conflito Teste", "2026-11-10", "10:00"))

    print("\n6. Teste: Reagendar para o fim (Código 5 de 08:00 para 18:00)...")
    agenda.reagendar(5, "2026-11-10", "18:00")
    agenda.listar_cronologica()

    print("\n7. Teste: Reagendar para o início (Código 40 de 16:00 para 07:30)...")
    agenda.reagendar(40, "2026-11-10", "07:30")
    agenda.listar_cronologica()

    print("\n8. Teste: Cancelar primeiro atendimento (Código 40)...")
    agenda.cancelar(40)
    agenda.listar_cronologica()

    print("\n9. Teste: Cancelar último atendimento (Código 5)...")
    agenda.cancelar(5)
    agenda.listar_cronologica()

    print("\n10. Teste: Cancelar até restar único e remover único...")
    agenda.cancelar(10)
    agenda.cancelar(20)
    print("Sobrou apenas 1 nó:")
    agenda.listar_cronologica()
    print("Removendo único nó (Código 30)...")
    agenda.cancelar(30)
    agenda.listar_cronologica()

    print("\n=========================================")
    print("   TESTES CONCLUÍDOS COM SUCESSO")
    print("=========================================\n")


def menu():
    agenda = AgendaAtendimentos()
    opcao = -1

    while opcao != 0:
        print("\n=====================================")
        print("     CLÍNICA - AGENDA DE ATENDIMENTO  ")
        print("=====================================")
        print("1. Novo Agendamento")
        print("2. Listar Ordem Cronológica")
        print("3. Listar Ordem Inversa")
        print("4. Buscar Atendimento por Código")
        print("5. Cancelar Atendimento")
        print("6. Reagendar Atendimento")
        print("7. Exibir Primeiro e Último Atendimento")
        print("8. Executar Testes Automatizados")
        print("0. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        if opcao == 1:
            try:
                codigo = int(input("Código: "))
                paciente = input("Paciente: ")
                data = input("Data (AAAA-MM-DD): ")
                horario = input("Horário (HH:MM): ")
                novo = Atendimento(codigo, paciente, data, horario)
                if agenda.inserir_ordenado(novo):
                    print("Atendimento agendado com sucesso!")
            except ValueError:
                print("Código deve ser um número inteiro.")
        elif opcao == 2:
            agenda.listar_cronologica()
        elif opcao == 3:
            agenda.listar_inversa()
        elif opcao == 4:
            try:
                codigo = int(input("Código para busca: "))
                no = agenda.buscar_por_codigo(codigo)
                if no:
                    print(f"\n[ENCONTRADO] Paciente: {no.paciente} | Data: {no.data} | Horário: {no.horario}")
                else:
                    print(f"Atendimento {codigo} não encontrado.")
            except ValueError:
                print("Código inválido.")
        elif opcao == 5:
            try:
                codigo = int(input("Código para cancelar: "))
                if agenda.cancelar(codigo):
                    print(f"Atendimento {codigo} cancelado com sucesso.")
                else:
                    print(f"Atendimento {codigo} não encontrado.")
            except ValueError:
                print("Código inválido.")
        elif opcao == 6:
            try:
                codigo = int(input("Código do atendimento: "))
                nova_data = input("Nova Data (AAAA-MM-DD): ")
                novo_horario = input("Novo Horário (HH:MM): ")
                if agenda.reagendar(codigo, nova_data, novo_horario):
                    print("Atendimento reagendado com sucesso!")
            except ValueError:
                print("Código inválido.")
        elif opcao == 7:
            agenda.exibir_primeiro_e_ultimo()
        elif opcao == 8:
            executar_testes_obrigatorios()
        elif opcao == 0:
            print("Encerrando a aplicação.")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()