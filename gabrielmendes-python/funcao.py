def nomes():
    print("Alunos Aprovados:")
    lista_nomes = ['Lucas', 'Ana', 'Pedro', 'Maria']
    return lista_nomes

print(nomes())

# função recebendo parâmetros
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def operacoes_basicas(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    return soma, subtracao, multiplicacao, divisao

resultados = operacoes_basicas(10, 2)
print("Resultados das operações básicas:\n"
    f"A Soma é: {resultados[0]}",
    f"\nA Subtração é: {resultados[1]}",
    f"\nA Multiplicação é: {resultados[2]}",
    f"\nA Divisão é: {resultados[3]}")