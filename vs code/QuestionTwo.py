def pertence_a_fibonacci(num):
    if num < 0:
        return False
    
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    
    return False

def numero_teste(numeros):
    resultados = {}
    for numero in numeros:
        resultados[numero] = pertence_a_fibonacci(numero)
    return resultados

def main():
    # Definição dos números a serem usados
    teste = [4, 5, 13, 22]
    
    # Teste dos números pré definidos
    resultados = numero_teste(teste)
    
    # Exibe os resultados
    for numero, pertence in resultados.items():
        if pertence:
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")

main()