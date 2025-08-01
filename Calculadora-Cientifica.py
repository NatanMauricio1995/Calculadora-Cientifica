'''
CALCULADORA CIENTÍFICA

Desenvolvido em Python
Autor: Natan Mauricio Santos
Data: 2025

Funcionalidades:
- Operações:
    - Soma
    - Subtração
    - Multiplicação
    - Divisão
    - Resto da divisão
    - Parte inteira da divisão
    - Fatorial
    - log
    - ln
    - Potência de 10
    - Potência
    - Elevar ao quadrado
    - Raiz
    - Raiz quadrada
    - Modulo
    - Seno
    - Cosseno
    - Tangente
    - Secante
    - Cossecante
    - Cotangente
    
    FAZES DO PROJETO:
    - Menu Principal
    - Seleção da operação
        1. Estrutura básica
        2. Escolhas
    - Operações
        1. Soma
        2. Subtração
        3. Multiplicação
        4. Divisão
        5. Fatorial
'''
operacoes = [
    "Soma (+);",
    "Subtração (-);",
    "Multiplicação (*);",
    "Divisão (/);",
    "Fatorial (x!);",
    "Porcentagem (%);",
    "Logarítmo (log);",
    "Potência (x^y);",
    "Raiz (√x);",
    "Modulo (|x|);",
    "Seno (sen x);",
    "Cosseno (cos x);",
    "Tangente (tg x);",
    "Secante (sec x);",
    "Cossecante (cossec x);",
    "Cotangente (cotg x);",
    "Sair."
]

# Exibe o menu completo
def menu():
    
    print("=" * 40)
    print("         CALCULADORA CIENTÍFICA")
    print("=" * 40)
    print("Opções de operações:")
    for indice, opcao  in enumerate(operacoes):
        print(f"{indice + 1}. {opcao}")
    print("-" * 40 + "\n")
    
def selecao():
    opcao = 0
    while (opcao != 17):
        try:
            menu()
            opcao = int(input("Digite a operação desejada (1 - 17): "))
            if(opcao > 0) and (opcao < 18):
                if (opcao == 1): #ADIÇÃO
                    adicao()
                elif (opcao == 2): #SUBTRAÇÃO
                    subtracao()
                elif (opcao == 3): #MULTIPLICAÇÃO
                    multiplicacao()    
                elif (opcao == 4): #DIVISÃO
                    divisao()
                elif (opcao == 5): #FATORIAL
                    fatorial()
                elif (opcao == 6): #PORCENTAGEM
                    porcentual()
            else:
                print("Digite um valor numérico válido!\n")
        except ValueError:
            print("Digite um valor numérico válido!\n")
    
def adicao():
    # Adição de 1 ou mais números
    print("=" * 40 + "\n\n")
    print("=" * 40)
    print("                  SOMA")
    print("=" * 40)
    
    numeros = input("Insira os valores a serem somados separados por espaço: ")
    lista = numeros.split()
    soma = 0
    for x in lista:
        soma += float(x)
    dados = " + ".join(lista)
    print(f"{dados} = {soma}")
    print("=" * 40 + "\n")
    
def subtracao():
    # Subtração de 1 ou mais números
    print("=" * 40 + "\n\n")
    print("=" * 40)
    print(" " * 15 + "SUBTRAÇÃO")
    print("=" * 40)
    
    numeros = input("Insira os valores a serem subtraidos separados por espaço: ")
    lista = numeros.split()
    menos = 0
    for indice, x in enumerate(lista):
        if(indice == 0):
            menos += float(x)
        else:
            menos -= float(x)
    dados = " - ".join(lista)
    print(f"{dados} = {menos}")
    print("=" * 40 + "\n")
    
def multiplicacao():
    # Multiplica 2 ou mais números
    print("=" * 40 + "\n\n")
    print("=" * 40)
    print(" " * 13 + "MULTIPLICAÇÃO")
    print("=" * 40)
    
    numeros = input("Insira os valores a serem multiplicados separados por espaço: ")
    lista = numeros.split()
    vezes = 1
    for x in lista:
        vezes *= float(x)
    dados = " * ".join(lista)
    print(f"{dados} = {vezes}")
    print("=" * 40 + "\n")
    
def divisao():
    # Divisão de dois números
    print("=" * 40 + "\n\n")
    print("=" * 40)
    print(" " * 16 + "DIVISÃO")
    print("=" * 40)
    
    dividendo = float(input("Insira o valor a ser dividido: "))
    divisor = 0
    while divisor == 0:
        divisor = float(input("Insira o valor que dividirá o primeiro número: "))
        if divisor == 0:
            print("Não se pode dividir por zero!\n")
    
    divisao = dividendo / divisor
    resto = dividendo % divisor
    
    print(f"{dividendo} / {divisor} = {divisao}")
    print(f"Resto da divisão: {resto}")
    print("=" * 40 + "\n")
    
def fatorial():
# Exibe o fatorial de um número inteiro
    print("=" * 40 + "\n\n")
    print("=" * 40)
    print(" " * 13 + "FATORIAL")
    print("=" * 40)
    numero = -1
    while numero < 0:
        try:
            numero = int(input("Insira um número inteiro positivo: "))
            if (numero < 0):
                print("Não se pode fazer fatorial de número negativo! Tente novamente!\n")
        except ValueError:
            print("Digite um valor numérico válido!\n")
    fat = 1
    for x in range(1, numero + 1):
        fat *= int(x)
    print(f"{numero}! = {fat}")
    print("=" * 40 + "\n")
    
def teste_float(valor):
# Testa se o valor inserido é float
    try:
        float(valor)
        return True
    except ValueError:
        return False

    
def porcentual():
# Calcula percentual
    print("=" * 40 + "\n\n")
    print("=" * 40)
    print(" " * 14 + "PORCENTAGEM")
    print("=" * 40)
    x = False
    while (x == False):
        try:
            numero_str = input("Digite o valor total: ")
            porcento_str = input("Digite o percentual desejado (não use %): ")

            if (teste_float(numero_str) == False) or (teste_float(porcento_str) == False):
                print("Digite um valor numérico válido!\n")
                continue

            numero = float(numero_str)
            porcento = float(porcento_str)
            x = True

        except ValueError:
            print("Digite um valor numérico válido!\n")

    percentagem = numero * porcento / 100
    print(f"{numero} * {porcento}% = {percentagem:.5f}")
    print("=" * 40 + "\n")

selecao()