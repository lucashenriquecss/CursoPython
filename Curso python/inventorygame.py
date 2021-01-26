inventory ={'corda': 1, 'espada': 1, 'escudo': 1,'comida':20,
            'moedas de ouro':100}
def displayinventory(inventario):
    print("Inventory: ")
    itens= 0
    for v in inventory.items():
        itens=sum(inventory.values())
        print(v)
    print(f'Numero total de itens no inventario: {itens}')
displayinventory(inventory)

