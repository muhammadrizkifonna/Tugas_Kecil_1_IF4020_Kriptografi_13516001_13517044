#using vigenere + Myszkowski transposition cipher

#myszkowski
import math 

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
    message = message.upper()
    key = key.upper()
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
    key = key.upper()
    decryptedMessage = "" 
    keyIndex = 0
    messageIndex = 0
    messageLength = float(len(message)) 
    messageList = list(message)
    column = len(key) 
    row = int(math.ceil(messageLength / column)) 
    keyList = generateKeyList(key)
    key = ''.join(keyList)
    sortedKeyList = sorted(keyList)
    decrytedMessageList = [] 
    for _ in range(row): 
        decrytedMessageList += [[None] * column] 
    for _ in range(column): 
        curr_idx = key.index(sortedKeyList[keyIndex]) 
        for j in range(row): 
            decrytedMessageList[j][curr_idx] = messageList[messageIndex] 
            messageIndex += 1
        keyIndex += 1
    decryptedMessage = ''.join(sum(decrytedMessageList, [])) 
    additionalTemp = decryptedMessage.count('*') 
    if additionalTemp > 0: 
        return decryptedMessage[: -additionalTemp] 
    return decryptedMessage 
  
#Driver Code 
# msg = "Mantap Jiwa"
# key = "AcakAcak"
  
# cipher = myszkowskiTranspositionEncrypt(msg, key) 
# print("Encrypted Message: {}". 
#                format(cipher)) 
  
# print("Decryped Message: {}". 
#        format(myszkowskiTranspositionDecrypt(cipher, key)))
