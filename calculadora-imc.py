height = float(input("Qual é a sua altura?\n"))
weight = float(input("Qual é o seu peso?\n"))

bmi_calc = weight / (height**2)

print(f"\nSeu IMC é %d." %bmi_calc)

if bmi_calc < 18.5:
    print("Você está abaixo do peso.")
elif bmi_calc >= 18.5 and bmi_calc <= 24.9:
    print("Você está no seu peso normal.")
elif bmi_calc >= 25 and bmi_calc <= 29.9:
    print("Você está em sobrepeso.")
elif bmi_calc >= 30 and bmi_calc <= 34.9:
    print("Você está com obesidade de grau 1.")
elif bmi_calc >= 35 and bmi_calc <= 39.9:
    print("Você está com obesidade de grau 2.")
else:
    print("Você está com obesidade de grau 3.")