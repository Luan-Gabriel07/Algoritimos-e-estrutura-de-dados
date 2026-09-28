def calcular_juros_compostos (capital_inicial, taxa_juros, tempo):
    montante_final = capital_inicial * (1 + taxa_juros)**tempo
    return montante_final
 
capital_inicial = float(input("Digite o capital inicial: R$"))
taxa_juros = float(input("Digite a taxa de juros anual (%): "))
taxa_juros_decimal = taxa_juros / 100
tempo = int(input("Digite o tempo de aplicação (anos): "))

montante_final = calcular_juros_compostos(capital_inicial, taxa_juros_decimal, tempo)
print (f"Montante final: R${montante_final}")
