
#Numero= numero de stromtroopers que quieres hacer, por defecto seran 2000, lo que nos pide el ejercicio

import random
    def stormtrooper(numero=2000)

lista_bichos = []
legiones = ["FL","TF","TK","CT","CN","FO"]
digitos = ["0","1","2","3","4","5","6","7","8","9"]
for i in range (0, numero):
    letras = ". join(random.choice(legiones))
    randomNumber = join(random.choice(digitos) for _ in range (4))
    #print("letras")
    #print("randomNumber")
    bicho = letras+"-"+randomNumber
    #print("bichos")
    lista_bichos.append(bicho)
return lista_bichos

