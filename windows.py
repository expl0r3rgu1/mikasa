#!/usr/bin/python3

import PySimpleGUI as sg

def default_window():
    empty_layout = [
        [sg.Text('Mikasa')],
        [sg.Button('Aggiungi cliente'), sg.Button('Rendi socio un cliente'), sg.Button('Rendi non socio un cliente'), sg.Button('Visualizza clienti')],
    ]

    return sg.Window('Mikasa', empty_layout, margins=(400, 200))

def clienti_window(clienti):
    table = sg.Table(values=clienti, headings=['Codice Fiscale', 'Nome', 'Cognome',
                                                    'Telefono', 'E-mail', 'Via', 'Civico', 'CAP', 'CITTÀ'])
    layout = [
        [sg.Text('Clienti')],
        [table],
        [sg.Button('Indietro')]
    ]
    return sg.Window('Clienti', layout, margins=(400, 200))