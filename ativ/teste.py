print("------------------------------------------------------")
print("**DECOMPOSIÇÃO DE NOTAS**")
valor_Reais = int(input("VALOR: R$ ")) # inteiro, notas inteiras, sem centavos
total_Valor = valor_Reais
cedula = 100
total_Atual = 0
print(f" R$ {valor_Reais}, pode ser decomposto em:", end=' ')
while True:
    if total_Valor >= cedula:
        total_Valor -= cedula
        total_Atual += 1
    else:
        if total_Atual > 0:
            print(f"{total_Atual} cédulas de R$ {cedula}")
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        total_Atual = 0
        if total_Valor == 0:
            break


