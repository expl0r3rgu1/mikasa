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
                db_cursor.execute(QUERIES['Aggiungi cliente'], (values[0], values[1], values[2],
                                  values[3], values[4], values[5], values[6], values[7], values[8]))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
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
            elif event == sg.WIN_CLOSED:
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
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Aggiungi manager':
        db_cursor.execute(QUERIES['Visualizza negozi'])
        negozi = db_cursor.fetchall()
        window.close()
        window = aggiungi_personale_window(negozi)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(QUERIES['Aggiungi manager'], (values[0], values[1], values[2], values[3],
                                  values[4], values[5], values[6], values[7], values[8], values[9], 2, values['negozio'][0]))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Aggiungi tecnico':
        db_cursor.execute(QUERIES['Visualizza negozi'])
        negozi = db_cursor.fetchall()
        window.close()
        window = aggiungi_personale_window(negozi)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Aggiungi tecnico'], (values[0], values[1], values[2], values[3],
                                                  values[4], values[5], values[6], values[7], values[8], values[9], 4, values['negozio'][0]))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Aggiungi tecnico commerciale':
        db_cursor.execute(QUERIES['Visualizza negozi'])
        negozi = db_cursor.fetchall()
        window.close()
        window = aggiungi_personale_window(negozi)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Aggiungi tecnico commerciale'], (values[0], values[1], values[2], values[3],
                                                              values[4], values[5], values[6], values[7], values[8], values[9], 4, values['negozio'][0]))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Aggiungi amministratore':
        db_cursor.execute(QUERIES['Visualizza negozi'])
        negozi = db_cursor.fetchall()
        zone = [(1, 'Alimentari'), (2, 'Ristoro'),
                (3, 'Esposizione'), (4, 'Magazzino')]
        window.close()
        window = aggiungi_amministratore_window(negozi, zone)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(QUERIES['Aggiungi amministratore'], (values[0], values[1], values[2], values[3], values[4],
                                  values[5], values[6], values[7], values[8], values[9], 4, values['negozio'][0], values['zona'][0]))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Aggiungi negozio':
        db_cursor.execute(QUERIES['Visualizza acquirenti'])
        acquirenti = db_cursor.fetchall()
        window.close()
        window = aggiungi_negozio_window(acquirenti)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(QUERIES['Aggiungi negozio'], (values[0], values[1], values[2], values[3],
                                  values['-CAL-'], values['acquirente'][0], 1, values['num_posti_ristoro'], values['num_composizioni']))
                db.commit()
                window.close()
                window = default_window()
                break
            elif event == 'Annulla':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Effettua ordine per cliente':
        db_cursor.execute(QUERIES['Visualizza clienti'])
        clienti = db_cursor.fetchall()
        db_cursor.execute(QUERIES['Visualizza prodotti'])
        prodotti = db_cursor.fetchall()
        db_cursor.execute(QUERIES['Visualizza composizioni'])
        composizioni = db_cursor.fetchall()
        db_cursor.execute(QUERIES['Visualizza negozi'])
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
                        QUERIES['Visualizza percentuale sconto di uno sconto'], (prodotto[7],))
                    sconto = db_cursor.fetchone()
                    if sconto is None:
                        costo_totale += prodotto[2]
                    else:
                        costo_totale += (prodotto[2] * (1 - sconto[0] / 100))
                    peso_totale += prodotto[6]

                for composizione in composizioni_acquistate:
                    db_cursor.execute(
                        QUERIES['Visualizza prodotti contenuti in una composizione'], (composizione[0],))
                    prodotti_composizione = db_cursor.fetchall()
                    for prodotto in prodotti_composizione:
                        db_cursor.execute(
                            QUERIES['Visualizza percentuale sconto di uno sconto'], (prodotto[7],))
                        sconto = db_cursor.fetchone()
                        if sconto is None:
                            costo_totale += prodotto[2]
                        else:
                            costo_totale += prodotto[2] * (1 - sconto[0] / 100)
                        peso_totale += prodotto[6]

                db_cursor.execute(QUERIES['Visualizza tecnici commerciali'])
                tecnici_commerciali = db_cursor.fetchall()

                db_cursor.execute(
                    QUERIES['Visualizza se cliente è socio'], (values['cliente'][0],))
                is_socio = db_cursor.fetchone()[0]
                if(is_socio):
                    costo_totale *= 0.95

                db_cursor.execute(QUERIES['Effettua ordine'], (date.today(), costo_totale, peso_totale, date.today(
                ) + timedelta(days=5), values['cliente'][0], random.choice(tecnici_commerciali)[0]))
                db.commit()

                cod_ordine = db_cursor.lastrowid

                for i, prodotto in enumerate(prodotti_acquistati):
                    db_cursor.execute(QUERIES['Aggiungi dettaglio prodotto'], (cod_ordine, prodotto[0], int(values['quantità_prodotti'].split(
                        ',')[i]), prodotto[2] * int(values['quantità_prodotti'].split(',')[i]), prodotto[6] * int(values['quantità_prodotti'].split(',')[i])))
                    db.commit()

                for i, composizione in enumerate(composizioni_acquistate):
                    db_cursor.execute(
                        QUERIES['Visualizza prodotti contenuti in una composizione'], (composizione[0],))
                    prodotti_composizione = db_cursor.fetchall()
                    costo_composizione = 0
                    peso_composizione = 0
                    for prodotto in prodotti_composizione:
                        costo_composizione += prodotto[2]
                        peso_composizione += prodotto[6]

                    db_cursor.execute(QUERIES['Aggiungi dettaglio composizione'], (
                        cod_ordine, composizione[0], int(values['quantità_composizioni'].split(',')[i]), costo_composizione, peso_composizione))

                if(values['spedizione'] == 'Con spedizione'):
                    db_cursor.execute(QUERIES['Visualizza tecnici'])
                    tecnici = db_cursor.fetchall()
                    tecnico = random.choice(tecnici)
                    db_cursor.execute(QUERIES[''], (
                        cod_ordine, values['indirizzo'], tecnico[0]))
                    db.commit()
                    if(values['montaggio'] == 'Con montaggio'):
                        db_cursor.execute(QUERIES['Effettua ordine con montaggio'], (
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
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Aggiungi prodotto':
        window.close()
        db_cursor.execute(QUERIES['Visualizza sconti'])
        sconti = db_cursor.fetchall()
        window = aggiungi_prodotto_window(sconti)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                sconto = None
                if values['sconto'] != 'NONE':
                    sconto = values['sconto'][0]
                db_cursor.execute(QUERIES['Aggiungi prodotto'], (
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
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Visualizza ordini in un mese':
        window.close()
        window = ordini_mese_window()

        while True:
            event, values = window.read()

            if event == '-CAL-':
                db_cursor.execute(QUERIES['Visualizza ordini in un mese'], (
                    values['-CAL-'].split('-')[0], values['-CAL-'].split('-')[1]))
                ordini = db_cursor.fetchall()
                window['ordini'].update(values=ordini)
            elif event == 'Indietro':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Visualizza ordini cliente':
        db_cursor.execute(QUERIES['Visualizza clienti'])
        clienti = db_cursor.fetchall()
        window.close()
        window = ordini_cliente_window(clienti)

        while True:
            event, values = window.read()

            if event == 'cliente':
                db_cursor.execute(
                    QUERIES['Visualizza ordini di un cliente'], (values['cliente'][0],))
                ordini = db_cursor.fetchall()
                window['ordini'].update(values=ordini)
            elif event == 'Indietro':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Visualizza spedizioni in un mese':
        window.close()
        window = spedizioni_mese_window()

        while True:
            event, values = window.read()

            if event == '-CAL-':
                db_cursor.execute(QUERIES['Visualizza spedizioni in un mese'], (
                    values['-CAL-'].split('-')[0], values['-CAL-'].split('-')[1]))
                spedizioni = db_cursor.fetchall()
                window['spedizioni'].update(values=spedizioni)
            elif event == 'Indietro':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Visualizza ritiri in un mese':
        window.close()
        window = ritiri_mese_window()

        while True:
            event, values = window.read()

            if event == '-CAL-':
                db_cursor.execute(QUERIES['Visualizza ritiri in un mese'], (
                    values['-CAL-'].split('-')[0], values['-CAL-'].split('-')[1]))
                ritiri = db_cursor.fetchall()
                window['ritiri'].update(values=ritiri)
            elif event == 'Indietro':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Visualizza montaggi in un mese':
        window.close()
        window = montaggi_mese_window()

        while True:
            event, values = window.read()

            if event == '-CAL-':
                db_cursor.execute(QUERIES['Visualizza montaggi in un mese'], (
                    values['-CAL-'].split('-')[0], values['-CAL-'].split('-')[1]))
                montaggi = db_cursor.fetchall()
                window['montaggi'].update(values=montaggi)
            elif event == 'Indietro':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Visualizza 10 prodotti più acquistati':
        db_cursor.execute(QUERIES['Visualizza 10 prodotti più acquistati'])
        prodotti = db_cursor.fetchall()

        window.close()
        window = prodotti_piu_acquistato_window(prodotti)
    elif event == 'Indietro':
        window.close()
        window = default_window()
    elif event == sg.WIN_CLOSED:
        break

window.close()
