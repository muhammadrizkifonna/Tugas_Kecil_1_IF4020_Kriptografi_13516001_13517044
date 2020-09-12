from textwrap import wrap

def generateUniqueAlphabetList(seq):
    seen = {}
    return [seen.setdefault(x, x) for x in seq if x not in seen]
 
def partition(seq, n):
    return [seq[i : i + n] for i in range(0, len(seq), n)]

def toUpperCase(text):
    return "".join(filter(str.isupper, text.upper()))

def splitMessageToDigraphs(message):
	#Change it to Array. Because I want used insert() method
	messageList=[]
	for e in message:
		messageList.append(e)
	for i in range(len(messageList)):
		if " " in messageList:
			messageList.remove(" ")
	i=0
	for e in range(len(messageList)//2):
		if messageList[i]==messageList[i+1]:
			messageList.insert(i+1,'X')
		i=i+2
	if len(messageList)%2==1:
		messageList.append("X")
	i=0
	digraphList=[]
	for x in range(1,len(messageList)//2+1):
		digraphList.append(messageList[i:i+2])
		i=i+2
	return digraphList

def formatMessage(message, replaceFrom, replaceTo):
        message = toUpperCase(message)
        formattedMessage = message.replace(replaceFrom, replaceTo)
        return formattedMessage

def generateEncryptionDictionary(matrix):
    encryptionDictionary = {}
    for row in matrix:
        for i in range(5):
            for j in range(5):
                if i != j:
                    encryptionDictionary[row[i] + row[j]] = row[(i + 1) % 5] + row[(j + 1) % 5]
    for c in zip(*matrix):
        for i in range(5):
            for j in range(5):
                if i != j:
                    encryptionDictionary[c[i] + c[j]] = c[(i + 1) % 5] + c[(j + 1) % 5]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    if i != k and j != l:
                        encryptionDictionary[matrix[i][j] + matrix[k][l]] = matrix[i][l] + matrix[k][j]
    return encryptionDictionary
    
def playfairEncrypt(message, key, replaceFrom = 'J', replaceTo = None):
    if replaceTo is None:
        replaceTo = 'I' if replaceFrom == 'J' else ''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digraphList = splitMessageToDigraphs(formatMessage(message, replaceFrom, replaceTo))
    uniqueFormattedMatrix = partition(generateUniqueAlphabetList(formatMessage(key + alphabet, replaceFrom, replaceTo)), 5)
    encryptionDictionary = generateEncryptionDictionary(uniqueFormattedMatrix)
    cipheredMessage = " ".join(encryptionDictionary[a + b] for a, b in digraphList)
    return cipheredMessage
    #return " ".join(enc[a + (b if b else 'X')] for a, b in lst)

def playfairDecrypt(message, key, replaceFrom = 'J', replaceTo = 'I'):
    if replaceTo is None:
        replaceTo = 'I' if replaceFrom == 'J' else ''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lst = splitMessageToDigraphs(formatMessage(message, replaceFrom, replaceTo))
    uniqueFormattedMatrix = partition(generateUniqueAlphabetList(formatMessage(key + alphabet, replaceFrom, replaceTo)), 5)
    encryptionDictionary = generateEncryptionDictionary(uniqueFormattedMatrix)
    decryptionDictionary = dict((value, key) for key, value in encryptionDictionary.items())
    decipheredMessage = " ".join(decryptionDictionary[p] for p in partition(formatMessage(message, replaceFrom, replaceTo), 2))
    return decipheredMessage

def wrapFiveCharacters(message):
    messageWrapFive = wrap(message,5)
    return ' '.join(messageWrapFive)
 
def write_to_file(path, text):
    file1 = open(path,"w+") 
    file1.write(text) 
    file1.close()

def readTextFromFile(path):
    file1 = open(path, "r")
    data = file1.read()
    file1.close()
    return data

def main():
    # orig = "Hi.de th.e go.ld in th.e tr.ee.stu.mp!"
    key = "Playfair example"
    # encrypted = toUpperCase(playfairEncrypt(orig, key))
    # print(encrypted)
    #printWrapFiveCharacters(encrypted)
    enc = "BMODZBXDNABEKUDMUIXMMOUVIF"
    decrypted = toUpperCase(playfairDecrypt(enc, key))
    print(decrypted)
    #printWrapFiveCharacters(decrypted)

if __name__ == "__main__":
    main()