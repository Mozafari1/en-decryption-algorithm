import string

class caesarCipher():
    def __init__(self):
        self.alphabet = []
        self.key = 3

    def fillAlphabet(self):
        for i in range(26):
            self.alphabet.append(string.ascii_uppercase[i])

    def encrypt(self, plaintext):
        cipher = ""
        for i in plaintext:
            for j in range(len(self.alphabet)):
                if i == self.alphabet[j]:
                    if j >= (len(self.alphabet) - self.key): j = j - len(self.alphabet)
                    cipher = cipher + self.alphabet[j+self.key]
                    print("- Replacing %s with %s" % (i, self.alphabet[j+self.key]))
        return cipher

cc = caesarCipher()
cc.fillAlphabet()
plaintext = input("Write something: ")
plaintext = plaintext.upper()
ciphertext = cc.encrypt(plaintext)
print("= Encrypted text: %s" % ciphertext)