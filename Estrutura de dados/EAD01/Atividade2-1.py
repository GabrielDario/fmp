class Acao:
    def __init__(self, identificador, descricao, horario):
        self.id = identificador
        self.descricao = descricao
        self.horario = horario
        self.proximo = None


class PilhaDesfazer:
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    # 1. Registrar uma ação usando push
    def push(self, identificador, descricao, horario):
        novo = Acao(identificador, descricao, horario)
        novo.proximo = self.topo
        self.topo = novo

    # 2. Mostrar a ação mais recente sem removê-la (Peek/Top)
    def peek(self):
        if self.esta_vazia():
            return None
        return self.topo

    # 3. Desfazer a última ação usando pop
    def pop(self):
        if self.esta_vazia():
            return None
        removido = self.topo
        self.topo = self.topo.proximo
        removido.proximo = None
        return removido

    # 4. Listar o histórico do topo até a base
    def listar(self):
        if self.esta_vazia():
            print("Histórico de desfazer vazio.")
            return
        print("\n--- Histórico de Ações (Topo à Base) ---")
        atual = self.topo
        while atual:
            print(f"ID: {atual.id} | Descrição: {atual.descricao} | Horário: {atual.horario}")
            atual = atual.proximo
        print("-" * 42)

    # 5. Contar as ações armazenadas
    def contar(self):
        contador = 0
        atual = self.topo
        while atual:
            contador += 1
            atual = atual.proximo
        return contador

    # 6. Esvaziar a pilha com segurança
    def esvaziar(self):
        self.topo = None
        print("Pilha esvaziada com segurança.")


# Testes Atividade 1
if __name__ == "__main__":
    print("=== TESTES: PILHA DESFAZER (EDITOR) ===")
    editor = PilhaDesfazer()

    # Pilha vazia
    editor.listar()
    print(f"Total de ações: {editor.contar()}")

    # Uma única ação
    editor.push(1, "Digitação de texto", "10:00")
    print("\n[Teste] Apenas uma ação:")
    editor.listar()
    
    # Várias ações
    editor.push(2, "Inserção de imagem", "10:02")
    editor.push(3, "Alteração de fonte", "10:05")
    editor.listar()
    print(f"Total de ações: {editor.contar()}")

    # Desfazimentos consecutivos
    desfeito = editor.pop()
    print(f"Desfeito: {desfeito.descricao}")
    editor.listar()

    # Tentativa de desfazer quando vazio / Esvaziar
    editor.pop()
    editor.pop()
    print("Tentando desfazer com pilha vazia:")
    if editor.pop() is None:
        print("Aviso: Pilha vazia, nada para desfazer.")