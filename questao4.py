valor_total = 0

# Dados de faturamento por estado
faturamentos = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcular o valor total mensal
for _, valor in faturamentos.items():
    valor_total += valor

for estado, faturamento in faturamentos.items():
    percentual = (faturamento / valor_total) * 100
    print("Percentual de representação de {}: {:.2f}%".format(estado, percentual))