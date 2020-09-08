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
            [sg.Text('Ciphertext:'), sg.Text(size=(30,1), key='-CIPHERTEXT_ENCRYPT-')],
            [sg.Button('Encrypt'), sg.Button('Exit')],
            [sg.Text('Decryption')],
            [sg.Text('Enter Ciphertext:'), sg.Input(key='-PLAINTEXT_DECRYPT-')],
            [sg.Text('Enter key:'), sg.Input(key='-KEY_DECRYPT-')],
            [sg.Text('Ciphertext:'), sg.Text(size=(30,1), key='-CIPHERTEXT_DECRYPT-')],
            [sg.Button('Decrypt'), sg.Button('Exit')]]
            

window = sg.Window('Cryptography Program', layout)

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    elif event=='Encrypt':
        window['-CIPHERTEXT_ENCRYPT-'].update(vg.encryption(values['-PLAINTEXT_ENCRYPT-'], values['-KEY_ENCRYPT-']))
    elif event=='Decrypt':
        window['-CIPHERTEXT_DECRYPT-'].update(vg.decryption(values['-PLAINTEXT_DECRYPT-'], values['-KEY_DECRYPT-']))

window.close()