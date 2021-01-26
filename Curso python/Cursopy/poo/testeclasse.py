

class Tarefas:


    def __init__(self,lista,redolista):
        self.lista
        self.redolista

    def display(lista):
        print()
        print("Tasks: ")
        print(lista)

    def undo(self, redolista, lista):
        if not self.lista:
            print('Nothing list')
            return
        lastlista = lista.pop()
        self.redolista.append(lastlista)

    def redo(self,lista, redolista):
        if not self.lista:
            print('Nothing list')
            return
        lastlista = redolista.pop()
        self.lista.append(lastlista)

    def add(self,option, lista):
        self.lista.append(option)




if __name__ == '__main__':
  lista = []
  redolista = []
  while True:
      option = input('Enter your list\n|1-Undo , 2-redo , 3-print list| \n')
      if option == 'print':
          lista.display(lista)
          continue
      elif option == 'undo':
          lista.undo(lista, redolista)
          continue
      elif option == 'redo':
          lista.redo(lista, redolista)
          continue

      lista.add(option, lista)
