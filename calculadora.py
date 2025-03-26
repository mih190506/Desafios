print("Bem vind@ a nossa calculadora!!")
num1 = int(input("Escolha um número inteiro: "))
num2 = int(input("Escolha outro número inteiro: "))

soma = num1 + num2 
multiplicacao = num1 * num2
subtracao = num1 - num2
if num2 == 0:
    divisao = "Erro! Divisão por zero"
else:
    divisao = num1 / num2


print("Seus Resultados:")
print("Soma:", soma)
print("Divisão:", divisao)
print("Multiplicação:", multiplicacao)
print("Subtração:", subtracao)

