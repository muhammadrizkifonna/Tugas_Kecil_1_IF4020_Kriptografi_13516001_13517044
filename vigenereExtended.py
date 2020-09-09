from textwrap import wrap

def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) - len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key)) 

def encryptByteExtendedVigenere(bytePlainText, key):
    result = [[0] for i in range(len(bytePlainText))]
    key = key.strip().upper()
    keyIndex = 0
    keylength = len(key)
    for i in range(len(bytePlainText)):
        keyIndex = keyIndex % keylength
        shift = ord(key[keyIndex]) - 65
        result[i] = bytes([(ord(bytePlainText[i]) + shift) % 256])
        keyIndex+=1
    return result

def decryptByteExtendedVigenere(byteCipherText, key):
    result = [[0] for i in range(len(byteCipherText))]
    key = key.strip().upper()
    keyIndex = 0
    keylength = len(key)
    for i in range(len(byteCipherText)):
        keyIndex = keyIndex % keylength
        shift = ord(key[keyIndex]) - 65
        result[i] = bytes([(ord(byteCipherText[i]) + 256 - shift) % 256])
        keyIndex+=1
    return result

def encryptTextExtendedVigenere(plaintext, key):
    result = [[0] for i in range(len(plaintext))]
    key = key.strip().upper()
    keyIndex = 0
    keylength = len(key)
    for i in range(len(plaintext)):
        keyIndex = keyIndex % keylength
        shift = ord(key[keyIndex]) - 65
        result[i] = [(ord(plaintext[i]) + shift) % 256]
        keyIndex+=1
    return result

def decryptTextExtendedVigenere(cipherText, key):
    result = [[0] for i in range(len(cipherText))]
    key = key.strip().upper()
    keyIndex = 0
    keylength = len(key)
    for i in range(len(cipherText)):
        keyIndex = keyIndex % keylength
        shift = ord(key[keyIndex]) - 65
        result[i] = [(ord(cipherText[i]) + 256 - shift) % 256]
        keyIndex+=1
    return result

def printWrapFiveCharacters(message):
    messageWrapFive = wrap(message,5)
    for i in messageWrapFive:
        print(i, end=' ')
    print()

if __name__ == "__main__": 
    listOfBytes = []
    with open("videoplayback.mp4", "rb") as f:
        while (byte := f.read(1)):
            listOfBytes.append(byte)
    f.close()
    keyword = "VigenereExample"
    key = generateKey(listOfBytes, keyword) 
    cipherText = encryptByteExtendedVigenere(listOfBytes, key)
    g = open("VigenereExtendedEncrypted.mp4", "wb+")
    for index in range(len(cipherText)):
        g.write(cipherText[index])
    g.close()
    decryptedText = decryptByteExtendedVigenere(cipherText, key)
    h = open("VigenereExtendedDecrypted.mp4", "wb+")
    for index in range(len(decryptedText)):
        h.write(decryptedText[index])
    h.close()
