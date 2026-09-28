from queue import PriorityQueue

class ProntoSocorro:

    def __init__(self):
        # Você criou uma fila de prioridade que pertence ao objeto ProntoSocorro
        self.fila = PriorityQueue()
    def adicionar_paciente (self,nome_paciente,prioridade):
        self.fila.put((prioridade,nome_paciente))
    def chamar_proximo (self):
        # O método get() retira o elemento que deve sair primeiro.
        prioridade,nome_paciente = self.fila.get()
        print(f"Chamando: {nome_paciente} (prioridade {prioridade})")
    def fila_vazia (self):
        return self.fila.empty()

hospital = ProntoSocorro()
hospital.adicionar_paciente("João",3)
hospital.adicionar_paciente("Maria", 1)
hospital.adicionar_paciente("Carlos", 2)
hospital.adicionar_paciente("Ana", 1)
hospital.adicionar_paciente("Pedro", 4)
hospital.adicionar_paciente("Lucas", 2)

# Enquanto a fila não estiver vazia chamar o proximo
while not hospital.fila_vazia():
    hospital.chamar_proximo()