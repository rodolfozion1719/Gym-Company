
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

treino_registrado = []
for exercicio in exercicios:
    repeticoes = []
    peso = []
    print(f"\nExercício: {exercicio}")
    
    series = int(input("Quantas séries ? "))
    carga = float(input("Carga inicial (kg): "))

    for i in range(series):

        print(f"Série {i+1}")
        print(f"\nCarga atual: {carga} kg ")
        peso.append(carga)
        rep = int(input("Repetições: "))
        repeticoes.append(rep)
        if i < series - 1:
            continuar = input("Manter a mesma carga? (s/n): ").strip().lower()
            if continuar == "n":
                carga = float(input("Nova carga: "))
        
    # depois guardaremos essas informações
    soma_peso = sum(peso)
    print("\n============ Exercício Registrado ============")
    peso_total = soma_peso * repeticoes
    print(f"Exercício: {exercicio} ")
    print(f"Peso levantado: {peso} kg X {repeticoes} repetições = {peso_total} ")
    print(f"Séries: {series}")
    print(f"Repetições: {repeticoes}")
    treino_registrado.append({
    "exercicio": exercicio,
    "peso": peso,
    "peso_total": peso_total,
    "series": series,
    "repeticoes": repeticoes
    })

print("\n========== TREINO COMPLETO ==========")

for registro in treino_registrado:

    print(f"\nExercício: {registro['exercicio']}")
    print(f"Cargas: {registro['peso']}")
    print(f"Séries: {registro['series']}")
    print(f"Repetições: {registro['repeticoes']}")
    print(f"Peso total levantado: {registro['peso_total']} kg")