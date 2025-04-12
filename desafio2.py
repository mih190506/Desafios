nome = input("Digite o Nome do aluno: ")
idade = int(input("digite a idade do aluno: "))
print("Olá  " + nome + "!")

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite agora sua segunda nota: "))
nota3 = float(input("Agora a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    status = print("Aprovado 🎉")
else:
   status = print("Reprovado 😢")

print(nome + " Aqui estão seus Dados: ")
print("Suas Notas: " + nota1, nota2, nota3)
print("Sua média: " + media)
print("Você foi... " + status)