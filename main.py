print("\n============= Gym Companion =============")
print("\nQual será seu treino de hoje ??")
print("\n 1. Peito e Ombro")
print("\n 2. Costas e Antebraço")
print("\n 3. Tríceps e Bíceps")
print("\n 4. Perna 1")
print("\n 5. Perna 2")
treino = int(input("Meu treino será de: "))
print(f"\nTreino: {treino} ")
if treino == 1:
    print("1.Supino, 2.CrossOver (baixo), 3.CrossOver (alto) 4.Desenvolvimento, 5.Elevação Lateral(Polia), 6.Elevação Lateral(Halter)")
    escolha = int(input("Digite o número do exercício: "))
    if escolha < 1 or escolha > 6:
        print("Inválido")
        escolha = int(input("Digite um Treino válido()"))
    if escolha == 1:

        print("\nQual Supino?")

        print("1. Reto (Halter)")
        print("2. Reto (Barra)")
        print("3. Inclinado (Halter)")
        print("4. Inclinado (Barra)")
        print("5. Declinado (Barra)")
        
if treino == 2:

    print("\n===== Costas =====")

    print("1. Barra Fixa")
    print("2. Remada Baixa Iso-Lateral")
    print("3. Remada Baixa")
    print("4. Puxada Alta (Triângulo)")
    print("5. Pulldown")
    print("6. Remada Sentado")
    print("7. Abertura Invertida (Posterior de Ombro)")
    print("8. Rosca de Pulso")
    print("9. Rosca Inversa")

    escolha = int(input("Digite o número do exercício: "))

    if escolha < 1 or escolha > 9:
        print("Inválido")
        escolha = int(input("Digite um exercício válido: "))
    print()
    tipo = int(input("Escolha: "))
carga = int(input("Digite a carga (kg): "))
series = int(input("Quantas Séries ??"))
repeticoes = []
for i in range(series):
    rep = int(input(f"Repetições da série {i+1}: "))
    repeticoes.append(rep)


print("\n============ Treino Registrado =============")

print(f"Exercício: {escolha}")
print(f"Carga: {carga} kg")
print(f"Séries: {series}")
print(f"Repetições: {repeticoes}")
