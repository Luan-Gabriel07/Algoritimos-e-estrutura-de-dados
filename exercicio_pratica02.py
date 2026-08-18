#cadastro 
nome = input("Informe seu nome:")
print ("Você deseja pedir?")
print ("1- Lanche")
print ("2- Bebida")
print ("3- Sobremesa")
categoria = int(input(""))
match categoria:
    case 1:
        def registrar_lanche(lanche):
            lanche = input ("Informe qual o seu lanche:")
            return f"Lanche adicionado: {lanche} "
    case 2:
        def registrar_bebida(bebida):
            bebida = input ("Informe qual a sua bebida:")
            return f"Bebida adicionada: {bebida}"
    case 3: 
        def registrar_sobremesa(sobremesa):
            sobremesa = input("Informe qual a sua sobremesa:")
            return f"Sobremesa registrada: {sobremesa}"