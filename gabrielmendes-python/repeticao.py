# ESTRUTURAS DE REPETIÇÃO (LOOPS)
'''
Em Python, existem duas principais estruturas de repetição:

Loop for – Usado para iterar sobre sequências (listas, tuplas, strings, dicionários, etc.) ou usar a função range().

Loop while – Executa um bloco de código enquanto uma condição for verdadeira.

Palavras-chave úteis
- break: Interrompe a execução do loop.
- continue: Pula a iteração atual e passa para a próxima.
- else: Executa um bloco de código quando o loop termina sem interrupção.
Exemplo com break e continue:
'''

for n in range(20):
    if n == 15:
        break # sai do loop quando n for 15
    if n % 2 == 0: 
        continue # imprime números impares
    print(n)

nomes = ["Ana", "Pedro", "Arthur", "Lucas", "Sandro"]

for nome in nomes:
    print(nome)
nomes.append("Gabriel")
print(nomes)

frase = input("Entre com a frase desejada").lower()
vogais = "aeiou"
contador = 0

for vogal in vogais:
    qtd_vogal = frase.count(vogal)
    contador += qtd_vogal
    if qtd_vogal > 0:
        print(f"{vogal}:{qtd_vogal}")
print(f"O total de vogais na frase é: {contador}")


''' #OU 
def contar_vogais(frase):
    frase = frase.lower()
    vogais = "aeiou"
    contador = {vogal: 0 for vogal in vogais}

    for letra in frase:
        if letra in vogais:
            contador[letra] += 1

    return contador

# Entrada do usuário
frase_usuario = input("Digite uma frase: ")

# Contagem das vogais
resultado = contar_vogais(frase_usuario)

# Exibição do resultado
for vogal, quantidade in resultado.items():
    if quantidade > 0:
        print(f"{vogal}: {quantidade}")

'''
'''
contar = 0
while contar < 5:
    print(contar)
    contar +=1 # incremento para evitar loop infinito
'''
