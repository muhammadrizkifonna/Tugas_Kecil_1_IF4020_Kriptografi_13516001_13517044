#Input plaintext

plaintext = input("Masukkan plaintext:")

print(plaintext[0])

#Input key from user#
key = input("Masukkan key:")

#print(key)

#Compare plaintext and key's length
if (key<plaintext):
    real_key=key
    times = len(plaintext)//len(key)

    for i in range(times-1):
        key+=real_key

    sisa = len(plaintext)-len(key)

    for i in range(sisa):
        key+=real_key[i]






print(key)
