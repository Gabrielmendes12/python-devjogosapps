import random

numSecreto = random.randint(1, 100)
tentativas = 0
adivinhou = False

while not adivinhou:
    palpite = int(input("Digite sua tentativa (1 a 100)"))
    tentativas +=1

# verifica se o número é maior ou menor
    if palpite < numSecreto:
        print("O número secreto é maior. Tente novamente!")

    elif palpite > numSecreto:
        print("O número secreto é menor. Tente novamente!")

    else:
        print("Parabéns, você adivinhou o número!")

    if palpite == numSecreto:
        adivinhou = True
        print(f"Você adivinhou o número{numSecreto} em {tentativas} tentativas.")