salario_base=float("digite o  salario base do funcionario:$")
gratifacao=50.00
percentual_imposto=0.10

imposto=salario_base*percentual_imposto

salario_receber=salario_base+gratifacao-imposto


print(f"\n---detalhamento do salario---")
print(f"salario base:${salario_base:.2f}")
print(f"gratificaçao:${gratifacacao:.2f}")
print(f"imposto(10%):${imposto:.2f}")
print(f"--------------------------------")
print(f"salario a receber:${salario_receber:.2f}")