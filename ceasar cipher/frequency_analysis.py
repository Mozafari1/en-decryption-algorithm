from matplotlib import pyplot as plt

alfa = ' abcdefghijklmnopqrstuvwxyzøæå'

def frequency_analysis(plantText):
    
    plantText = plantText.lower()
    #we are going to use a dictionary to store the letters-frequency pari
    letter_frequency ={}
    #Initialize the dictionary 
    for letter in alfa:
        letter_frequency[letter]=0
    
    # Now we cosider the text we want to analyse
    for letter in plantText:
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

if __name__ == "__main__":
    plantText = input("Enter some text\n")
    freqencies = frequency_analysis(plantText)
    plot(freqencies)
