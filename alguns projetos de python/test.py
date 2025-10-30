import time
import sys

print("O dispositivo vai desligar em breve...")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1) 
print("Desligando...")

# Simula a tela preta
for i in range(3):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(1)

print("\nPrograma finalizado. Dispositivo")