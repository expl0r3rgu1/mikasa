#!/usr/bin/python3

import PySimpleGUI as sg
import mysql.connector
from credentials import *
from windows import *
from queries import *
from datetime import date, timedelta
import random

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
                db_cursor.execute(QUERIES['Aggiungi persona'], (values[0], values[1], values[2],
                                  values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                db_cursor.execute(QUERIES['Aggiungi cliente'], (values[0],))
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
        db_cursor.execute(QUERIES['Visualizza clienti'])
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
                db_cursor.execute(QUERIES['Aggiungi persona'], (values[0], values[1], values[2],
                                  values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi personale'], (values[0], values[9], 2))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi manager'], (values[0], values['negozio'][0]))
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
                db_cursor.execute(QUERIES['Aggiungi persona'], (values[0], values[1], values[2],
                                  values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi personale'], (values[0], values[9], 2))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi tecnico'], (values[0], values['negozio'][0], 4))
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
                db_cursor.execute(QUERIES['Aggiungi persona'], (values[0], values[1], values[2],
                                  values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi personale'], (values[0], values[9], 2))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi tecnico commerciale'], (values[0], values['negozio'][0], 1, 2))
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
                db_cursor.execute(QUERIES['Aggiungi persona'], (values[0], values[1], values[2],
                                  values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                db_cursor.execute(
                    QUERIES['Aggiungi personale'], (values[0], values[9], 2))
                db.commit()
                db_cursor.execute(QUERIES['Aggiungi amministratore'],
                                  (values[0], values['negozio'][0], values['zona'][0]))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Aggiungi negozio':
        db_cursor.execute("SELECT * FROM acquirenti")
        acquirenti = db_cursor.fetchall()
        window.close()
        window = aggiungi_negozio_window(acquirenti)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(QUERIES['Aggiungi negozio'], (values[0], values[1],
                                  values[2], values[3], values['-CAL-'], values['acquirente'][0], 1))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Effettua ordine per cliente':
        db_cursor.execute(QUERIES['Visualizza clienti'])
        clienti = db_cursor.fetchall()
        db_cursor.execute("SELECT * FROM prodotti")
        prodotti = db_cursor.fetchall()
        db_cursor.execute("SELECT * FROM composizioni")
        composizioni = db_cursor.fetchall()
        db_cursor.execute("SELECT * FROM negozi")
        negozi = db_cursor.fetchall()
        window.close()
        window = effettua_ordine_cliente_window(
            clienti, prodotti, composizioni, negozi)
        window['montaggio'].update(disabled=True)
        window['indirizzo'].update(disabled=True)
        window['negozio'].update(disabled=True)

        while True:
            event, values = window.read()
            if event == 'spedizione':
                if(values['spedizione'] == 'Con spedizione'):
                    window['montaggio'].update(disabled=False)
                    window['indirizzo'].update(disabled=False)
                    window['negozio'].update(disabled=True)
                else:
                    window['montaggio'].update(disabled=True)
                    window['indirizzo'].update(disabled=True)
                    window['negozio'].update(disabled=False)
            elif event == 'Conferma':
                prodotti_acquistati = values['prodotti']
                composizioni_acquistate = values['composizioni']

                costo_totale = 0
                peso_totale = 0
                for prodotto in prodotti_acquistati:
                    db_cursor.execute(
                        'SELECT s.percentuale FROM sconti s WHERE s.cod_sconto = %s', (prodotto[7],))
                    sconto = db_cursor.fetchone()
                    if sconto is None:
                        costo_totale += prodotto[2]
                    else:
                        costo_totale += (prodotto[2] * (1 - sconto[0] / 100))
                    peso_totale += prodotto[6]

                for composizione in composizioni_acquistate:
                    db_cursor.execute(
                        'SELECT * FROM prodotti WHERE EXISTS (SELECT * FROM composte WHERE cod_composizione = %s)', (composizione[0],))
                    prodotti_composizione = db_cursor.fetchall()
                    for prodotto in prodotti_composizione:
                        db_cursor.execute(
                            'SELECT s.percentuale FROM sconti s WHERE s.cod_sconto = %s', (prodotto[7],))
                        sconto = db_cursor.fetchone()
                        if sconto is None:
                            costo_totale += prodotto[2]
                        else:
                            costo_totale += prodotto[2] * (1 - sconto[0] / 100)
                        peso_totale += prodotto[6]

                db_cursor.execute('SELECT * FROM tecnici_commerciali')
                tecnici_commerciali = db_cursor.fetchall()

                db_cursor.execute(
                    'SELECT c.socio FROM clienti c WHERE c.cf_cliente = %s', (values['cliente'][0],))
                is_socio = db_cursor.fetchone()[0]
                if(is_socio):
                    costo_totale *= 0.95

                db_cursor.execute('INSERT INTO ordini (data_effettuazione, costo_totale, peso_totale, data_arrivo, cf_cliente, cf_tecnico_commerciale) VALUES (%s, %s, %s, %s, %s, %s)', (
                    date.today(), costo_totale, peso_totale, date.today() + timedelta(days=5), values['cliente'][0], random.choice(tecnici_commerciali)[0]))
                db.commit()

                cod_ordine = db_cursor.lastrowid

                for i, prodotto in enumerate(prodotti_acquistati):
                    db_cursor.execute('INSERT INTO dettagli_prodotto (cod_ordine, cod_prodotto, quantità, prezzo_totale, peso_totale) VALUES (%s, %s, %s, %s, %s)', (cod_ordine, prodotto[0], int(values['quantità_prodotti'].split(
                        ',')[i]), prodotto[2] * int(values['quantità_prodotti'].split(',')[i]), prodotto[6] * int(values['quantità_prodotti'].split(',')[i])))
                    db.commit()

                for i, composizione in enumerate(composizioni_acquistate):
                    db_cursor.execute(
                        'SELECT * FROM prodotti WHERE EXISTS (SELECT * FROM composte WHERE cod_composizione = %s)', (composizione[0],))
                    prodotti_composizione = db_cursor.fetchall()
                    costo_composizione = 0
                    peso_composizione = 0
                    for prodotto in prodotti_composizione:
                        costo_composizione += prodotto[2]
                        peso_composizione += prodotto[6]

                    db_cursor.execute('INSERT INTO dettagli_composizione (cod_ordine, cod_composizione, quantità, prezzo_totale, peso_totale) VALUES (%s, %s, %s, %s, %s)', (
                        cod_ordine, composizione[0], int(values['quantità_composizioni'].split(',')[i]), costo_composizione, peso_composizione))

                if(values['spedizione'] == 'Con spedizione'):
                    db_cursor.execute('SELECT * FROM tecnici')
                    tecnici = db_cursor.fetchall()
                    tecnico = random.choice(tecnici)
                    db_cursor.execute('INSERT INTO ordini_spedizione(cod_ordine, indirizzo, cf_tecnico) VALUES (%s, %s, %s)', (
                        cod_ordine, values['indirizzo'], tecnico[0]))
                    db.commit()
                    if(values['montaggio'] == 'Con montaggio'):
                        db_cursor.execute('INSERT INTO ordini_montaggio(cod_ordine, indirizzo, cf_tecnico) VALUES (%s, %s, %s)', (
                            cod_ordine, values['indirizzo'], tecnico[0]))
                        db.commit()
                    else:
                        db_cursor.execute(
                            QUERIES['Effettua ordine senza montaggio'], (cod_ordine,))
                        db.commit()
                else:
                    db_cursor.execute(
                        QUERIES['Effettua ordine senza spedizione'], (cod_ordine, values['negozio'][0]))
                    db.commit()

                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Aggiungi prodotto':
        window.close()
        db_cursor.execute('SELECT * FROM sconti')
        sconti = db_cursor.fetchall()
        window = aggiungi_prodotto_window(sconti)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                sconto = None
                if values['sconto'] != 'NONE':
                    sconto = values['sconto'][0]
                db_cursor.execute('INSERT INTO prodotti(nome, prezzo, altezza, larghezza, profondità, peso, cod_sconto) VALUES (%s, %s, %s, %s, %s, %s, %s)', (
                    values[0], values[1], values[2], values[3], values[4], values[5], sconto))
                db.commit()

                if values['categoria'] == 'Accessori':
                    db_cursor.execute(
                        QUERIES['Aggiungi accessorio'], (db_cursor.lastrowid,))
                    db.commit()
                elif values['categoria'] == 'Mobili':
                    db_cursor.execute(
                        QUERIES['Aggiungi mobile'], (db_cursor.lastrowid,))
                    db.commit()
                elif values['categoria'] == 'Elettrodomestici':
                    db_cursor.execute(
                        QUERIES['Aggiungi elettrodomestico'], (db_cursor.lastrowid,))
                    db.commit()

                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
    elif event == 'Visualizza ordini in un mese':
        window.close()
        window = ordini_mese_window()

        while True:
            event, values = window.read()

            if event == '-CAL-':
                db_cursor.execute('SELECT * FROM ordini WHERE YEAR(data_effettuazione) = %s AND MONTH(data_effettuazione) = %s',
                                  (values['-CAL-'].split('-')[0], values['-CAL-'].split('-')[1]))
                ordini = db_cursor.fetchall()
                window['ordini'].update(values=ordini)
            elif event == 'Indietro':
                window.close()
                window = default_window()
                break
    elif event == 'Indietro':
        window.close()
        window = default_window()
    elif event == sg.WIN_CLOSED:
        break

window.close()
