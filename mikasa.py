#!/usr/bin/python3

import PySimpleGUI as sg
import mysql.connector
from credentials import *
from windows import *

db = mysql.connector.connect(
    host = HOST,
    user = USER,
    passwd = PASSWORD,
    database = DATABASE,
    auth_plugin = AUTH_PLUGIN
)

db_cursor = db.cursor()

window = default_window()


while True:
    event, values = window.read()
    if event == 'Visualizza clienti':
        db_cursor.execute("SELECT * FROM persone WHERE EXISTS (SELECT 1 FROM clienti WHERE clienti.cf_cliente = persone.cf)")
        clienti = db_cursor.fetchall()
        window.close()
        window = clienti_window(clienti)
    elif event == 'Aggiungi cliente':
        window.close()
        window = aggiungi_cliente_window()
    elif event == 'Indietro':
        window.close()
        window = default_window()
    elif event == sg.WIN_CLOSED:
        break

window.close()