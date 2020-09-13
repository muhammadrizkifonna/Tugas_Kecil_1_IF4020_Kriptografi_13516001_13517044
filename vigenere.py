from textwrap import wrap

def write_to_file(path, ciphertext):
    file1 = open(path,"w") 
    file1.write(ciphertext) 
    file1.close()

def wrapFiveCharacters(message):
    messageWrapFive = wrap(message,5)
    return ' '.join(messageWrapFive)

def encryption(plaintext, key, from_file, path, write_to_file):
    #Input plaintext

    #plaintext = input("Masukkan plaintext:")

    #Input key from user#
    #key = input("Masukkan key:")
    if (from_file):
        file1 = open(path,"r") 
        plaintext_list = file1.readlines()
        seperator=''
        file1.close()
        plaintext=seperator.join(plaintext_list)

    #Convert into lowercase#
    plaintext=plaintext.lower()
    key=key.lower()

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
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
             'w', 'x', 'y', 'z']
    ciphertext=''
    for i in range(len(plaintext)):
        # if (i%5==0) and (i!=0):
        #     ciphertext+='-'
        ciphernumber=(alphabet.index(plaintext[i])+alphabet.index(key[i]))%26
        #print(ciphernumber, end=', ')
        ciphertext+=alphabet[ciphernumber]
        #print(ciphertext)
    return ciphertext


def decryption(ciphertext, key, from_file = False, path = ''):
    #Input ciphertext
    if (from_file):
        file1 = open(path,"r") 
        ciphertext_list = file1.readlines()
        seperator=''
        file1.close()
        ciphertext=seperator.join(ciphertext_list)

    #ciphertext = input("Masukkan ciphertext:")

    print(ciphertext[0])

    #Input key from user#
    #key = input("Masukkan key:")

    #print(key)

    #Convert into lowercase#
    ciphertext=ciphertext.lower()
    key=key.lower()

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
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
             'w', 'x', 'y', 'z']

    
    plaintext=''
    for i in range(len(ciphertext)):
        #alphabet_cycle=itertools.cycle(alphabet)
        #print(key[i])
        plainnumber=(alphabet.index(ciphertext[i])-alphabet.index(key[i]))%26


        plaintext+=alphabet[plainnumber]
        #print(ciphertext)
    return plaintext

