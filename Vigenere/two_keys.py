#alfa = ' abcdefghijklmnopqrstuvwxyz.'
alfa  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# vigenere algorithm
#Mathematical formula is:  Ci (mi)  =(mi+ki) mod 28
# mod is  28 with space and .

def en_vigenere_key_1(plainText,key_1):
    #the text we want to encrypt
    plainText = plainText.upper()
    key_1 = key_1.upper()


    cipherText = ''
    # repesenting the key index as far as key is concerned
    indexKey = 0
    # now we are going to concider all characters in plainText
    for char in plainText:
        #The number of shifts is equal to the index of the char in the alfabet and plus index of the char in the private key
        index = (alfa.find(char) + (alfa.find(key_1[indexKey]))) % len (alfa) # this is the mathematical operation
        # adding the encrypted char to the cipherText
        cipherText = cipherText +alfa[index]
        # Now I'm concider the next letter and need to increment the key index 
        indexKey = indexKey + 1

        # we need to start agin when we have concidered the last letter of key
        if indexKey == len(key_1):
            indexKey =0
    return cipherText

# Now I'm going to decrypt and using the following formula
# The number og shifts is equal to the index  of the char in the alfabet  and minus index of the char in the key
#Mathematical formula is:  Di (mi)  = (mi-ki) mod 28
def de_vigenere_key_1(cipherText, key_1):
    cipherText = cipherText.upper()
    key_1 = key_1.upper()
    plainText = ''
    indexKey = 0

    for char in cipherText:
        index = (alfa.find(char) - (alfa.find(key_1[indexKey]))) % len(alfa)
        plainText  = plainText + alfa[index]

        indexKey = indexKey +1
        if indexKey ==len(key_1):
            indexKey =0

    return plainText


# Encrypting agin with with the second key = WATERMELON

def en_vigenere_key_2(encrypted_text_with_key_1,key_2):
    #the text we want to encrypt
    encrypted_text_with_key_1 = encrypted_text_with_key_1.upper()
    key_2 = key_2.upper()


    cipherText = ''
    # repesenting the key index as far as key is concerned
    indexKey = 0
    # now we are going to concider all characters in plainText
    for char in encrypted_text_with_key_1:
        #The number of shifts is equal to the index of the char in the alfabet and plus index of the char in the private key
        index = (alfa.find(char) + (alfa.find(key_2[indexKey]))) % len (alfa) # this is the mathematical operation
        # adding the encrypted char to the cipherText
        cipherText = cipherText +alfa[index]
        # Now I'm concider the next letter and need to increment the key index 
        indexKey = indexKey + 1

        # we need to start agin when we have concidered the last letter of key
        if indexKey == len(key_2):
            indexKey =0
    return cipherText

# Now I'm going to decrypt and using the following formula
# The number og shifts is equal to the index  of the char in the alfabet  and minus index of the char in the key
#Mathematical formula is:  Di (mi)  = (mi-ki) mod 28
def de_vigenere_key_2(cipherText_2, key_2):
    cipherText_2 = cipherText_2.upper()
    key_2 = key_2.upper()
    plainText = ''
    indexKey = 0

    for char in cipherText_2:
        index = (alfa.find(char) - (alfa.find(key_2[indexKey]))) % len(alfa)
        plainText  = plainText + alfa[index]

        indexKey = indexKey +1
        if indexKey ==len(key_2):
            indexKey =0

    return plainText


if __name__ =="__main__":
    plainText = input("Enter some text to encrypt\n")
    encrypt = en_vigenere_key_1(plainText, 'Green')
    print("The encrypted message with the first is: %s" % encrypt)
    encrypt_key_2 = en_vigenere_key_2(encrypt,'Watermelon')
    print("Ecrypted text with the second key is: %s" %encrypt_key_2)



    decrypt_key_2 = de_vigenere_key_2(encrypt_key_2,'Green')
    print("Decrypted text with the second key  is: %s" %decrypt_key_2)
    decrypt = de_vigenere_key_1(decrypt_key_2, 'ABC')
    print("The Decrypted message with the first key is: %s" % decrypt)

