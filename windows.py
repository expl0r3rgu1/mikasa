#!/usr/bin/python3

import PySimpleGUI as sg

MARGINS = (100, 30)
SIZE = (1700, 860)


def default_window():
    empty_layout = [
        [sg.Text('Mikasa')],
        [sg.Button('Aggiungi cliente'), sg.Button('Rendi socio un cliente'), sg.Button('Rendi non socio un cliente'), sg.Button(
            'Aggiungi manager'), sg.Button('Aggiungi negozio')],
        [sg.Button('Effettua ordine per cliente'), sg.Button('Aggiungi prodotto'), sg.Button('Aggiungi alimento'), sg.Button(
            'Aggiungi composizione'), sg.Button('Aggiungi sconto'), sg.Button('Aggiungi orario')],
        [sg.Button('Visualizza ordini in un mese'), sg.Button('Visualizza ordini cliente'), sg.Button('Visualizza spedizioni in un mese'), sg.Button('Visualizza ritiri in un mese'), sg.Button('Visualizza montaggi in un mese')],
        [sg.Button('Visualizza prodotto più acquistato'), sg.Button('Visualizza prodotto meno acquistato'), sg.Button('Visualizza prodotto più costoso'), sg.Button('Visualizza prodotto meno costoso'), sg.Button('Visualizza alimento porzionato più costoso')],
        [sg.Button('Visualizza alimento confezionato più costoso'), sg.Button('Visualizza quantità prodotto nei magazzini'), sg.Button('Visualizza prodotti terminati nei magazzini'), sg.Button('Visualizza personale'), sg.Button('Visualizza prodotti con sconto maggiore')],
        [sg.Button('Visualizza clienti'), sg.Button('Visualizza ordini da una data'), sg.Button('Visualizza ordine più costoso'), sg.Button('Visualizza ordine più costoso di un cliente')]
    ]

    return sg.Window('Mikasa', empty_layout, margins=MARGINS, size=SIZE, element_justification='c', resizable=False, finalize=True)


def clienti_window(clienti):
    table = sg.Table(values=clienti, headings=['Codice Fiscale', 'Nome', 'Cognome',
                                               'Telefono', 'E-mail', 'Via', 'Civico', 'CAP', 'CITTÀ'])
    layout = [
        [sg.Text('Clienti')],
        [table],
        [sg.Button('Indietro')]
    ]
    return sg.Window('Clienti', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)

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

def aggiungi_manager_window(negozi):
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
        [sg.Text('Negozio'), sg.Combo(negozi, default_value=negozi[0], key='negozio')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi manager', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)