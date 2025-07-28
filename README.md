# Calculadora Científica - Python

Projeto de uma calculadora científica desenvolvida em Python como parte dos estudos acadêmicos na FAETERJ. O sistema oferece funcionalidades matemáticas essenciais com interface de linha de comando robusta e tratamento de erros.
Sobre o Projeto
Este projeto foi desenvolvido para consolidar conhecimentos fundamentais de programação em Python, aplicando conceitos essenciais da engenharia de software:

Arquitetura modular com separação de responsabilidades
Estruturas de controle e algoritmos eficientes
Tratamento robusto de exceções e validação de entrada
Manipulação de dados e estruturas de dados Python
Integração com bibliotecas padrão do Python

Funcionalidades Implementadas
Operações Aritméticas

Adição com suporte a múltiplos operandos
Subtração sequencial de múltiplos valores
Multiplicação de múltiplos fatores
Divisão com cálculo de quociente e resto

Operações Matemáticas Avançadas

Cálculo de Porcentagem com validação de entrada
Fatorial para números inteiros positivos
Logaritmo com base customizável (e ou base numérica)
Potenciação com base e expoente configuráveis

Características Técnicas

Sistema de menu interativo com navegação intuitiva
Validação rigorosa de tipos de dados
Tratamento de exceções para casos edge (divisão por zero, valores inválidos)
Formatação consistente de saída de dados

Arquitetura e Implementação
Tecnologias Utilizadas

Python 3.x
Biblioteca math para funções matemáticas avançadas
Estruturas de controle (while, if/elif/else)
Tratamento de exceções (try/except blocks)
Manipulação de strings e listas

Estrutura do Código
python# Exemplo de função modular com tratamento de erro
def teste_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
python# Sistema de menu com estrutura escalável
def selecao():
    opcao = 0
    while (opcao != 17):
        try:
            menu()
            opcao = int(input("Digite a operação desejada (1 - 17): "))
            # Estrutura condicional para direcionamento de funções
        except ValueError:
            print("Digite um valor numérico válido!")
Como Executar
Pré-requisitos

Python 3.x instalado
Ambiente de desenvolvimento configurado

Instalação e Execução
bash# Executar o programa
python calculadora_cientifica.py
Exemplo de Uso
========================================
         CALCULADORA CIENTÍFICA
========================================
Opções de operações:
1. Soma (+)
2. Subtração (-)
3. Multiplicação (*)
4. Divisão (/)
5. Fatorial (x!)
6. Porcentagem (%)
7. Logarítmo (log)
8. Potência (x^y)
...
Digite a operação desejada (1 - 17): 1

Insira os valores a serem somados separados por espaço: 15.5 23.2 8.3
15.5 + 23.2 + 8.3 = 47.0
Competências Técnicas Demonstradas
Programação Estruturada

Organização de código em funções especializadas
Implementação de algoritmos matemáticos
Estruturas de dados adequadas para cada operação

Qualidade de Software

Validação rigorosa de entrada de dados
Tratamento preventivo de exceções
Interface de usuário consistente e intuitiva
Código limpo e bem documentado

Resolução de Problemas

Análise de requisitos matemáticos
Implementação de soluções algorítmicas
Otimização de performance para operações múltiplas

Próximas Implementações

Interface gráfica com tkinter ou PyQt
Implementação completa de funções trigonométricas
Sistema de histórico de cálculos
Exportação de resultados para diferentes formatos
Testes unitários automatizados
Documentação técnica completa

Resultados e Aprendizados
Este projeto consolidou conhecimentos fundamentais em:

Lógica de programação aplicada a problemas reais
Desenvolvimento orientado a funções e modularidade
Tratamento de dados e validação robusta
Integração de bibliotecas Python
Boas práticas de desenvolvimento

Autor
Natan Mauricio Santos
Tecnólogo em Tecnologia da Informação - FAETERJ
Petrópolis - RJ
Email: natanmauriciosantos@hotmail.com
LinkedIn: [linkedin.com/in/natan-mauricio-santos]
Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

Projeto desenvolvido como parte do portfólio acadêmico e profissional em Tecnologia da Informação.
