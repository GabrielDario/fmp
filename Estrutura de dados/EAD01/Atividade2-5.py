class Impressao:
    def __init__(self, identificador, usuario, arquivo, paginas):
        self.id = identificador
        self.usuario = usuario
        self.arquivo = arquivo
        self.paginas = paginas
        self.proximo = None


class ServidorImpressao:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    # 1. Adicionar trabalho ao final
    def enqueue(self, identificador, usuario, arquivo, paginas):
        novo = Impressao(identificador, usuario, arquivo, paginas)
        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        print(f"Trabalho '{identificador}' ({arquivo}) enfileirado.")

    # 2. Mostrar o próximo documento
    def peek(self):
        if self.esta_vazia():
            return None
        return self.inicio

    # 3. Processar e remover o primeiro
    def dequeue(self):
        if self.esta_vazia():
            return None
        removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        removido.proximo = None
        return removido

    # 4. Cancelar um trabalho por identificador preservando a ordem
    def cancelar(self, identificador):
        if self.esta_vazia():
            print("Fila de impressão vazia.")
            return False

        atual = self.inicio
        anterior = None

        while atual and atual.id != identificador:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            print(f"Trabalho ID '{identificador}' não encontrado.")
            return False

        # Se for o único / primeiro elemento
        if atual == self.inicio:
            self.inicio = self.inicio.proximo
            if self.inicio is None:
                self.fim = None
        # Se for o último elemento
        elif atual == self.fim:
            self.fim = anterior
            self.fim.proximo = None
        else:
            # Elemento no meio
            anterior.proximo = atual.proximo

        print(f"Trabalho ID '{identificador}' cancelado com sucesso.")
        return True

    # 5. Calcular o total de páginas pendentes
    def calcular_paginas(self):
        total = 0
        atual = self.inicio
        while atual:
            total += atual.paginas
            atual = atual.proximo
        return total

    # 6. Listar todos os trabalhos
    def listar(self):
        if self.esta_vazia():
            print("Fila de impressão vazia.")
            return
        print("\n--- Fila de Impressão ---")
        atual = self.inicio
        while atual:
            print(f"ID: {atual.id} | Usuário: {atual.usuario} | Arquivo: {atual.arquivo} | Páginas: {atual.paginas}")
            atual = atual.proximo
        print("-" * 45)


# Testes Obrigatórios - Exercício 5
if __name__ == "__main__":
    print("\n=== TESTES: SERVIDOR DE IMPRESSÃO ===")
    servidor = ServidorImpressao()

    # Inserindo dados iniciais
    servidor.enqueue("J1", "Daniel", "relatorio.pdf", 10)
    servidor.enqueue("J2", "Beatriz", "foto.png", 2)
    servidor.enqueue("J3", "Carlos", "tese.docx", 45)
    servidor.enqueue("J4", "Ana", "tabela.xlsx", 5)
    servidor.listar()
    print(f"Total de páginas pendentes: {servidor.calcular_paginas()}")

    # Cancelar o primeiro trabalho (J1)
    print("\n[Teste] Cancelar o primeiro trabalho (J1):")
    servidor.cancelar("J1")
    servidor.listar()

    # Cancelar o último trabalho (J4)
    print("\n[Teste] Cancelar o último trabalho (J4):")
    servidor.cancelar("J4")
    servidor.listar()

    # Código inexistente
    print("\n[Teste] Código inexistente:")
    servidor.cancelar("J99")

    # Cancelar o único trabalho restante de uma fila de 1 elemento
    print("\n[Teste] Esvaziando e testando cancelamento de único trabalho:")
    servidor.cancelar("J2") # Sobra apenas J3
    servidor.listar()
    servidor.cancelar("J3") # Cancela o último único trabalho
    servidor.listar()

    # Inserir novamente após esvaziar a fila
    print("\n[Teste] Inserir novamente após esvaziamento total:")
    servidor.enqueue("J5", "Helena", "contrato.pdf", 3)
    servidor.listar()