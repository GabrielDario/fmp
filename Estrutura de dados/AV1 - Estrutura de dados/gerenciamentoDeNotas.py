# ==============================================================================
# SISTEMA DE GERENCIAMENTO DE NOTAS DE ALUNOS
# Estrutura utilizando Vetores Paralelos (listas independentes para nomes e notas)
# ==============================================================================

# Vetores paralelos para armazenamento dos dados
nomes = []
notas = []

# ------------------------------------------------------------------------------
# FUNÇÕES DE VALIDAÇÃO (Requisitos Não Funcionais)
# ------------------------------------------------------------------------------

def validar_nome(mensagem):
    # Garante que o nome contenha apenas letras e espaços e não seja vazio
    while True:
        entrada = input(mensagem).strip()
        #  Substitui espaços para verificar se o restante é alfabético
        if entrada.replace(" ", "").isalpha() and len(entrada) > 0:
            return entrada
        print("Opção invalida: O nome deve conter apenas letras.")

def validar_nota(mensagem):
    #  Garante que a nota digitada seja um número válido entre 0 e 10
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            print("Opção invalida: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Opção invalida: Digite apenas números.")

# ------------------------------------------------------------------------------
# FUNÇÕES RECURSIVAS (Mínimo 2 funções recursivas)
# ------------------------------------------------------------------------------

def somar_notas_recursivo(vetor_notas, indice=0):
    #  Função Recursiva 1: Soma recursivamente todas as notas do vetor
    if indice >= len(vetor_notas):
        return 0.0
    return vetor_notas[indice] + somar_notas_recursivo(vetor_notas, indice + 1)

def buscar_por_intervalo_recursivo(vetores_paralelos, min_val, max_val, indice=0):
    #  Função Recursiva 2: Filtra alunos no intervalo [min_val, max_val] de forma recursiva
    #  vetores_paralelos é uma tupla: (lista_nomes, lista_notas)
    nomes_v, notas_v = vetores_paralelos
    
    if indice >= len(notas_v):
        return []
    
    resultado_atual = []
    if min_val <= notas_v[indice] <= max_val:
        resultado_atual.append((nomes_v[indice], notas_v[indice]))
        
    return resultado_atual + buscar_por_intervalo_recursivo(vetores_paralelos, min_val, max_val, indice + 1)

# ------------------------------------------------------------------------------
# FUNÇÕES PRINCIPAIS E MODULARIZAÇÃO (Mínimo 6 funções)
# ------------------------------------------------------------------------------

def cadastrar_aluno():
    # Função 1: Cadastra um aluno e sua nota nos vetores paralelos
    nome = validar_nome("Digite o nome do aluno: ")
    nota = validar_nota("Digite a nota do aluno (0 a 10): ")
    
    nomes.append(nome)
    notas.append(nota)
    print(f"Aluno {nome} cadastrado com sucesso!")

def listar_alunos():
    # Função 2: Exibe todos os alunos e suas respectivas notas
    if not nomes:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- LISTAGEM DE ALUNOS ---")
    for i in range(len(nomes)):
        print(f"Aluno: {nomes[i]} | Nota: {notas[i]:.2f}")

def calcular_media_geral():
    # Função 3: Calcula e retorna a média da turma usando a função recursiva de soma
    if not notas:
        return 0.0
    soma_total = somar_notas_recursivo(notas)
    return soma_total / len(notas)

def exibir_maior_menor_nota():
    # Função 4: Identifica e mostra a maior e a menor nota cadastrada
    if not notas:
        print("Nenhum aluno cadastrado.")
        return
    maior = max(notas)
    menor = min(notas)
    print(f"\nMaior nota registrada: {maior:.2f}")
    print(f"Menor nota registrada: {menor:.2f}")

def mostrar_aprovados():
    # Função 5: Exibe alunos com nota maior ou igual a 7.0
    if not nomes:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- ALUNOS APROVADOS (Média >= 7.0) ---")
    encontrou = False
    for i in range(len(nomes)):
        if notas[i] >= 7.0:
            print(f"Aluno: {nomes[i]} | Nota: {notas[i]:.2f}")
            encontrou = True
    if not encontrou:
        print("Nenhum aluno aprovado.")

def mostrar_reprovados():
    # Função 6: Exibe alunos com nota menor que 7.0
    if not nomes:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- ALUNOS REPROVADOS (Nota < 7.0) ---")
    encontrou = False
    for i in range(len(nomes)):
        if notas[i] < 7.0:
            print(f"Aluno: {nomes[i]} | Nota: {notas[i]:.2f}")
            encontrou = True
    if not encontrou:
        print("Nenhum aluno reprovado.")

def ordenar_e_exibir(por_nome=False, decrescente=False):
    # Função Auxiliar: Ordena mantendo o vínculo dos vetores paralelos
    if not nomes:
        print("Nenhum aluno cadastrado.")
        return
    
    # Agrupa os vetores paralelos em pares (nome, nota) para ordenação correta
    dados = list(zip(nomes, notas))
    
    if por_nome:
        # Ordena por nome em ordem alfabética
        dados.sort(key=lambda x: x[0].lower())
    else:
        # Ordena por nota (crescente ou decrescente)
        dados.sort(key=lambda x: x[1], reverse=decrescente)
        
    for nome, nota in dados:
        print(f"Aluno: {nome} | Nota: {nota:.2f}")

def calcular_desvio_padrao_aluno():
    # Função Auxiliar Submenu: Calcula o desvio da nota do aluno em relação à média geral
    if not nomes:
        print("Nenhum aluno cadastrado.")
        return
    
    media = calcular_media_geral()
    print(f"Média atual da turma: {media:.2f}")
    
    listar_alunos()
    nome_busca = input("\nDigite o nome exato do aluno para ver o desvio: ").strip()
    
    encontrado = False
    for i in range(len(nomes)):
        if nomes[i].lower() == nome_busca.lower():
            desvio = notas[i] - media
            print(f"\nAluno: {nomes[i]}")
            print(f"Nota do Aluno: {notas[i]:.2f}")
            print(f"Desvio em relação à média ({media:.2f}): {desvio:+.2f}")
            encontrado = True
            break
            
    if not encontrado:
        print("Aluno não encontrado.")

# ------------------------------------------------------------------------------
# MENUS E SUBMENUS
# ------------------------------------------------------------------------------

def submenu():
    # Gerenciador do Submenu
    while True:
        print("\n" + "="*30)
        print("       SUBMENU - EXTRAS       ")
        print("="*30)
        print("1 - Mostrar turma em ordem alfabética")
        print("2 - Mostrar turma em ordem decrescente de notas")
        print("3 - Mostrar turma em ordem crescente de notas")
        print("4 - Mostrar alunos reprovados (nota < 7)")
        print("5 - Listar alunos com notas de X a Y")
        print("6 - Desvio de nota individual em relação à média da turma")
        print("0 - Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            print("\n--- ORDEM ALFABÉTICA ---")
            ordenar_e_exibir(por_nome=True)
        elif opcao == '2':
            print("\n--- NOTAS DECRESCENTES ---")
            ordenar_e_exibir(por_nome=False, decrescente=True)
        elif opcao == '3':
            print("\n--- NOTAS CRESCENTES ---")
            ordenar_e_exibir(por_nome=False, decrescente=False)
        elif opcao == '4':
            mostrar_reprovados()
        elif opcao == '5':
            if not nomes:
                print("Nenhum aluno cadastrado.")
            else:
                x = validar_nota("Digite o valor mínimo (X): ")
                y = validar_nota("Digite o valor máximo (Y): ")
                min_val, max_val = min(x, y), max(x, y)
                
                # Chamada da função recursiva de filtragem por intervalo
                resultados = buscar_por_intervalo_recursivo((nomes, notas), min_val, max_val)
                print(f"\n--- ALUNOS COM NOTAS ENTRE {min_val:.2f} E {max_val:.2f} ---")
                if resultados:
                    for nome_aluno, nota_aluno in resultados:
                        print(f"Aluno: {nome_aluno} | Nota: {nota_aluno:.2f}")
                else:
                    print("Nenhum aluno encontrado nesse intervalo.")
        elif opcao == '6':
            calcular_desvio_padrao_aluno()
        elif opcao == '0':
            break
        else:
            print("Opção invalida")

def menu_principal():
    # Gerenciador do Menu Principal
    while True:
        print("\n" + "="*30)
        print("   GERENCIADOR DE NOTAS    ")
        print("="*30)
        print("1 - Cadastrar alunos e notas")
        print("2 - Listagem alunos com notas")
        print("3 - Calcular e exibir média geral da turma")
        print("4 - Maior e menor nota registrada")
        print("5 - Mostrar alunos aprovados (média >= 7)")
        print("6 - Abrir submenu")
        print("0 - Encerrar aplicação")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            if not notas:
                print("Nenhum aluno cadastrado.")
            else:
                media = calcular_media_geral()
                print(f"\nMédia geral da turma: {media:.2f}")
        elif opcao == '4':
            exibir_maior_menor_nota()
        elif opcao == '5':
            mostrar_aprovados()
        elif opcao == '6':
            submenu()
        elif opcao == '0':
            print("Encerrando a aplicação... Até logo!")
            break
        else:
            print("Opção invalida")

# Ponto de entrada da aplicação
if __name__ == "__main__":
    menu_principal()