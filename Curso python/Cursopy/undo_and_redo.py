def display(lista):
    print()
    print("Tasks: ")
    print(lista)

def undo(lista,redolista):
    if not lista:
        print('Nothing list')
        return
    lastlista = lista.pop()
    redolista.append(lastlista)

def redo(lista,redolista):
    if not lista:
        print('Nothing list')
        return
    lastlista = redolista.pop()
    lista.append(lastlista)

def add(option,lista):
    lista.append(option)


if __name__ == '__main__':

    lista=[]
    redolista=[]

    while True:
        option=input('Enter your list\n|1-Undo , 2-redo , 3-print list| \n')
        if option == 'print':
            display(lista)
            continue
        elif option == 'undo':
            undo(lista,redolista)
            continue
        elif option == 'redo':
            redo(lista,redolista)
            continue

        add(option,lista)