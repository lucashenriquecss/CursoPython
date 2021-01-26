print()

print("Quiz de perguntas")
print()
perguntas = {
    'pergunta 1': {
      'pergunta' :'Quantas regiões existem no brasil?',
      'resposta': {'a': 5,'b': 4, 'c': 7, 'd': 10, 'e': 2},
      'respostacerta': 'a',
    },
    'pergunta 2': {
      'pergunta' :'Qual a ordem das estações?',
      'resposta': {'a': 'inverno,verão,primavera,verão' ,'b':'verão,primavera,inverno,inverno', 'c': 'sempre inverno',
                   'd': 'primavera e verão',
                   'e': 'inverno,primavera,verão,outono'},
      'respostacerta': 'e',
    },
    'pergunta 3': {
      'pergunta' :'O que é um numero decimal?',
      'resposta': {'a': 'qualquer número que termina em zero','b': 'um número que passou por 10 multiplicações', 'c': 'um número expresso em forma de fração',
                   'd': 'são todos os múltiplos de 10', 'e': 'aquele no qual a parte inteira é separada da parte decimal por uma vírgula'},
      'respostacerta': 'e',
    },
    'pergunta 4': {
      'pergunta' :'Brasil participou da segunda guerra mundial?',
      'resposta': {'a': 'sim','b': 'não'},
      'respostacerta': 'a',
    },
    'pergunta 5': {
      'pergunta' :'Qual simbolo atomico do ouro e que grupo ele pertence?',
      'resposta': {'a': 'Ou, não metais','b': 'Ou, semi-metais', 'c': 'Ai, gases nobres', 'd': 'Au, metais-transição',
                   'e': 'Au, metal'},
      'respostacerta': 'd',
    },
}
pontos =0

for p , v in perguntas.items():
    print(f'{p} : {v["pergunta"]}')
    print()
    for pr, pv in v['resposta'].items():
        print(f'{pr}: {pv}')

    escolharesp= input("Escolha a resposta:")
    if escolharesp == v['respostacerta']:
      print("Você acertou")
      pontos +=1
    else:
      print("voce errou!")
print()

quantidadep= len(perguntas)
porcentagem= pontos / quantidadep * 100
print(f'Total de pontos: {pontos}')
print(f'Porcentagem de acertos :{porcentagem}%')