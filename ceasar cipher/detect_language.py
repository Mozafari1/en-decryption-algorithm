
alfa = ' abcdefghijklmnopqrstuvwxyz'

# storing the englsih words in al list
eng_words = []

# loading the english words
def get_data ():
    #First we need to load all the english words from our .txt file
    f = open("english3.txt","r")
    #Now we need to initialze the english words list with the words present in ht efile
    #WE need also to split the line 
    for word in f.read().split('\n'):
        eng_words.append(word)
    f.close()

# Now we counting the number og english words in a given text
def count_words(text):
    text = text.lower()
    #tranforming text into a list 
    words = text.split(' ')
    # matches count the number of english words in text
    matches = 0
    
    #Checking the words in text is english or not
    for word in words:
        if word in eng_words:
            matches = matches + 1
    return matches

#deciding the given is english or not
def is_text_english(text):
    #number of english words in the given text
    matches = count_words(text)
    #defining the classification algorithm
    if(float(matches)/len(text.split('\n')))*100>=75:
        return True
    return False

# using brute force to cracking the caesar encryption algorithm
def crack_caesar(cipher_text):
    # we are checking all the possiblity of key values
    for key in range(len(alfa)):
        plainText = ''
    # decrypting
        for i in cipher_text:
            index = alfa.find(i)
            index = (index-key)%len(alfa)
            plainText = plainText + alfa[index]

        # printing the acutal decrypted string with the given key
        if is_text_english(plainText):
            print("The key is used to encrypt this text is: [%s] and the message is: [%s]"% (key, plainText))
        #print("When key is: %s and the result is: %s" %(key, plainText))

if __name__ == "__main__":
    get_data()
    engcrypted = input("Enter the text you want to decrypt\n")
    crack_caesar(engcrypted)
