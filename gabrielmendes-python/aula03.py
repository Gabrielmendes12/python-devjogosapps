# tabela verdade operadores lógicos

#idade = int(input("Digite a sua idade: "))
#tolerancia = input("Qual sua tolerância ao álcool? (baixa, média, alta): ").lower()

while True:
    try:
        idade = int(input("Digite a sua idade: "))
        if 0 < idade <= 100:
            break
        else:
            print("Idade inválida! Digite um número entre 0 e 100")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro")

# Classificação Etária
if (idade >= 18):
    print("Você é maior de idade")

elif 16 <= idade < 18:
    print("Você é pré-adulto")

elif 13 <= idade < 16:
    print("Você é adolescente")

elif 10 <= idade < 13:
    print("Você é pré-adolescente")

else:
    print("Você é criança.")