alfabeto2 = { 1: "A",   2:"B",  3: "C", 4:"D", 5 :"E",  6 :"F", 7 : "G",  8: "H", 9 : "I",  10:"J", 11: "K",  12:"L",  13:"M",  14:"N",  15:"O",  16:"P",  17:"Q",  18:"R",  19:"S",  20:"T",  21:"U", 22:"V", 23: "W", 24: "X", 25:"Y", 26:"Z"}

cifradoCompleto = ""
contador = 0
print("ingresar el codigo de la letra, y separar con un -")
frase = input("ingresa la frase cifrada: ")
desp = int(input("cuantos desplazamientos fueron? "))
explotado =  frase.split("-")
print(frase)

for letra in explotado:
    cifrado = int(letra) - desp
    if int(letra) - desp <= 1:
        diferencia = 26 - (desp -int(letra)) 
        cifrado = diferencia
    if contador+1 == len(explotado): 
        cifradoCompleto+=alfabeto2[cifrado]
    else:
        cifradoCompleto+=alfabeto2[cifrado]+"-"
    contador+=1
    
print(cifradoCompleto)