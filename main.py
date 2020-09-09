import PySimpleGUI as sg
import vigenere as vg
import full_vigenere as fvg
import vigenereExtended as vge
import enigma as e
import playfair as p
import hill as h

layout = [[sg.Text('Cipher method')],
            [sg.Radio('vignere', "cipherMethod", default=True, size=(10,1), key='vignere'), 
                sg.Radio('FullVignere', "cipherMethod", key='FullVignere'), 
                sg.Radio('RunningKeyVignere', "cipherMethod", key='RunningKeyVignere'), 
                sg.Radio('ExtendedVignere', "cipherMethod", key='ExtendedVignere'), 
                sg.Radio('Playfair', "cipherMethod", key='Playfair'),
                sg.Radio('SuperEncryption', "cipherMethod", key='SuperEncryption'),
                sg.Radio('Affine', "cipherMethod", key='Affine'),
                sg.Radio('Hill', "cipherMethod", key='Hill'), 
                sg.Radio('Enigma', "cipherMethod", key='Enigma')],
            [sg.Text('Encryption')], 
            [sg.Text('Enter Plaintext:'), sg.Input(key='-PLAINTEXT_ENCRYPT-')], 
            [sg.Text('Enter key:'), sg.Input(key='-KEY_ENCRYPT-')],
            [sg.Text('Enter Filename (Path):'), sg.Input(key='-PATH_ENCRYPT-')],
            [sg.Text('Ciphertext:'), sg.Text(size=(30,1), key='-CIPHERTEXT_ENCRYPT-')],
            [sg.Button('Encrypt'), sg.Button('Encrypt Text File'), sg.Button("Output into Text File"), sg.Button('Exit')],
            [sg.Text('Decryption')],
            [sg.Text('Enter Ciphertext:'), sg.Input(key='-CIPHERTEXT_DECRYPT-')],
            [sg.Text('Enter key:'), sg.Input(key='-KEY_DECRYPT-')],
            [sg.Text('Plaintext:'), sg.Text(size=(30,1), key='-PLAINTEXT_DECRYPT-')],
            [sg.Button('Decrypt'), sg.Button('Exit')]]
            

window = sg.Window('Cryptography Program', layout)

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    elif event=='Encrypt':
        if values['vignere'] == True:
            window['-CIPHERTEXT_ENCRYPT-'].update(vg.encryption(values['-PLAINTEXT_ENCRYPT-'], values['-KEY_ENCRYPT-'], False, '', False))
        if values['FullVignere'] == True:
            window['-CIPHERTEXT_ENCRYPT-'].update(fvg.encryption(values['-PLAINTEXT_ENCRYPT-'], values['-KEY_ENCRYPT-'], False, '', False))
        if values['RunningKeyVignere'] == True:
            pass
        if values['ExtendedVignere'] == True:
            message = values['-PLAINTEXT_ENCRYPT-']
            key = values['-KEY_ENCRYPT-']
            window['-CIPHERTEXT_ENCRYPT-'].update(vge.encryptTextExtendedVigenere(message, key))
        if values['Playfair'] == True:
            message = values['-PLAINTEXT_ENCRYPT-']
            key = values['-KEY_ENCRYPT-']
            window['-CIPHERTEXT_ENCRYPT-'].update(p.toUpperCase(p.playfairEncrypt(message, key)))
        if values['SuperEncryption'] == True:
            pass
        if values['Affine'] == True:
            pass
        if values['Hill'] == True:
            message = values['-PLAINTEXT_ENCRYPT-']
            key = values['-KEY_ENCRYPT-']
            resultList = []
            message = h.toUpperCase(message)
            message = h.wrap(message, 3)
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
                cipherText = h.HillCipherEncryption(messagePart, key)
                # if add > 0:
                #     for i in range(add):
                #         cipherText = cipherText[:-1]
                resultList.append(cipherText)
            resultMessage = ''.join(resultList)
            window['-CIPHERTEXT_ENCRYPT-'].update(resultMessage)
        if values['Enigma'] == True:
            text = values['-PLAINTEXT_ENCRYPT-']
            alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alphabetList = list(alphabet)
            steckerbrettDictionary = {' ': ' '}
            pairsInSteckerbrett = sg.popup_get_text('Input the number of pairs in steckerbrett (min 0)', 'Input the number of pairs in steckerbrett')
            for i in range(int(pairsInSteckerbrett)):
                firstSteckerbrettAlphabet = sg.popup_get_text("Pair #" + str(i+1),"Input the first alphabet in pair: ")
                secondSteckerbrettAlphabet = sg.popup_get_text("Pair #" + str(i+1), "Input the second alphabet in pair: ")
                steckerbrettDictionary[firstSteckerbrettAlphabet.upper()] = secondSteckerbrettAlphabet.upper()
            #print("Input alpha, beta and gamma rotor s")
            alphaRotor = int(sg.popup_get_text("Input Alpha Rotor shift (0-25)", "Input Alpha Rotor shift (0-25)"))
            betaRotor = int(sg.popup_get_text("Input Beta Rotor shift (0-25)", "Input Beta Rotor shift (0-25)"))
            gammaRotor = int(sg.popup_get_text("Input Gamma Rotor shift (0-25)", "Input Gamma Rotor shift (0-25)"))
            for letter in list(steckerbrettDictionary.keys()):
                if letter in alphabetList:
                    alphabetList.remove(letter)
                    alphabetList.remove(steckerbrettDictionary[letter])
                    steckerbrettDictionary.update({steckerbrettDictionary[letter]:letter})
            reflector = [letter for letter in reversed(alphabetList)]
            window['-CIPHERTEXT_ENCRYPT-'].update(e.encryptDecrypt(text, steckerbrettDictionary, alphaRotor, betaRotor, gammaRotor, alphabetList, reflector))
    elif event=='Encrypt Text File':
        if values['vignere'] == True:
            window['-CIPHERTEXT_ENCRYPT-'].update(vg.encryption('', values['-KEY_ENCRYPT-'], True, values['-PATH_ENCRYPT-']))
        if values['FullVignere'] == True:
            pass
        if values['RunningKeyVignere'] == True:
            pass
        if values['ExtendedVignere'] == True:
            pass
        if values['Playfair'] == True:
            pass
        if values['SuperEncryption'] == True:
            pass
        if values['Affine'] == True:
            pass
        if values['Hill'] == True:
            pass
        if values['Enigma'] == True:
            print(values['-PATH_ENCRYPT-'])
            pass

    elif event=='Output into Text File':
        if values['vignere'] == True:
            window['-CIPHERTEXT_ENCRYPT-'].update(vg.write_to_file(values['-PATH_ENCRYPT-'], vg.encryption(values['-PLAINTEXT_ENCRYPT-'], values['-KEY_ENCRYPT-'], False, '', False)))
        if values['FullVignere'] == True:
            pass
        if values['RunningKeyVignere'] == True:
            pass
        if values['ExtendedVignere'] == True:
            message = values['-PLAINTEXT_ENCRYPT-']
            key = values['-KEY_ENCRYPT-']
            window['-CIPHERTEXT_ENCRYPT-'].update(vge.write_to_file(values['-PATH_ENCRYPT-'], vge.encryptTextExtendedVigenere(message, key)))
        if values['Playfair'] == True:
            message = values['-PLAINTEXT_ENCRYPT-']
            key = values['-KEY_ENCRYPT-']
            window['-CIPHERTEXT_ENCRYPT-'].update(p.write_to_file(values['-PATH_ENCRYPT-'], p.toUpperCase(p.playfairEncrypt(message, key))))
        if values['SuperEncryption'] == True:
            pass
        if values['Affine'] == True:
            pass
        if values['Hill'] == True:
            message = values['-PLAINTEXT_ENCRYPT-']
            key = values['-KEY_ENCRYPT-']
            resultList = []
            message = h.toUpperCase(message)
            message = h.wrap(message, 3)
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
                cipherText = h.HillCipherEncryption(messagePart, key)
                # if add > 0:
                #     for i in range(add):
                #         cipherText = cipherText[:-1]
                resultList.append(cipherText)
            resultMessage = ''.join(resultList)
            window['-CIPHERTEXT_ENCRYPT-'].update(h.write_to_file(values['-PATH_ENCRYPT-'], resultMessage))
        if values['Enigma'] == True:
            text = values['-PLAINTEXT_ENCRYPT-']
            alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alphabetList = list(alphabet)
            steckerbrettDictionary = {' ': ' '}
            pairsInSteckerbrett = sg.popup_get_text('Input the number of pairs in steckerbrett (min 0)', 'Input the number of pairs in steckerbrett')
            for i in range(int(pairsInSteckerbrett)):
                firstSteckerbrettAlphabet = sg.popup_get_text("Pair #" + str(i+1),"Input the first alphabet in pair: ")
                secondSteckerbrettAlphabet = sg.popup_get_text("Pair #" + str(i+1), "Input the second alphabet in pair: ")
                steckerbrettDictionary[firstSteckerbrettAlphabet.upper()] = secondSteckerbrettAlphabet.upper()
            #print("Input alpha, beta and gamma rotor s")
            alphaRotor = int(sg.popup_get_text("Input Alpha Rotor shift (0-25)", "Input Alpha Rotor shift (0-25)"))
            betaRotor = int(sg.popup_get_text("Input Beta Rotor shift (0-25)", "Input Beta Rotor shift (0-25)"))
            gammaRotor = int(sg.popup_get_text("Input Gamma Rotor shift (0-25)", "Input Gamma Rotor shift (0-25)"))
            for letter in list(steckerbrettDictionary.keys()):
                if letter in alphabetList:
                    alphabetList.remove(letter)
                    alphabetList.remove(steckerbrettDictionary[letter])
                    steckerbrettDictionary.update({steckerbrettDictionary[letter]:letter})
            reflector = [letter for letter in reversed(alphabetList)]
            window['-CIPHERTEXT_ENCRYPT-'].update(e.write_to_file(values['-PATH_ENCRYPT-'], e.encryptDecrypt(text, steckerbrettDictionary, alphaRotor, betaRotor, gammaRotor, alphabetList, reflector)))
    elif event=='Decrypt':
        if values['vignere'] == True:
            window['-PLAINTEXT_DECRYPT-'].update(vg.decryption(values['-CIPHERTEXT_DECRYPT-'], values['-KEY_DECRYPT-']))
        if values['FullVignere'] == True:
            #window['-CIPHERTEXT_ENCRYPT-'].update(fvg.encryption(values['-PLAINTEXT_ENCRYPT-'], values['-KEY_ENCRYPT-'], False, '', False))
            window['-PLAINTEXT_DECRYPT-'].update(fvg.decryption(values['-CIPHERTEXT_DECRYPT-'], values['-KEY_DECRYPT-']))
        if values['RunningKeyVignere'] == True:
            pass
        if values['ExtendedVignere'] == True:
            message = values['-CIPHERTEXT_DECRYPT-']
            key = values['-KEY_DECRYPT-']
            window['-PLAINTEXT_DECRYPT-'].update(vge.decryptTextExtendedVigenere(message, key))
        if values['Playfair'] == True:
            message = values['-CIPHERTEXT_DECRYPT-']
            key = values['-KEY_DECRYPT-']
            window['-PLAINTEXT_DECRYPT-'].update(p.toUpperCase(p.playfairDecrypt(message, key)))
        if values['SuperEncryption'] == True:
            pass
        if values['Affine'] == True:
            pass
        if values['Hill'] == True:
            message = values['-CIPHERTEXT_DECRYPT-']
            key = values['-KEY_DECRYPT-']
            resultList = []
            message = h.toUpperCase(message)
            message = h.wrap(message, 3)
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
                # add = 0
                # if len(messagePart) < 3:
                #     add = 3 - len(messagePart) 
                #     for i in range(add):
                #         messagePart = ''.join([messagePart, 'X'])
                decipherText = h.HillCipherDecryption(messagePart, key)
                # if add > 0:
                #     for i in range(add):
                #         decipherText = decipherText[:-1]
                resultList.append(decipherText)
            resultMessage = ''.join(resultList)
            window['-PLAINTEXT_DECRYPT-'].update(resultMessage)
        if values['Enigma'] == True:
            text = values['-CIPHERTEXT_DECRYPT-']
            alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alphabetList = list(alphabet)
            steckerbrettDictionary = {' ': ' '}
            pairsInSteckerbrett = sg.popup_get_text('Input the number of pairs in steckerbrett (min 0)', 'Input the number of pairs in steckerbrett')
            for i in range(int(pairsInSteckerbrett)):
                firstSteckerbrettAlphabet = sg.popup_get_text("Pair #" + str(i+1),"Input the first alphabet in pair: ")
                secondSteckerbrettAlphabet = sg.popup_get_text("Pair #" + str(i+1), "Input the second alphabet in pair: ")
                steckerbrettDictionary[firstSteckerbrettAlphabet.upper()] = secondSteckerbrettAlphabet.upper()
            #print("Input alpha, beta and gamma rotor s")
            alphaRotor = int(sg.popup_get_text("Input Alpha Rotor shift (0-25)", "Input Alpha Rotor shift (0-25)"))
            betaRotor = int(sg.popup_get_text("Input Beta Rotor shift (0-25)", "Input Beta Rotor shift (0-25)"))
            gammaRotor = int(sg.popup_get_text("Input Gamma Rotor shift (0-25)", "Input Gamma Rotor shift (0-25)"))
            for letter in list(steckerbrettDictionary.keys()):
                if letter in alphabetList:
                    alphabetList.remove(letter)
                    alphabetList.remove(steckerbrettDictionary[letter])
                    steckerbrettDictionary.update({steckerbrettDictionary[letter]:letter})
            reflector = [letter for letter in reversed(alphabetList)]
            window['-PLAINTEXT_DECRYPT-'].update(e.encryptDecrypt(text, steckerbrettDictionary, alphaRotor, betaRotor, gammaRotor, alphabetList, reflector))

window.close()