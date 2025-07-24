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
'''






operacoes = [
    "Soma (+);",
    "Subtração (-);",
    "Multiplicação (*);",
    "Divisão (/);",
    "Fatorial (x!);",
    "Porcentagem (%);"
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
                if (opcao == 1):
                    soma()
                
            else:
                print("Digite um valor numérico válido!\n")
        except ValueError:
            print("Digite um valor numérico válido!\n")
    
def soma():
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
    
selecao()