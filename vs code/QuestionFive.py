def inverter_string(s):
    # Lista de caracteres invertidos
    caracteres_invertidos = []
    
    # Iteração de trás para frente
    for i in range(len(s) - 1, -1, -1):
        caracteres_invertidos.append(s[i])
    
    # Converte novamente de lista pra string
    string_invertida = ''.join(caracteres_invertidos)
    
    return string_invertida

def main():
    # Definição da string teste
    string_original = "Vou passar no estagio"
    
    # Inverte a string
    string_invertida = inverter_string(string_original)
    
    # Exibe a string invertida
    print(f"String original: {string_original}")
    print(f"String invertida: {string_invertida}")

main()