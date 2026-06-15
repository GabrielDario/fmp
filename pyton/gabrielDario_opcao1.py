###Gabriel Dario da Rosa

import os

num_mesas = []       
produtos_lista = []    
preco_lista = []    
total_atendimentos = 0
extrato_geral = 0.0


# Configurações do Estabelecimento
tipo_estab = ""
artigo = ""
nome_estab = ""

def qnt_mesas():
    global tipo_estab, artigo, nome_estab, num_mesas
    
    print("\n--- PERSONALIZE SEU ESTABELECIMENTO ---")
    tipo_estab = input("Tipo de estabelecimento (ex: Lanchonete, Restaurante...): ").strip()
    artigo = input("Artigo (ex: do, da): ").strip()
    nome_estab = input("Nome do estabelecimento: ").strip()
    
    while True:
        try:
            qnt = int(input("Digite a quantidade de mesas (Entre 1 e 50): "))
            if 0 < qnt <= 50 and tipo_estab != "" and nome_estab != "":
                
                num_mesas = [[] for _ in range(qnt)]
                print(f"\n{tipo_estab} {artigo} {nome_estab} configurado com sucesso!")
                break
            else:
                print("[Erro] Quantidade inválida ou campos vazios. Tente novamente.")
                qnt_mesas()
        except ValueError:
            print("[Erro] Por favor, digite um número válido.")

def adicionar_produtos():
    print("\n--- CADASTRO DE PRODUTOS ---")

    i = 0
    tamanhoCardapio = len(produtos_lista)
    if tamanhoCardapio > 0:
        print("PRODUTOS JÁ CADASTRADOS: ")
        for i in range(0, tamanhoCardapio):
         print(produtos_lista[i], " R$", preco_lista[i])
    else:
        print("NENHUM PRODUTO CADASTRADO!")
    print(" ")
    nome_produto = input("Nome do produto: ").strip().upper()

    try:
        preco_produto = float(input("Preço do produto: R$ "))
        if nome_produto != "" and preco_produto > 0:
            produtos_lista.append(nome_produto)
            preco_lista.append(preco_produto)
            print(f"Produto '{nome_produto}' cadastrado com sucesso!")
        else:
            print("[Erro] Cadastro inválido! Nome vazio ou preço menor/igual a zero.")
    except ValueError:
        print("[Erro] Preço inválido. Use pontos para centavos (Ex: 15.50).")

def conferir_mesas():
    print(f"\n=== STATUS DAS MESAS - {tipo_estab.upper()} {nome_estab.upper()} ===")
    if not num_mesas:
        print("Nenhuma mesa configurada ainda.")
        return

    for i, mesa in enumerate(num_mesas):
        
        if len(mesa) > 0:
         status = "[Ocupada]"
        else:
         status = "[Livre]"

        print(f"Mesa {i + 1:02d}: {status:<9}", end="   ")
        if (i + 1) % 5 == 0: 
            print()
    print()

def lancar_produto():
    if not produtos_lista:
        print("\n[Erro] Nenhum produto cadastrado no sistema ainda!")
        return

    conferir_mesas()
    try:
        mesa_comandar = int(input("Deseja lançar em qual mesa? "))
        if 1 <= mesa_comandar <= len(num_mesas):
            
            # Mostra os produtos disponíveis
            print("\n--- PRODUTOS DISPONÍVEIS ---")
            for idx, prod in enumerate(produtos_lista):
                print(f"[{idx + 1}] {prod} - R$ {preco_lista[idx]:.2f}")
                
            escolha_prod = int(input("Escolha o número do produto: ")) - 1
            
            if 0 <= escolha_prod < len(produtos_lista):
                # Adiciona o preço do produto selecionado na lista daquela mesa
                preco_do_produto = preco_lista[escolha_prod]
                num_mesas[mesa_comandar - 1].append(preco_do_produto)
                print(f"Sucesso: {produtos_lista[escolha_prod]} lançado na Mesa {mesa_comandar}!")
            else:
                print("[Erro] Produto inválido!")
        else:
            print("[Erro] Esta mesa não existe!")
    except ValueError:
        print("[Erro] Entrada inválida. Digite apenas números.")

def consultar_mesa():
    try:
        num_mesa = int(input("\nDigite o número da mesa para consultar: "))
        if 1 <= num_mesa <= len(num_mesas):
            mesa_index = num_mesa - 1
            
            print(f"\n--- CONTA DA MESA {num_mesa} ---")
            if len(num_mesas[mesa_index]) == 0:
                print("Mesa vazia.")
                return False
            else:
                valor_total = sum(num_mesas[mesa_index])
                print(f"CONSUMO TOTAL: R$ {valor_total:.2f}")
                return True
        else:
            print("[Erro] Mesa inválida!")
            return False
    except ValueError:
        print("[Erro] Digite um número válido.")
        return False

def fechar_mesa():
    global extrato_geral
    global total_atendimentos
    try:
        num_mesa = int(input("\nDigite o número da mesa que deseja FECHAR E PAGAR: "))
        if 1 <= num_mesa <= len(num_mesas):
            mesa_index = num_mesa - 1
            
            if len(num_mesas[mesa_index]) == 0:
                print("[Aviso] Mesa Vazia! Não há o que pagar.")
                return
            
            valor_total = sum(num_mesas[mesa_index])
            print(f"\nFechando conta da Mesa {num_mesa}: Total de R$ {valor_total:.2f}")

            extrato_geral += valor_total
            total_atendimentos += 1
            num_mesas[mesa_index].clear()
            print(f"Mesa {num_mesa} paga com sucesso e agora está livre!")
        else:
            print("[Erro] Mesa inválida!")
    except ValueError:
        print("[Erro] Digite um número válido.")

def apagar_Item():
    print("="*40)
    print("        APAGAR ITEM        ")
    try:
        num_mesa = int(input("\nDigite o número da mesa que teve o item lançado errado: "))
        if 1 <= num_mesa <= len(num_mesas):
            mesa_index = num_mesa - 1
            
            # Se a mesa estiver vazia, não há o que estornar
            if len(num_mesas[mesa_index]) == 0:
                print("[Aviso] Esta mesa já está vazia. Nenhum item para remover.")
                return
            
            # Mostra os itens atuais para o usuário escolher qual tirar
            print(f"\n--- ITENS DA MESA {num_mesa} ---")
            for i, valor in enumerate(num_mesas[mesa_index]):
                print(f"[{i + 1}] Lançamento de R$ {valor:.2f}")
            
            escolha = int(input("\nDigite o número do item que deseja CANCELAR/REMOVER: ")) - 1
            
            # Verifica se o número escolhido é válido dentro da lista da mesa
            if 0 <= escolha < len(num_mesas[mesa_index]):
                # .pop(escolha) remove o item daquela posição exata
                valor_removido = num_mesas[mesa_index].pop(escolha)
                print(f"\nSucesso: O lançamento de R$ {valor_removido:.2f} foi removido da Mesa {num_mesa}!")
            else:
                print("[Erro] Número de item inválido!")
        else:
            print("[Erro] Mesa inválida!")
    except ValueError:
        print("[Erro] Entrada inválida. Digite apenas números.")
   
def inf_geral():
    print("="*35)
    print("        CONTROLE FINANCEIRO        ")
    print(f"Valor bruto gerado: R$ {extrato_geral:.2f} Reais")
    
    # Cálculo do Ticket Médio
    if total_atendimentos > 0:
        tm = extrato_geral / total_atendimentos
    else:
        tm = 0.0
        
    print(f"Ticket Médio: R$ {tm:.2f}")
    print(f"Total de mesas fechadas/atendidas: {total_atendimentos}")

def visualizar_cardapio():
     print("="*35)
     print("        CARDAPIO        ")
     print(" ")
     tamanhoCardapio = len(produtos_lista)
     i = 0
     
     if tamanhoCardapio == 0 :
         print("---------------CARDÁPIO VAZIO---------------")
     else:
         for i in range(0, tamanhoCardapio):
             print(produtos_lista[i], " = R$", preco_lista[i])

     
# MENU PRINCIPAL
def menu_principal():
    qnt_mesas() 
    
    while True:
        print("\n" + "="*40)
        titulo = f"{tipo_estab} {artigo} {nome_estab}".upper() if nome_estab else "SISTEMA"
        print(f"   MENU PRINCIPAL - {titulo}")
        print("="*40)
        print("1. Cadastrar Produto")
        print("2. Mostrar Cardápio")
        print("3. Visualizar Status das Mesas")
        print("4. Comandar (Lançar Produto)")
        print("5. Consultar Mesa")
        print("6. Fechar/Pagar Mesa")
        print("7. Apagar/Estornar item")
        print("8. Relatório de Informações Gerais")
        print("0. Sair do Sistema")
        print("="*40)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_produtos()
        elif opcao == "2":
            visualizar_cardapio()
        elif opcao == "3":
            conferir_mesas()
        elif opcao == "4":
            lancar_produto()
        elif opcao == "5":
            consultar_mesa()
        elif opcao == "6":
            fechar_mesa()
        elif opcao == "7":
            apagar_Item()
        elif opcao == "8":
            inf_geral()
        elif opcao == "0":
            print("\nEncerrando sistema. Até mais!")
            break
        else:
            print("\n[Erro] Opção inválida! Escolha um número de 0 a 7.")

menu_principal()
