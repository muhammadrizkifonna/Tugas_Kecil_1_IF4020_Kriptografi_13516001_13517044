from textwrap import wrap

alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetList = list(alphabet)

# text = input("Input text: ")
# text = 'iwzqz jx kl kxvz'
# steckerbrettDictionary = {' ': ' '}
# pairsInSteckerBrett = input("Input the number of pairs in steckerbrett: ")
# for i in range(int(pairsInSteckerBrett)):
#     print("Pair #" + str(i+1))
#     firstSteckerbrettAlphabet = input("Input the first alphabet in pair: ")
#     secondSteckerbrettAlphabet = input("Input the second alphabet in pair: ")
#     steckerbrettDictionary[firstSteckerbrettAlphabet.upper()] = secondSteckerbrettAlphabet.upper()
# print("Input alpha, beta and gamma rotors")
# alphaRotor = int(input("Alpha Rotor = "))
# betaRotor = int(input("Beta Rotor = "))
# gammaRotor = int(input("Gamma Rotor = "))
# for letter in list(steckerbrettDictionary.keys()):
#     if letter in alphabetList:
#         alphabetList.remove(letter)
#         alphabetList.remove(steckerbrettDictionary[letter])
#         steckerbrettDictionary.update({steckerbrettDictionary[letter]:letter})
# reflector = [letter for letter in reversed(alphabetList)]

def permutate(rotor, alphabetList):
    newAlphabet = ''.join(alphabetList)
    newAlphabetList = list(newAlphabet)
    for i in range(rotor):
        newAlphabetList.insert(0, newAlphabetList[-1])
        newAlphabetList.pop(-1)
    return newAlphabetList

def inversePermutation(rotor, alphabetList):
    newAlphabet = ''.join(alphabetList)
    newAlphabetList = list(newAlphabet)
    for i in range(rotor):
        newAlphabetList.append(newAlphabetList[0])
        newAlphabetList.pop(0)
    return newAlphabetList

def turnRotors(alphaRotor, betaRotor, gammaRotor):
    alphaRotor += 1
    if alphaRotor % len(alphabetList) == 0:
        betaRotor += 1
        alphaRotor = 0
    if betaRotor % len(alphabetList) == 0 and alphaRotor % len(alphabetList) != 0 and betaRotor >= (len(alphabetList) - 1):
        gammaRotor += 1
        betaRotor = 1
    return alphaRotor, betaRotor, gammaRotor

def encryptDecrypt(text, steckerbrettDictionary, alphaRotor, betaRotor, gammaRotor, alphabetList):
    resultText = []
    upperCaseText = text.upper()
    upperCaseText.split()
    for letter in upperCaseText:
        if letter in steckerbrettDictionary:
            resultText.append(steckerbrettDictionary[letter])
            alphaRotor, betaRotor, gammaRotor = turnRotors(alphaRotor, betaRotor, gammaRotor)
        else:
            tempLetter = permutate((alphaRotor), alphabetList)[alphabetList.index(letter)]
            tempLetter = permutate((betaRotor), alphabetList)[alphabetList.index(tempLetter)]
            tempLetter = permutate((gammaRotor), alphabetList)[alphabetList.index(tempLetter)]
            tempLetter = reflector[alphabetList.index(tempLetter)]
            tempLetter = inversePermutation((gammaRotor), alphabetList)[alphabetList.index(tempLetter)]
            tempLetter = inversePermutation((betaRotor), alphabetList)[alphabetList.index(tempLetter)]
            tempLetter = inversePermutation((alphaRotor), alphabetList)[alphabetList.index(tempLetter)]
            resultText.append(tempLetter)
            alphaRotor, betaRotor, gammaRotor = turnRotors(alphaRotor, betaRotor, gammaRotor)
    return ''.join(resultText)

def printWrapFiveCharacters(message):
    messageWrapFive = wrap(message,5)
    for i in messageWrapFive:
        print(i, end=' ')
    print()

#print(encryptDecrypt(text, steckerbrettDictionary, alphaRotor, betaRotor, gammaRotor, alphabetList))