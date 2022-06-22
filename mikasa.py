#!/usr/bin/python3

import PySimpleGUI as sg
import mysql.connector
from credentials import *
from windows import *

db = mysql.connector.connect(
    host=HOST,
    user=USER,
    passwd=PASSWORD,
    database=DATABASE,
    auth_plugin=AUTH_PLUGIN
)

db_cursor = db.cursor()

window = default_window()


while True:
    event, values = window.read()
    if event == 'Visualizza clienti':
        db_cursor.execute(
            "SELECT * FROM persone WHERE EXISTS (SELECT 1 FROM clienti WHERE clienti.cf_cliente = persone.cf)")
        clienti = db_cursor.fetchall()
        window.close()
        window = clienti_window(clienti)
    elif event == 'Aggiungi cliente':
        window.close()
        window = aggiungi_cliente_window()

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute("INSERT INTO persone (cf, nome, cognome, telefono, email, via, civico, cap, città) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                db_cursor.execute(
                    "INSERT INTO clienti (cf_cliente, socio) VALUES (%s, 0)", (values[0],))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Rendi socio un cliente':
        db_cursor.execute(
            "SELECT * FROM persone WHERE EXISTS (SELECT 1 FROM clienti WHERE clienti.cf_cliente = persone.cf)")
        clienti = db_cursor.fetchall()
        window.close()
        window = rendi_socio_cliente_window(clienti)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                print(values['cliente'][0])
                db_cursor.execute(
                    "UPDATE clienti SET socio = 1 WHERE cf_cliente = %s", (values['cliente'][0],))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Indietro':
        window.close()
        window = default_window()
    elif event == sg.WIN_CLOSED:
        break

window.close()
