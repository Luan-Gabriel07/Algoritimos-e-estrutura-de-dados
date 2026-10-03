estoque = []
pedidos = []

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
    for indice, produto in enumerate(estoque): # enumerando os indices da lista
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

def cadastrar_pedido (pedidos):
    numero = int(input("Número do pedido: "))
    cliente = input("Nome do cliente: ")
    opc_prioridade = int(input("Prioridade do pedido: [1-Alta / 2-Média / 3-Baixa] "))
    if opc_prioridade == 1:
        prioridade = 1
    elif opc_prioridade == 2:
        prioridade = 2
    elif opc_prioridade == 3:
        prioridade = 3
    else:
        print ("Opão inválida!")
        return
    pedido = [numero,cliente,prioridade]
    pedidos.append(pedido)

def visualizar_pedidos (pedidos):
    for pedido in pedidos:
        print (f"Pedido {pedido[0]}")  
        print (f"Cliente: {pedido[1]}")   
        print (f"Prioridade {pedido [2]}")
        print('-'*20)

def pedidos_prioridade (pedidos,pedido): #fila prioridade
    indice_prioridade = 0
    for indice, pedido in enumerate(pedidos):
        if pedido[2] < pedidos [indice_prioridade][2]:
            indice_prioridade = indice
    return indice_prioridade
''' 
Comparamos a prioridade do pedido atual com a prioridade do pedido
que estamos considerando como prioritário. Se encontrarmos uma
prioridade maior, atualizamos o índice do pedido prioritário.
'''

def processar_pedido (pedidos):
    indice = pedidos_prioridade(pedidos)
    pedido = pedidos.pop(indice)
    print (f"Pedido processado: Cliente {pedido[1]} - Pedido {pedido[0]} - Prioridade {pedido[2]} ")

def ordenar_estoque(estoque):
    for i in range(len(estoque)): # "range" serve para controlar quantas vezes os o for vai se repetir
        for j in estoque:
            print
            #terminar essa função

def buscar_produto (estoque): # Busca Binaria
    codigo_busca = int(input("Código do produto: "))
    inicio = 0
    fim = len(estoque) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2 # o "//" realiza a divisão inteira, descartando a parte decimal
        if codigo_busca == estoque[meio][0]:
            print ("Produto encontrado!")
            print (f"Código: {estoque[meio][0]}")
            print (f"Cliente: {estoque[meio][1]}")
            print (f"Quantidade: {estoque[meio][2]}")
            print (f"Preço: R${estoque[meio][3]:.2f}")
            return
        elif codigo_busca > estoque[meio][0]:
            inicio = meio + 1
        elif codigo_busca < estoque[meio][0]:
           fim = meio - 1
    print ("Produto não encontrado!")
opcao = 1
while opcao != 10:
    print('-=-'*20)
    print("                      DISTRIBUIDORA")
    print('-=-'*20)
    print ("1- Cadastrar produto")
    print ("2- Remover produto")
    print ("3- Ver estoque")
    print ("4- Cadastrar pedido")
    print ("5- Processar próximo pedido")
    print ("6- Ver pedidos prioritários")
    print ("7- Buscar produto")
    print ("8- Ver históricos de ações")
    print ("9- Desfazer última ação")
    print ("10- Sair")
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
        case 4:
            cadastrar_pedido(pedidos)
        case 5:
            processar_pedido(pedidos)
        case 6:
            pedidos_prioridade(pedidos)
        case 7:
            buscar_produto(estoque)
     