# import random
#
# def gerarnumerovivo():
#     numero= random.randint(981000000,981999999)
#     print(numero)
# def gerarnumeroclaro():
#     numero= random.randint(991000000,991999999)
#     print(numero)
# while True:
#     escolha= int(input('Escolha sua operadora:\n1-Claro\n2-vivo\n'))
#     if escolha == 1:
#         gerarnumeroclaro()
#     elif escolha == 2:
#         gerarnumerovivo()
#     else:
#         print('Apenas digite os numero das opções')
import re
phoneNumRegex = re.compile (r'(\ d \ d \ d) - (\ d \ d \ d- \ d \ d \ d \ d)')
mo = phoneNumRegex.findall('Meu número é 415-555-4242. ')

print(mo.findall())

