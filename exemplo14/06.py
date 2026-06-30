numero = input("digite o numero 1 ou numero2:")

match numero:
    case 1:
        print("voce escolheu o numro 1")
    case 2:
        print("voce escolheu o numero 2")
    case _:
        print("Número invalido") 