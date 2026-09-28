estoque = []
preco = []
quantidade = []

def buscar_produto (estoque,nome_produto,preco,quantidade):
    for nome_produto in estoque:
        print (f"{estoque} / {preco} / {quantidade}")

def verificar_disponibilidade (estoque,nome_produto,preco,quantidade):
    produto_procurar = ("Infome o produto que quer procurar: ")
    quantidade_produto_procurar = int(input("Infome a quanntidade que deseja:"))
    for produto_procurar in estoque:
        if produto_procurar == nome_produto and quantidade_produto_procurar > quantidade:
            print ("Produto disponivel")
        else :
            print ("Produto indisponivel")
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
            estoque.append(nome_produto)
            preco.append(preco_produto)
            quantidade.append(quantidade_produto)
        case 2:
            for i in estoque:
                print (f"{estoque} / {preco} / {quantidade}")
        case 3:
            buscar_produto (estoque,nome_produto,preco,quantidade)
        case 4:
            print ("Saindo...")


