
#GymCompanion
def treino_peito():

    print("\n===== Peito e Ombro =====")

    exercicios = [
        "Supino Reto (Halter)",
        "Supino Reto (Barra)",
        "Supino Inclinado (Halter)",
        "Supino Inclinado (Barra)",
        "Supino Declinado (Barra)",
        "CrossOver (Baixo)",
        "CrossOver (Alto)",
        "Desenvolvimento",
        "Elevação Lateral (Polia)",
        "Elevação Lateral (Halter)"
    ]

    for i, exercicio in enumerate(exercicios, start=1):
        print(f"{i}. {exercicio}")

    return exercicios


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


    return exercicios

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


    return exercicios

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

    return exercicios

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


    return exercicios
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
    exercicios = treino_peito()

elif treino == 2:
    print("\nTreino de Costas e Antebraço")
    exercicios = treino_costas()

elif treino == 3:
    print("\nTreino de Bíceps e Tríceps")
    exercicios =  treino_bracos()

elif treino == 4:
    print("\nTreino de Pernas 1")
    exercicios = treino_pernas1()
elif treino == 5:
    print("\nTreino de Pernas 2.")
    exercicios = treino_pernas2()


print("===========================")
print("REGISTRO DO TREINO")
print("===========================")


for exercicio in exercicios:

    print(f"\nExercício: {exercicio}")

    carga = float(input("Digite a carga (kg): "))

    series = int(input("Quantas séries? "))

    repeticoes = []

    for i in range(series):
        rep = int(input(f"Repetições da série {i+1}: "))
        repeticoes.append(rep)

    # depois guardaremos essas informações
    print("\n============ Treino Registrado ============")

    print(f"Exercício: {exercicios}")
    print(f"Carga: {carga} kg")
    print(f"Séries: {series}")
    print(f"Repetições: {repeticoes}")