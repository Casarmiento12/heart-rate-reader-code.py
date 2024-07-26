import time
import random

# Definir los límites de pulsaciones
LIMITE_INFERIOR = 60
LIMITE_SUPERIOR = 100

def leer_pulsaciones():
    # Simular la lectura de pulsaciones cardíacas
    return random.randint(50, 120)

def monitorear_pulsaciones():
    while True:
        pulsaciones = leer_pulsaciones()
        print(f"Pulsaciones: {pulsaciones}")
        
        if pulsaciones < LIMITE_INFERIOR:
            print("Alerta: Pulsaciones por debajo del límite inferior!")
        elif pulsaciones > LIMITE_SUPERIOR:
            print("Alerta: Pulsaciones por encima del límite superior!")
        
        # Esperar 1 segundo antes de la siguiente lectura
        time.sleep(1)

if __name__ == "__main__":
    monitorear_pulsaciones()
