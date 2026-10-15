class Produto:
    def __init__(self, codigo, descricao, quantidade, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
        self.proximo = None


class EstoqueOrdenado:
    def __init__(self):
        self.inicio = None

    # 1. Inserir produto mantendo a ordem crescente do código
    # 2. Não permitir códigos duplicados
    def inserir_ordenado(self, codigo, descricao, quantidade, preco):
        # Verifica se o código já existe
        if self.buscar_por_codigo(codigo) is not None:
            print(f"\n[Erro] Código #{codigo} já cadastrado. Inserção não permitida.")
            return False

        novo = Produto(codigo, descricao, quantidade, preco)

        # Caso 1: Lista vazia ou inserção antes do primeiro elemento (código menor que todos)
        if self.inicio is None or codigo < self.inicio.codigo:
            novo.proximo = self.inicio
            self.inicio = novo
            print(f"Produto #{codigo} ({descricao}) inserido no início/posição correta!")
            return True

        # Caso 2: Inserção no meio ou no final
        anterior = None
        atual = self.inicio

        while atual is not None and atual.codigo < codigo:
            anterior = atual
            atual = atual.proximo

        # Regra do ponteiro: novo aponta para atual antes de anterior apontar para novo
        novo.proximo = atual
        anterior.proximo = novo

        print(f"Produto #{codigo} ({descricao}) inserido na posição correta!")
        return True

    # 3. Registrar entrada de unidades
    def registrar_entrada(self, codigo, quantidade):
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            print(f"\n[Erro] Produto #{codigo} não encontrado.")
            return False

        if quantidade <= 0:
            print("\n[Erro] A quantidade de entrada deve ser maior que zero.")
            return False

        produto.quantidade += quantidade
        print(f"\n[Entrada] +{quantidade} un. no produto #{codigo}. Estoque atual: {produto.quantidade}")
        return True

    # 4. Registrar saída sem permitir estoque negativo
    def registrar_saida(self, codigo, quantidade):
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            print(f"\n[Erro] Produto #{codigo} não encontrado.")
            return False

        if quantidade <= 0:
            print("\n[Erro] A quantidade de saída deve ser maior que zero.")
            return False

        if quantidade > produto.quantidade:
            print(f"\n[Erro] Estoque insuficiente! Disponível: {produto.quantidade}, Solicitado: {quantidade}")
            return False

        produto.quantidade -= quantidade
        print(f"\n[Saída] -{quantidade} un. do produto #{codigo}. Estoque atual: {produto.quantidade}")
        return True

    # 5. Buscar um produto pelo código
    def buscar_por_codigo(self, codigo):
        atual = self.inicio
        while atual is not None:
            if atual.codigo == codigo:
                return atual
            # Otimização: como a lista é ordenada, se passar do código, ele não existe
            if atual.codigo > codigo:
                break
            atual = atual.proximo
        return None

    # 6. Listar todos os produtos
    def listar_todos(self):
        if self.inicio is None:
            print("\n[Estoque Vazio] Nenhum produto cadastrado.")
            return

        print("\n--- RELATÓRIO DE ESTOQUE (ORDEM CRESCENTE) ---")
        atual = self.inicio
        while atual is not None:
            print(f"Código: {atual.codigo:03d} | Descrição: {atual.descricao:<18} | "
                  f"Qtd: {atual.quantidade:<4} | Preço: R$ {atual.preco:,.2f}")
            atual = atual.proximo
        print("---------------------------------------------")

    # 7. Listar produtos com menos de cinco unidades
    def listar_estoque_baixo(self):
        if self.inicio is None:
            print("\n[Estoque Vazio] Nenhum produto cadastrado.")
            return

        print("\n--- ALERTA: PRODUTOS COM MENOS DE 5 UNIDADES ---")
        encontrado = False
        atual = self.inicio
        while atual is not None:
            if atual.quantidade < 5:
                print(f"Código: {atual.codigo:03d} | Descrição: {atual.descricao:<18} | Qtd: {atual.quantidade}")
                encontrado = True
            atual = atual.proximo

        if not encontrado:
            print("Nenhum produto está com estoque crítico (< 5 un).")
        print("-----------------------------------------------")

    # 8. Remover somente produtos com estoque zero
    def remover_estoque_zero(self, codigo):
        if self.inicio is None:
            print("\n[Erro] Estoque vazio. Nenhuma remoção possível.")
            return False

        atual = self.inicio
        anterior = None

        while atual is not None and atual.codigo != codigo:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            print(f"\n[Erro] Produto #{codigo} não foi encontrado.")
            return False

        # Validação obrigatória: só remove se o estoque for ZERO
        if atual.quantidade > 0:
            print(f"\n[Erro] Remoção recusada. Produto #{codigo} ainda possui {atual.quantidade} unidades em estoque.")
            return False

        # Remoção do primeiro nó
        if anterior is None:
            self.inicio = atual.proximo
        # Remoção do meio ou fim
        else:
            anterior.proximo = atual.proximo

        print(f"\nProduto #{codigo} ({atual.descricao}) removido por estar com estoque ZERO.")
        del atual
        return True

    # 9. Encerrar o sistema
    def encerrar(self):
        atual = self.inicio
        while atual is not None:
            proximo_no = atual.proximo
            del atual
            atual = proximo_no
        self.inicio = None
        print("\nSistema encerrado. Todos os nós de estoque foram liberados da memória.")


# ==========================================
# BATERIA DE TESTES OBRIGATÓRIOS
# ==========================================
if __name__ == "__main__":
    estoque = EstoqueOrdenado()

    print("=== CADASTRO INICIAL (TESTES DE INSERÇÃO) ===")
    
    # Inserção base
    estoque.inserir_ordenado(30, "Teclado Mecânico", 10, 250.0)
    estoque.inserir_ordenado(50, "Monitor 24pol", 3, 900.0)

    print("\n1. TESTE: Inserir código menor que todos os existentes (Código 10)")
    estoque.inserir_ordenado(10, "Mouse Sem Fio", 2, 80.0)

    print("\n2. TESTE: Inserir entre dois códigos (Código 20, entre 10 e 30)")
    estoque.inserir_ordenado(20, "Headset Gamer", 15, 180.0)

    print("\n3. TESTE: Inserir código maior que todos (Código 70)")
    estoque.inserir_ordenado(70, "Gabinete ATX", 0, 320.0)

    print("\n4. TESTE: Tentar inserir código duplicado (Código 30)")
    estoque.inserir_ordenado(30, "Teclado Duplicado", 5, 200.0)

    estoque.listar_todos()

    print("\n=== TESTES DE REGRAS DE NEGÓCIO E MOVIMENTAÇÃO ===")
    
    # Listar estoque baixo (< 5)
    estoque.listar_estoque_baixo()

    # Movimentações de estoque
    estoque.registrar_saida(10, 2)  # Zera estoque do produto 10 (era 2)
    estoque.registrar_saida(20, 20) # Tenta retirar mais do que existe (erro)
    estoque.registrar_entrada(50, 5) # Adiciona +5 un no produto 50

    estoque.listar_todos()

    print("\n=== TESTES DE REMOÇÃO (SOMENTE ESTOQUE ZERO) ===")
    
    # Tentativa de remover produto com estoque > 0
    estoque.remover_estoque_zero(30)

    # Remoção com sucesso (Produto 10 foi zerado no teste anterior)
    estoque.remover_estoque_zero(10)

    # Remoção do produto 70 que já foi cadastrado com estoque 0
    estoque.remover_estoque_zero(70)

    estoque.listar_todos()

    print("\n=== ENCERRAMENTO ===")
    estoque.encerrar()