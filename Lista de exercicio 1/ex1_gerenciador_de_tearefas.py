tarefas = []
def adicionar_tarefa (tarefas):
    nome_tarefa = input("Informe o nome da tarefa: ")
    tarefas.append(nome_tarefa)
    print ("Tarefas adicionada com sucesso!")
def visualisar_tarefa (tarefas):
    for i, tarefas in enumerate(tarefas):
        print (f"{i} - {tarefas}")
def remover_tarefa (tarefas):
    print (tarefas)
    indice = int(input("Informe qual tarefa quer remover: "))
    tarefas.pop(indice)
    print ("Tarefa removida com sucesso!")
opcao = 1
while opcao != 4:
    print ("----------- GERENCIADOR DE TAREFAS -----------")
    print ("1- Adicionar Tarefa")
    print ("2- Visualizar Tarefas")
    print ("3- Remover Tarefas")
    print ("4- Sair")
    print ("")
    opcao = int(input("Informe a ação:(1 a 4) "))
    print ('-' * 20)
    match opcao:
        case 1:
            adicionar_tarefa(tarefas)
        case 2: 
            visualisar_tarefa(tarefas)
        case 3: 
            remover_tarefa(tarefas)
        case 4: 
            print ("Saindo...")