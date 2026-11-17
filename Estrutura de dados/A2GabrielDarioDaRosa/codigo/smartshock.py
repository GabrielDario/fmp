import time
import copy
from models import Produto
from dados import (carregar_dados_iniciais,carregar_dados_aleatorios,carregar_dados_crescentes,carregar_dados_decrescentes)

class Produto:
    def __init__(self, codigo, nome, categoria, preco, estoque, quantidade_vendida):
        self.codigo = int(codigo)
        self.nome = str(nome)
        self.categoria = str(categoria)
        self.preco = float(preco)
        self.estoque = int(estoque)
        self.quantidade_vendida = int(quantidade_vendida)

    def __str__(self):
        return (f"Cód: {self.codigo:04d} | {self.nome:<22} | Cat: {self.categoria:<12} | "
                f"R$ {self.preco:7.2f} | Est: {self.estoque:3d} | Vendidos: {self.quantidade_vendida:4d}")


class Metricas:
    """Armazena os contadores de operações e tempo de execução de cada algoritmo."""
    def __init__(self, nome_algoritmo=""):
        self.nome = nome_algoritmo
        self.comparacoes = 0
        self.trocas = 0
        self.deslocamentos = 0
        self.divisoes = 0
        self.particoes = 0
        self.tempo_ms = 0.0

    def __str__(self):
        return (f"[{self.nome:<15}] Tempo: {self.tempo_ms:6.3f} ms | "
                f"Comp: {self.comparacoes:4d} | Trocas: {self.trocas:4d} | "
                f"Desloc: {self.deslocamentos:4d} | Div: {self.divisoes:3d} | Part: {self.particoes:3d}")


# ==============================================================================
# ALGORITMOS DE BUSCA
# ==============================================================================

def busca_sequencial(lista, codigo_alvo):
    m = Metricas("Busca Sequencial")
    inicio = time.perf_counter()

    for i, prod in enumerate(lista):
        m.comparacoes += 1
        if prod.codigo == codigo_alvo:
            m.tempo_ms = (time.perf_counter() - inicio) * 1000
            return prod, i, m

    m.tempo_ms = (time.perf_counter() - inicio) * 1000
    return None, -1, m


def busca_binaria(lista, codigo_alvo):
    """Exige que a lista esteja previamente ordenada por 'codigo'."""
    m = Metricas("Busca Binária")
    inicio = time.perf_counter()

    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        m.divisoes += 1
        meio = (esquerda + direita) // 2
        m.comparacoes += 1

        if lista[meio].codigo == codigo_alvo:
            m.tempo_ms = (time.perf_counter() - inicio) * 1000
            return lista[meio], meio, m
        elif lista[meio].codigo < codigo_alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    m.tempo_ms = (time.perf_counter() - inicio) * 1000
    return None, -1, m


# ==============================================================================
# ALGORITMOS DE ORDENAÇÃO
# ==============================================================================

def bubble_sort(lista, chave, reverso=False):
    arr = copy.copy(lista)
    m = Metricas("Bubble Sort")
    inicio = time.perf_counter()
    n = len(arr)

    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            m.comparacoes += 1
            val_a = getattr(arr[j], chave)
            val_b = getattr(arr[j + 1], chave)
            condicao = (val_a < val_b) if reverso else (val_a > val_b)

            if condicao:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                m.trocas += 1
                trocou = True
        if not trocou:  # Otimização de melhor caso O(n)
            break

    m.tempo_ms = (time.perf_counter() - inicio) * 1000
    return arr, m


def selection_sort(lista, chave, reverso=False):
    arr = copy.copy(lista)
    m = Metricas("Selection Sort")
    inicio = time.perf_counter()
    n = len(arr)

    for i in range(n):
        idx_extremo = i
        for j in range(i + 1, n):
            m.comparacoes += 1
            val_j = getattr(arr[j], chave)
            val_ext = getattr(arr[idx_extremo], chave)
            condicao = (val_j > val_ext) if reverso else (val_j < val_ext)

            if condicao:
                idx_extremo = j

        if idx_extremo != i:
            arr[i], arr[idx_extremo] = arr[idx_extremo], arr[i]
            m.trocas += 1

    m.tempo_ms = (time.perf_counter() - inicio) * 1000
    return arr, m


def insertion_sort(lista, chave, reverso=False):
    arr = copy.copy(lista)
    m = Metricas("Insertion Sort")
    inicio = time.perf_counter()

    for i in range(1, len(arr)):
        atual = arr[i]
        val_atual = getattr(atual, chave)
        j = i - 1

        while j >= 0:
            m.comparacoes += 1
            val_j = getattr(arr[j], chave)
            condicao = (val_j < val_atual) if reverso else (val_j > val_atual)
            if condicao:
                arr[j + 1] = arr[j]
                m.deslocamentos += 1
                j -= 1
            else:
                break
        arr[j + 1] = atual

    m.tempo_ms = (time.perf_counter() - inicio) * 1000
    return arr, m


def merge_sort(lista, chave, reverso=False):
    m = Metricas("Merge Sort")
    inicio = time.perf_counter()

    def _merge_sort(sublista):
        if len(sublista) <= 1:
            return sublista

        m.divisoes += 1
        meio = len(sublista) // 2
        esquerda = _merge_sort(sublista[:meio])
        direita = _merge_sort(sublista[meio:])
        return _merge(esquerda, direita)

    def _merge(esq, dir_):
        resultado = []
        i = j = 0
        while i < len(esq) and j < len(dir_):
            m.comparacoes += 1
            val_e = getattr(esq[i], chave)
            val_d = getattr(dir_[j], chave)
            condicao = (val_e >= val_d) if reverso else (val_e <= val_d)

            if condicao:
                resultado.append(esq[i])
                i += 1
            else:
                resultado.append(dir_[j])
                j += 1
            m.deslocamentos += 1

        while i < len(esq):
            resultado.append(esq[i])
            i += 1
            m.deslocamentos += 1

        while j < len(dir_):
            resultado.append(dir_[j])
            j += 1
            m.deslocamentos += 1

        return resultado

    arr = _merge_sort(copy.copy(lista))
    m.tempo_ms = (time.perf_counter() - inicio) * 1000
    return arr, m


def quick_sort(lista, chave, reverso=False):
    arr = copy.copy(lista)
    m = Metricas("Quick Sort")
    inicio = time.perf_counter()

    def _particionar(baixo, alto):
        m.particoes += 1
        pivo = getattr(arr[alto], chave)
        i = baixo - 1

        for j in range(baixo, alto):
            m.comparacoes += 1
            val_j = getattr(arr[j], chave)
            condicao = (val_j >= pivo) if reverso else (val_j <= pivo)

            if condicao:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    m.trocas += 1

        if (i + 1) != alto:
            arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
            m.trocas += 1
        return i + 1

    def _quick_sort(baixo, alto):
        if baixo < alto:
            pi = _particionar(baixo, alto)
            _quick_sort(baixo, pi - 1)
            _quick_sort(pi + 1, alto)

    _quick_sort(0, len(arr) - 1)
    m.tempo_ms = (time.perf_counter() - inicio) * 1000
    return arr, m


# ==============================================================================
# SISTEMA SMARTSTOCK (MENU E CONTROLE)
# ==============================================================================


def esta_ordenado_por_codigo(lista):
    return all(lista[i].codigo <= lista[i + 1].codigo for i in range(len(lista) - 1))


def main():
    produtos = carregar_dados_iniciais()
    historico_metricas = []

    while True:
        print("\n========== SMARTSTOCK ==========")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Busca sequencial por código")
        print("4 - Busca binária por código")
        print("5 - Ordenar por nome")
        print("6 - Ordenar por preço")
        print("7 - Ordenar por estoque")
        print("8 - Ordenar pela quantidade vendida")
        print("9 - Ordenar por código")
        print("10 - Comparar algoritmos")
        print("11 - Exibir relatório de desempenho")
        print("0 - Encerrar")
        print("================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                cod = int(input("Código único: "))
                if any(p.codigo == cod for p in produtos):
                    print("Erro: Já existe um produto com este código.")
                    continue
                nome = input("Nome comercial: ")
                cat = input("Categoria: ")
                preco = float(input("Preço unitário: "))
                est = int(input("Quantidade em estoque: "))
                vend = int(input("Quantidade vendida: "))
                produtos.append(Produto(cod, nome, cat, preco, est, vend))
                print("Produto cadastrado com sucesso!")
            except ValueError:
                print("Entrada inválida. Verifique os tipos numéricos.")

        elif opcao == "2":
            print("\n--- CATÁLOGO DE PRODUTOS ---")
            for p in produtos:
                print(p)

        elif opcao == "3":
            cod = int(input("Digite o código para busca sequencial: "))
            prod, idx, m = busca_sequencial(produtos, cod)
            historico_metricas.append(m)
            if prod:
                print(f"Encontrado no índice {idx}: {prod}")
            else:
                print("Produto não encontrado.")
            print(f"Métricas -> {m}")

        elif opcao == "4":
            if not esta_ordenado_por_codigo(produtos):
                print("Aviso: A lista não estava ordenada por código. Ordenando com QuickSort antes da busca...")
                produtos, m_ord = quick_sort(produtos, "codigo")
                historico_metricas.append(m_ord)

            cod = int(input("Digite o código para busca binária: "))
            prod, idx, m = busca_binaria(produtos, cod)
            historico_metricas.append(m)
            if prod:
                print(f"Encontrado no índice {idx}: {prod}")
            else:
                print("Produto não encontrado.")
            print(f"Métricas -> {m}")

        elif opcao in ("5", "6", "7", "8", "9"):
            mapa_chaves = {
                "5": ("nome", "Nome (A-Z)", False, insertion_sort),
                "6": ("preco", "Preço (Menor -> Maior)", False, merge_sort),
                "7": ("estoque", "Estoque (Menor -> Maior)", False, selection_sort),
                "8": ("quantidade_vendida", "Mais Vendidos (Maior -> Menor)", True, quick_sort),
                "9": ("codigo", "Código (Crescente)", False, quick_sort),
            }
            chave, desc, rev, algoritmo = mapa_chaves[opcao]
            produtos, m = algoritmo(produtos, chave, reverso=rev)
            historico_metricas.append(m)
            print(f"\nLista ordenada por {desc} usando {m.nome}:")
            for p in produtos:
                print(p)
            print(f"Métricas -> {m}")

        elif opcao == "10":
            criterio = "codigo"
            cenarios = [
                ("1. ENTRADA ALEATÓRIA (Caso Médio)", carregar_dados_aleatorios()),
                ("2. ENTRADA CRESCENTE (Melhor Caso p/ Bubble/Insertion)", carregar_dados_crescentes()),
                ("3. ENTRADA DECRESCENTE (Pior Caso)", carregar_dados_decrescentes()),
            ]

            algoritmos = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort]

            for titulo_cenario, lista_teste in cenarios:
                print(f"\n--- {titulo_cenario} (Critério: {criterio}) ---")
                for alg in algoritmos:
                    _, m = alg(lista_teste, criterio)
                    m.nome = f"{m.nome} [{titulo_cenario[:12]}]"
                    historico_metricas.append(m)
                    print(m)

        elif opcao == "11":
            print("\n========== RELATÓRIO DE DESEMPENHO ==========")
            if not historico_metricas:
                print("Nenhuma operação registrada ainda.")
            else:
                for i, m in enumerate(historico_metricas, 1):
                    print(f"{i:02d}. {m}")

        elif opcao == "0":
            print("Encerrando SmartStock...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()