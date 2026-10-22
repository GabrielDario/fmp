class Pagina:
    """Nó da lista duplamente encadeada representando uma página web."""
    def __init__(self, url, titulo):
        self.url = url
        self.titulo = titulo
        self.anterior = None
        self.proximo = None

    def __str__(self):
        return f"[{self.titulo}] ({self.url})"


class HistoricoNavegacao:
    """Estrutura da Lista Duplamente Encadeada para gerenciar o histórico."""
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.atual = None

    def visitar_pagina(self, url, titulo):
        """Insere uma nova página após a página atual e remove o histórico à frente."""
        nova_pagina = Pagina(url, titulo)

        # Caso 1: Histórico vazio
        if self.inicio is None:
            self.inicio = nova_pagina
            self.fim = nova_pagina
            self.atual = nova_pagina
            print(f"\n-> Visitando primeira página: {nova_pagina}")
            return

        # Caso 2: Já existem páginas (inserir após a página 'atual')
        # Limpa referências futuras da página 'atual' (descarte do histórico à frente)
        nova_pagina.anterior = self.atual
        self.atual.proximo = nova_pagina
        
        # O novo nó se torna o novo 'fim' da lista
        self.fim = nova_pagina
        self.atual = nova_pagina
        
        print(f"\n-> Visitando: {nova_pagina}")

    def voltar(self):
        """Volta para a página anterior, se houver."""
        if self.atual is None:
            print("\n[!] Histórico vazio. Não há como voltar.")
            return

        if self.atual.anterior is not None:
            self.atual = self.atual.anterior
            print(f"\n<- Voltando para: {self.atual}")
        else:
            print("\n[!] Você já está na primeira página do histórico.")

    def me_avancar(self):
        """Avança para a próxima página, se houver."""
        if self.atual is None:
            print("\n[!] Histórico vazio. Não há como avançar.")
            return

        if self.atual.proximo is not None:
            self.atual = self.atual.proximo
            print(f"\n-> Avançando para: {self.atual}")
        else:
            print("\n[!] Você já está na última página do histórico.")

    def exibir_atual(self):
        """Exibe a página atual."""
        if self.atual is None:
            print("\nNenhuma página aberta (Histórico vazio).")
        else:
            print(f"\nPágina Atual: {self.atual}")

    def exibir_inicio_ao_fim(self):
        """Exibe o histórico do início ao fim (ordem cronológica)."""
        print("\n--- Histórico (Início ao Fim) ---")
        if self.inicio is None:
            print("(Histórico vazio)")
            return

        aux = self.inicio
        i = 1
        while aux is not None:
            marcador = " <= [ATUAL]" if aux == self.atual else ""
            print(f"{i}. {aux}{marcador}")
            aux = aux.proximo
            i += 1

    def exibir_fim_ao_inicio(self):
        """Exibe o histórico do fim ao início (ordem inversa)."""
        print("\n--- Histórico (Fim ao Início) ---")
        if self.fim is None:
            print("(Histórico vazio)")
            return

        aux = self.fim
        i = 1
        while aux is not None:
            marcador = " <= [ATUAL]" if aux == self.atual else ""
            print(f"{i}. {aux}{marcador}")
            aux = aux.anterior
            i += 1


def menu():
    historico = HistoricoNavegacao()

    while True:
        print("\n" + "="*40)
        print("    NAVEGADOR - HISTÓRICO DE PÁGINAS    ")
        print("="*40)
        print("1. Visitar nova página")
        print("2. Voltar página")
        print("3. Avançar página")
        print("4. Exibir página atual")
        print("5. Exibir histórico (Início -> Fim)")
        print("6. Exibir histórico (Fim -> Início)")
        print("0. Sair")
        print("="*40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            url = input("Digite a URL (ex: google.com): ").strip()
            titulo = input("Digite o Título da Página: ").strip()
            if url and titulo:
                historico.visitar_pagina(url, titulo)
            else:
                print("\n[!] URL e Título não podem ser vazios.")
        elif opcao == "2":
            historico.voltar()
        elif opcao == "3":
            historico.me_avancar()
        elif opcao == "4":
            historico.exibir_atual()
        elif opcao == "5":
            historico.exibir_inicio_ao_fim()
        elif opcao == "6":
            historico.exibir_fim_ao_inicio()
        elif opcao == "0":
            print("\nEncerrando o programa...")
            break
        else:
            print("\n[!] Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()