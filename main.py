import random
import string
from paquetes import bd_palabras
from paquetes import diagramas

def juego_ahorcados(palabra):
    print("========================================")
    print("¡Bienvenido al juego del Ahorcado!")
    print("========================================")
    
    letrasPorAdivinar= set(palabra) #set es una clase, va a poner los datos en las variables
    abecedario= set(string.ascii_uppercase) #se importa el string.... el upper para quereconozca las mayusculas
    letrasAdivinadas = set()
    
    intentos = 7
    
    while len(letrasPorAdivinar) >0 and intentos >0:
        print(f"Te quedan {intentos} intentos y has usado estas letras: {''.join(letrasAdivinadas)}")
        
        palabraLista= [letra if letra in letrasAdivinadas else '-' for letra in palabra]
        print(diagramas.vidas[intentos])
        print(f"Palabras: {' '.join(palabraLista)}")
        letraUsuario= input("Digite una letra para la palabra: ").upper()
        
        if letraUsuario in abecedario - letrasAdivinadas:
            letrasAdivinadas.add(letraUsuario)
            if letraUsuario in letrasPorAdivinar:
                letrasPorAdivinar.remove(letraUsuario)
                print('')
            else:
                intentos = intentos -1 # intentos -=1
                print(f"\n Tu letra, {letraUsuario} no se encuentra en la palabra")
        elif letraUsuario in letrasAdivinadas:
            print("\n Ya escogiste esa letra. Por favor escoge una nueva letra")
        else:
            print("\n Este caracter no es valido")
    if intentos ==0:
        print(diagramas.vidas[intentos])
        print(f"¡AHORCADO! Perdiste. Lo lamento mucho. La palabra era {palabra}")
    else:
        print(f"¡EXCELENTE! ¡Adivinaste la palabra {palabra}")
palabra= random.choice(bd_palabras.bdPalabras).upper()
juego_ahorcados(palabra)