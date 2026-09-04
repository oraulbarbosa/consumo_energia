# CÁLCULO CONSUMO DE ENERGIA
# Constantes
preco_kwh = 0.79 # (valor ENEL)
dias_no_mes = 30

# Entrada de dados
nome_aparelho = input("Qual o nome do aparelho: ")
potencia_watts = float(input("Qual a potência do aparelho: "))
horas_dia = float(input("Qual o tempo médio de uso: "))

# Processamento de dados
consumo_mensal = (potencia_watts * horas_dia * dias_no_mes) / 1000
custo_estimado = consumo_mensal * preco_kwh

# Saída de dados
print(f"Aparelho: {nome_aparelho}")
print(f"Potência: {potencia_watts:.1f} W")
print(f"Uso diário: {horas_dia} horas")
print(f"Consumo estimado: {consumo_mensal} kwh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")