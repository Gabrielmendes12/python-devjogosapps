def eh_palindromo(numero):
    if type(numero) != str:
        numero_str = str(numero)

#verifica se a string é igual ao seu reverso
    if numero_str == numero_str[::-1]:
        return "É um número palíndromo!"
    else:
        return "Não é um número palíndromo."
    
#solicita um número do usuário
num = int(input("Digite o número: "))
print(eh_palindromo(num))