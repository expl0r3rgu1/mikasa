#!/usr/bin/python3

import PySimpleGUI as sg

MARGINS = (100, 30)
SIZE = (1700, 860)


def default_window():
    empty_layout = [
        [sg.Text('Mikasa')],
        [sg.Button('Aggiungi cliente'), sg.Button('Rendi socio un cliente'), sg.Button('Rendi non socio un cliente'), sg.Button(
            'Aggiungi manager'), sg.Button('Aggiungi tecnico'), sg.Button('Aggiungi Tecnico commerciale'), sg.Button('Aggiungi amministratore'), sg.Button('Aggiungi negozio')],
        [sg.Button('Effettua ordine per cliente'), sg.Button('Aggiungi prodotto'), sg.Button('Aggiungi alimento'), sg.Button(
            'Aggiungi composizione'), sg.Button('Aggiungi sconto'), sg.Button('Aggiungi orario')],
        [sg.Button('Visualizza ordini in un mese'), sg.Button('Visualizza ordini cliente'), sg.Button(
            'Visualizza spedizioni in un mese'), sg.Button('Visualizza ritiri in un mese'), sg.Button('Visualizza montaggi in un mese')],
        [sg.Button('Visualizza prodotto più acquistato'), sg.Button('Visualizza prodotto meno acquistato'), sg.Button(
            'Visualizza prodotto più costoso'), sg.Button('Visualizza prodotto meno costoso'), sg.Button('Visualizza alimento porzionato più costoso')],
        [sg.Button('Visualizza alimento confezionato più costoso'), sg.Button('Visualizza quantità prodotto nei magazzini'), sg.Button(
            'Visualizza prodotti terminati nei magazzini'), sg.Button('Visualizza personale'), sg.Button('Visualizza prodotti con sconto maggiore')],
        [sg.Button('Visualizza clienti'), sg.Button('Visualizza ordini da una data'), sg.Button(
            'Visualizza ordine più costoso'), sg.Button('Visualizza ordine più costoso di un cliente')]
    ]

    return sg.Window('Mikasa', empty_layout, margins=MARGINS, size=SIZE, element_justification='c', resizable=False, finalize=True)


def aggiungi_cliente_window():
    layout = [
        [sg.Text('Aggiungi cliente')],
        [sg.Text('Codice Fiscale'), sg.InputText()],
        [sg.Text('Nome'), sg.InputText()],
        [sg.Text('Cognome'), sg.InputText()],
        [sg.Text('Telefono'), sg.InputText()],
        [sg.Text('E-mail'), sg.InputText()],
        [sg.Text('Via'), sg.InputText()],
        [sg.Text('Civico'), sg.InputText()],
        [sg.Text('CAP'), sg.InputText()],
        [sg.Text('Città'), sg.InputText()],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi cliente', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def rendi_socio_cliente_window(clienti):
    layout = [
        [sg.Text('Iscrivi cliente')],
        [sg.Combo(clienti, default_value=clienti[0], key='cliente')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Iscrivi cliente', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def rendi_non_socio_cliente_window(clienti):
    layout = [
        [sg.Text('Rendi non socio un cliente')],
        [sg.Combo(clienti, default_value=clienti[0], key='cliente')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Rendi non socio un cliente', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_personale_window(negozi):
    layout = [
        [sg.Text('Aggiungi manager')],
        [sg.Text('Codice Fiscale'), sg.InputText()],
        [sg.Text('Nome'), sg.InputText()],
        [sg.Text('Cognome'), sg.InputText()],
        [sg.Text('Telefono'), sg.InputText()],
        [sg.Text('E-mail'), sg.InputText()],
        [sg.Text('Via'), sg.InputText()],
        [sg.Text('Civico'), sg.InputText()],
        [sg.Text('CAP'), sg.InputText()],
        [sg.Text('Città'), sg.InputText()],
        [sg.Text('Salario'), sg.InputText()],
        [sg.Text('Negozio'), sg.Combo(
            negozi, default_value=negozi[0], key='negozio')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi manager', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_amministratore_window(negozi, zone):
    layout = [
        [sg.Text('Aggiungi manager')],
        [sg.Text('Codice Fiscale'), sg.InputText()],
        [sg.Text('Nome'), sg.InputText()],
        [sg.Text('Cognome'), sg.InputText()],
        [sg.Text('Telefono'), sg.InputText()],
        [sg.Text('E-mail'), sg.InputText()],
        [sg.Text('Via'), sg.InputText()],
        [sg.Text('Civico'), sg.InputText()],
        [sg.Text('CAP'), sg.InputText()],
        [sg.Text('Città'), sg.InputText()],
        [sg.Text('Salario'), sg.InputText()],
        [sg.Text('Negozio'), sg.Combo(
            negozi, default_value=negozi[0], key='negozio')],
        [sg.Text('Zona'), sg.Combo(zone, default_value=zone[0], key='zona')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi manager', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_negozio_window(acquirenti):
    layout = [
        [sg.Text('Aggiungi negozio')],
        [sg.Text('Via'), sg.InputText()],
        [sg.Text('Civico'), sg.InputText()],
        [sg.Text('CAP'), sg.InputText()],
        [sg.Text('Città'), sg.InputText()],
        [sg.In(key='-CAL-', enable_events=True, visible=False),
         sg.CalendarButton('Data inaugurazione', target='-CAL-')],
        [sg.Text('Acquirente'), sg.Combo(
            acquirenti, default_value=acquirenti[0], key='acquirente')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi negozio', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def effettua_ordine_cliente_window(clienti, prodotti, composizioni, negozi):
    layout = [
        [sg.Text('Effettua ordine')],
        [sg.Combo(clienti, default_value=clienti[0], key='cliente')],
        [sg.Text('Prodotti'), sg.Text('Composizioni')],
        [sg.Listbox(values=prodotti, select_mode='extended', key='prodotti', size=(0, 10)), sg.Listbox(
            values=composizioni, select_mode='extended', key='composizioni', size=(0, 10))],
        [sg.Text('Quantità prodotti (10,4,...):'), sg.InputText(key='quantità_prodotti'), sg.Text(
            'Quantità composizioni (10,4,...):'), sg.InputText(key='quantità_composizioni')],
        [sg.Combo(['Con spedizione', 'senza spedizione'],
                  default_value='Con spedizione', key='spedizione', enable_events=True)],
        [sg.Combo(['Con montaggio', 'senza montaggio'],
                  default_value='Con montaggio', key='montaggio')],
        [sg.Text('Indirizzo di consegna'), sg.InputText(key='indirizzo')],
        [sg.Combo(negozi, default_value=negozi[0], key='negozio')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Effettua ordine', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_prodotto_window(sconti):
    categories = ['Accessori', 'Mobili', 'Elettrodomestici']
    layout = [
        [sg.Text('Aggiungi prodotto')],
        [sg.Text('Categoria'), sg.Combo(
            categories, default_value=categories[0], key='categoria')],
        [sg.Text('Nome'), sg.InputText()],
        [sg.Text('Prezzo'), sg.InputText()],
        [sg.Text('Altezza'), sg.InputText()],
        [sg.Text('Larghezza'), sg.InputText()],
        [sg.Text('Profondità'), sg.InputText()],
        [sg.Text('Peso'), sg.InputText()],
        [sg.Text('Sconto'), sg.Combo(
            sconti, default_value='NONE', key='sconto')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi prodotto', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)

# VISUALIZZAZIONE


def clienti_window(clienti):
    table = sg.Table(values=clienti, headings=['Codice Fiscale', 'Nome', 'Cognome',
                                               'Telefono', 'E-mail', 'Via', 'Civico', 'CAP', 'CITTÀ'])
    layout = [
        [sg.Text('Clienti')],
        [table],
        [sg.Button('Indietro')]
    ]
    return sg.Window('Clienti', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def ordini_mese_window():

    table = sg.Table(key='ordini', values=[], headings=['Codice Ordine', 'Data effettuazione', 'Costo totale',
                     'Peso totale', 'Data arrivo', 'Codice Fiscale Cliente', 'Codice Fiscale tecnico commerciale'])

    layout = [
        [sg.Text('Ordini in un mese')],
        [sg.In(key='-CAL-', enable_events=True, visible=False),
         sg.CalendarButton('Mese', target='-CAL-', format='%Y-%m')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Ordini in un mese', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def ordini_cliente_window(clienti):
    table = sg.Table(key='ordini', values=[], headings=['Codice Ordine', 'Data effettuazione', 'Costo totale',
                     'Peso totale', 'Data arrivo', 'Codice Fiscale Cliente', 'Codice Fiscale tecnico commerciale'])

    layout = [
        [sg.Text('Ordini di un cliente')],
        [sg.Combo(clienti, default_value=clienti[0],
                  key='cliente', enable_events=True)],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Ordini di un cliente', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def spedizioni_mese_window():
    table = sg.Table(key='spedizioni', values=[], headings=[
                     'Codice Ordine', 'Indirizzo', 'Codice Fiscale tecnico', 'Data effettuazione', 'Data arrivo'])

    layout = [
        [sg.Text('Spedizioni in un mese')],
        [sg.In(key='-CAL-', enable_events=True, visible=False),
         sg.CalendarButton('Mese', target='-CAL-', format='%Y-%m')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Spedizioni in un mese', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)

def ritiri_mese_window():
    table = sg.Table(key='ritiri', values=[], headings=[
                     'Codice Ordine', 'Codice Negozio', 'Data effettuazione', 'Data arrivo'])

    layout = [
        [sg.Text('Ritiri in un mese')],
        [sg.In(key='-CAL-', enable_events=True, visible=False),
         sg.CalendarButton('Mese', target='-CAL-', format='%Y-%m')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Ritiri in un mese', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)