#alfa = ' abcdefghijklmnopqrstuvwxyz.'
alfa  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ. '
# vigenere algorithm
#Mathematical formula is:  Ci (mi)  =(mi+ki) mod 28
# mod is  28 with space and .

def en_vigenere(plainText,key):
    #the text we want to encrypt
    plainText = plainText.upper()
    key = key.upper()
    cipherText = ''
    # repesenting the key index as far as key is concerned
    indexKey = 0
    # now we are going to concider all characters in plainText
    for char in plainText:
        #The number of shifts is equal to the index of the char in the alfabet and plus index of the char in the private key
        index = (alfa.find(char) + (alfa.find(key[indexKey]))) % len (alfa) # this is the mathematical operation
        # adding the encrypted char to the cipherText
        cipherText = cipherText +alfa[index]
        # Now I'm concider the next letter and need to increment the key index 
        indexKey = indexKey + 1

        # we need to start agin when we have concidered the last letter of key
        if indexKey == len(key):
            indexKey =0
    return cipherText

# Now I'm going to decrypt and using the following formula
# The number og shifts is equal to the index  of the char in the alfabet  and minus index of the char in the key
#Mathematical formula is:  Di (mi)  = (mi-ki) mod 28
def de_vigenere(cipherText, key):
    cipherText = cipherText.upper()
    key = key.upper()
    plainText = ''
    indexKey = 0

    for char in cipherText:
        index = (alfa.find(char) - (alfa.find(key[indexKey]))) % len(alfa)
        plainText  = plainText + alfa[index]

        indexKey = indexKey +1
        if indexKey ==len(key):
            indexKey =0

    return plainText

if __name__ =="__main__":
    plainText = input("Enter some text to encrypt\n")
    key_1  =    input("Enter the first key:\n")
    encrypt1 = en_vigenere(plainText, key_1)         # Calling the Encrypting function to encrypt the message with the key 1 
    print("The encrypted message with key 1 is: %s" % encrypt1)
    key_2 =     input("Enter the second key:\n")
    encrypt2 = en_vigenere(encrypt1, key_2)          # Encrypting the message with the help of key 2. Calling the same function as I call when I encrypting the message with help of the key 1
    print("The encrypted message wwith the key 2 is: %s" % encrypt2)

    decrypt2 = de_vigenere(encrypt2, key_2)            # Decrypting the message to call the decrypting function, but first I decrypting the text with help of the second to get the encrypt1 text, then I decrypting the encrypt1 to get the plain text
    print("Decrypted message with the key 2 is: %s" % decrypt2)
    decrypt1 = de_vigenere(decrypt2, key_1)
    print("The Decrypted message with the key 1 is: %s" % decrypt1)

