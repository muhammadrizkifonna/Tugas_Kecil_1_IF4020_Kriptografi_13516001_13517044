# Hill Cipher
# By Ignatius Timothy Manullang 13517044

from textwrap import wrap

def generateMessageVector(message, n):
    messageVector = [[0] for i in range(n)] 
    for i in range(n):
        messageVector[i][0] = ord(message[i]) % 65
    return messageVector

def generateKeyMatrix(key, n): 
    keyMatrix = [[0] * n for i in range(n)] 
    k = 0
    for i in range(n): 
        for j in range(n):
            print(key[k]) 
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    return keyMatrix

def generateCipherMatrix(message, keyMatrix, messageVector, n):
    cipherMatrix = [[0] for i in range(n)] 
    for i in range(n): 
        for j in range(1): 
            cipherMatrix[i][j] = 0
            for x in range(n): 
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j]) 
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
    return cipherMatrix

def generateInverseMatrix(matrix):
    determinant = round(calculateDeterminant(matrix))
    inverseMatrix = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        inverseMatrix[i][i] = 1
    for focusDiagonal in range(len(matrix)):
        focusDiagonalScaler = 1.0 / matrix[focusDiagonal][focusDiagonal]
        for j in range(len(matrix)):
            matrix[focusDiagonal][j] *= focusDiagonalScaler
            inverseMatrix[focusDiagonal][j] *= focusDiagonalScaler
        for i in list(range(len(matrix)))[0:focusDiagonal] + list(range(len(matrix)))[focusDiagonal+1:]:
            currentRowScaler = matrix[i][focusDiagonal]
            for j in range(len(matrix)):
                matrix[i][j] = matrix[i][j] - currentRowScaler * matrix[focusDiagonal][j]
                inverseMatrix[i][j] = inverseMatrix[i][j] - currentRowScaler * inverseMatrix[focusDiagonal][j]
    for x in range(len(inverseMatrix)):
        for y in range(len(inverseMatrix[0])):
            inverseMatrix[x][y] = round(inverseMatrix[x][y]*determinant)
    for x in range(len(inverseMatrix)):
        for y in range(len(inverseMatrix[0])):
            inverseMatrix[x][y] = inverseMatrix[x][y] * (determinant % 26)
    return inverseMatrix

def generateZeroMatrix(rows, cols):
    zeroMatrix = []
    while len(zeroMatrix) < rows:
        zeroMatrix.append([])
        while len(zeroMatrix[-1]) < cols:
            zeroMatrix[-1].append(0.0)
    return zeroMatrix

def generateMatrixCopy(matrix):
    MatrixCopy = generateZeroMatrix(len(matrix), len(matrix[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            MatrixCopy[i][j] = matrix[i][j]
    return MatrixCopy

def calculateDeterminant(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    matrixCopy = generateMatrixCopy(matrix)
    for focusDiagonal in range(len(matrix)):  
        if matrixCopy[focusDiagonal][focusDiagonal] == 0:
            matrixCopy[focusDiagonal][focusDiagonal] = 1.0e-18  
        for i in range(focusDiagonal+1, len(matrix)):  
            currentRowScaler = matrixCopy[i][focusDiagonal] / matrixCopy[focusDiagonal][focusDiagonal]  
            for j in range(len(matrix)):  
                matrixCopy[i][j] = matrixCopy[i][j] - currentRowScaler * matrixCopy[focusDiagonal][j]
    product = 1.0
    for i in range(len(matrix)):
        product *= matrixCopy[i][i] 
    return product

def generateDecipherMatrix(message, keyMatrix, messageVector, n):
    decipherMatrix = [[0] for i in range(n)] 
    for i in range(n):
        for j in range(1):
            decipherMatrix[i][j] = 0
            for x in range(n): 
                decipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j]) 
            decipherMatrix[i][j] = decipherMatrix[i][j] % 26
    return decipherMatrix

def HillCipherEncryption(message, key): 
    n = 3
    keyMatrix = generateKeyMatrix(key, n) 
    messageVector = generateMessageVector(message, n)
    cipherMatrix = generateCipherMatrix(messageVector, keyMatrix, messageVector, n) 
    CipherText = [] 
    for i in range(n): 
        CipherText.append(chr(cipherMatrix[i][0] + 65)) 
    CipheredText = "".join(CipherText)
    return CipheredText

def HillCipherDecryption(message, key):
    n = len(message)
    keyMatrix = generateKeyMatrix(key, n) 
    invertedKeyMatrix = generateInverseMatrix(keyMatrix)
    decipherMessageVector = generateMessageVector(message, n)
    decipherMatrix = generateDecipherMatrix(message, invertedKeyMatrix, decipherMessageVector, n)
    DecipherText = [] 
    for i in range(n): 
        DecipherText.append(chr(round(decipherMatrix[i][0] + 65))) 
    DecipheredText = "".join(DecipherText)
    return DecipheredText 

def printWrapFiveCharacters(message):
    messageWrapFive = wrap(message,5)
    for i in messageWrapFive:
        print(i, end=' ')
    print()

def main(): 
    #3x3 Hill Cipher
    message = "ACT"
    message = wrap(message, 3)
    key = "GYBNQKURP"

    #Compare plaintext and key's length#
    if (len(key)<9):
        real_key=key
        times = 9//len(key)

        for i in range(times-1):
            key+=real_key

        sisa = 9-len(key)

        for i in range(sisa):
            key+=real_key[i]

    #If key>plaintext#
    elif (len(key)>9):
        key=key[:9]

    for messagePart in message:
        add = 0
        if len(messagePart) < 3:
            add = 3 - len(messagePart) 
            for i in range(add):
                messagePart = ''.join([messagePart, 'X']) 
        print(messagePart)
        cipherText = HillCipherEncryption(messagePart, key)
        decipherText = HillCipherDecryption(messagePart, key)
        if add > 0:
            for i in range(add):
                message = message[:-1]
        #print("Ciphertext: ", message) 

if __name__ == "__main__": 
    main() 
  