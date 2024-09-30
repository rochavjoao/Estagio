import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

# Extraindo os valores de faturamento, ignorando os dias com faturamento 0
fat_valores = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor = min(fat_valores)
maior = max(fat_valores)

media = sum(fat_valores) / len(fat_valores)

# Contando os dias com faturamento superior a média
dias_acima_media = len([valor for valor in fat_valores if valor > media])


print(f"Menor faturamento: {menor:.2f}")
print(f"Maior faturamento: {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")