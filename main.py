import pandas as pd

cardapio = pd.read_csv("cardapio.csv")
carrinho = []

def exibir_itens_da_categoria(categoria):
    filtro = cardapio["Categoria"] == categoria
    itens = cardapio[filtro]

    if itens.empty:
        print(f"\n❌ Nenhum item encontrado na categoria '{categoria}'.")
        return

    print(f"\n----- {categoria.upper()} -----")
    for indice, item in itens.iterrows():
        print(f"{indice + 1} - {item['Produto']} (R$ {item['Preço']:.2f})")

    while True:
        try:
            escolha = int(input("\nDigite o código do produto que deseja adicionar ao carrinho (0 para voltar): "))
            if escolha == 0:
                break
            elif (escolha - 1) in itens.index:
                produto = cardapio.loc[escolha - 1]
                quantidade = int(input(f"Quantas unidades de '{produto['Produto']}' deseja adicionar? "))
                if quantidade <= 0:
                    print("❌ Quantidade inválida. Deve ser maior que zero.")
                    continue
                for i in range(quantidade):
                    carrinho.append(produto)
                print(f"✅ {quantidade}x {produto['Produto']} adicionado(s) ao carrinho!")
            else:
                print("❌ Código inválido.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número.")


def mostrar_carrinho():
    if carrinho == []:
        print("\n🛒 Seu carrinho está vazio.")
        return

    print("\n----- CARRINHO -----")
    total = 0
    produtos_agrupados = {}

    for item in carrinho:
        nome = item['Produto']
        preco = item['Preço']
        if nome in produtos_agrupados:
            produtos_agrupados[nome]['quantidade'] += 1
        else:
            produtos_agrupados[nome] = {'quantidade': 1, 'preco': preco}

    for nome, dados in produtos_agrupados.items():
        quantidade = dados['quantidade']
        preco_unitario = dados['preco']
        subtotal = quantidade * preco_unitario

        print(f"{quantidade}x {nome} - R$ {subtotal:.2f}")
        total += subtotal


    print(f"💰 Total: R$ {total:.2f}")

    while True:
        escolha = input("\nDeseja finalizar a compra? (s/n): ").strip().lower()
        if escolha == 's':
            finalizar_pagamento(total)
            break
        elif escolha == 'n':
            break
        else:
            print("❌ Digite 's' ou 'n'.")

def finalizar_pagamento(total):
    print("\n💳 Formas de pagamento:")
    print("1. Dinheiro\n2. Pix\n3. Cartão de Débito\n4. Cartão de Crédito")
    metodo = input("Escolha a forma de pagamento (1-4): ").strip()

    if metodo == "1":
        print(f"\n🧾 Total a pagar: R$ {total:.2f} - Pagamento em dinheiro.")
    elif metodo == "2":
        chave_pix = "cardapioautomatico@pix.com.br"
        print(f"\n🔷 Pix selecionado. Chave: {chave_pix} | Valor: R$ {total:.2f}")
        if input("Digite 'ok' após o pagamento: ").strip().lower() == 'ok':
            print("✅ Pagamento via Pix confirmado.")
        else:
            print("❌ Pagamento não confirmado. Cancelando.")
    elif metodo == "3":
        print(f"\n💳 Débito - Valor: R$ {total:.2f}. Insira o cartão.")
    elif metodo == "4":
        print(f"\n💳 Crédito - Valor: R$ {total:.2f}. Insira o cartão.")
    else:
        print("❌ Método inválido.")

def menu_principal():
    while True:
        print("\n╔══════════════════════════════════════════════╗")
        print("║              🍽️  MENU PRINCIPAL               ║")
        print("╠══════════════════════════════════════════════╣")
        print("║ 1 - 🥤 Ver Bebidas                           ║")
        print("║ 2 - 🍔 Ver Lanches                           ║")
        print("║ 3 - 🍰 Ver Sobremesas                        ║")
        print("║ 4 - 🛒 Ver Carrinho                          ║")
        print("║ 0 - ❌ Sair                                  ║")
        print("╚══════════════════════════════════════════════╝")
        
        opcao = input("Digite sua opção: ").strip()

        if opcao == "1":
            exibir_itens_da_categoria("Bebida")
        elif opcao == "2":
            exibir_itens_da_categoria("Lanche")
        elif opcao == "3":
            exibir_itens_da_categoria("Sobremesa")
        elif opcao == "4":
            mostrar_carrinho()
        elif opcao == "0":
            print("👋 Obrigado pela sua visita! Volte sempre.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


menu_principal()
