estoque = []

def cadastrar_produto (estoque):
    codigo = int(input("Código do produto: "))
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço do produto (uni): R$"))
    produto = [codigo,nome,quantidade,preco]
    estoque.append(produto)

def remover_produto (estoque):
    for produto in estoque:
        print (f"Código: {produto [0]} - Nome {produto [1]} - Quantidade: {produto [2]} - Preço: {produto [3]}")
    print ("")
    remocao = int(input("Insira o código do produto que você deseja remover: "))
    for indice, produto in enumerate(estoque): #enumerando os indices da lista
        if remocao == produto[0]:
            estoque.pop(indice)
            print ("Produto removido!")
            return
    print ("Produto não encontrado!")
   
def ver_estoque (estoque):
    for produto in estoque:
            print (f"Código: {produto [0]}")
            print (f"Nome: {produto [1]}")
            print (f"Quantidade: {produto [2]}")
            print (f"Preço: {produto [3]:.2f}")
            print ('-'*20)

opcao = 1
while opcao != 0:
    print('-=-'*20)
    print("                      DISTRIBUIDORA")
    print('-=-'*20)
    print ("1- Cadastrar produto")
    print ("2- Remover produto")
    print ("3- Ver estoque")
    print ("4- Cadastrar pedido")
    print ("5- Inserir pedido na fila")
    print ("6- Processar próximo pedido")
    print ("7- Ver pedidos prioritários")
    print ("8- Buscar produto")
    print ("9- Ordenar estoque")
    print ("10- Ver históricos de ações")
    print ("11- Desfazer última ação")
    print ("0- Sair")
    print ("")
    opcao = int(input("Escolha o que deseja: "))  
    print ('-'*20)   
    match opcao:
        case 1: 
            cadastrar_produto(estoque)
        case 2: 
            remover_produto(estoque)
        case 3:
            ver_estoque(estoque)