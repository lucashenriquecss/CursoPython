carrinho=[]
total=0
nomeitem = str
valoritem = float
voltar= str
def main():
    def back():


  voltar=input("Deseja voltar s ou n? :\n")
  if voltar == 's':
        inicio()

  elif voltar == 'n':
        add() or inicio() or exibir()
  else:
        print("Escolha apenas as letras s(sim) ou n (não)")
        add()

def inicio():
    escolha = int(input("Escolha:\n1- Adicionar produto\n2-Remover produto\n3-Exibir a lista de produtos\n"))
    if escolha == 1:
       add()
    elif escolha == 2:
       remover()
    elif escolha == 3:
       exibir()
    else:
       print("Escolha apenas as opções numeradas a cima 1,2 ou 3 !")
       inicio()

def exibir():
     quantidade=len(carrinho)
     total = [sum(float(y) for x,y in carrinho)]
     produtos= [(x,y) for x,y in carrinho]
     print(f"Sua lista:{produtos}\nA soma dos produtos:{total}\nVocê tem {quantidade} produto(s) na sua lista\n")

     # print(f"{carrinho}\n Você tem {quantidade} na sua lista")

     back()

def add():
    nomeitem=input("Digite o nome do  item:\n")
    valoritem= float(input("Digite o valor do item:\n"))

    carrinho.append((nomeitem,valoritem))
    back()
    return carrinho

def remover():
     nomeitem= input("Digite o nome do item para se excluido:\n")
     nomeitem.remove((" "))
     voltar = input("Deseja voltar s ou n? :\n")
     if voltar == 's':
         inicio()
     elif voltar == 'n':
         remover()

     else:

         print("Escolha apenas as letras s(sim) ou n (não)")
         remover()



if __name__ == '__main__':
    main()








    # total = 0
    #
    # carrinho = []
    # for rep in carrinho:
    #     nome = input('adicione o nome do produto:\n')  # add product name
    #     valor = input('Adicione o valor do produto:\n')  # add product value
    #
    # carrinho.append((nome, valor))
    #
    # # print(f'Sua lista:{carrinho}')