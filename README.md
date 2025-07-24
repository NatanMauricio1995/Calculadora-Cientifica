# Calculadora Científica - Python

Projeto de uma calculadora científica simples, desenvolvido como parte dos meus estudos em Python pela FAETERJ.

## Sobre o Projeto

Este sistema tem como objetivo simular uma calculadora científica com diversas funcionalidades matemáticas, trabalhando conceitos fundamentais de programação em Python:

* Operações aritméticas
* Estruturas de decisão e repetição
* Organização lógica em funções
* Tratamento de exceções e validação de entrada

## Funcionalidades

* **Adição, Subtração, Multiplicação e Divisão**
* **Potenciação e Radiciação**
* **Fatorial de um número**
* **Cálculo de seno, cosseno e tangente**
* **Logaritmo decimal e natural**
* **Arredondamento para cima ou para baixo**
* **Cálculo de porcentagens**
* **Conversão de ângulos entre graus e radianos**
* **Remoção de item por posição em listas**
* **Exibição de tabela ASCII (símbolos)**

## Tecnologias Utilizadas

* **Python 3.x**
* Bibliotecas:

  * `math` (funções matemáticas)
* Estruturas de controle: `if`, `elif`, `else`, `while`
* Funções personalizadas
* Manipulação de strings e listas
* Tratamento de erros com `try/except`

## Como Executar

1. **Pré-requisitos:**

   * Python 3.x instalado

2. **Executar o programa:**

   ```bash
   python calculadora_cientifica.py
   ```

3. **Uso:**

   * O programa exibe um menu com opções numéricas
   * O usuário escolhe a operação desejada e insere os dados quando solicitado
   * O resultado é mostrado no terminal

## Demonstração

```
=======================================
        CALCULADORA CIENTÍFICA
=======================================

1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potência
6 - Raiz quadrada
7 - Fatorial
8 - Seno / Cosseno / Tangente
9 - Logaritmos
10 - Porcentagem
11 - Arredondamentos
12 - Remover item por posição
13 - Sair
---------------------------------------
Escolha uma opção:
```

## Conceitos de Programação Aplicados

### Estruturas de Repetição e Decisão:

```python
while opcao != 13:
    if opcao == 1:
        # Soma
    elif opcao == 2:
        # Subtração
```

### Validação de Entrada:

```python
try:
    numero = float(input("Digite um número: "))
except ValueError:
    print("Entrada inválida! Tente novamente.")
```

### Funções Matemáticas:

```python
from math import sqrt, factorial, sin, cos, tan, log10, log, radians
```

## Aprendizados

Este projeto proporcionou prática com:

* Criação de **menus interativos**
* Manipulação de **entradas numéricas**
* Uso de **funções matemáticas da biblioteca `math`**
* **Tratamento de exceções** para evitar erros inesperados
* Organização modular de código e **boas práticas**

## Próximas Melhorias

* Interface gráfica com `tkinter`
* Histórico de cálculos
* Suporte a mais funções matemáticas
* Exportar resultados para arquivo `.txt`
* Adicionar testes automatizados

## Autor

**Natan Mauricio Santos**
Tecnólogo em Tecnologia da Informação - FAETERJ
📍 Petrópolis - RJ
📧 [natanmauriciosantos@hotmail.com](mailto:natanmauriciosantos@hotmail.com)
🔗 [LinkedIn](https://linkedin.com/in/seu-perfil)

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações.

---

**"Com cada cálculo, avanço mais na minha jornada na programação!"**

---
