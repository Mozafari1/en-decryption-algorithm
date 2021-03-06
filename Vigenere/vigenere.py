alfa = ' abcdefghijklmnopqrstuvwxyz.'

# vigenere algorithm
#Mathematical formula is:  Ej (mj)  = (mj+kj) mod 26

def en_vigenere(plainText,key):
    #the text we want to encrypt
    plainText = plainText.lower()
    key = key.lower()
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
#Mathematical formula is:  Dj (mj)  = (mj-kj) mod 26
def de_vigenere(cipherText, key):
    cipherText = cipherText.lower()
    key = key.lower()
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
    encrypt = en_vigenere(plainText, 'Lemon')
    print("The encrypted message is: %s" % encrypt)
    decrypt = de_vigenere(encrypt, 'Lemon')
    print("The Decrypted message is: %s" % decrypt)


