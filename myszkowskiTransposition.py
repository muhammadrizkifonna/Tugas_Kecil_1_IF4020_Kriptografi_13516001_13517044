#SuperEncryption using vigenere.py + Myszkowski transposition cipher (this file)

#myszkowski
import math 
from textwrap import wrap

def write_to_file(path, ciphertext):
    file1 = open(path,"w") 
    file1.write(ciphertext) 
    file1.close()

def readTextFromFile(path):
    file1 = open(path, "r")
    data = file1.read()
    file1.close()
    return data

def wrapFiveCharacters(message):
    messageWrapFive = wrap(message,5)
    return ' '.join(messageWrapFive)

def toUpperCase(text):
    return "".join(filter(str.isupper, text.upper()))

def generateKeyList(key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keyList = []
    duplicateFound = True
    for i in key:
        duplicateFound = True
        while duplicateFound:
            if i in keyList:
                i = alphabet[(alphabet.index(i) + 1) % 26]
            else:
                duplicateFound = False
        keyList.append(i)
    return keyList
  
def myszkowskiTranspositionEncrypt(message, key): 
    message = toUpperCase(message)
    key = toUpperCase(key)
    encryptedMessage = "" 
    keyIndex = 0
    messageLength = float(len(message)) 
    messageList = list(message) 
    keyList = generateKeyList(key)
    key = ''.join(keyList)
    sortedKeyList = sorted(keyList)
    column = len(key) 
    row = int(math.ceil(messageLength / column)) 
    fill_null = int((row * column) - messageLength) 
    messageList.extend('*' * fill_null) 
    matrix = [messageList[i: i + column]  
              for i in range(0, len(messageList), column)] 
    for _ in range(column): 
        curr_idx = key.index(sortedKeyList[keyIndex]) 
        encryptedMessage += ''.join([row[curr_idx] for row in matrix]) 
        keyIndex += 1
    return encryptedMessage 
  
def myszkowskiTranspositionDecrypt(message, key): 
    message = message.upper()
    key = toUpperCase(key)
    decryptedMessage = "" 
    keyIndex = 0
    messageIndex = 0
    messageLength = float(len(message)) 
    messageList = list(message)
    column = len(key) 
    row = int(math.ceil(messageLength / column)) 
    keyList = generateKeyList(key)
    print("Keylist = ", keyList)
    key = ''.join(keyList)
    sortedKeyList = sorted(keyList)
    print("Sorted Keylist = ", sortedKeyList)
    decryptedMessageList = [] 
    for _ in range(row): 
        decryptedMessageList += [[''] * column] 
    print(range(column))
    for _ in range(column): 
        curr_idx = key.index(sortedKeyList[keyIndex]) 
        print("messageListLength = ", len(messageList))
        print(range(row))
        for j in range(row): 
            print("j = ", j)
            print("curr_idx = ", curr_idx)
            print("messageIndex = ", messageIndex)
            decryptedMessageList[j][curr_idx] = messageList[messageIndex] 
            messageIndex += 1
        keyIndex += 1
    print("decryptedMessageList = \n", decryptedMessageList)
    decryptedMessage = ''.join(sum(decryptedMessageList, [])) 
    additionalTemp = decryptedMessage.count('*') 
    if additionalTemp > 0: 
        return decryptedMessage[: -additionalTemp] 
    return decryptedMessage 
# print(myszkowskiTranspositionEncrypt("GeeksForGeeks","HACK"))
# print(myszkowskiTranspositionDecrypt(myszkowskiTranspositionEncrypt("GeeksForGeeks","HACK"), "HACK"))