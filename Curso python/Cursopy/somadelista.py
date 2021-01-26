lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4]

# for x,y in zip(lista1,lista2):
#     lis = x+y
#     lis= list(lis)
#     print(lis)
soma_lista=[ (x+y) for x,y in zip(lista1,lista2)]
print(soma_lista)

