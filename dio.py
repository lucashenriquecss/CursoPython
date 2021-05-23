try:

    lista = [1, 2]

    print(lista[2])

except Exception:

    print('Ocorreu um erro desconhecido')

except IndexError:

    print('Não foi possível acessar o index pois ele não existe na lista')