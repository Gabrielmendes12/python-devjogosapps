#print("hello world")

#chama a função e exibe o resultado
 
name = "Gabriel"
age = "21"
score = 100
city = "Rio de Janeiro"
birth_year = 2004

#print("Hello, my name is", name, "and I am", age, "years old. I live in", city)

#print("I was born in the year", birth_year, "which makes me have", 2025 - birth_year, "years old.")
'''
numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))
soma = numero1 + numero2
sub = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2
resto = numero1 % numero2
potencia = numero1 ** numero2

print("A soma é:", soma)
print("A subtração é:", sub)
print("A multiplicação é:", mult)
print("A divisão é:", div)
print("O resto da divisão é:", resto)
print(numero1, "elevado a", numero2, "é:", potencia)
'''
import random

numero_secreto = random.randint(1,50)
tentativas = 0 #attempts
advinhou  = False #guess

print("Bem vindo ao jogo da adivinhação!")

while not advinhou:
    guess = int(input("Digite sua tentativa (1 a 50): ")) #palpite
    tentativas += 1
    diferenca = abs(guess - numero_secreto) #distância entre os números

    #verifica se o número do palpite é maior ou menor ao número secreto
    if guess < numero_secreto:
        print("O número secreto é maior! tente novamente")
    elif guess > numero_secreto:
        print("O numero secreto é menor!, tente novamente")
    else:
        advinhou = True
        print(f"parabéns, você advinhou o número{numero_secreto} em {tentativas} tentativas.")

    #dicas de proximidade
    if diferenca >= 10:
        print("Você está muito longe!")
    elif 5 < diferenca <= 10:
        print("Você está perto!")
    else:
        print("Você está muito perto!")