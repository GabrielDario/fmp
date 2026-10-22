class Musica:
    """Nó da lista duplamente encadeada representando uma música."""
    def __init__(self, codigo, titulo, artista, duracao):
        self.codigo = codigo
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao  # Duração em segundos ou float de minutos
        self.anterior = None
        self.proximo = None

    def __str__(self):
        mins = int(self.duracao)
        segs = int(round((self.duracao - mins) * 60)) if isinstance(self.duracao, float) else 0
        dur_str = f"{mins}m{segs:02d}s" if isinstance(self.duracao, float) else f"{self.duracao}s"
        return f"[Cód: {self.codigo}] {self.titulo} - {self.artista} ({dur_str})"


class Playlist:
    """Estrutura da Lista Duplamente Encadeada para gerenciar a Playlist."""
    def __init__(self):
        self.inicio = None
        self.fim = None

    def _buscar_no(self, codigo):
        """Método auxiliar privado para encontrar o objeto nó pelo código."""
        aux = self.inicio
        while aux is not None:
            if aux.codigo == codigo:
                return aux
            aux = aux.proximo
        return None

    def adicionar_fim(self, codigo, titulo, artista, duracao):
        """1. Adicionar música ao final."""
        if self._buscar_no(codigo):
            print(f"\n[!] Erro: Já existe uma música com o código {codigo}.")
            return False

        nova = Musica(codigo, titulo, artista, duracao)
        if self.inicio is None:
            self.inicio = nova
            self.fim = nova
        else:
            nova.anterior = self.fim
            self.fim.proximo = nova
            self.fim = nova
        print(f"\n-> Música '{titulo}' adicionada ao final da playlist.")
        return True

    def inserir_antes(self, codigo_ref, codigo, titulo, artista, duracao):
        """2. Inserir uma música antes de um código informado."""
        no_ref = self._buscar_no(codigo_ref)
        if not no_ref:
            print(f"\n[!] Código de referência {codigo_ref} não encontrado.")
            return False

        if self._buscar_no(codigo):
            print(f"\n[!] Erro: Já existe uma música com o código {codigo}.")
            return False

        nova = Musica(codigo, titulo, artista, duracao)

        # Se for o primeiro nó
        if no_ref == self.inicio:
            nova.proximo = self.inicio
            self.inicio.anterior = nova
            self.inicio = nova
        else:
            nova.anterior = no_ref.anterior
            nova.proximo = no_ref
            no_ref.anterior.proximo = nova
            no_ref.anterior = nova

        print(f"\n-> Música '{titulo}' inserida ANTES do código {codigo_ref}.")
        return True

    def inserir_depois(self, codigo_ref, codigo, titulo, artista, duracao):
        """3. Inserir uma música depois de um código informado."""
        no_ref = self._buscar_no(codigo_ref)
        if not no_ref:
            print(f"\n[!] Código de referência {codigo_ref} não encontrado.")
            return False

        if self._buscar_no(codigo):
            print(f"\n[!] Erro: Já existe uma música com o código {codigo}.")
            return False

        nova = Musica(codigo, titulo, artista, duracao)

        # Se for o último nó
        if no_ref == self.fim:
            nova.anterior = self.fim
            self.fim.proximo = nova
            self.fim = nova
        else:
            nova.proximo = no_ref.proximo
            nova.anterior = no_ref
            no_ref.proximo.anterior = nova
            no_ref.proximo = nova

        print(f"\n-> Música '{titulo}' inserida DEPOIS do código {codigo_ref}.")
        return True

    def listar_inicio_ao_fim(self):
        """4a. Listar do início ao fim."""
        print("\n--- Playlist (Início ao Fim) ---")
        if self.inicio is None:
            print("(Playlist vazia)")
            return

        aux = self.inicio
        i = 1
        while aux is not None:
            print(f"{i}. {aux}")
            aux = aux.proximo
            i += 1

    def listar_fim_ao_inicio(self):
        """4b. Listar do fim ao início."""
        print("\n--- Playlist (Fim ao Início) ---")
        if self.fim is None:
            print("(Playlist vazia)")
            return

        aux = self.fim
        i = 1
        while aux is not None:
            print(f"{i}. {aux}")
            aux = aux.anterior
            i += 1

    def buscar(self, codigo):
        """5. Buscar uma música pelo código."""
        no = self._buscar_no(codigo)
        if no:
            print(f"\n[✓] Música encontrada: {no}")
            return no
        else:
            print(f"\n[!] Música com código {codigo} NÃO foi encontrada.")
            return None

    def remover(self, codigo):
        """6. Remover uma música pelo código."""
        no = self._buscar_no(codigo)
        if not no:
            print(f"\n[!] Não foi possível remover: Código {codigo} inexistente.")
            return False

        # Ajusta ponteiro anterior
        if no.anterior is not None:
            no.anterior.proximo = no.proximo
        else:
            self.inicio = no.proximo  # Era o primeiro elemento

        # Ajusta ponteiro próximo
        if no.proximo is not None:
            no.proximo.anterior = no.anterior
        else:
            self.fim = no.anterior  # Era o último elemento

        # Limpa referências do nó removido
        no.anterior = None
        no.proximo = None

        print(f"\n-> Música '{no.titulo}' (Código {codigo}) removida com sucesso.")
        return True

    def mover_para_inicio(self, codigo):
        """7. Mover uma música existente para o início."""
        no = self._buscar_no(codigo)
        if not no:
            print(f"\n[!] Código {codigo} não encontrado para mover.")
            return False

        # Se já estiver no início, não faz nada
        if no == self.inicio:
            print(f"\n-> A música '{no.titulo}' já é a primeira da playlist.")
            return True

        # Desconecta o nó da posição atual
        if no.anterior is not None:
            no.anterior.proximo = no.proximo

        if no.proximo is not None:
            no.proximo.anterior = no.anterior
        else:
            self.fim = no.anterior  # Se era o último, atualiza o fim

        # Insere no início
        no.anterior = None
        no.proximo = self.inicio
        self.inicio.anterior = no
        self.inicio = no

        print(f"\n-> Música '{no.titulo}' movida para o INÍCIO da playlist.")
        return True

    def calcular_duracao_total(self):
        """8. Calcular a duração total."""
        total_segundos = 0.0
        aux = self.inicio
        count = 0
        while aux is not None:
            total_segundos += float(aux.duracao)
            count += 1
            aux = aux.proximo

        mins = int(total_segundos // 60)
        segs = int(total_segundos % 60)
        print(f"\nTotal de Faixas: {count}")
        print(f"Duração Total: {mins} minutos e {segs} segundos ({total_segundos}s)")
        return total_segundos


def menu():
    playlist = Playlist()

    while True:
        print("\n" + "="*45)
        print("         GERENCIADOR DE PLAYLIST        ")
        print("="*45)
        print("1. Adicionar música ao final")
        print("2. Inserir música ANTES de um código")
        print("3. Inserir música DEPOIS de um código")
        print("4. Listar playlist (Início -> Fim)")
        print("5. Listar playlist (Fim -> Início)")
        print("6. Buscar música por código")
        print("7. Remover música por código")
        print("8. Mover música para o início")
        print("9. Calcular duração total")
        print("0. Sair")
        print("="*45)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                cod = int(input("Código da música: "))
                tit = input("Título: ").strip()
                art = input("Artista: ").strip()
                dur = float(input("Duração em segundos (ex: 210): "))
                playlist.adicionar_fim(cod, tit, art, dur)
            except ValueError:
                print("\n[!] Entrada inválida para código ou duração.")

        elif opcao == "2":
            try:
                ref = int(input("Inserir ANTES de qual código? "))
                cod = int(input("Novo código da música: "))
                tit = input("Título: ").strip()
                art = input("Artista: ").strip()
                dur = float(input("Duração em segundos: "))
                playlist.inserir_antes(ref, cod, tit, art, dur)
            except ValueError:
                print("\n[!] Entrada inválida.")

        elif opcao == "3":
            try:
                ref = int(input("Inserir DEPOIS de qual código? "))
                cod = int(input("Novo código da música: "))
                tit = input("Título: ").strip()
                art = input("Artista: ").strip()
                dur = float(input("Duração em segundos: "))
                playlist.inserir_depois(ref, cod, tit, art, dur)
            except ValueError:
                print("\n[!] Entrada inválida.")

        elif opcao == "4":
            playlist.listar_inicio_ao_fim()

        elif opcao == "5":
            playlist.listar_fim_ao_inicio()

        elif opcao == "6":
            try:
                cod = int(input("Código para busca: "))
                playlist.buscar(cod)
            except ValueError:
                print("\n[!] Digite um código numérico válido.")

        elif opcao == "7":
            try:
                cod = int(input("Código para remoção: "))
                playlist.remover(cod)
            except ValueError:
                print("\n[!] Digite um código numérico válido.")

        elif opcao == "8":
            try:
                cod = int(input("Código da música a mover para o início: "))
                playlist.mover_para_inicio(cod)
            except ValueError:
                print("\n[!] Digite um código numérico válido.")

        elif opcao == "9":
            playlist.calcular_duracao_total()

        elif opcao == "0":
            print("\nEncerrando o programa de playlist...")
            break
        else:
            print("\n[!] Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()