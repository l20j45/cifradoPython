abecedario = "abcdefghijklmnopqrstuvwxyz" # this is the english letters
def encrypt(phrase, key):
    crypt = ""
    keypos = [] # return the index of characters ex: if k='d' then kpos= 3
    for x in key:
       # kpos += alphabets.find(x) #change the int value to string
        keypos.append(abecedario.find(x))
    i = 0
    for x in phrase:
      if i == len(keypos):
          i = 0
      pos = abecedario.find(x) + keypos[i] #find the number or index of the character and perform the shift with the key
      if pos > 25:
          pos = pos-26               # check you exceed the limit
      crypt += abecedario[pos].capitalize()  #because the cipher text always capital letters
      i +=1
    return crypt

def decrypt(crypt, key):
    plain = ""
    keypos = []
    for x in keypos:
        keypos.append(abecedario.find(x))
    i = 0
    for x in crypt:
      if i == len(keypos):
          i = 0
      pos = abecedario.find(x.lower()) - keypos[i]
      if pos < 0:
          pos = pos + 26
      plain += abecedario[pos].lower()
      i +=1
    return plain
try:
    print("Welcome to vigenere cipher.\n\n"
          "The text message should contain only characters and the key should be one character word \n"
          "Press 1 to Enrypt a message \npress 2 to Decrypt a message")
    choose = input("Choice: ")
    if choose == '1':
       phrase = input("enter the plain text: ")
       phrase = phrase.replace(" ", "")  # this will make sure that there is no space in the message
       if phrase.isalpha():
           key = input("Enter the key: ")
           key = key.strip()  # remove the white spaces from both sides
           if key.isalpha():
              # print(k)
               crypt = encrypt(phrase, key)
               print("The cipher text is: ", crypt)

           else:
               print(key)
               print("Enter valid key, key is only one character word!")
       else:
           print("only letters are allowed !!")

    elif choose == '2':
        crypt = input("enter the cipher text: ")
        crypt = crypt.replace(" ", "")
        if crypt.isalpha():
            key = input("Enter the key: ")
            if not key.isalpha():
                print("Enter valid key, key is only one character word!")
            else:
                plain = decrypt(crypt, key)
                print("The plain text is: ", plain)
        else:
            print("only letters are allowed!")

    else:
        print("Please enter a valid choice!")
except Exception as e:
    print(e)
    exit("Enter a valid text please! ")