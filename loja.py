# Sistema de Classificação de Cliente e Desconto Progressivo

print("=== SISTEMA DE CAIXA - LOJA DE DEPARTAMENTO ===")

# 1. Entrada de dados
try:
    idade = int(input("Digite a idade do cliente: "))
    valor_total = float(input("Digite o valor total da compra (R$): "))
    
    # 2. Classificação do  base na idade
    if idade < 12:
        classificacao = "Criança"
    elif 12 <= idade <= 17:
        classificacao = "Adolescente"
    elif 18 <= idade <= 59:
        classificacao = "Adulto"
    else:
        classificacao = "Idoso"

    # 3. Cálculo do Desconto Progressivo (Exemplo lógico)
    
    if valor_total < 100:
        percentual_desconto = 0  # Sem desconto para compras menores que R$100
    elif 100 <= valor_total < 300:
        percentual_desconto = 5  # 5% de desconto
    elif 300 <= valor_total < 500:
        percentual_desconto = 10 # 10% de desconto
    else:
        percentual_desconto = 15 # 15% de desconto para compras de R$500 ou mais

    
    valor_desconto = valor_total * (percentual_desconto / 100)
    valor_final = valor_total - valor_desconto

    # Resultados
    print("\n" + "="*30)
    print(f"Classe do Cliente: {classificacao}")
    print(f"Valor Original: R$ {valor_total:.2f}")
    print(f"Desconto Aplicado ({percentual_desconto}%): R$ {valor_desconto:.2f}")
    print(f"Valor Final a Pagar: R$ {valor_final:.2f}")
    print("="*30)

except ValueError:
    print("\n[Erro] Por favor, insira valores numéricos válidos para idade e valor da compra.")