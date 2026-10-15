class Musica:
    def __init__(self, codigo, titulo, artista, duracao_segundos):
        self.codigo = codigo
        self.titulo = titulo
        self.artista = artista
        self.duracao_segundos = duracao_segundos
        self.proximo = None


class Playlist:
    def __init__(self):
        self.inicio = None

    # 1. Adicionar uma música ao final
    def adicionar_ao_final(self, codigo, titulo, artista, duracao_segundos):
        nova_musica = Musica(codigo, titulo, artista, duracao_segundos)
        if not self.inicio:
            self.inicio = nova_musica
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nova_musica
        print(f"[Adicionado] '{titulo}' de {artista}")

    # 2. Inserir uma música depois de outra música informada (por código)
    def inserir_depois(self, codigo_alvo, codigo, titulo, artista, duracao_segundos):
        atual = self.inicio
        while atual and atual.codigo != codigo_alvo:
            atual = atual.proximo

        if not atual:
            print(f"[Erro] Código alvo '{codigo_alvo}' não encontrado. Falha ao inserir '{titulo}'.")
            return False

        nova_musica = Musica(codigo, titulo, artista, duracao_segundos)
        nova_musica.proximo = atual.proximo
        atual.proximo = nova_musica
        print(f"[Inserido após '{atual.titulo}'] '{titulo}'")
        return True

    # 3. Listar toda a playlist
    def listar_playlist(self):
        if not self.inicio:
            print("\nA playlist está vazia.")
            return
        
        print("\n" + "="*40)
        print("         MINHA PLAYLIST DE MÚSICAS")
        print("="*40)
        atual = self.inicio
        idx = 1
        while atual:
            mins = atual.duracao_segundos // 60
            segs = atual.duracao_segundos % 60
            print(f"{idx}. [Cód: {atual.codigo}] {atual.titulo} - {atual.artista} ({mins:02d}:{segs:02d})")
            atual = atual.proximo
        print("="*40 + "\n")

    # 4. Buscar músicas por artista
    def buscar_por_artista(self, artista_busca):
        atual = self.inicio
        encontradas = []
        while atual:
            if artista_busca.lower() in atual.artista.lower():
                encontradas.append(atual)
            atual = atual.proximo

        if not encontradas:
            print(f"Nenhuma música encontrada para o artista '{artista_busca}'.")
        else:
            print(f"\n--- Músicas encontradas para '{artista_busca}' ---")
            for m in encontradas:
                print(f"[Cód: {m.codigo}] {m.titulo} ({m.duracao_segundos}s)")
            print("-" * 45)

    # 5. Remover uma música pelo código
    def remover_por_codigo(self, codigo):
        atual = self.inicio
        anterior = None

        while atual and atual.codigo != codigo:
            anterior = atual
            atual = atual.proximo

        if not atual:
            print(f"[Erro] Música com código {codigo} não encontrada para remoção.")
            return False

        if not anterior:  # É o primeiro elemento
            self.inicio = atual.proximo
        else:
            anterior.proximo = atual.proximo

        print(f"[Removido] Música '{atual.titulo}' (Código: {codigo})")
        return True

    # 6. Calcular a duração total
    def calcular_duracao_total(self):
        total_segundos = 0
        atual = self.inicio
        while atual:
            total_segundos += atual.duracao_segundos
            atual = atual.proximo

        mins = total_segundos // 60
        segs = total_segundos % 60
        print(f"\n>> Duração total da playlist: {mins} minutos e {segs} segundos ({total_segundos}s total).\n")
        return total_segundos

    # 7. Mover uma música existente para o início
    def mover_para_inicio(self, codigo):
        if not self.inicio or self.inicio.codigo == codigo:
            print("A música já está no início ou a playlist está vazia.")
            return

        atual = self.inicio
        anterior = None

        while atual and atual.codigo != codigo:
            anterior = atual
            atual = atual.proximo

        if not atual:
            print(f"[Erro] Música com código {codigo} não encontrada.")
            return False

        # Desconecta o elemento
        anterior.proximo = atual.proximo
        # Move para o início
        atual.proximo = self.inicio
        self.inicio = atual
        print(f"[Movido para o início] '{atual.titulo}'")
        return True

def executar_testes():
    print("--- INICIANDO TESTES OBRIGATÓRIOS ---")
    minha_playlist = Playlist()

    # Cenário de base: Adicionar músicas iniciais
    minha_playlist.adicionar_ao_final(1, "Song A", "Artist 1", 200)
    minha_playlist.adicionar_ao_final(2, "Song B", "Artist 2", 180)
    minha_playlist.adicionar_ao_final(3, "Song C", "Artist 3", 240)
    
    print("\n[Estado Inicial]")
    minha_playlist.listar_playlist()

    # Teste 1: Inserir depois do primeiro elemento (Código 1)
    print("\n--- TESTE 1: Inserir depois do primeiro elemento (Cód 1) ---")
    minha_playlist.inserir_depois(1, 10, "Song X (Após 1)", "Artist X", 150)
    minha_playlist.listar_playlist()

    # Teste 2: Inserir depois de um elemento do meio (Código 2)
    print("\n--- TESTE 2: Inserir depois de um elemento do meio (Cód 2) ---")
    minha_playlist.inserir_depois(2, 20, "Song Y (Após 2)", "Artist Y", 210)
    minha_playlist.listar_playlist()

    # Teste 3: Inserir depois do último elemento (Código atual da última música, ex: 3)
    print("\n--- TESTE 3: Inserir depois do último elemento (Cód 3) ---")
    minha_playlist.inserir_depois(3, 30, "Song Z (Após Último)", "Artist Z", 190)
    minha_playlist.listar_playlist()

    # Teste 4: Tentar inserir após um código inexistente
    print("\n--- TESTE 4: Tentar inserir após código inexistente (Cód 999) ---")
    minha_playlist.inserir_depois(999, 40, "Song Erro", "Artist Fail", 100)

    # Teste de outras funcionalidades
    print("\n--- TESTES ADICIONAIS (Duração, Mover, Buscar, Remover) ---")
    minha_playlist.calcular_duracao_total()
    minha_playlist.buscar_por_artista("Artist X")
    minha_playlist.mover_para_inicio(30) # Move a música 30 para o topo
    minha_playlist.listar_playlist()
    minha_playlist.remover_por_codigo(10)
    minha_playlist.listar_playlist()


if __name__ == "__main__":
    executar_testes()

def menu():
    playlist = Playlist()
    
    while True:
        print("\n--- MENU PLAYLIST MULTIMÍDIA ---")
        print("1. Adicionar música ao final")
        print("2. Inserir música depois de outra")
        print("3. Listar playlist")
        print("4. Buscar músicas por artista")
        print("5. Remover música pelo código")
        print("6. Calcular duração total")
        print("7. Mover música para o início")
        print("8. Encerrar o sistema")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            codigo = int(input("Código: "))
            titulo = input("Título: ")
            artista = input("Artista: ")
            duracao = int(input("Duração em segundos: "))
            playlist.adicionar_ao_final(codigo, titulo, artista, duracao)
            
        elif opcao == '2':
            codigo_alvo = int(input("Código da música referência (depois de qual inserir): "))
            codigo = int(input("Código da nova música: "))
            titulo = input("Título: ")
            artista = input("Artista: ")
            duracao = int(input("Duração em segundos: "))
            playlist.inserir_depois(codigo_alvo, codigo, titulo, artista, duracao)
            
        elif opcao == '3':
            playlist.listar_playlist()
            
        elif opcao == '4':
            artista = input("Digite o nome do artista: ")
            playlist.buscar_por_artista(artista)
            
        elif opcao == '5':
            codigo = int(input("Código da música a remover: "))
            playlist.remover_por_codigo(codigo)
            
        elif opcao == '6':
            playlist.calcular_duracao_total()
            
        elif opcao == '7':
            codigo = int(input("Código da música para mover ao início: "))
            playlist.mover_para_inicio(codigo)
            
        elif opcao == '8':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Descomente a linha abaixo para rodar o menu interativo:
menu()