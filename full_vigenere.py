#full vigenere cipher

import random
import pickle
from textwrap import wrap

def write_to_file(path, ciphertext):
    file1 = open(path,"w") 
    file1.write(ciphertext) 
    file1.close()

def wrapFiveCharacters(message):
    messageWrapFive = wrap(message,5)
    return ' '.join(messageWrapFive)

def encryption(plaintext, key, from_file, path, write_to_file):
    if (from_file):
        file1 = open(path,"r") 
        plaintext_list = file1.readlines()
        seperator=''
        file1.close()
        plaintext=seperator.join(plaintext_list)

    #Convert into lowercase#
    plaintext= toUpperCase(plaintext)
    key=toUpperCase(key)

    #Remove comma
    plaintext = plaintext.replace(',', '')
    key = key.replace(',', '')
    #print(plaintext)

    #Remove space
    plaintext = plaintext.replace(' ', '')
    key = key.replace(' ', '')

    #Remove punctuation
    # Define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Remove punctuation from plaintext
    no_punct = ""
    for char in plaintext:
        if char not in punctuations:
            no_punct = no_punct + char
    plaintext=no_punct

    # Remove punctuation from key
    no_punct = ""
    for char in key:
        if char not in punctuations:
            no_punct = no_punct + char
    key=no_punct

    #Compare plaintext and key's length#
    if (len(key)<len(plaintext)):
        real_key=key
        times = len(plaintext)//len(key)

        for i in range(times-1):
            key+=real_key

        sisa = len(plaintext)-len(key)

        for i in range(sisa):
            key+=real_key[i]

    #If key>plaintext#
    elif (len(key)>len(plaintext)):
        key=key[:len(plaintext)]

    print(key)
    
    #Alphabet list for conversion from number to character#
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = list(alphabet)

    # define an empty list
    alphabet_shuffled = []

    # open file and read the content in a list
    with open('full_vigenere_matrix.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentAlphabet = line[:-1]

            # add item to the list
            alphabet_shuffled.append(currentAlphabet)

    print(alphabet_shuffled[0][0])
    ciphertext=''
    for i in range(len(plaintext)):
        ciphernumber_x=alphabet.index(plaintext[i])
        ciphernumber_y=alphabet.index(key[i])
        print(ciphernumber_x)
        print(ciphernumber_y)
        ciphertext+=alphabet_shuffled[ciphernumber_x][ciphernumber_y]
        print(ciphertext)

    return ciphertext
    
def write_to_file(path, ciphertext):
    file1 = open(path,"w") 
    file1.write(ciphertext) 
    file1.close()

def toUpperCase(text):
    return "".join(filter(str.isupper, text.upper()))

def decryption(ciphertext, key, from_file = False, path = ''):
    #Input ciphertext
    if (from_file):
        file1 = open(path,"r") 
        ciphertext_list = file1.readlines()
        seperator=''
        file1.close()
        ciphertext=seperator.join(ciphertext_list)

    #ciphertext = input("Masukkan ciphertext:")
    print("Ciphertext:", end="")
    print(ciphertext)

    #Input key from user#
    #key = input("Masukkan key:")

    #print(key)

    #Convert into lowercase#
    ciphertext=toUpperCase(ciphertext)
    key=toUpperCase(key)

    #Remove comma
    ciphertext = ciphertext.replace(',', '')
    key = key.replace(',', '')

    #Remove space
    ciphertext = ciphertext.replace(' ', '')
    key = key.replace(' ', '')

    #Remove punctuation
    # Define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Remove punctuation from ciphertext
    no_punct = ""
    for char in ciphertext:
        if char not in punctuations:
            no_punct = no_punct + char
    ciphertext=no_punct

    # Remove punctuation from key
    no_punct = ""
    for char in key:
        if char not in punctuations:
            no_punct = no_punct + char
    key=no_punct



    #Compare plaintext and key's length#
    if (len(key)<len(ciphertext)):
        real_key=key
        times = len(ciphertext)//len(key)
        print(len(ciphertext))

        for i in range(times-1):
            key+=real_key

        sisa = len(ciphertext)-len(key)

        for i in range(sisa):
            key+=real_key[i]
    

    #If key>plaintext#
    elif (len(key)>len(ciphertext)):
        key=key[:len(ciphertext)]

    print(key)

    #Alphabet list for conversion from number to character#
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = list(alphabet)
    
    # define an empty list
    alphabet_shuffled = []

    # open file and read the content in a list
    with open('full_vigenere_matrix.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentAlphabet = line[:-1]

            # add item to the list
            alphabet_shuffled.append(currentAlphabet)

    """
    f = open("full_vigenere_matrix.txt", "r")
    f1=f.readlines()
    for x in f1:
        alphabet_shuffled.append(x)
    """

    plaintext=''
    
    for i in range(len(ciphertext)):
        a = alphabet.index(key[i])
        for j in range(0,26):
            if (alphabet_shuffled[j][a]==ciphertext[i]):
                break
        plainnumber=j
        plaintext+=alphabet[plainnumber]
        


    return plaintext
