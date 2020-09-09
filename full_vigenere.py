import random
import pickle

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
    """
    #Alphabet list for conversion from number to character#
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
             'w', 'x', 'y', 'z']

    #Shuffle aplhabet list for matrix
    alphabet_shuffled = [random.shuffle(alphabet) for _ in range(0,26)]
    print(alphabet_shuffled)
    
    ciphertext=''
    for i in range(len(plaintext)):
        if (i%5==0) and (i!=0):
            ciphertext+='-'
        ciphernumber=(alphabet.index(plaintext[i])+alphabet.index(key[i]))%26
        #print(ciphernumber, end=', ')
        ciphertext+=alphabet[ciphernumber]
        #print(ciphertext)
    """
    
    #Alphabet list for conversion from number to character#
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
                'w', 'x', 'y', 'z']

    #print(random.sample(alphabet, len(alphabet)))
    """
    #Shuffle aplhabet list for matrix
    alphabet_shuffled = [random.sample(alphabet, len(alphabet)) for _ in range(0,26)]
    seperator=''
    for i in range(len(alphabet_shuffled)):
        alphabet_shuffled[i]=seperator.join(alphabet_shuffled[i])
    print(alphabet_shuffled)
    #seperator=''
    #alphabet_shuffled_string=seperator.join(alphabet_shuffled)
    
    with open('full_vigenere_matrix.txt', 'w') as filehandle:
        for listitem in alphabet_shuffled:
            filehandle.write('%s\n' % listitem)
    
    for i in range(len(alphabet_shuffled)):
        print(alphabet_shuffled[i])

    #Alphabet list for conversion from number to character#
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
                'w', 'x', 'y', 'z']
    """
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
        if (i%5==0) and (i!=0):
            ciphertext+='-'
        """
        ciphernumber=(alphabet.index(plaintext[i])+alphabet.index(key[i]))%26
        #print(ciphernumber, end=', ')
        ciphertext+=alphabet[ciphernumber]
        #print(ciphertext)
        """
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

def decryption(ciphertext, key):
    #Input plaintext

    #ciphertext = input("Masukkan ciphertext:")
    print("Ciphertext:", end="")
    print(ciphertext)

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
    """
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
    """
    #Alphabet list for conversion from number to character#
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
             'w', 'x', 'y', 'z']
    
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
        #alphabet_cycle=itertools.cycle(alphabet)
        #print(key[i])
        #print(alphabet.index(key[i]))
        #row=alphabet_shuffled[alphabet.index(key[i])]
        #print(row)
        #plainnumber = row.index(ciphertext[i])
        #plaintext+=alphabet[plainnumber]
        a = alphabet.index(key[i])
        for j in range(0,26):
            if (alphabet_shuffled[j][a]==ciphertext[i]):
                break
        plainnumber=j
        plaintext+=alphabet[plainnumber]
        
        
        #plainnumber=(alphabet.index(ciphertext[i])-alphabet.index(key[i]))%26


        #plaintext+=alphabet[plainnumber]
        
        #print(ciphertext)
        
    


    #row=alphabet_shuffled[alphabet.index(key[1])]
    #print(row)
    #plainnumber = row.index(ciphertext[1])
    #plaintext+=alphabet[plainnumber]


    return plaintext
"""
#Outputs the ciphertext#
print("Ciphertext:"+encryption())
"""
#Outputs the plaintext#
#print("Ciphertext:"+decryption())

"""
#Alphabet list for conversion from number to character#
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
            'w', 'x', 'y', 'z']

#print(random.sample(alphabet, len(alphabet)))
#Shuffle aplhabet list for matrix
alphabet_shuffled = [random.sample(alphabet, len(alphabet)) for _ in range(0,26)]

with open('full_vigenere_matrix.txt', 'w') as filehandle:
    for listitem in alphabet_shuffled:
        filehandle.write('%s\n' % listitem)


# define an empty list
alphabet_shuffled = []

# open file and read the content in a list
with open('full_vigenere_matrix.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentAlphabet = line[:-1]

        # add item to the list
        alphabet_shuffled.append(currentAlphabet)

for i in range(len(alphabet_shuffled)):
    print(alphabet_shuffled[i])   
"""