"""
Esse programa é uma calculadora simples feita em Python.
Ele permite ao usuário realizar operações matemáticas básicas: soma, subtração, multiplicação e divisão.
O usuário pode continuar fazendo cálculos até digitar "sair", quando o programa é encerrado.
O código também trata casos como divisão por zero e operadores inválidos.
"""


"""Minha primeira calculadora em python"""


print ("=== Calculadora ===")  # Exibe título no início

# ==========================
# Funções matemáticas básicas
# ==========================
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero." # Exibe erro (mas retorna None)
    return a / b


# ==========================
# Loop principal da calculadora
# ==========================
while True:

    # Pergunta se o usuário quer sair ou calcular
    sair = input("Digite algo sair ou Calcular: ")


    if sair.lower() == "calcular":# Se digitar "calcular", começa a operação

        # Entrada do primeiro número
        numero1 = float(input("Digite um numero: "))

        # Entrada do operador matemático
        operador = input("Operador [+, -, *, /]: ")

        # Entrada do segundo número
        numero2 = float(input("Digite um numero: "))

        # Verifica qual operação foi escolhida
        if operador == "+":
            resultado = somar(numero1, numero2) # Chama função de soma
            print(f"{numero1} + {numero2} = {resultado}") # Mostra o resultado

        elif operador == "-":
            resultado = subtrair(numero1, numero2) # Chama função de subtração
            print(f" {numero1} - {numero2} = {resultado}")

        elif operador == "*":
            resultado = multiplicar(numero1, numero2) # Chama função de multiplicação
            print(f" {numero1} * {numero2} = {resultado}")

        elif operador == "/":
            if numero2 == 0: # Verifica divisão por zero
                print("Erro: divisão por zero!") # Mostra erro
            else:
                resultado = dividir(numero1, numero2) # Chama função de divisão
                print(f"{numero1} / {numero2} = {resultado}")

        else:
            print("Operador inválido!") # Caso o usuário digite algo errado

    elif sair.lower() == "sair": # Se digitar "sair", o programa é encerrado
        print(sair.lower())
        print("Encerrando a calculadora...")
        break # Interrompe o laço infinito (while True)




