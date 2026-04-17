#1. Escrever um algoritmo que recebe 4 notas de um aluno e que calcula a média aritmética simples das notas. 
# O algoritmo deve imprimir o valor da média e a palavra “aprovado”, se a média é maior ou igual a 6,0 ou “reprovado”, caso contrário.
soma = 0
contador = 1

while contador <= 4:
    nota = float(input(f"Digite a nota {contador}: "))
    soma += nota
    contador += 1

media = soma / 4

if media >= 6:
    print("Média:", media, "Aprovado")
else:
    print("Média:", media, "Reprovado")

#2. Escreva um algoritmo que recebe como entrada um caractere que representa um nucleotídeo (A, G, C, T) e retorna qual é o seu complementar.
# Caso o usuário informe um caractere que não é um nucleotídeo, o seu algoritmo deve retornar a mensagem: “Nucleotídeo inválido!”
nucleotideo = input("Digite um nucleotídeo (A, T, C, G): ").upper()
if nucleotideo == "A":
    print("Complementar: T")
elif nucleotideo == "T":
    print("Complementar: A")
elif nucleotideo == "C":
    print("Complementar: G")
elif nucleotideo == "G":
    print("Complementar: C")
else:
    print("Nucleotídeo inválido!")

#3. Escreva um algoritmo que permite ao usuário executar ações a partir de dois números informados por ele.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha uma opção:")
print("1 - Soma de 2 números")
print("2 - Diferença entre 2 números (maior pelo menor)")
print("3 - Produto entre 2 números")
print("4 - Divisão entre 2 números (denominador não pode ser zero)")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    soma = num1 + num2
    print("Resultado da soma:", soma)
elif opcao == 2:
    if num1 > num2:
        diferenca = num1 - num2
    else:
        diferenca = num2 - num1
    print("Resultado da diferença:", diferenca)
elif opcao == 3:
    produto = num1 * num2
    print("Resultado do produto:", produto)
elif opcao == 4:
    if num2 != 0:
        divisao = num1 / num2
        print("Resultado da divisão:", divisao)
    else:
        print("Erro: não é possível dividir por zero!")
else:
    print("Opção inválida!")

#4. Escrever um algoritmo que lê o sexo (“m” ou “M” ou “f” ou “F”) e a idade de uma pessoa e que escreve o valor da entrada a ser pago.
sexo = input("Digite o sexo (M/F): ")
idade = int(input("Digite a idade: "))

sexo = sexo.lower()

if idade < 10 or idade > 65:
    valor = 0.50

elif idade >= 10 and idade <= 17:
    valor = 4.28

elif idade >= 18 and idade <= 65:
    if sexo == "f":
        valor = 5.50
    elif sexo == "m":
        valor = 8.25
    else:
        print("Sexo inválido!")
else:
    print("Dados inválidos!")
if valor is not None:
    print("Valor da entrada: R$", valor)

#5. Um determinado material radioativo perde metade de sua massa a cada 50 segundos. 
# Dada a massa inicial em gramas informada pelo usuário, fazer um programa que calcula o tempo necessário para que essa massa se torne menor que 0,5 grama.
massa_inicial = float(input("Digite a massa inicial (g): "))

massa = massa_inicial
tempo = 0

while massa >= 0.5:
    massa = massa / 2
    tempo = tempo + 50

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

print("Massa inicial:", massa_inicial, "g")
print("Massa final:", massa, "g")
print("Tempo:", horas, "h", minutos, "m", segundos, "s")

#6. A série de Fibonacci é formada pela sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
# Escreva um algoritmo que gere a série de FIBONACCI até o N-ésimo termo, sendo este informado pelo usuário.
n = int(input("Digite a quantidade de termos: "))

i = 1
a, b = 1, 1

while i <= n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1

#7. Faça um programa que receba um conjunto de valores inteiros e positivos e que calcule e mostre o
# maior e o menor valor do conjunto.
valor = int(input("Digite um valor (0 para encerrar): "))

if valor == 0:
    print("Nenhum valor informado.")
else:
    maior = menor = valor

    while valor != 0:
        if valor < 0:
            print("Valor negativo ignorado.")
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor

        valor = int(input("Digite outro valor (0 para encerrar): "))

    print("Maior valor:", maior)
    print("Menor valor:", menor)


#8. Escreva um algoritmo que recebe uma sequência de DNA e que percorre essa sequência imprimindo, 
# para cada posição, qual é o nome do nucleotídeo da posição.
dna = input("Digite a sequência de DNA: ").upper()

i = 0

while i < len(dna):
    letra = dna[i]

    if letra == "A":
        print(f"{i+1} - A: Adenina")
    elif letra == "G":
        print(f"{i+1} - G: Guanina")
    elif letra == "T":
        print(f"{i+1} - T: Timina")
    elif letra == "C":
        print(f"{i+1} - C: Citosina")
    else:
        print(f"{i+1} - Nucleotídeo inválido!")

    i += 1