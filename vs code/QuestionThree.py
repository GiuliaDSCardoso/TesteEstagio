import xml.etree.ElementTree as ET 

def calcular_estatisticas(faturamento):

    # Extraindo os valores de faturamento do XML, ignorando os valores = zero.
    valores = [int(dia.find('valor').text) for dia in faturamento if int(dia.find('valor').text) > 0]
    
    # Verificando se tem valores de faturamento válidos
    if not valores:
        return None, None, 0  # Retorna valores padrão se não houver faturamento válido.
    
    # Calculando o menor e o maior valor.
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    
    # Calculando a média dos valores.
    media_faturamento = sum(valores) / len(valores)
    
    # Conta o número de dias com faturamento acima da média.
    dias_acima_da_media = sum(1 for valor in valores if valor > media_faturamento)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

def main():

    caminho_arquivo = 'faturamento.xml'  # caminho do arquivo XML.
    
    try:
        #chegando até a raiz do documento.
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()
        
        # Encontrando todos os elementos <dia> no XML.
        faturamento = root.findall('dia')
        
        # Calculando as estatísticas usando a função calcular_estatisticas.
        menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_estatisticas(faturamento)
        
        # Imprimindo os resultados das estatísticas calculadas.
        print(f"Menor valor de faturamento: R${menor_faturamento}")
        print(f"Maior valor de faturamento: R${maior_faturamento}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
        
    except Exception as e:
        # Capturando erros
        print(f"Erro: {e}")

# Chamando a main.
main()
