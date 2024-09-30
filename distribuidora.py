faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

fat_total = sum(faturamento.values())

# Cálculo e exibição do percentual de cada estado
percentuais = {estado: (valor / fat_total) * 100 for estado, valor in faturamento.items()}


print('Percentuais de representação do faturamento mensal por estado:')
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
