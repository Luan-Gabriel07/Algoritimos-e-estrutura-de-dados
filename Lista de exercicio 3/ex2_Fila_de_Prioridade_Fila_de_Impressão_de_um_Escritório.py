from queue import PriorityQueue
class FilaImpressao():
    def __init__(self):
        self.fila = PriorityQueue()
    def enviar_documento (self,nome_arquivo,urgencia):
        self.fila.put(urgencia,nome_arquivo)
    def imprimir_proximo (self):
        urgencia,nome_arquivo = self.fila.get()
        print (f"Imprimindo: Nome do arquivo: {nome_arquivo} - Urgência{urgencia}")
    def fila_vazia (self):
        return self.fila.empty()

fila = FilaImpressao()

fila.enviar_documento("relatorio.pdf", 1)
fila.enviar_documento("trabalho.pdf", 3)
fila.enviar_documento("planilha.xlsx", 2)
fila.enviar_documento("contrato.pdf", 1)
fila.enviar_documento("apresentacao.pptx", 4)
fila.enviar_documento("documento.docx", 2)


while not fila.fila_vazia():
    fila.imprimir_proximo()