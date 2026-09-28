from queue import PriorityQueue

class FilaBanco():
    def __init__(self):
        self.fila = PriorityQueue()
    def adicionar_cliente (self,nome_cliente,prioridade):
        self.fila.put((prioridade,nome_cliente))
    def atender_cliente (self,prioridade,nome_cliente):
        prioridade,nome_cliente = self.fila.get()
        print (f"Atendendo {nome_cliente} - Prioridade {prioridade}")
    def fila_vazia (self):
        return self.fila.empty()
    
banco = FilaBanco()

banco.adicionar_cliente("João", 3)
banco.adicionar_cliente("Maria", 1)
banco.adicionar_cliente("Carlos", 2)
banco.adicionar_cliente("Ana", 3)
banco.adicionar_cliente("Pedro", 1)
banco.adicionar_cliente("Lucas", 2)
banco.adicionar_cliente("Paulo", 3)
banco.adicionar_cliente("Julia", 1)


while not banco.fila_vazia():
    banco.atender_cliente()