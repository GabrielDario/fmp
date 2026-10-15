class Chamado:
    def __init__(self, codigo, solicitante, descricao, prioridade):
        self.codigo = codigo
        self.solicitante = solicitante
        self.descricao = descricao
        self.prioridade = prioridade
        self.proximo = None


class FilaChamados:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.total = 0

    # 1. Registrar chamado no final (O(1) usando ponteiro fim)
    def registrar(self, codigo, solicitante, descricao, prioridade):
        novo = Chamado(codigo, solicitante, descricao, prioridade)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.total += 1
        print(f"Chamado #{codigo} registrado com sucesso!")

    # 2. Listar todos os chamados na ordem de abertura
    def listar(self):
        if self.inicio is None:
            print("\nA fila de chamados está vazia.")
            return

        print("\n--- Lista de Chamados ---")
        atual = self.inicio
        while atual is not None:
            print(f"Código: {atual.codigo} | Solicitante: {atual.solicitante} | "
                  f"Descrição: {atual.descricao} | Prioridade: {atual.prioridade}")
            atual = atual.proximo
        print("------------------------")

    # 3. Buscar chamado pelo código
    def buscar(self, codigo):
        atual = self.inicio
        while atual is not None:
            if atual.codigo == codigo:
                return atual
            atual = atual.proximo
        return None

    # 4. Exibir quantidade de chamados
    def quantidade(self):
        return self.total

    # 5. Remover o primeiro chamado (Atende aos 3 testes obrigatórios)
    def remover_primeiro(self):
        # Teste 1: Lista vazia
        if self.inicio is None:
            print("\n[Erro] Não é possível remover: a fila está vazia.")
            return None

        removido = self.inicio

        # Teste 2: Apenas 1 chamado
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        # Teste 3: Vários chamados
        else:
            self.inicio = self.inicio.proximo

        self.total -= 1
        print(f"\nChamado #{removido.codigo} atendido/removido com sucesso!")
        return removido

    # 6. Encerrar sistema
    def encerrar(self):
        atual = self.inicio
        while atual is not None:
            proximo_no = atual.proximo
            del atual  # Libera a referência do nó
            atual = proximo_no
        self.inicio = None
        self.fim = None
        self.total = 0
        print("\nSistema encerrado. Memória de todos os nós liberada.")


# ==========================================
# TESTES OBRIGATÓRIOS E FUNCIONALIDADES
# ==========================================
if __name__ == "__main__":
    fila = FilaChamados()

    print("=== TESTE 1: Remover com lista vazia ===")
    fila.remover_primeiro()

    print("\n=== REGISTRANDO CHAMADOS ===")
    fila.registrar(101, "Ana", "Computador não liga", "Alta")
    fila.registrar(102, "Carlos", "Sem acesso à rede", "Média")
    fila.registrar(103, "Beatriz", "Erro no sistema de vendas", "Alta")

    print(f"\nTotal de chamados: {fila.quantidade()}")
    fila.listar()

    print("\n=== TESTE 3: Remover com vários chamados ===")
    fila.remover_primeiro()
    fila.listar()

    print("\n=== BUSCAR CHAMADO ===")
    busca = fila.buscar(102)
    if busca:
        print(f"Encontrado -> Código: {busca.codigo}, Solicitante: {busca.solicitante}")
    else:
        print("Chamado não encontrado.")

    print("\n=== TESTE 2: Remover até restar 1 e remover o único chamado ===")
    fila.remover_primeiro()  # Resta apenas o 103
    fila.listar()
    fila.remover_primeiro()  # Remove o único chamado restante (inicio e fim voltam a None)
    fila.listar()

    print("\n=== ENCERRAMENTO ===")
    fila.encerrar()