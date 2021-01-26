#JOGO DA VIDA DE CONWAY | THE GAME OF LIFE CONWAY
import random, time, copy

height = 60  #altura e largura
width =20

next=[] # proxima celula

for i in range(width):
    column = []
    for x in range(height):
        if random.randint(0,1) == 0:
            column.append('#')
        else: #add uma celula viva ou morta
            column.append(' ')
    next.append(column)

while True:
    print('\n\n\n\n\n')
    current = copy.deepcopy(next)
    for x in range(height):
        for i in range(width):
            print(current[i][x], end='')
        print()

    for i in range(width): #Vai obter as coordenadas vizinhas
        for x in range(height):
            leftcoor = (i - 1) % width
            rightcoor = (i + 1) % width
            upcoor = (x - 1) % height
            downcoor = (x + 1) % height

            num = 0
            if current[leftcoor][upcoor] == '#':
                num+=1
            elif current[i][upcoor] == '#':
                num+=1
            elif current[rightcoor][upcoor] == '#':
                num+=1
            elif current[leftcoor][x] == '#':
                num+=1
            elif current[rightcoor][x] == '#':
                num+=1
            elif current[leftcoor][downcoor] == '#':
                num+=1
            elif current[x][downcoor] == '#':
                num+=1
            elif current[rightcoor][downcoor] == '#':
                num+=1

            if current[i][x] == '#' and(num == 2 or num == 3):
                next[i][x] = '#'
            elif current [i][x] == '' and num == 3:
                next[i][x] = '#'
            else:
                next[i][x]= ''
    time.sleep(1)




