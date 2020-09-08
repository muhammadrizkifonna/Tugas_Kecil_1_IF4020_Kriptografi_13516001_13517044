def encryption(plaintext, key):
    #Input plaintext

    #plaintext = input("Masukkan plaintext:")

    #Input key from user#
    #key = input("Masukkan key:")

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
        ciphernumber=(alphabet.index(plaintext[i])+alphabet.index(key[i]))%26
        #print(ciphernumber, end=', ')
        ciphertext+=alphabet[ciphernumber]
        #print(ciphertext)
    return ciphertext


def decryption(ciphertext, key):
    #Input plaintext

    #ciphertext = input("Masukkan ciphertext:")

    print(ciphertext[0])

    #Input key from user#
    #key = input("Masukkan key:")

    #print(key)

    #Convert into lowercase#
    ciphertext=ciphertext.lower()
    key=key.lower()

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


"""
#Outputs the ciphertext#
print("Ciphertext:"+encryption())
"""
#Outputs the plaintext#
#print("Ciphertext:"+decryption())
