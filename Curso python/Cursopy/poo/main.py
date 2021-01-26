import testeclasse
from testeclasse import Tarefas

if __name__ == '__main__':
  lista = []
  redolista = []

  while True:
      option=Tarefas

      option = input('Enter your list\n|1-Undo , 2-redo , 3-print list| \n')
      if option == 'print':
          lista.display()
          continue
      elif option == 'undo':
          lista.undo(lista, redolista)
          continue
      elif option == 'redo':
         lista.redo(lista, redolista)
         continue

      lista.add(option,lista)





