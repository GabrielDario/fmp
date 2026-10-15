class Imovel:
    def __init__(self, codigo, bairro, tipo, dormitorios, valor):
        self.codigo = codigo
        self.bairro = bairro
        self.tipo = tipo
        self.dormitorios = dormitorios
        self.valor = valor
        self.proximo = None


class CatalogoImobiliaria:
    def __init__(self):
        self.inicio = None
        self.fim = None

    # 1. Inserir imóvel no final (O(1))
    def inserir_final(self, codigo, bairro, tipo, dormitorios, valor):
        novo = Imovel(codigo, bairro, tipo, dormitorios, valor)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        print(f"Imóvel código #{codigo} inserido com sucesso!")

    # 2. Listar todos os imóveis
    def listar_todos(self):
        if self.inicio is None:
            print("\n[Catálogo Vazio] Nenhum imóvel cadastrado.")
            return

        print("\n--- CATÁLOGO DE IMÓVEIS ---")
        atual = self.inicio
        while atual is not None:
            print(f"Código: {atual.codigo} | Bairro: {atual.bairro} | "
                  f"Tipo: {atual.tipo} | Dormitórios: {atual.dormitorios} | "
                  f"Valor: R$ {atual.valor:,.2f}")
            atual = atual.proximo
        print("---------------------------")

    # 3. Buscar um imóvel pelo código
    def buscar_por_codigo(self, codigo):
        if self.inicio is None:
            print("\n[Catálogo Vazio] Não há imóveis para pesquisar.")
            return None

        atual = self.inicio
        while atual is not None:
            if atual.codigo == codigo:
                return atual
            atual = atual.proximo
        return None

    # 4. Listar imóveis de um bairro informado
    def listar_por_bairro(self, bairro):
        if self.inicio is None:
            print("\n[Catálogo Vazio] Não há imóveis para filtrar por bairro.")
            return

        print(f"\n--- Imóveis no bairro: {bairro} ---")
        encontrado = False
        atual = self.inicio
        while atual is not None:
            if atual.bairro.lower() == bairro.lower():
                print(f"Código: {atual.codigo} | Tipo: {atual.tipo} | "
                      f"Quartos: {atual.dormitorios} | Valor: R$ {atual.valor:,.2f}")
                encontrado = True
            atual = atual.proximo

        if not encontrado:
            print(f"Nenhum imóvel encontrado no bairro '{bairro}'.")
        print("-----------------------------------")

    # 5. Alterar o valor de um imóvel
    def alterar_valor(self, codigo, novo_valor):
        imovel = self.buscar_por_codigo(codigo)
        if imovel:
            valor_antigo = imovel.valor
            imovel.valor = novo_valor
            print(f"\nValor do imóvel #{codigo} alterado: R$ {valor_antigo:,.2f} -> R$ {novo_valor:,.2f}")
        else:
            print(f"\n[Erro] Imóvel código #{codigo} não encontrado para alteração de valor.")

    # 6. Remover imóvel pelo código (Início, Meio e Fim)
    def remover_por_codigo(self, codigo):
        if self.inicio is None:
            print("\n[Erro] Catálogo vazio. Não é possível remover.")
            return False

        atual = self.inicio
        anterior = None

        # Percorre a lista buscando o código
        while atual is not None and atual.codigo != codigo:
            anterior = atual
            atual = atual.proximo

        # Caso 1: Código não encontrado
        if atual is None:
            print(f"\n[Erro] Código #{codigo} não encontrado no catálogo.")
            return False

        # Caso 2: Remoção do PRIMEIRO nó
        if anterior is None:
            self.inicio = atual.proximo
            if self.inicio is None:  # Era o único elemento
                self.fim = None

        # Caso 3: Remoção do MEIO ou do FIM
        else:
            anterior.proximo = atual.proximo
            if atual == self.fim:  # Era o ÚLTIMO elemento
                self.fim = anterior

        print(f"\nImóvel código #{codigo} removido com sucesso!")
        del atual
        return True

    # 7. Exibir o imóvel de maior valor
    def maior_valor(self):
        if self.inicio is None:
            print("\n[Catálogo Vazio] Impossível determinar imóvel de maior valor.")
            return None

        maior = self.inicio
        atual = self.inicio.proximo

        while atual is not None:
            if atual.valor > maior.valor:
                maior = atual
            atual = atual.proximo

        print("\n--- IMÓVEL DE MAIOR VALOR ---")
        print(f"Código: {maior.codigo} | Bairro: {maior.bairro} | "
              f"Tipo: {maior.tipo} | Valor: R$ {maior.valor:,.2f}")
        print("------------------------------")
        return maior

    # 8. Remover o primeiro elemento da lista
    def remover_primeiro(self):
        if self.inicio is None:
            print("Lista vazia!")
            return None

        removido = self.inicio
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        print("Primeiro elemento removido com sucesso!")
        return removido

        # 9. Remover o último elemento da lista
    def remover_ultimo(self):
        if self.inicio is None:
                        print("Lista vazia!")
                        return None

                # Caso especial: Apenas 1 elemento na lista
        if self.inicio == self.fim:
            removido = self.inicio
            self.inicio = None
            self.fim = None
            print("Único elemento removido!")
            return removido

        # Caso geral: Percorre até encontrar o penúltimo elemento
        atual = self.inicio
        while atual.proximo != self.fim:
            atual = atual.proximo

        removido = self.fim
        atual.proximo = None  # Desconecta o último nó
        self.fim = atual      # Atualiza o ponteiro fim para o penúltimo

        print("Último elemento removido com sucesso!")
        return removido

    def remover_no_do_meio(self):
        if self.inicio is None:
            print("Lista vazia!")
            return None

        # Para listas pares, remove o elemento central mais à direita.
        lento = self.inicio
        rapido = self.inicio
        anterior = None

        while rapido is not None and rapido.proximo is not None:
            rapido = rapido.proximo.proximo
            anterior = lento
            lento = lento.proximo

        if anterior is None:
            # A lista contém apenas um elemento.
            self.inicio = None
            self.fim = None
        else:
            anterior.proximo = lento.proximo
            if lento is self.fim:
                self.fim = anterior

        lento.proximo = None
        print("Elemento do meio da lista removido!")
        return lento
    # 11. Encerrar o sistema
    def encerrar(self):
        atual = self.inicio
        while atual is not None:
            proximo_no = atual.proximo
            del atual
            atual = proximo_no
        self.inicio = None
        self.fim = None
        print("\nSistema encerrado. Memória do catálogo totalmente liberada.")

# TESTES OBRIGATÓRIOS E BATERIA DE EXECUÇÃO

if __name__ == "__main__":
    cat = CatalogoImobiliaria()

    print("=== TESTE: Operações com lista vazia ===")
    cat.listar_todos()
    cat.remover_por_codigo(999)
    cat.alterar_valor(999, 500000)
    cat.maior_valor()

    print("\n=== CADASTRAMENTO DE IMÓVEIS ===")
    cat.inserir_final(10, "Centro", "Apartamento", 2, 350000.0)
    cat.inserir_final(20, "Jardins", "Casa", 4, 1200000.0)
    cat.inserir_final(30, "Centro", "Studio", 1, 220000.0)
    cat.inserir_final(40, "Moema", "Cobertura", 3, 2100000.0)
    cat.inserir_final(50, "Pinheiros", "Apartamento", 2, 400000.0)

    cat.listar_todos()

    print("\n=== TESTE: Pesquisar código inexistente ===")
    busca = cat.buscar_por_codigo(999)
    if not busca:
        print("Resultado: Código 999 realmente não existe.")

    print("\n=== CONSULTAS E ALTERAÇÕES ===")
    cat.listar_por_bairro("Centro")
    cat.alterar_valor(30, 250000.0)
    cat.maior_valor()

    print("\n=== TESTE: Remover imóvel do MEIO ")
    cat.remover_no_do_meio()
    cat.listar_todos()

    print("\n=== TESTE: Remover o PRIMEIRO imóvel ")
    cat.remover_primeiro()
    cat.listar_todos()

    print("\n=== TESTE: Remover o ultimate imóvel")
    cat.remover_ultimo()
    cat.listar_todos()

    print("\n=== ENCERRAMENTO DO SISTEMA ===")
    cat.encerrar()
    