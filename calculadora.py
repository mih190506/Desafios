while True:
    print("Bem-vind@ à nossa calculadora!!")
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


    repetir = input("\nVocê deseja fazer outro cálculo? (sim/não): ").strip().lower()
    if repetir != 'sim':
        print("Obrigado por usar a calculadora! Até logo!")
        break
