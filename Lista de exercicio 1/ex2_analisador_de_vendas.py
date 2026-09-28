import math
vendas = []
def analisar_vendas (vendas):
    total = sum(vendas)
    media = total/12
    maior_venda = max(vendas)
    indice = vendas.index(maior_venda)
    return total,media,indice
for i in range (1,13):
    vendas.append(float(input(f"Diite as vendas do mês {i}: ")))

total,media,indice = analisar_vendas(vendas)
print ("")
print (f"Total: {total:.2f}")
print (f"Média: R${media:.2f}")
print (f"Índice do melhor mês: {indice}")