from random import seed
from random import randint
class GeneratePasswords:
    def __init__(self, passwordLength, numberPasswords, seedNumber):
        self.passwordLength = passwordLength
        self.numberPasswords = numberPasswords
        self.bestPassword = None
        self.seed = seed (seedNumber)

    def generateRandomPassword(self):
        string = ""
        for i in range(self.passwordLength):
            asciiValue = randint(97, 123)
            randomCharacter = chr(asciiValue)
            string = string + randomCharacter
        return string

obj = GeneratePasswords(5, 2, 100)
print(obj.generateRandomPassword())
print(obj.generateRandomPassword())
