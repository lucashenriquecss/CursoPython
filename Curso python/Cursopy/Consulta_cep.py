import requests
def main():
    print('####################')
    print('### Consulta CEP ###')
    print('####################')
    print()

    cep = input('Digite o CEP para a consulta:\n')

    if len(cep) != 8:
        print('CEP invalido, Quantidade de digitos incorretos\n')
        main()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    addres_data = request.json()

    if 'erro' not in addres_data:
        print('=== CEP encontrado! ===')

        print('CEP: {}'.format(addres_data['cep']))
        print('Logradouro: {}'.format(addres_data['logradouro']))
        print('Complemento: {}'.format(addres_data['complemento']))
        print('Bairro: {}'.format(addres_data['bairro']))
        print('Cidade: {}'.format(addres_data['localidade']))
        print('Estado: {}'.format(addres_data['uf']))
    else:
        print('{}: Cep invalido.'.format(cep))
    while True:
      op = input('Deseja sair ou continuar?\n 1- Sim\n 2- Não\n')
      if op == 1 or 'Sim' or 'sim':
          main()
      elif op == 2 or 'Não' or'não' or 'Nao' or 'nao':
          print('Saindo...')
          exit()
if __name__ == '__main__':
    main()