estoque = []

def buscar_produto (estoque,nome_produto):
    produto = input("Informe o produto que quer procurar")
    for produto in estoque:
        if produto[0] == nome_produto:
            return produto
    return None

def verificar_disponibilidade (estoque,nome_produto,quantidade_desejada):
    produto = buscar_produto(estoque,nome_produto)
    if produto is None:
        print ("Produto não encontrado")
    if quantidade_desejada <= produto[2]:
        print ("Compra possivel")
    else: 
        print("Compra impossível. Quantidade insuficiente.")
opcao = 1
while opcao != 4:
    print ("---------- Gerenciador de Tarefas ----------")
    print ("1- Adicionar produto")
    print ("2- Visualizar estoque")
    print ("3- Procurar produto")
    print ("4- Sair")
    print ("")
    opcao = int(input(""))
    print ("-=-"*10)
    match opcao:
        case 1:
            nome_produto = input("Informe o nome do produto: ")
            preco_produto = float(input("Infome o preço do produto: "))
            quantidade_produto = int(input("Informe a quantidade do produto: "))
            produto = [nome_produto, preco_produto, quantidade_produto]
            estoque.append(produto)
        case 2:
            for produto in estoque:
                print (f"Produto: {produto[0]}")
                print (f"Preço: R$ {produto[1]}")
                print (f"Quantidade: {produto[2]}")
                print ('-'*20)
        case 3:
            nome_produto = input("Informe o produto: ")
            quantidade_desejada = int(input("Informe a quantidade desejada: "))
            verificar_disponibilidade(estoque,nome_produto,quantidade_desejada)
        case 4:
            print ("Saindo...")
        case _:
            print ("Opção inválida")


