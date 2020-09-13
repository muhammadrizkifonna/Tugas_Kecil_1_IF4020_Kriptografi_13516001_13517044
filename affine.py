#affine

from textwrap import wrap

def write_to_file(path, ciphertext):
    file1 = open(path,"w") 
    file1.write(ciphertext) 
    file1.close()

def wrapFiveCharacters(message):
    messageWrapFive = wrap(message,5)
    return ' '.join(messageWrapFive)

def toUpperCase(text):
    return "".join(filter(str.isupper, text.upper()))

def extendedGCDEuclideanAlgorithm(a, b):
    if a == 0 :   
        return b, 0, 1
    greatestCommonDenominator, x1, y1 = extendedGCDEuclideanAlgorithm(b%a, a)
    x = y1 - (b//a) * x1  
    y = x1
    return greatestCommonDenominator, x, y

def getModularInverse(a, m):
    greatestCommonDenominator, x, y = extendedGCDEuclideanAlgorithm(a, m) 
    if greatestCommonDenominator != 1: 
        return None  
    else: 
        return x % m

def encryption(plaintext, key_m, key_b, from_file, path, write_to_file):
    if (from_file):
        file1 = open(path,"r") 
        plaintext_list = file1.readlines()
        seperator=''
        file1.close()
        plaintext=seperator.join(plaintext_list)

    plaintext=toUpperCase(plaintext)

    #Remove comma
    plaintext = plaintext.replace(',', '')
    #key = key.replace(',', '')
    #print(plaintext)

    #Remove space
    plaintext = plaintext.replace(' ', '')
    #key = key.replace(' ', '')

    #Remove punctuation
    # Define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Remove punctuation from plaintext
    no_punct = ""
    for char in plaintext:
        if char not in punctuations:
            no_punct = no_punct + char
    plaintext=no_punct

    #Alphabet list for conversion from number to character#
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = list(alphabet)
    ciphertext=''
    for i in range(len(plaintext)):
        # if (i%5==0) and (i!=0):
        #     ciphertext+='-'
        ciphernumber=(int(key_m)*alphabet.index(plaintext[i])+int(key_b))%26
        #ciphernumber=(alphabet.index(plaintext[i])+alphabet.index(key[i]))%26
        #print(ciphernumber, end=', ')
        ciphertext+=alphabet[ciphernumber]
        #print(ciphertext)
    return ciphertext


def decryption(ciphertext, key_m, key_b, from_file = False, path = '', write_to_file = False):
    #Input plaintext
    if (from_file):
        file1 = open(path,"r") 
        ciphertext_list = file1.readlines()
        seperator=''
        file1.close()
        ciphertext=seperator.join(ciphertext_list)

    ciphertext=toUpperCase(ciphertext)

    #Remove comma
    ciphertext = ciphertext.replace(',', '')
    #key = key.replace(',', '')

    #Remove space
    ciphertext = ciphertext.replace(' ', '')
    #key = key.replace(' ', '')

    #Remove punctuation
    # Define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Remove punctuation from ciphertext
    no_punct = ""
    for char in ciphertext:
        if char not in punctuations:
            no_punct = no_punct + char
    ciphertext=no_punct
    
    #Alphabet list for conversion from number to character#
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = list(alphabet)
    key_m=int(key_m)
    key_b=int(key_b)
    #Find the inverse of key_m

    key_m_inverse = getModularInverse(key_m, 26)

    plaintext=''
    for i in range(len(ciphertext)):
        plainnumber=(key_m_inverse*(alphabet.index(ciphertext[i])-key_b))%26

        plaintext+=alphabet[plainnumber]
        print(ciphertext)
    return plaintext

