nome = input("Digite o Nome do aluno: ")
idade = int(input("digite a idade do aluno: "))
print("Olá  " + nome + "!")

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite agora sua segunda nota: "))
nota3 = float(input("Agora a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    status = "Aprovado 🎉"
else:
   status = "Reprovado 😢"

print("\n📋", nome, "aqui estão seus dados:")
print("Idade:", idade)
print("Suas Notas:", nota1, ",", nota2, ",", nota3)
print(f"Sua média: {media:.2f}")
print("Você foi...", status)