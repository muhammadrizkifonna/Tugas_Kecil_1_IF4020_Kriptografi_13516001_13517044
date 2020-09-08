from textwrap import wrap

def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) - len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key)) 

def encryptByteExtendedVignere(bytePlainText, key):
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

def decryptByteExtendedVignere(byteCipherText, key):
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

def encryptTextExtendedVignere(plaintext, key):
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

def decryptTextExtendedVignere(cipherText, key):
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
    keyword = "VignereExample"
    key = generateKey(listOfBytes, keyword) 
    cipherText = encryptByteExtendedVignere(listOfBytes, key)
    g = open("vignereExtendedEncrypted.mp4", "wb+")
    for index in range(len(cipherText)):
        g.write(cipherText[index])
    g.close()
    decryptedText = decryptByteExtendedVignere(cipherText, key)
    h = open("vignereExtendedDecrypted.mp4", "wb+")
    for index in range(len(decryptedText)):
        h.write(decryptedText[index])
    h.close()
