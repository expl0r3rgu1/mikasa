#!/usr/bin/python3

import PySimpleGUI as sg
import mysql.connector
from credentials import *

db = mysql.connector.connect(
    host = HOST,
    user = USER,
    passwd = PASSWORD,
    database = DATABASE,
    auth_plugin = AUTH_PLUGIN
)

db_cursor = db.cursor()

empty_layout = [
    [sg.Text('Mikasa')],
    [sg.Button('Visualizza clienti')]
]

window = sg.Window('Mikasa', empty_layout, margins=(400, 200))

while True:
    event, values = window.read()
    if event == 'Visualizza clienti':
        db_cursor.execute("SELECT * FROM persone WHERE cf = (SELECT cf_cliente FROM clienti)")
        clienti = db_cursor.fetchall()
        window.close()
        table = sg.Table(values=clienti, headings=['Codice Fiscale', 'Nome', 'Cognome',
                                                    'Telefono', 'E-mail', 'Via', 'Civico', 'CAP', 'CITTÀ'])
        layout = [
            [sg.Text('Clienti')],
            [table],
            [sg.Button('Indietro')]
        ]
        window = sg.Window('Clienti', layout, margins=(400, 200))
    elif event == 'Indietro':
        window.close()
        layout = [
            [sg.Text('Mikasa')],
            [sg.Button('Visualizza clienti')]
        ]
        window = sg.Window('Mikasa', layout, margins=(400, 200))