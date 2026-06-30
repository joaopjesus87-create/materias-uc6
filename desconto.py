# 1. Entrada dados
idade = int(input("Digite a idade do cliente: "))
valor = float(input("Digite o valor total da compra (R$): "))

#  CLASSIFICAÇÃO DO CLIENTE 
if idade < 12:
    categoria = "Criança"
elif 12 <= idade <= 17:
    categoria = "Adolescente"
elif 18 <= idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"

#  DESCONTO -
if valor > 500.00:
    porcentagem_desconto = 20
elif valor > 200.00:
    porcentagem_desconto = 10
elif valor > 100.00:
    porcentagem_desconto = 5
else:
    porcentagem_desconto = 0

# Cálculos dos valores
valor_economizado = valor * (porcentagem_desconto / 100)
valor_final = valor - valor_economizado

# resultado
print("\n" + "="*30)
print("       RESUMO DA COMPRA       ")
print("="*30)
print(f"Categoria do Cliente: {categoria}")
print(f"Desconto Aplicado:    {porcentagem_desconto}%")
print(f"Valor Original:       R$ {valor:.2f}")
print(f"Valor Economizado:    R$ {valor_economizado:.2f}")
print(f"Valor Final a Pagar:  R$ {valor_final:.2f}")
print("="*30)