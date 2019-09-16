import matplotlib.pylab as plt

alfa = ' abcdefghijklmnopqrstuvwxyzøæå'

def frequency_analysis(cipherText):
    
    cipherText = cipherText.lower()
    #we are going to use a dictionary to store the letters-frequency pari
    letter_frequency ={}
    #Initialize the dictionary 
    for letter in alfa:
        letter_frequency[letter]=0
    
    # Now we cosider the text we want to analyse
    for letter in cipherText:
        # we incrementing the occurence of the given letter
        if (letter in alfa):
            letter_frequency[letter] +=1
    return letter_frequency

# ploting the histogram of the letter- frequency paris
def plot(letter_frequency):
    centers = range (len(alfa))
    plt.bar(centers, letter_frequency.values(), align='center', tick_label = letter_frequency.keys())
    plt.xlim([0,len(alfa)-1])
   
    plt.show()

def cracking_ceasar(cipherText):
    letter_frequency = frequency_analysis(cipherText)
    print(letter_frequency)
    plot(letter_frequency)

if __name__ == "__main__":
    cipherText = input("Enter some text\n")
    cracking_ceasar(cipherText)
    
    #freqencies = frequency_analysis(cipherText)
    #plot(freqencies)
