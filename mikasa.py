#!/usr/bin/python3

import PySimpleGUI as sg
import mysql.connector
from credentials import *
from windows import *
from queries import *
from datetime import date, timedelta, datetime
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
        db.commit()
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
        db.commit()
        window.close()
        window = rendi_socio_cliente_window(clienti)

        while True:
            event, values = window.read()
            if event == 'Conferma':
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
        db.commit()
        window.close()
        window = rendi_non_socio_cliente_window(clienti)

        while True:
            event, values = window.read()
            if event == 'Conferma':
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
        db.commit()
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
        db.commit()
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
        db.commit()
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
        db.commit()
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
        db.commit()
        window.close()
        window = aggiungi_negozio_window(acquirenti)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                db_cursor.execute(QUERIES['Aggiungi negozio'], (values[0], values[1], values[2], values[3],
                                  values['-CAL-'], values['acquirente'][0], 1, values['num_posti_ristoro']))
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
        db.commit()
        db_cursor.execute(QUERIES['Visualizza prodotti'])
        prodotti = db_cursor.fetchall()
        db.commit()
        db_cursor.execute(QUERIES['Visualizza composizioni'])
        composizioni = db_cursor.fetchall()
        db.commit()
        db_cursor.execute(QUERIES['Visualizza negozi'])
        negozi = db_cursor.fetchall()
        db.commit()
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
                for i, prodotto in enumerate(prodotti_acquistati):
                    costo_prodotto = 0
                    peso_prodotto = 0
                    db_cursor.execute(
                        QUERIES['Visualizza percentuale sconto di uno sconto'], (prodotto[7],))
                    sconto = db_cursor.fetchone()
                    db.commit()
                    if sconto is None:
                        costo_prodotto += prodotto[2]
                    else:
                        db_cursor.execute(
                            QUERIES['Visualizza storico sconto prodotto'], (prodotto[7],))
                        storico = db_cursor.fetchone()
                        db.commit()
                        data_inizio = storico[0]
                        data_fine = storico[1]
                        data_inizio.replace(year=date.today().year)
                        data_fine.replace(year=date.today().year)

                        if date.today() > data_inizio and date.today() < data_fine:
                            costo_prodotto += (prodotto[2]
                                               * (1 - sconto[0] / 100))
                        else:
                            costo_prodotto += prodotto[2]
                    peso_prodotto += prodotto[6]
                    costo_totale += costo_prodotto * \
                        int(values['quantità_prodotti'].split(',')[i])
                    peso_totale += peso_prodotto * \
                        int(values['quantità_prodotti'].split(',')[i])

                for i, composizione in enumerate(composizioni_acquistate):
                    costo_composizione = 0
                    peso_composizione = 0
                    db_cursor.execute(
                        QUERIES['Visualizza prodotti in composizione'], (composizione[0],))
                    prodotti_composizione = db_cursor.fetchall()
                    db.commit()
                    for prodotto in prodotti_composizione:
                        costo_prodotto = 0
                        peso_prodotto = 0
                        db_cursor.execute(
                            QUERIES['Visualizza percentuale sconto di uno sconto'], (prodotto[7],))
                        sconto = db_cursor.fetchone()
                        db.commit()
                        db_cursor.execute(
                            'SELECT quantità FROM composte WHERE cod_prodotto = %s AND cod_composizione = %s LIMIT 1', (prodotto[0], composizione[0]))
                        quantita_prodotto = int(db_cursor.fetchone()[0])
                        if sconto is None:
                            costo_prodotto += prodotto[2]
                        else:
                            db_cursor.execute(
                                QUERIES['Visualizza storico sconto prodotto'], (prodotto[7],))
                            storico = db_cursor.fetchone()
                            db.commit()
                            data_inizio = storico[0]
                            data_fine = storico[1]
                            data_inizio.replace(year=date.today().year)
                            data_fine.replace(year=date.today().year)

                            if date.today() > data_inizio and date.today() < data_fine:
                                costo_prodotto += prodotto[2] * \
                                    (1 - sconto[0] / 100)
                            else:
                                costo_prodotto += prodotto[2]
                        peso_prodotto += prodotto[6]
                        costo_composizione += costo_prodotto * quantita_prodotto
                        peso_composizione += peso_prodotto * quantita_prodotto
                    costo_totale += costo_composizione * \
                        int(values['quantità_composizioni'].split(',')[i])
                    peso_totale += peso_composizione * \
                        int(values['quantità_composizioni'].split(',')[i])

                db_cursor.execute(QUERIES['Visualizza tecnici commerciali'])
                tecnici_commerciali = db_cursor.fetchall()
                db.commit()

                db_cursor.execute(
                    QUERIES['Visualizza se cliente è socio'], (values['cliente'][0],))
                is_socio = db_cursor.fetchone()[0]
                db.commit()
                if(is_socio):
                    costo_totale *= 0.95

                db_cursor.execute(QUERIES['Effettua ordine'], (date.today(), costo_totale, peso_totale, date.today(
                ) + timedelta(days=5), values['cliente'][0], random.choice(tecnici_commerciali)[0]))
                db.commit()

                cod_ordine = db_cursor.lastrowid

                parameters = "(%s, %s, %s, %s, %s),"
                insert_dettaglio_prodotto = QUERIES['Aggiungi dettaglio prodotto'] + len(
                    prodotti_acquistati) * parameters
                insert_dettaglio_prodotto = insert_dettaglio_prodotto[:(
                    len(insert_dettaglio_prodotto) - 1)] + ';'
                data_prodotti = ()
                for i, prodotto in enumerate(prodotti_acquistati):
                    data_prodotti += (cod_ordine, prodotto[0], int(values['quantità_prodotti'].split(',')[i]), prodotto[2] * int(
                        values['quantità_prodotti'].split(',')[i]), prodotto[6] * int(values['quantità_prodotti'].split(',')[i]))

                insert_dettaglio_composizione = QUERIES['Aggiungi dettaglio composizione'] + len(
                    composizioni_acquistate) * parameters
                insert_dettaglio_composizione = insert_dettaglio_composizione[:(
                    len(insert_dettaglio_composizione) - 1)] + ';'
                data_composizioni = ()
                for i, composizione in enumerate(composizioni_acquistate):
                    db_cursor.execute(
                        QUERIES['Visualizza prodotti in composizione'], (composizione[0],))
                    prodotti_composizione = db_cursor.fetchall()
                    db.commit()
                    costo_composizione = 0
                    peso_composizione = 0
                    for prodotto in prodotti_composizione:
                        db_cursor.execute(
                            'SELECT quantità FROM composte WHERE cod_prodotto = %s AND cod_composizione = %s LIMIT 1', (prodotto[0], composizione[0]))
                        quantita_prodotto = int(db_cursor.fetchone()[0])
                        costo_composizione += prodotto[2] * quantita_prodotto
                        peso_composizione += prodotto[6] * quantita_prodotto

                    data_composizioni += (cod_ordine, composizione[0], int(values['quantità_composizioni'].split(
                        ',')[i]), costo_composizione, peso_composizione)

                if data_prodotti != ():
                    db_cursor.execute(insert_dettaglio_prodotto, data_prodotti)
                    db.commit()

                if data_composizioni != ():
                    db_cursor.execute(
                        insert_dettaglio_composizione, data_composizioni)
                    db.commit()

                if(values['spedizione'] == 'Con spedizione' and (data_prodotti != () or data_composizioni != ())):
                    db_cursor.execute(QUERIES['Visualizza tecnici'])
                    tecnici = db_cursor.fetchall()
                    db.commit()
                    tecnico = random.choice(tecnici)
                    db_cursor.execute(
                        QUERIES['Aggiungi spedizione'], (cod_ordine, values['indirizzo'], tecnico[0]))
                    db.commit()
                    if(values['montaggio'] == 'Con montaggio'):
                        db_cursor.execute(
                            QUERIES['Aggiungi montaggio'], (cod_ordine,))
                        db.commit()
                        weights = [1] * len(tecnici)
                        weights[tecnici.index(tecnico)] = 0
                        tecnici_montaggio = random.choices(
                            tecnici, weights, k=1)
                        weights[tecnici.index(tecnici_montaggio[0])] = 0
                        tecnici_montaggio += random.choices(
                            tecnici, weights, k=1)
                        db_cursor.execute(QUERIES['Aggiungi dettaglio montaggio'] + ",(%s,%s)", (
                            tecnici_montaggio[0][0], cod_ordine, tecnici_montaggio[1][0], cod_ordine))
                        db.commit()
                else:
                    db_cursor.execute(QUERIES['Aggiungi ritiro'], (cod_ordine, values['negozio']))
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
        db.commit()
        window = aggiungi_prodotto_window(sconti)

        while True:
            event, values = window.read()
            if event == 'Conferma':
                sconto = None
                if values['sconto'] != 'NONE':
                    sconto = values['sconto'][0]

                tipo = 0

                if values['categoria'] == 'Mobili':
                    tipo = 1
                elif values['categoria'] == 'Accessori':
                    tipo = 2
                elif values['categoria'] == 'Elettrodomestici':
                    tipo = 3

                db_cursor.execute(QUERIES['Aggiungi prodotto'], (
                    values[0], values[1], values[2], values[3], values[4], values[5], sconto, tipo))
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
                db.commit()
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
        db.commit()
        window.close()
        window = ordini_cliente_window(clienti)

        while True:
            event, values = window.read()

            if event == 'cliente':
                db_cursor.execute(
                    QUERIES['Visualizza ordini di un cliente'], (values['cliente'][0],))
                ordini = db_cursor.fetchall()
                db.commit()
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
                db.commit()
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
                db.commit()
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
                db.commit()
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
        db.commit()

        window.close()
        window = prodotti_piu_acquistato_window(prodotti)
    elif event == 'Visualizza 10 prodotti meno acquistati':
        db_cursor.execute(QUERIES['Visualizza 10 prodotti meno acquistati'])
        prodotti = db_cursor.fetchall()
        db.commit()

        window.close()
        window = prodotti_meno_acquistati_window(prodotti)
    elif event == 'Visualizza 10 prodotti più costosi':
        db_cursor.execute(QUERIES['Visualizza 10 prodotti più costosi'])
        prodotti = db_cursor.fetchall()
        db.commit()

        window.close()
        window = prodotti_piu_costosi_window(prodotti)
    elif event == 'Visualizza 10 prodotti meno costosi':
        db_cursor.execute(QUERIES['Visualizza 10 prodotti meno costosi'])
        prodotti = db_cursor.fetchall()
        db.commit()

        window.close()
        window = prodotti_meno_costosi_window(prodotti)
    elif event == 'Visualizza 10 alimenti porzionati più costosi':
        db_cursor.execute(
            QUERIES['Visualizza 10 alimenti porzionati più costosi'])
        prodotti = db_cursor.fetchall()
        db.commit()

        window.close()
        window = alimenti_porzionati_piu_costosi_window(prodotti)
    elif event == 'Visualizza 10 alimenti porzionati meno costosi':
        db_cursor.execute(
            QUERIES['Visualizza 10 alimenti porzionati meno costosi'])
        prodotti = db_cursor.fetchall()
        db.commit()

        window.close()
        window = alimenti_porzionati_meno_costosi_window(prodotti)
    elif event == 'Visualizza 10 alimenti confezionati più costosi':
        db_cursor.execute(
            QUERIES['Visualizza 10 alimenti confezionati più costosi'])
        prodotti = db_cursor.fetchall()
        db.commit()

        window.close()
        window = alimenti_confezionati_piu_costosi_window(prodotti)
    elif event == 'Visualizza 10 alimenti confezionati meno costosi':
        db_cursor.execute(
            QUERIES['Visualizza 10 alimenti confezionati meno costosi'])
        prodotti = db_cursor.fetchall()
        db.commit()

        window.close()
        window = alimenti_confezionati_meno_costosi_window(prodotti)
    elif event == 'Visualizza quantità prodotto nei magazzini':
        db_cursor.execute(QUERIES['Visualizza prodotti'])
        prodotti = db_cursor.fetchall()
        db.commit()
        window.close()
        window = quantita_prodotto_magazzini_window(prodotti)

        while True:
            event, values = window.read()

            if event == 'prodotto':
                db_cursor.execute(
                    QUERIES['Visualizza quantità magazzini prodotto'], (values['prodotto'][0],))
                quantita = db_cursor.fetchall()
                db.commit()
                window['quantita'].update(values=quantita)
            elif event == 'Indietro':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Visualizza prodotti terminati nei magazzini':
        db_cursor.execute(QUERIES['Visualizza prodotti terminati'])
        quantita = db_cursor.fetchall()
        db.commit()

        window.close()
        window = prodotti_terminati_window(quantita)
    elif event == 'Visualizza personale':
        db_cursor.execute(QUERIES['Visualizza personale'])
        personale = db_cursor.fetchall()
        db.commit()

        window.close()
        window = personale_window(personale)
    elif event == 'Visualizza 10 prodotti con sconto maggiore':
        db_cursor.execute(
            QUERIES['Visualizza 10 prodotti con sconto maggiore'])
        prodotti = db_cursor.fetchall()
        db.commit()

        window.close()
        window = prodotti_sconto_maggiore_window(prodotti)
    elif event == 'Visualizza ordini da una data':
        window.close()
        window = ordini_data_window()

        while True:
            event, values = window.read()

            if event == '-CAL-':
                db_cursor.execute(
                    QUERIES['Visualizza ordini dopo data'], (values['-CAL-'],))
                ordini = db_cursor.fetchall()
                db.commit()
                window['ordini'].update(values=ordini)
            elif event == 'Indietro':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Visualizza 10 ordini più costosi':
        db_cursor.execute(QUERIES['Visualizza 10 ordini più costosi'])
        ordini = db_cursor.fetchall()
        db.commit()

        window.close()
        window = ordini_costosi_window(ordini)
    elif event == 'Visualizza 10 ordini più costosi di un cliente':
        db_cursor.execute(QUERIES['Visualizza clienti'])
        clienti = db_cursor.fetchall()
        db.commit()
        window.close()
        window = ordini_costosi_cliente_window(clienti)g ad

        while True:
            event, values = window.read()

            if event == 'cliente':
                db_cursor.execute(
                    QUERIES['Visualizza 10 ordini più costosi cliente'], (values['cliente'][0],))
                ordini = db_cursor.fetchall()
                db.commit()
                window['ordini'].update(values=ordini)
            elif event == 'Indietro':
                window.close()
                window = default_window()
                break
            elif event == sg.WIN_CLOSED:
                break
    elif event == 'Aggiungi alimento':
        window.close()
        window = aggiungi_alimento_window()

        while True:
            event, values = window.read()

            if event == 'Conferma':
                db_cursor.execute(QUERIES['Aggiungi alimento'], (values['nome'], values['provenienza'], values['scadenza'],
                                  values['ingredienti'], values['allergeni'], values['prezzo_porzionato'], values['prezzo_confezionato']))
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
    elif event == 'Aggiungi composizione':
        db_cursor.execute(QUERIES['Visualizza prodotti'])
        prodotti = db_cursor.fetchall()
        db.commit()
        window.close()
        window = aggiungi_composizione_window(prodotti)

        while True:
            event, values = window.read()

            if event == 'Conferma':
                costo_totale = 0
                prodotti_composizione = values['prodotti']

                for i, prodotto in enumerate(prodotti_composizione):
                    costo_totale += prodotto[2] * \
                        int(values['quantita'].split(',')[i])

                db_cursor.execute(QUERIES['Aggiungi composizione'], (values['nome'], len(
                    prodotti_composizione), costo_totale))
                db.commit()

                cod_composizione = db_cursor.lastrowid
                for i, prodotto in enumerate(prodotti_composizione):
                    db_cursor.execute(
                        QUERIES['Aggiungi composta'], (cod_composizione, prodotto[0], int(values['quantita'].split(',')[i])))
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
    elif event == 'Aggiungi sconto':
        db_cursor.execute(QUERIES['Visualizza storico sconti'])
        storico_sconti = db_cursor.fetchall()
        db.commit()
        window.close()
        window = aggiungi_sconto_window(storico_sconti)

        while True:
            event, values = window.read()

            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Aggiungi sconto'], (values['percentuale'], values['storico'][0]))
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
    elif event == 'Aggiungi storico sconto':
        window.close()
        window = aggiungi_storico_sconto_window()

        while True:
            event, values = window.read()

            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Aggiungi storico sconti'], ('1111-' + values['-DATA INIZIO-'], '1111-' + values['-DATA FINE-']))
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
    elif event == 'Aggiungi orario':
        window.close()
        window = aggiungi_orario_window()

        while True:
            event, values = window.read()

            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Aggiungi orario'], (values[0], values[1], values[2]))
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
    elif event == 'Aggiungi confezione':
        db_cursor.execute(QUERIES['Visualizza negozi'])
        negozi = db_cursor.fetchall()
        db.commit()
        db_cursor.execute(QUERIES['Visualizza alimenti'])
        alimenti = db_cursor.fetchall()
        db.commit()
        window.close()
        window = aggiungi_confezione_window(negozi, alimenti)

        while True:
            event, values = window.read()

            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Aggiungi confezione'], (values['negozio'][0], values['alimento'][0], values['quantita']))
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
    elif event == 'Aggiungi porzione':
        db_cursor.execute(QUERIES['Visualizza negozi'])
        negozi = db_cursor.fetchall()
        db.commit()
        db_cursor.execute(QUERIES['Visualizza alimenti'])
        alimenti = db_cursor.fetchall()
        db.commit()
        window.close()
        window = aggiungi_porzione_window(negozi, alimenti)

        while True:
            event, values = window.read()

            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Aggiungi porzione'], (values['negozio'][0], values['alimento'][0]))
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
    elif event == 'Aggiungi colorazione':
        db_cursor.execute(QUERIES['Visualizza colori'])
        colori = db_cursor.fetchall()
        db.commit()
        db_cursor.execute(QUERIES['Visualizza prodotti'])
        prodotti = db_cursor.fetchall()
        db.commit()
        window.close()
        window = aggiungi_colorazione_window(colori, prodotti)

        while True:
            event, values = window.read()

            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Aggiungi colorazione'], (values['colore'][0], values['prodotto'][0]))
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
    elif event == 'Licenzia personale':
        db_cursor.execute(QUERIES['Visualizza manager'])
        manager = db_cursor.fetchall()
        db.commit()
        db_cursor.execute(QUERIES['Visualizza amministratori'])
        amministratori = db_cursor.fetchall()
        db.commit()
        db_cursor.execute(QUERIES['Visualizza tecnici'])
        tecnici = db_cursor.fetchall()
        db.commit()
        db_cursor.execute(QUERIES['Visualizza tecnici commerciali'])
        tecnici_commerciali = db_cursor.fetchall()
        db.commit()
        window.close()
        window = licenzia_personale_window(
            manager, amministratori, tecnici, tecnici_commerciali)

        while True:
            event, values = window.read()

            if event == 'Licenzia':
                for key, value in values.items():
                    for personale in value:
                        db_cursor.execute(
                            QUERIES['Licenzia ' + key], (personale[0],))
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
    elif event == 'Aggiungi colore':
        db_cursor.execute(QUERIES['Visualizza colori'])
        colori = db_cursor.fetchall()
        db.commit()
        window.close()
        window = aggiungi_colore_window(colori)

        while True:
            event, values = window.read()

            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Aggiungi colore'], (values['nome'],))
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
    elif event == 'Esponi composizione':
        db_cursor.execute(QUERIES['Visualizza composizioni'])
        composizioni = db_cursor.fetchall()
        db.commit()
        db_cursor.execute(QUERIES['Visualizza negozi'])
        negozi = db_cursor.fetchall()
        db.commit()
        window.close()
        window = esponi_composizione_window(composizioni, negozi)

        while True:
            event, values = window.read()

            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Aggiungi esposta'], (values['composizione'][0], values['negozio'][0]))
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
    elif event == 'Restock prodotto':
        db_cursor.execute(QUERIES['Visualizza prodotti'])
        prodotti = db_cursor.fetchall()
        db.commit()
        db_cursor.execute(QUERIES['Visualizza negozi'])
        negozi = db_cursor.fetchall()
        db.commit()
        window.close()
        window = restock_prodotto_window(prodotti, negozi)

        while True:
            event, values = window.read()

            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Restock prodotto'], (values['quantita'], values['prodotto'][0], values['negozio'][0]))
                db.commit()
                rows_affected = db_cursor.rowcount
                if rows_affected == 0:
                    db_cursor.execute(QUERIES['Aggiungi quantità'], (
                        values['prodotto'][0], values['negozio'][0], values['quantita']))
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
    elif event == 'Aggiungi acquirente':
        window.close()
        window = aggiungi_acquirente_window()

        while True:
            event, values = window.read()

            if event == 'Conferma':
                db_cursor.execute(
                    QUERIES['Aggiungi acquirente'], (values['codice_fiscale'], values['nome'], values['cognome'], values['telefono'], values['email'], values['via'], values['civico'], values['cap'], values['citta']))
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
    elif event == 'Indietro':
        window.close()
        window = default_window()
    elif event == sg.WIN_CLOSED:
        break

window.close()
