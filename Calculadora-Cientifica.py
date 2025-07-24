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
        print(f"{indice}. {opcao}")
    print("-" * 40)
    
menu()