import random

alfa = ' abcdefghijklmnopqrstuvwxyzøæå'

key = random.randrange(3,10)

# def readfile ():
#     f = open("readme.txt","r")
#     for i in f:
    
#         print (i)

#     f.close()



def ceasar_en(plain_text):
    cipher_text = ''
    plain_text = plain_text.lower()
    
    for i in plain_text:
        index = alfa.find(i)
        index = (index+key)% len(alfa)
        cipher_text = cipher_text+alfa[index]
    return cipher_text


def ceasar_de (cipher_text):
    plain_text=''
    for i in cipher_text:
        index = alfa.find(i)
        index =(index-key)%len(alfa)
        plain_text = plain_text+alfa[index]
    return plain_text

if __name__ == "__main__":
    # readfile()
    
    encrypted = ceasar_en(input("enter some value\n"))
    print(encrypted)

    decrypted = ceasar_de (encrypted)   
    print(decrypted)




