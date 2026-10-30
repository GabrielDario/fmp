class Ponto:
    def __init__(self, codigo, setor, intervalo_min):
        self.codigo = codigo
        self.setor = setor
        self.intervalo_min = intervalo_min
        self.inspecionado = False
        self.proximo = None


class RotaInspecao:
    def __init__(self):
        self.inicio = None
        self.atual = None

    def esta_vazia(self):
        return self.inicio is None

    # 1. Adicionar um ponto ao final da rota
    def adicionar_fim(self, codigo, setor, intervalo_min):
        novo = Ponto(codigo, setor, intervalo_min)
        if self.esta_vazia():
            self.inicio = novo
            novo.proximo = novo
            self.atual = novo
        else:
            # Encontra o último nó
            temp = self.inicio
            while temp.proximo != self.inicio:
                temp = temp.proximo
            temp.proximo = novo
            novo.proximo = self.inicio

    # 2. Inserir um ponto depois de um código informado
    def inserir_apos(self, codigo_alvo, novo_codigo, setor, intervalo_min):
        if self.esta_vazia():
            print("Erro: Rota vazia.")
            return False

        temp = self.inicio
        while True:
            if temp.codigo == codigo_alvo:
                novo = Ponto(novo_codigo, setor, intervalo_min)
                novo.proximo = temp.proximo
                temp.proximo = novo
                print(f"Ponto '{novo_codigo}' inserido após '{codigo_alvo}'.")
                return True
            temp = temp.proximo
            if temp == self.inicio:
                break

        print(f"Código '{codigo_alvo}' não encontrado.")
        return False

    # 3. Listar uma volta completa
    def listar_volta(self):
        if self.esta_vazia():
            print("Rota vazia.")
            return

        print("\n--- Rota de Inspeção (Uma Volta Completa) ---")
        temp = self.inicio
        while True:
            status = "[X]" if temp.inspecionado else "[ ]"
            dest = " <--- [ATUAL]" if temp == self.atual else ""
            print(f"{status} Código: {temp.codigo} | Setor: {temp.setor} | Intervalo: {temp.intervalo_min}min{dest}")
            temp = temp.proximo
            if temp == self.inicio:
                break
        print("-" * 45)

    # 4. Avançar para o próximo ponto da inspeção
    def avancar(self):
        if self.esta_vazia():
            print("Rota vazia.")
            return
        self.atual = self.atual.proximo
        print(f"Avançado para o ponto: {self.atual.codigo} (Setor: {self.atual.setor})")

    # 5. Marcar o ponto atual como inspecionado
    def marcar_inspecionado(self):
        if self.esta_vazia():
            print("Rota vazia.")
            return
        self.atual.inspecionado = True
        print(f"Ponto {self.atual.codigo} marcado como inspecionado.")

    # 6. Remover um ponto da rota
    def remover_ponto(self, codigo):
        if self.esta_vazia():
            print("Erro: Rota vazia.")
            return False

        atual = self.inicio
        anterior = None

        # Achar o último nó para gerenciar a circularidade
        ultimo = self.inicio
        while ultimo.proximo != self.inicio:
            ultimo = ultimo.proximo

        # Caso especial: único nó na lista
        if self.inicio.codigo == codigo and self.inicio.proximo == self.inicio:
            print(f"Removido o único ponto da rota: {codigo}")
            self.inicio = None
            self.atual = None
            return True

        # Percorre para achar o nó a remover
        while True:
            if atual.codigo == codigo:
                break
            anterior = atual
            atual = atual.proximo
            if atual == self.inicio:
                print(f"Código '{codigo}' não encontrado para remoção.")
                return False

        # Se o nó a ser removido é o início
        if atual == self.inicio:
            self.inicio = self.inicio.proximo
            ultimo.proximo = self.inicio
        else:
            anterior.proximo = atual.proximo

        # Se o ponto removido era o 'atual' de inspeção, movemos o ponteiro atual
        if self.atual == atual:
            self.atual = atual.proximo

        print(f"Ponto '{codigo}' removido com sucesso.")
        return True

    # 7. Calcular o tempo total de uma volta
    def calcular_tempo_total(self):
        if self.esta_vazia():
            return 0

        total = 0
        temp = self.inicio
        while True:
            total += temp.intervalo_min
            temp = temp.proximo
            if temp == self.inicio:
                break
        return total

    # 8. Reiniciar os estados para uma nova rodada
    def reiniciar_rodada(self):
        if self.esta_vazia():
            return

        temp = self.inicio
        while True:
            temp.inspecionado = False
            temp = temp.proximo
            if temp == self.inicio:
                break
        self.atual = self.inicio
        print("Estados reiniciados para uma nova rodada de inspeção.")

if __name__ == "__main__":
    print("=== INICIALIZANDO TESTES DO ESCALONADOR DE INSPEÇÃO ===")
    rota = RotaInspecao()

    # --- Teste: Rota com um ponto ---
    print("\n[TESTE] Adicionando um único ponto...")
    rota.adicionar_fim("P1", "Caldeiraria", 15)
    rota.listar_volta()
    print(f"Tempo total da volta: {rota.calcular_tempo_total()} min")

    # --- Teste: Inserção depois do último ---
    print("\n[TESTE] Inserindo pontos adicionais e testando inserção após o último...")
    rota.adicionar_fim("P2", "Montagem", 20)
    rota.adicionar_fim("P3", "Pintura", 10)
    # Inserindo depois de P3 (que é o último)
    rota.inserir_apos("P3", "P4", "Expedição", 25)
    rota.listar_volta()

    # --- Teste: Código não encontrado ---
    print("\n[TESTE] Tentando inserir e remover código inexistente...")
    rota.inserir_apos("P99", "PX", "Inexistente", 5)
    rota.remover_ponto("P99")

    # --- Teste: Inspeção e avanço de duas voltas consecutivas ---
    print("\n[TESTE] Simulando duas voltas consecutivas de inspeção...")
    for volta in range(1, 3):
        print(f"\n--- VOLTA {volta} ---")
        for _ in range(4): # 4 pontos na rota
            rota.marcar_inspecionado()
            rota.avancar()
        rota.listar_volta()
        if volta < 2:
            rota.reiniciar_rodada()

    # --- Teste: Remoções (Fim, Início e Único) ---
    print("\n[TESTE] Testando remoções...")
    # Removendo do fim (P4)
    rota.remover_ponto("P4")
    # Removendo do início (P1)
    rota.remover_ponto("P1")
    rota.listar_volta()

    # Removendo o último ponto restante para zerar a rota (Único ponto restante)
    print("\n[TESTE] Removendo os pontos restantes até esvaziar...")
    rota.remover_ponto("P2")
    rota.remover_ponto("P3")
    rota.listar_volta()
    print(f"A rota está vazia? {rota.esta_vazia()}")