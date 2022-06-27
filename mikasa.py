#!/usr/bin/python3

import PySimpleGUI as sg
import mysql.connector
from credentials import *
from windows import *
from queries import *

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
        db_cursor.execute(QUERIES['Visualizza clienti'])
        clienti = db_cursor.fetchall()
        window.close()
        window = clienti_window(clienti)
    elif event == 'Aggiungi cliente':
        window.close()
        window = aggiungi_cliente_window()

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(QUERIES['Aggiungi persona'], (
                    values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi cliente'], (values[0],))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Rendi socio un cliente':
        db_cursor.execute(QUERIES['Visualizza clienti'])
        clienti = db_cursor.fetchall()
        window.close()
        window = rendi_socio_cliente_window(clienti)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                print(values['cliente'][0])
                db_cursor.execute(
                    QUERIES['Rendi socio un cliente'], (values['cliente'][0],))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Rendi non socio un cliente':
        db_cursor.execute(
            QUERIES['Visualizza clienti'])
        clienti = db_cursor.fetchall()
        window.close()
        window = rendi_socio_cliente_window(clienti)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                print(values['cliente'][0])
                db_cursor.execute(
                    QUERIES['Rendi non socio un cliente'], (values['cliente'][0],))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Aggiungi manager':
        db_cursor.execute("SELECT * FROM negozi")
        negozi = db_cursor.fetchall()
        window.close()
        window = aggiungi_personale_window(negozi)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(QUERIES['Aggiungi persona'], (
                    values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi personale'], (values[0], values[9], 2))
                db.commit()
                db_cursor.execute(
                    "INSERT INTO manager (cf_manager, cod_negozio) VALUES (%s, %s)", (values[0], values['negozio'][0]))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Aggiungi tecnico':
        db_cursor.execute("SELECT * FROM negozi")
        negozi = db_cursor.fetchall()
        window.close()
        window = aggiungi_personale_window(negozi)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(QUERIES['Aggiungi persona'], (
                    values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi personale'], (values[0], values[9], 2))
                db.commit()
                db_cursor.execute(
                    "INSERT INTO tecnico (cf_tecnico, cod_negozio, cod_magazzino) VALUES (%s, %s, %s)", (values[0], values['negozio'][0], 4))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Aggiungi tecnico commerciale':
        db_cursor.execute("SELECT * FROM negozi")
        negozi = db_cursor.fetchall()
        window.close()
        window = aggiungi_personale_window(negozi)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(QUERIES['Aggiungi persona'], (
                    values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi personale'], (values[0], values[9], 2))
                db.commit()
                db_cursor.execute("INSERT INTO tecnici_commerciali (cf_tecnico_commerciale, cod_negozio, cod_alimentari, cod_ristoro) VALUES (%s, %s, %s, %s)", (
                    values[0], values['negozio'][0], 1, 2))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Aggiungi amministratore':
        db_cursor.execute("SELECT * FROM negozi")
        negozi = db_cursor.fetchall()
        zone = [(1, 'Alimentari'), (2, 'Ristoro'),
                (3, 'Esposizione'), (4, 'Magazzino')]
        window.close()
        window = aggiungi_amministratore_window(negozi, zone)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(QUERIES['Aggiungi persona'], (
                    values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi personale'], (values[0], values[9], 2))
                db.commit()
                db_cursor.execute("INSERT INTO amministratori (cf_amministratore, cod_negozio, cod_zona) VALUES (%s, %s, %s)", (
                    values[0], values['negozio'][0], values['zona'][0]))
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
