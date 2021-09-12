polibiusDecrypt = {
  11:"A",  12:"B",  13:"C",  14:"D",  15:"E",  21:"F",  22:"G",  23:"H",  24:"I",  24:"J",  25:"K",  31:"L",  32:"M",  33:"N",  34:"O",  35:"P",  41:"Q",  42:"R",  43:"S",  44:"T",  45:"U",  51:"V",  52:"W",  53:"X",  54:"Y",  55:"Z"}

cifradoCompleto = ""
contador = 0
print("ingresar el codigo de la letra, y separar con un -")
frase = input("ingresa la frase cifrada: ")
explotado =  frase.split("-")
print(frase)

for letra in explotado:
    if contador+1 == len(explotado): 
        cifradoCompleto+=polibiusDecrypt[letra]
    else:
        cifradoCompleto+=polibiusDecrypt[letra]+"-"
    contador+=1
    
print(cifradoCompleto)