#entrada de dado 


idade=int(input("digite a idade do cliente "))
valor=int(input("digite valor total da compra ($):"))

if idade < 12:
    categoria = "Criança"
elif 12 <= idade <= 17:
    categoria = "Adolescente"
elif 18 <= idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"

if valor > 500.00:
    porcentagem_desconto = 20
elif valor > 200.00:
    porcentagem_desconto = 10
elif valor > 100.00:
    porcentagem_desconto = 5
else:
    porcentagem_desconto = 0


valor_economizado = valor * (porcentagem_desconto / 100)
valor_final = valor - valor_economizado


print("\n" + "="*30)
print("       RESUMO DA COMPRA       ")
print("="*30)
print(f"Categoria do Cliente: {categoria}")
print(f"Desconto Aplicado:    {porcentagem_desconto}%")
print(f"Valor Original:       R$ {valor:.2f}")
print(f"Valor Economizado:    R$ {valor_economizado:.2f}")
print(f"Valor Final a Pagar:  R$ {valor_final:.2f}")
print("="*30)
