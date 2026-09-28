from collections import deque

class FilaCaixa ():
    def __init__(self):
        self.fila = deque()
    def entrar_fila(self,nome_cliente):
        self.fila.append(nome_cliente)
    def atender_cliente (self):
        nome_cliente = self.fila.popleft()
        print (f"Atendendo: {nome_cliente}")
    def tamanho_fila(self):
        return (len(self.fila))

fila_caixa = FilaCaixa()

fila_caixa.entrar_fila("Maria")
fila_caixa.entrar_fila("João")
fila_caixa.entrar_fila("Carlos")
fila_caixa.entrar_fila("Ana")
fila_caixa.entrar_fila("Pedro")

print(f"Clientes na fila: {fila_caixa.tamanho_fila()}")

while fila_caixa.tamanho_fila() > 0:
    fila_caixa.atender_cliente()

print("Fila vazia!")

#FIFO -> First in, First out: Adiciona no final e remove do inicio