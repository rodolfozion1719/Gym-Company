
#GymCompanion
def treino_peito():

    print("\n===== Peito e Ombro =====")

    print("1. Supino")
    print("2. CrossOver (baixo)")
    print("3. CrossOver (alto)")
    print("4. Desenvolvimento")
    print("5. Elevação Lateral (Polia)")
    print("6. Elevação Lateral (Halter)")

    escolha = int(input("Digite o número do exercício: "))

    if escolha < 1 or escolha > 6:
        print("Inválido")
        escolha = int(input("Digite um exercício válido: "))

    if escolha == 1:

        print("\nQual Supino?")

        print("1. Reto (Halter)")
        print("2. Reto (Barra)")
        print("3. Inclinado (Halter)")
        print("4. Inclinado (Barra)")
        print("5. Declinado (Barra)")

        tipo = int(input("Escolha: "))

    return escolha


def treino_costas():

    print("\n===== Costas e Antebraço =====")

    print("1. Barra Fixa")
    print("2. Remada Baixa Iso-Lateral")
    print("3. Remada Baixa")
    print("4. Puxada Alta (Triângulo)")
    print("5. Pulldown")
    print("6. Remada Sentado")
    print("7. Abertura Invertida (Posterior Ombro)")
    print("8. Rosca de Pulso")
    print("9. Rosca Inversa")

    escolha = int(input("Digite o número do exercício: "))

    if escolha < 1 or escolha > 9:
        print("Inválido")
        escolha = int(input("Digite um exercício válido: "))

    return escolha


def treino_bracos():

    print("\n ===== Tríceps e Bíceps =====")

    print("1. Tríceps na Polia (Corda)")
    print("2. Extensão de Tríceps")
    print("3. Sinuca Tríceps")
    print("4. Francês")
    print("5. Rosca Direta (Polia)")
    print("6. Rosca por Trás")
    print("7. Rosca Inclinada")

    escolha = int(input("Digite o número do exercício: "))

    if escolha < 1 or escolha > 7:
        print("Inválido")
        escolha = int(input("Digite um exercício válido: "))

    return escolha

def treino_pernas1():

    print("\n ===== Quadríceps e Isquiossurais 1 =====")

    print("1. Hiperextensão de Lombar Com Peso")
    print("2. Cadeira Adutora")
    print("3. Cadeira Flexora")
    print("4. Cadeira Extensora")
    print("5. Elevação Panturrillha")
    print("6. Panturrillha Sentado")

    escolha = int(input("Digite o número do exercício: "))
    
    if escolha < 1 or escolha > 6:
        print("Inválido")
        escolha = int(input("Digite um exercício válido: "))
    
    return escolha
    

def treino_pernas2():
    print("\n ===== Quadríceps e Isquiossurais 2 =====")

    print("1. Hiperextensão de Lombar Com Peso")
    print("2. Cadeira Adutora")
    print("3. Leg Press 45º")
    print("4. Mesa Flexora")
    print("5. Elevação Panturrillha")
    print("6. Panturrillha Sentado")

    escolha = int(input("Digite o número do exercício: "))
        
    if escolha < 1 or escolha > 6:
        print("Inválido")
        escolha = int(input("Digite um exercício válido: "))
        
    return escolha
# ===========================
# MENU PRINCIPAL
# ===========================

print("\n============= Gym Companion =============")

print("\nQual será seu treino de hoje?")

print("\n1. Peito e Ombro")
print("2. Costas e Antebraço")
print("3. Tríceps e Bíceps")
print("4. Perna 1")
print("5. Perna 2")

treino = int(input("\nMeu treino será de: "))

print("===========================")
print("ESCOLHA DO TREINO")
print("===========================")

if treino == 1:
    print("\nTreino de Peito e Ombro")
    escolha = treino_peito()

elif treino == 2:
    print("\nTreino de Costas e Antebraço")
    escolha = treino_costas()

elif treino == 3:
    print("\nTreino de Bíceps e Tríceps")
    escolha = treino_bracos()

elif treino == 4:
    print("\nTreino de Pernas 1")
    escolha = treino_pernas1()
elif treino == 5:
    print("\nTreino de Pernas 2.")
    escolha = treino_pernas2()

else:
    print("\nTreino inválido.")
    escolha = None

print("===========================")
print("REGISTRO DO TREINO")
print("===========================")

if escolha is not None:

    carga = float(input("\nDigite a carga (kg): "))

    series = int(input("Quantas séries? "))

    repeticoes = []

    for i in range(series):
        rep = int(input(f"Repetições da série {i+1}: "))
        repeticoes.append(rep)

    print("\n============ Treino Registrado ============")

    print(f"Exercício: {escolha}")
    print(f"Carga: {carga} kg")
    print(f"Séries: {series}")
    print(f"Repetições: {repeticoes}")