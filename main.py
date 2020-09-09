import PySimpleGUI as sg
import vigenere as vg
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
            pass
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
            pass

    elif event=='Output into Text File':
        if values['vignere'] == True:
            window['-CIPHERTEXT_ENCRYPT-'].update(vg.write_to_file(values['-PATH_ENCRYPT-'], vg.encryption(values['-PLAINTEXT_ENCRYPT-'], values['-KEY_ENCRYPT-'], False, '', False)))
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
            pass
    elif event=='Decrypt':
        if values['vignere'] == True:
            window['-CIPHERTEXT_DECRYPT-'].update(vg.decryption(values['-PLAINTEXT_DECRYPT-'], values['-KEY_DECRYPT-']))
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
            pass

window.close()