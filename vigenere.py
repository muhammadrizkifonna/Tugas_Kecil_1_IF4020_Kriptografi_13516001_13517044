#Input plaintext

plaintext = input("Masukkan plaintext:")

print(plaintext[0])

#Input key from user#
key = input("Masukkan key:")

#print(key)

#Compare plaintext and key's length#
if (key<plaintext):
    real_key=key
    times = len(plaintext)//len(key)

    for i in range(times-1):
        key+=real_key

    sisa = len(plaintext)-len(key)

    for i in range(sisa):
        key+=real_key[i]

#If key>plaintext (has not finished)#

#Alphabet list for conversion from number to character#
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
             'w', 'x', 'y', 'z']

#Conversion from plaintext to ciphertext#

def plain_to_cipher(plaintext, key):
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

#Outputs the ciphertext#
print("Ciphertext:"+plain_to_cipher(plaintext, key))




