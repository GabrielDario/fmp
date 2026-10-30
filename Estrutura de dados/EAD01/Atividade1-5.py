class Processo:
    def __init__(self, pid, nome, tempo_restante):
        self.pid = pid
        self.nome = nome
        self.tempo_restante = tempo_restante
        self.proximo = None


class EscalonadorRoundRobin:
    def __init__(self, quantum):
        self.inicio = None
        self. quantum = quantum

    def esta_vazia(self):
        return self.inicio is None

    def adicionar_processo(self, pid, nome, tempo_restante):
        """Adiciona um processo ao final lógico da lista circular."""
        novo = Processo(pid, nome, tempo_restante)

        if self.esta_vazia():
            self.inicio = novo
            novo.proximo = novo  # Único nó aponta para ele mesmo
        else:
            # Encontra o último nó (cujo proximo é o inicio)
            atual = self.inicio
            while atual.proximo != self.inicio:
                atual = atual.proximo

            atual.proximo = novo
            novo.proximo = self.inicio  # Garante a circularidade

    def executar_ciclo(self):
        """
        Executa o escalonador processando cada nó com a fatia de tempo (quantum).
        Remove processos concluídos e ajusta os ponteiros mantendo a circularidade.
        """
        if self.esta_vazia():
            print("Nenhum processo a ser executado.")
            return

        atual = self.inicio
        anterior = None

        # Para encontrar o 'anterior' inicial (último nó da lista)
        temp = self.inicio
        while temp.proximo != self.inicio:
            temp = temp.proximo
        anterior = temp

        print(f"\n--- Iniciando Escalonamento Round Robin (Quantum = {self.quantum}) ---")

        while self.inicio is not None:
            # Executa a fatia de tempo
            tempo_executado = min(atual.tempo_restante, self.quantum)
            atual.tempo_restante -= tempo_executado

            print(f"Executando {atual.nome} (PID: {atual.pid}) por {tempo_executado}s | "
                  f"Tempo Restante: {atual.tempo_restante}s")

            # Caso 1: O processo terminou
            if atual.tempo_restante == 0:
                print(f"--> Processo {atual.nome} (PID: {atual.pid}) CONCLUÍDO e removido.")

                # Se era o único elemento restante na lista
                if atual.proximo == atual:
                    self.inicio = None
                    print("\nTodos os processos foram concluídos.")
                    break
                else:
                    # Remove o nó atual atualizando o ponteiro do anterior
                    anterior.proximo = atual.proximo

                    # Se estamos removendo o nó que é o início, atualizamos o início
                    if atual == self.inicio:
                        self.inicio = atual.proximo

                    atual = atual.proximo

            # Caso 2: O processo não terminou (continua no ciclo)
            else:
                anterior = atual
                atual = atual.proximo


# --- Exemplo de Uso / Testes ---
if __name__ == "__main__":
    # Instancia escalonador com fatia de tempo (quantum) = 3
    escalonador = EscalonadorRoundRobin(quantum=3)

    # Adiciona processos
    escalonador.adicionar_processo(1, "Navegador", 7)
    escalonador.adicionar_processo(2, "EditorTextos", 4)
    escalonador.adicionar_processo(3, "Terminal", 2)

    # Executa a simulação
    escalonador.executar_ciclo()