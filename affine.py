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
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 
    # if a == 0 :   
    #     return b, 0, 1
    # greatestCommonDenominator, x1, y1 = extendedGCDEuclideanAlgorithm(b%a, a)
    # x = y1 - (b//a) * x1  
    # y = x1
    # return greatestCommonDenominator, x, y

def getModularInverse(a, m):
    gcd, x, y = extendedGCDEuclideanAlgorithm(a, m) 
    if gcd != 1: 
        return None  # modular inverse does not exist 
    else: 
        return x % m

def encryption(plaintext, key_m, key_b, from_file, path, write_to_file):
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
    plaintext=toUpperCase(plaintext)
    #key=key.lower()

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

    # Remove punctuation from key
    """
    no_punct = ""
    for char in key:
        if char not in punctuations:
            no_punct = no_punct + char
    """
    #key=no_punct

    """
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

    #ciphertext = input("Masukkan ciphertext:")

    #print(ciphertext[0])

    #Input key from user#
    #key = input("Masukkan key:")

    #print(key)

    #Convert into lowercase#
    ciphertext=toUpperCase(ciphertext)
    #key=key.lower()

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

    # Remove punctuation from key
    """
    no_punct = ""
    for char in key:
        if char not in punctuations:
            no_punct = no_punct + char
    key=no_punct
    """

    """
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
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = list(alphabet)
    key_m=int(key_m)
    key_b=int(key_b)
    #Find the inverse of key_m
    # plaintextList = []
    # for i in range(len(ciphertext)):
    #     modularInverse = getModularInverse(key_m, 26)
    #     shift = ord(ciphertext[i])-ord('A')-key_b
    #     char = chr(((modularInverse*shift)%26)+ord('A'))
    #     plaintextList.append(char)
    # plaintext = ''.join(plaintextList)

    # for i in range(0,1000):
    #     if (((key_m*i)%26)==1):
    #         break
    
    key_m_inverse = getModularInverse(key_m, 26)

    plaintext=''
    for i in range(len(ciphertext)):
        #alphabet_cycle=itertools.cycle(alphabet)
        #print(key[i])
        #plainnumber=(alphabet.index(ciphertext[i])-alphabet.index(key[i]))%26
        plainnumber=(key_m_inverse*(alphabet.index(ciphertext[i])-key_b))%26

        plaintext+=alphabet[plainnumber]
        print(ciphertext)
    return plaintext


"""
#Outputs the ciphertext#
print("Ciphertext:"+encryption())
"""
#Outputs the plaintext#
#print("Ciphertext:"+decryption())
