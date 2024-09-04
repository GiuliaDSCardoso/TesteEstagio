def calcular_percentuais(faturamentos):
   
    total_mensal = sum(faturamentos.values())  # Calcula o valor total mensal
    percentuais = {}
    
    for estado, valor in faturamentos.items():
        percentual = (valor / total_mensal) * 100  # Calcula o percentual
        percentuais[estado] = percentual
    
    return percentuais

def main():
    # Faturamento por estado
    faturamentos = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    
    # Calcula os percentuais
    percentuais = calcular_percentuais(faturamentos)
    
    # Exibe os resultados
    print("Percentual de representação de cada estado no faturamento total:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()
