import random

alfa_small = ' abcdefghijklmnopqrstuvwxyz'
alfa_big = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#key = random.randrange(3,25)

def ceasar_en(plain_text, key):
    cipher_text = ''
    for i in range(len(plain_text)):

        index  = plain_text[i]

        if (index.islower()):
           cipher_text += chr((ord(index)+ key-alfa_small.find(index))%26 +alfa_small.find(index))

            #index = plain_text.find(i)
            #index = (index+key)% len(alfa_small)
            #cipher_text += cipher_text+alfa_small[index]
        else:
           cipher_text += chr((ord(index)+ key-alfa_big.find(index))%26 +alfa_big.find(index))

           #index = plain_text.find(i)
           #index = (index+key)% len(alfa_big)
           #cipher_text += cipher_text+alfa_big[index]
    return cipher_text


if __name__ == "__main__":
   plain_text = "Rahmat oH det er"
   key = 4
   print("Cipher" + ceasar_en(plain_text, key)) 
   
   # encrypted = ceasar_en(input("Enter some value\n"))
    #print(encrypted)

