
#GymCompanion
def treino_peito():

    print("\n===== Peito e Ombro =====")

    exercicios = [
        "Supino",
        "CrossOver (Baixo)",
        "CrossOver (Alto)",
        "Desenvolvimento",
        "Elevação Lateral (Polia)",
        "Elevação Lateral (Halter)"
    ]

    for i, exercicio in enumerate(exercicios, start=1):
        print(f"{i}. {exercicio}")

    escolha = int(input("Digite o número do exercício: "))

    if escolha < 1 or escolha > len(exercicios):
        print("Inválido")
        escolha = int(input("Digite um exercício válido: "))

    if escolha == 1:

        supinos = [
            "Reto (Halter)",
            "Reto (Barra)",
            "Inclinado (Halter)",
            "Inclinado (Barra)",
            "Declinado (Barra)"
        ]

        print("\nQual Supino?")

        for i, supino in enumerate(supinos, start=1):
            print(f"{i}. {supino}")

        tipo = int(input("Escolha: "))

        if tipo < 1 or tipo > len(supinos):
            print("Inválido")
            tipo = int(input("Digite uma opção válida: "))

        return f"Supino - {supinos[tipo - 1]}"

    return exercicios[escolha - 1]


def treino_costas():

    exercicios = [
        "Barra Fixa",
        "Remada Baixa Iso-Lateral",
        "Remada Baixa",
        "Puxada Alta (Triângulo)",
        "Pulldown",
        "Remada Sentado",
        "Abertura Invertida (Posterior Ombro)",
        "Rosca de Pulso",
        "Rosca Inversa"
    ]

    for i, exercicio in enumerate(exercicios, start=1):
        print(f"{i}. {exercicio}")

    escolha = int(input("Escolha: "))

    return exercicios[escolha - 1]


def treino_bracos():

    print("\n===== Tríceps e Bíceps =====")

    exercicios = [
        "Tríceps na Polia (Corda)",
        "Extensão de Tríceps",
        "Sinuca Tríceps",
        "Francês",
        "Rosca Direta (Polia)",
        "Rosca por Trás",
        "Rosca Inclinada"
    ]

    for i, exercicio in enumerate(exercicios, start=1):
        print(f"{i}. {exercicio}")

    escolha = int(input("Digite o número do exercício: "))

    if escolha < 1 or escolha > len(exercicios):
        print("Inválido")
        escolha = int(input("Digite um exercício válido: "))

    return exercicios[escolha - 1]

def treino_pernas1():

    print("\n===== Quadríceps e Isquiossurais 1 =====")

    exercicios = [
        "Hiperextensão de Lombar com Peso",
        "Cadeira Adutora",
        "Cadeira Flexora",
        "Cadeira Extensora",
        "Elevação de Panturrilha",
        "Panturrilha Sentado"
    ]

    for i, exercicio in enumerate(exercicios, start=1):
        print(f"{i}. {exercicio}")

    escolha = int(input("Digite o número do exercício: "))

    if escolha < 1 or escolha > len(exercicios):
        print("Inválido")
        escolha = int(input("Digite um exercício válido: "))

    return exercicios[escolha - 1]

def treino_pernas2():

    print("\n===== Quadríceps e Isquiossurais 2 =====")

    exercicios = [
        "Hiperextensão de Lombar com Peso",
        "Cadeira Adutora",
        "Leg Press 45º",
        "Mesa Flexora",
        "Elevação de Panturrilha",
        "Panturrilha Sentado"
    ]

    for i, exercicio in enumerate(exercicios, start=1):
        print(f"{i}. {exercicio}")

    escolha = int(input("Digite o número do exercício: "))

    if escolha < 1 or escolha > len(exercicios):
        print("Inválido")
        escolha = int(input("Digite um exercício válido: "))

    return exercicios[escolha - 1]
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