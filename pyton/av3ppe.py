import os

num_mesas = []       
produtos_lista = []    
preco_lista = []    

extrato_geral = 0.0


cont_dinheiro = 0
cont_cred = 0
cont_deb = 0
cont_pix = 0
cont_cheque = 0

val_dinheiro = 0.0
val_cred = 0.0
val_deb = 0.0
val_pix = 0.0
val_cheque = 0.0

# Configurações do Estabelecimento
tipo_estab = ""
artigo = ""
nome_estab = ""

def qnt_mesas():
    """Inicializa as configurações do restaurante e gera as mesas."""
    global tipo_estab, artigo, nome_estab, num_mesas
    
    print("\n--- CONFIGURAÇÃO INICIAL DO ESTABELECIMENTO ---")
    tipo_estab = input("Tipo de estabelecimento (ex: Lanchonete, Restaurante): ").strip()
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
        except ValueError:
            print("[Erro] Por favor, digite um número válido.")

def adicionar_produtos():
    """Cadastra um produto e seu preço no sistema."""
    print("\n--- CADASTRO DE PRODUTOS ---")
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

def ir_mesas():
    """Exibe visualmente o status das mesas (Livre / Ocupada)."""
    print(f"\n=== STATUS DAS MESAS - {tipo_estab.upper()} {nome_estab.upper()} ===")
    if not num_mesas:
        print("Nenhuma mesa configurada ainda.")
        return

    for i, mesa in enumerate(num_mesas):
        # Se a mesa tiver itens, ela está Ocupada [O], se não, está Livre [L]
        status = "[Ocupada]" if len(mesa) > 0 else "[Livre]"
        print(f"Mesa {i + 1:02d}: {status:<9}", end="   ")
        if (i + 1) % 5 == 0:  # Quebra de linha a cada 5 mesas (igual ao seu % 5 do JS)
            print()
    print()

def lancar_produto():
    """Lança um produto cadastrado na conta de uma mesa."""
    if not produtos_lista:
        print("\n[Erro] Nenhum produto cadastrado no sistema ainda!")
        return

    ir_mesas()
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
    """Consulta o consumo atual de uma mesa específica."""
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

def verificar_pagamento(valor_mesa):
    """Contabiliza o método de pagamento e atualiza o financeiro."""
    global cont_dinheiro, cont_cred, cont_deb, cont_pix, cont_cheque
    global val_dinheiro, val_cred, val_deb, val_pix, val_cheque, extrato_geral
    
    print("\n--- FORMA DE PAGAMENTO ---")
    print("1. Dinheiro\n2. Crédito\n3. Débito\n4. Pix\n5. Cheque")
    
    opcao = input("Escolha o método: ")
    
    if opcao == "1":
        cont_dinheiro += 1
        val_dinheiro += valor_mesa
    elif opcao == "2":
        cont_cred += 1
        val_cred += valor_mesa
    elif opcao == "3":
        cont_deb += 1
        val_deb += valor_mesa
    elif opcao == "4":
        cont_pix += 1
        val_pix += valor_mesa
    elif opcao == "5":
        cont_cheque += 1
        val_cheque += valor_mesa
    else:
        print("[Aviso] Opção inválida. Atribuído automaticamente como Dinheiro.")
        cont_dinheiro += 1
        val_dinheiro += valor_mesa
        
    extrato_geral += valor_mesa

def fechar_mesa():
    """Fecha a conta da mesa, recebe o pagamento e limpa a mesa."""
    try:
        num_mesa = int(input("\nDigite o número da mesa que deseja FECHAR E PAGAR: "))
        if 1 <= num_mesa <= len(num_mesas):
            mesa_index = num_mesa - 1
            
            if len(num_mesas[mesa_index]) == 0:
                print("[Aviso] Mesa Vazia! Não há o que pagar.")
                return
            
            valor_total = sum(num_mesas[mesa_index])
            print(f"\nFechando conta da Mesa {num_mesa}: Total de R$ {valor_total:.2f}")
            
            # Executa o fluxo de pagamento
            verificar_pagamento(valor_total)
            
            # Esvazia a mesa (Equivalente ao shift() repetido do seu JS)
            num_mesas[mesa_index].clear()
            print(f"Mesa {num_mesa} paga com sucesso e agora está livre!")
        else:
            print("[Erro] Mesa inválida!")
    except ValueError:
        print("[Erro] Digite um número válido.")

def apagarItem():
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
    print(f"Dinheiro: [{cont_dinheiro}] vendas | Total: R$ {val_dinheiro:.2f}")
    print(f"Crédito:  [{cont_cred}] vendas | Total: R$ {val_cred:.2f}")
    print(f"Débito:   [{cont_deb}] vendas | Total: R$ {val_deb:.2f}")
    print(f"Pix:      [{cont_pix}] vendas | Total: R$ {val_pix:.2f}")
    print(f"Cheque:   [{cont_cheque}] vendas | Total: R$ {val_cheque:.2f}")
    print("="*35)
 
    
    total_atendimentos = cont_dinheiro + cont_cred + cont_deb + cont_pix + cont_cheque
    
    # Cálculo do Ticket Médio
    if total_atendimentos > 0:
        tm = extrato_geral / total_atendimentos
    else:
        tm = 0.0
        
    print(f"Ticket Médio: R$ {tm:.2f}")
    print(f"Total de mesas fechadas/atendidas: {total_atendimentos}")

# MENU PRINCIPAL
def menu_principal():
    qnt_mesas() 
    
    while True:
        print("\n" + "="*40)
        titulo = f"{tipo_estab} {artigo} {nome_estab}".upper() if nome_estab else "SISTEMA"
        print(f"   MENU PRINCIPAL - {titulo}")
        print("="*40)
        print("1. Cadastrar Produto")
        print("2. Visualizar Status das Mesas")
        print("3. Comandar (Lançar Produto)")
        print("4. Consultar Mesa")
        print("5. Fechar/Pagar Mesa")
        print("6. Apagar/Estornar item")
        print("7. Relatório de Informações Gerais")
        print("0. Sair do Sistema")
        print("="*40)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_produtos()
        elif opcao == "2":
            ir_mesas()
        elif opcao == "3":
            lancar_produto()
        elif opcao == "4":
            consultar_mesa()
        elif opcao == "5":
            fechar_mesa()
        elif opcao == "6":
            apagarItem()
        elif opcao == "7":
            inf_geral()
        elif opcao == "0":
            print("\nEncerrando sistema. Até mais!")
            break
        else:
            print("\n[Erro] Opção inválida! Escolha um número de 0 a 7.")

menu_principal()
