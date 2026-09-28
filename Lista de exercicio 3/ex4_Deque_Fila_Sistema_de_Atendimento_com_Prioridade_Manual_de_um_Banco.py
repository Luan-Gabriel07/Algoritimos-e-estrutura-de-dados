from collections import deque

class FilaBanco():
    def __init__(self):
        self.fila = deque()

    def chegar_fila(self,nome_cliente):
        self.fila.append(nome_cliente)

    def inserir_prioridade (self,nome_cliente):
        self.fila.appendleft(nome_cliente)

    def atender_proximo (self):
        nome_cliente = self.fila.popleft()
        print (f"Atendendo: {nome_cliente}")

    def tamanho_fila (self):
        return (len(self.fila))

banco = FilaBanco()

# Chegada normal de clientes
banco.chegar_fila("João")
banco.chegar_fila("Maria")

# Cliente prioritário chega no meio do processo
banco.inserir_prioritario("Carlos")

# Mais clientes chegam normalmente
banco.chegar_fila("Ana")
banco.chegar_fila("Pedro")


print("Ordem de atendimento:")
print("-" * 25)

while banco.tamanho_fila() > 0:
    banco.atender_proximo()
        