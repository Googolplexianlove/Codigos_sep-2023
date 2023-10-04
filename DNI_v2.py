import time

def calcular_potencia_2(dni):
    potencia = 0
    while dni >= 2:
        dni /= 2
        potencia += 1
    return potencia

def calcular_potencia_10(dni):
    potencia = 0
    while dni >= 10:
        dni /= 10
        potencia += 1
    return potencia

print("Bienvenido al programa para calcular la potencia de 2 o 10 de tu DNI.")
dni = int(input("Por favor, ingresa tu número de DNI: "))

opcion = input("Elige una opción (2 o 10) para calcular la potencia: ")

if opcion == "2":
    potencia = calcular_potencia_2(dni)
elif opcion == "10":
    potencia = calcular_potencia_10(dni)
else:
    print("Opción no válida. Debes elegir '2' o '10'.")

if opcion == "2" or opcion == "10":
    print(f"La potencia de {opcion} para representar tu DNI es: {potencia}")
    time.sleep(10)  # Pausa de 10 segundos al final