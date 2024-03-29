# Logic Jota 

### ⚠️AVISO: 
A linguagem está sendo desenvolvida e eventualmente ela vai ter mais funcionalidades. Tabém, pode aprensetar falhas e bugs ao longo da execução, pois ela está em fase de desenvolvimento.
# Logic Jota: Uma Linguagem de Programação Simples

## O que é Logic Jota?
Logic Jota é uma linguagem de programação simples e intuitiva, projetada para facilitar o aprendizado de programação. Ela apresenta uma sintaxe amigável e utiliza palavras-chave em português para comandos comuns, projetada para desenvolver a logíca de programação e a resolução de algoritmos de nível básicos e complexos.

## Qual o Propósito?
O propósito principal do Logic Jota é fornecer uma linguagem de programação acessível, especialmente para iniciantes, enquanto permite a execução de código legivel e fácil de interpretar. Ele atua como um tradutor que converte programas escritos em Jota para código Python equivalente, assim interpretando e executando eles em sequência após a conversão.

## Como Foi Desenvolvida
O interpretador Logic Jota foi desenvolvido em Python, aproveitando as capacidades poderosas dessa linguagem para manipulação de strings, listas e execução dinâmica de código. O projeto visa tornar a programação mais acessível ao público de língua portuguesa.

## Como criar meu codigos com a linguagem
1. Dentro do diretorio: src/jota, você cria seus arquivos com a extensão .jota e é só isso, simples e intuitivo.
2. Para executar o seu script você tem que rodar o seguinte comando no seu terminal:
```` python
python .\src\interface.py
````




## Comandos e funções do Logic Jota
### Basicos:
1. escreva(msg) 
2. recebe() 

### Operadores Aritméticos:
1. adição(+)
2. subtração(-)
3. multiplicação(*)
4. divisão(/)
5. módulo, resto da divisão(%)
6. exponenciação(*)

### Operadores de Comparação:
1. igual a (==)
2. diferente de (!=)
3. menor que (<)
4. maior que (>)
5. menor ou igual a (<=) 
6. maior ou igual a (>=)




### Estruturas condincionais:
1. se(condinção) 
2. casoNao(condicao) 
3. nadaAcima 
### Estruturas de repetição
1. para(x em contagem(10))
2. enquanto()
3. quebre
4. continue
### Tipos primitivos
1. inteiro → ex: 1, 2, 3, 4 
2. letras → ex: "Jeová", "123"
3. real → 1.5, 9.0, 10.2
4. logico → True ou Falso
### funções
1. funcao()
2. retornar

## Futuras implementações:
1. Operadores logicos -> and, or e not
2. Estruturas de dados → dicionatios, listas e tuplas
3. manipulação de Strings → upper(), lower(). split(), etc.
4. Tratamento de exceções → try, except e finally

## Exemplos de Algoritmos em Jota
### Verificar se um Número é Par ou Ímpar
````jota
escreva("Digite um número: ")
numero = inteiro(recebe())
se(numero % 2 == 0):
    escreva("O número é par.")
casoNao:
    escreva("O número é ímpar.")
````

### Função que soma dois numeros
````jota
funcao soma(a, b):
    retornar a+b

escreva(soma(2, 2))
````


### Calculadora de IMC
````jota
escreva("Digite seu peso (em kg): ")
peso = real(recebe())
escreva("Digite sua altura (em metros): ")
altura = real(recebe())

imc = peso / (altura ** 2)
escreva("Seu IMC é:", imc)

````

### Fórmula de Bhaskara
````jota
escreva("Digite o valor de a: ")
a = real(recebe())
escreva("Digite o valor de b: ")
b = real(recebe())
escreva("Digite o valor de c: ")
c = real(recebe())

delta = b ** 2 - 4 * a * c
se(delta > 0):
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    escreva("As raízes são:", x1, "e", x2)
casoNao:
    escreva("Não existem raízes reais.")
````

### Como Baixar em Meu Computador
1. clone o repositorio:
````markdown
git clone https://github.com/Jeova-1704/logic-jota
````
2. Acesse o diretório:
````markdown
cd Jota
````

## Autor:
- Nome: Jeová Bezerra Leite
- Estudante de engenharia de software
- [linkedin ](https://www.linkedin.com/in/jeov%C3%A1-bezerra-leite-29127826a/)
- [instagram](https://www.instagram.com/jeova_bl)