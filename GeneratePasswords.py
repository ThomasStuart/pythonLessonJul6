from random import seed
from random import randint
from math   import inf


class GeneratePasswords:
    def __init__(self, passwordLength, numberPasswords, seedNumber):
        self.passwordLength           = passwordLength
        self.numberPasswords          = numberPasswords
        self.passwordList             = []
        self.bestPasswordScorePair    = None
        self.seed                     = seed (seedNumber)

    def generateRandomPassword(self):
        string = ""  # creat an empty string
        # start a for loop from 0 to whatever the user inputted password length wise
        for i in range(self.passwordLength):
            asciiValue = randint(33, 126)     # generating a random number from 97 to 122
            randomCharacter = chr(asciiValue) # mapping the numeric value to an ascii value
            string = string + randomCharacter # adding the newly generated randomCharacter to the end our variable string
        #returning that string
        return string

    # deals with the 'numberPasswords' property
    def generateListPasswords(self):
        # create an empty list to hold a certain amount of passwords
        passwordList = []
        # start a for loop from 0 to 'self.numberPasswords'
        for i in range(0, self.numberPasswords):
            # create new password variable called newPassword by calling the helper method generateRandomPassword
            newPassword = self.generateRandomPassword()
            # add that variable newPassword to the list
            passwordList.append(newPassword)
        # return the list
        self.passwordList = passwordList
        return passwordList


    def ratePassword(self, passwod):
        score = 0

        for i in range(0 , len( passwod) ) :
            currentCharacter = passwod[i]
            asciiDecValue    = ord(currentCharacter)

            # range[97,122]
            if   asciiDecValue >= 97 and asciiDecValue <= 122:
                score = score + 1

            # range[48,57]
            elif asciiDecValue >= 48 and asciiDecValue <= 57 :
                score = score + 2

            else:
                score = score + 3

        return score

    # Assumes that the list of passwords has been generated
    def getBestPassword(self):
        # pseudo-code
        # create an empty list called pairs, that stores the password with the score
        pairs = []

        # List: passwordList
        sizeOfList =  len( self.passwordList)
        # for loop: to give scores to the passwords
        for i in range( 0, sizeOfList ):
            currentPassword = self.passwordList[i]
            currentScore    = self.ratePassword(currentPassword)
            # add this to the list called pairs,  as a {currentPassword, currentScore}
            currentPair     = (currentPassword, currentScore)
            pairs.append(currentPair)

        # create a variable called maxScore and set it equal to -inf
        maxScore    = -inf
        maxPassword = ''

        # for loop: finding the max
        for i in range(0, len(pairs)):
            currentPassword = pairs[i][0]
            currentScore    = pairs[i][1]

            if currentScore > maxScore:
                maxScore    =  currentScore
                maxPassword = currentPassword

        self.bestPasswordScorePair = (maxPassword, maxScore)
        return  self.bestPasswordScorePair



obj1 = GeneratePasswords(5, 3, 100)
print('object 1:')
print( obj1.generateListPasswords() )
print( obj1.getBestPassword() )

print()
print()
print('object 2:')
obj2 = GeneratePasswords(7, 10, 500)
print( obj2.generateListPasswords() )
print( obj2.getBestPassword() )
