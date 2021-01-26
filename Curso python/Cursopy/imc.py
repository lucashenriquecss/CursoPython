
nome=input("Digite seu nome:  ")
peso = float(input("Digite seu peso:  "))
altura = float(input("Digite a sua altura:  "))
idade = int(input("Digite a sua idade:  "))
ano_atual=int(input("Digite o ano atual: "))

nasceu = ano_atual - idade
imc= (peso / (altura**2) )

if imc < 18.5:
    print(f"{nome} seu IMC é:{imc:.2f}\n Classicado como: Magreza | Obseidade grau :0\n Parabens esta com peso adequado e se alimente bem!")
    print(f"Nascido em: {nasceu}")
elif imc == 18.5 or imc <= 24.9:
    print(f"{nome} seu IMC é:{imc:.2f}\n Classicado como: Normal | Obseidade grau :0\n Parabens esta com o peso adequado")
    print(f"Nascido em: {nasceu}")
elif imc == 25.0 or imc <=29.9:
    print(f"{nome} seu IMC é:{imc:.2f}\n Classicado como: Sobrepeso | Obseidade grau :1\n Comece a fazer exercicios fisicos e mantenha uma boa alimentação!!")
    print(f"Nascido em: {nasceu}")
elif imc == 30.0 or imc <=39.9:
    print(f"{nome} seu IMC é:{imc:.2f}\n Classicado como: Obesidade | Obseidade grau :2\n Procure um medico especializado!!")
    print(f"Nascido em: {nasceu}")
elif imc>=40.0:
    print(f"{nome} seu IMC é:{imc:.2f}\n Classicado como: Obesidade Grave| Obseidade grau :3\n Procure um medico especializado!!")
   print(f"Nascido em: {nasceu}")

