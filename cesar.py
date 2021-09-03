alfabeto = {
  "A": 1,  "B": 2,  "C": 3,  "D": 4,  "E": 5,  "F": 6,  "G": 7,  "H": 8,  "I": 9,  "J": 10,  "K": 11,  "L": 12,  "M": 13,  "N": 14,  "O": 15,  "P": 16,  "Q": 17,  "R": 18,  "S": 19,  "T": 20,  "U": 21,  "V": 22,  "W": 23,  "X": 24,  "Y": 25,  "Z": 26}

cifradoCompleto = ""
contador = 0
frase = input("ingresa la frase: ")
desp = int(input("cuantos desplazamientos quieres? "))
print(frase)

for letra in frase:
  letraMayuscula = letra.upper()
  cifrado = alfabeto[letraMayuscula] + desp
  if alfabeto[letraMayuscula] + desp > 26:
    diferencia = alfabeto[letraMayuscula]+desp - 26 
    cifrado = diferencia
  if contador+1 == len(frase): 
    cifradoCompleto+=str(cifrado)
  else:
    cifradoCompleto+=str(cifrado)+"-"
  contador+=1
  
print(cifradoCompleto)