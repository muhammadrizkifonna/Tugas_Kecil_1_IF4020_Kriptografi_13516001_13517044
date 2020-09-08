import PySimpleGUI as sg
import vigenere as vg

layout =   [[sg.Text('Encryption')],
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