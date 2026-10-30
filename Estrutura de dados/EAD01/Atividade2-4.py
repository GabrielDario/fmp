class Chamado:
    def __init__(self, protocolo, cliente, descricao):
        self.protocolo = protocolo
        self.cliente = cliente
        self.descricao = descricao
        self.proximo = None


class FilaSuporte:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    # 1. Cadastrar chamado no final usando enqueue
    def enqueue(self, protocolo, cliente, descricao):
        novo = Chamado(protocolo, cliente, descricao)
        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        print(f"Chamado '{protocolo}' cadastrado para {cliente}.")

    # 2. Consultar o próximo chamado sem removê-lo
    def peek(self):
        if self.esta_vazia():
            return None
        return self.inicio

    # 3. Atender e retirar o primeiro usando dequeue
    def dequeue(self):
        if self.esta_vazia():
            return None
        removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        removido.proximo = None
        return removido

    # 4. Listar do início ao fim
    def listar(self):
        if self.esta_vazia():
            print("Fila de suporte vazia.")
            return
        print("\n--- Fila de Suporte (Início ao Fim) ---")
        atual = self.inicio
        while atual:
            print(f"Protocolo: {atual.protocolo} | Cliente: {atual.cliente} | Descrição: {atual.descricao}")
            atual = atual.proximo
        print("-" * 45)

    # 5. Contar chamados pendentes
    def contar(self):
        contador = 0
        atual = self.inicio
        while atual:
            contador += 1
            atual = atual.proximo
        return contador

    # 6. Buscar protocolo sem alterar a ordem
    def buscar(self, protocolo):
        atual = self.inicio
        while atual:
            if atual.protocolo == protocolo:
                return atual
            atual = atual.proximo
        return None


# Testes Obrigatórios - Exercício 4
if __name__ == "__main__":
    print("=== TESTES: FILA DE SUPORTE ===")
    fila = FilaSuporte()

    # Fila vazia
    fila.listar()
    print(f"Chamados pendentes: {fila.contar()}")

    # Um único chamado
    print("\n[Teste] Adicionando um único chamado:")
    fila.enqueue("T01", "Alice", "Erro de login")
    fila.listar()

    # Vários enqueue seguidos de dequeue
    fila.enqueue("T02", "Bruno", "Sem internet")
    fila.enqueue("T03", "Carla", "Lentidão no sistema")
    fila.listar()

    print("\nRealizando atendimento (dequeue):")
    atendido = fila.dequeue()
    print(f"Atendido agora: {atendido.protocolo} ({atendido.cliente})")
    fila.listar()

    # Protocolo inexistente
    print("\n[Teste] Buscando protocolo inexistente:")
    res = fila.buscar("T99")
    print("Resultado da busca T99:", res)

    # Atendimento até esvaziar a fila
    print("\n[Teste] Esvaziando fila restante:")
    while not fila.esta_vazia():
        rem = fila.dequeue()
        print(f"Removido: {rem.protocolo}")
    fila.listar()