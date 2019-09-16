# First we convert the letters into numerical values
# Mathematical operations
# To use of brute force we need to look at all the possibility to crack the message
# Brute force is looking at 26 possibility in this case because the letters are 26 



alfa = ' abcdefghijklmnopqrstuvwxyzøæå'

#Now we need to crack the ceasar encryption algorithm with brute force
def crack_ceasar(cipherText):
    for key in range (len(alfa)):
        #defining empty string 
        plainText =''

        # creating a simple ceasar decryption
        for i in cipherText:
            index = alfa.find(i)
            index = (index-key)%len(alfa)
            plainText = plainText + alfa[index]

        # Now we printing the decrypted text with the given KEY
        print('When Key is: %s, and the result is: %s' % (key, plainText))

if __name__ == "__main__":
    encrypted = input("Enter the text you want to decrypt and also check the key value which is used for encryption this text\n")

    crack_ceasar(encrypted)
