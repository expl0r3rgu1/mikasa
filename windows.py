#!/usr/bin/python3

import PySimpleGUI as sg

MARGINS = (100, 30)


def default_window():
    empty_layout = [
        [sg.Text('Gestisci personale')],
        [sg.Button('Visualizza personale'), sg.Button('Aggiungi manager'), sg.Button('Aggiungi amministratore'), sg.Button(
            'Aggiungi tecnico'), sg.Button('Aggiungi tecnico commerciale'), sg.Button('Licenzia personale')],
        [sg.Text('Gestisci Prodotti')],
        [sg.Button('Aggiungi prodotto'), sg.Button('Aggiungi sconto'), sg.Button('Aggiungi storico sconto'), sg.Button('Aggiungi composizione'), sg.Button(
            'Restock prodotto'), sg.Button('Esponi composizione'), sg.Button('Aggiungi colore'), sg.Button('Aggiungi colorazione')],
        [sg.Text('Gestisci clienti')],
        [sg.Button('Visualizza clienti'), sg.Button('Aggiungi cliente'), sg.Button('Rendi socio un cliente'), sg.Button('Rendi non socio un cliente'), sg.Button(
            'Visualizza ordini cliente'), sg.Button('Effettua ordine per cliente'), sg.Button('Visualizza 10 ordini più costosi di un cliente')],
        [sg.Text('Gestisci ordini')],
        [sg.Button('Visualizza ordini in un mese'), sg.Button('Visualizza spedizioni in un mese'), sg.Button('Visualizza ritiri in un mese'), sg.Button(
            'Visualizza montaggi in un mese'), sg.Button('Visualizza ordini da una data'), sg.Button('Visualizza 10 ordini più costosi')],
        [sg.Text('Gestisci negozi')],
        [sg.Button('Aggiungi acquirente'), sg.Button('Aggiungi negozio'), sg.Button('Aggiungi alimento'), sg.Button('Aggiungi orario'), sg.Button('Aggiungi confezione'), sg.Button(
            'Aggiungi porzione'), sg.Button('Visualizza quantità prodotto nei magazzini'), sg.Button('Visualizza prodotti terminati nei magazzini')],
        [sg.Text('Statistiche')],
        [sg.Button('Visualizza 10 prodotti più acquistati'), sg.Button('Visualizza 10 prodotti meno acquistati'), sg.Button('Visualizza 10 prodotti più costosi'), sg.Button(
            'Visualizza 10 prodotti meno costosi'), sg.Button('Visualizza 10 alimenti porzionati più costosi')],
        [sg.Button('Visualizza 10 alimenti porzionati meno costosi'), sg.Button('Visualizza 10 alimenti confezionati più costosi'), sg.Button(
            'Visualizza 10 alimenti confezionati meno costosi'), sg.Button('Visualizza 10 prodotti con sconto maggiore')]
    ]

    return sg.Window('Mikasa', empty_layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


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
        [sg.Text('Aggiungi manager o tecnico o tecnico commerciale')],
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

    return sg.Window('Aggiungi manager o tecnico o tecnico commerciale', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_amministratore_window(negozi, zone):
    layout = [
        [sg.Text('Aggiungi amministratore')],
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

    return sg.Window('Aggiungi amministratore', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_negozio_window(acquirenti):
    layout = [
        [sg.Text('Aggiungi negozio')],
        [sg.Text('Via'), sg.InputText()],
        [sg.Text('Civico'), sg.InputText()],
        [sg.Text('CAP'), sg.InputText()],
        [sg.Text('Città'), sg.InputText()],
        [sg.In(key='-CAL-', enable_events=True, disabled=True),
         sg.CalendarButton('Data inaugurazione', target='-CAL-', format='%Y-%m-%d')],
        [sg.Text('Acquirente'), sg.Combo(
            acquirenti, default_value=acquirenti[0], key='acquirente')],
        [sg.Text('Numero posti ristoro'),
         sg.InputText(key='num_posti_ristoro')],
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
                  key='spedizione', enable_events=True)],
        [sg.Combo(['Con montaggio', 'senza montaggio'],
                  default_value='senza montaggio', key='montaggio')],
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
        [sg.In(key='-CAL-', enable_events=True, disabled=True),
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
        [sg.Combo(clienti, key='cliente', enable_events=True)],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Ordini di un cliente', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def spedizioni_mese_window():
    table = sg.Table(key='spedizioni', values=[], headings=[
                     'Codice Ordine', 'Indirizzo', 'Codice Fiscale tecnico', 'Data effettuazione', 'Data arrivo'])

    layout = [
        [sg.Text('Spedizioni in un mese')],
        [sg.In(key='-CAL-', enable_events=True, disabled=True),
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
        [sg.In(key='-CAL-', enable_events=True, disabled=True),
         sg.CalendarButton('Mese', target='-CAL-', format='%Y-%m')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Ritiri in un mese', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def montaggi_mese_window():
    table = sg.Table(key='montaggi', values=[], headings=[
                     'Codice Ordine', 'Data arrivo'])

    layout = [
        [sg.Text('Montaggi in un mese')],
        [sg.In(key='-CAL-', enable_events=True, disabled=True),
         sg.CalendarButton('Mese', target='-CAL-', format='%Y-%m')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Montaggi in un mese', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def prodotti_piu_acquistato_window(prodotti):
    table = sg.Table(values=prodotti, headings=[
                     'Codice', 'Nome', 'Prezzo', 'Altezza', 'Larghezza', 'Profondità', 'Peso', 'Codice Sconto'])

    layout = [
        [sg.Text('Top 10 prodotti più acquistati')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Top 10 prodotti più acquistati', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def prodotti_meno_acquistati_window(prodotti):
    table = sg.Table(values=prodotti, headings=[
                     'Codice', 'Nome', 'Prezzo', 'Altezza', 'Larghezza', 'Profondità', 'Peso', 'Codice Sconto', 'Tipo'])

    layout = [
        [sg.Text('Top 10 prodotti meno acquistati')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Top 10 prodotti meno acquistati', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def prodotti_piu_costosi_window(prodotti):
    table = sg.Table(values=prodotti, headings=[
                     'Codice', 'Nome', 'Prezzo', 'Altezza', 'Larghezza', 'Profondità', 'Peso', 'Codice Sconto', 'Tipo'])

    layout = [
        [sg.Text('Top 10 prodotti più costosi')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Top 10 prodotti più costosi', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def prodotti_meno_costosi_window(prodotti):
    table = sg.Table(values=prodotti, headings=[
                     'Codice', 'Nome', 'Prezzo', 'Altezza', 'Larghezza', 'Profondità', 'Peso', 'Codice Sconto', 'Tipo'])

    layout = [
        [sg.Text('Top 10 prodotti meno costosi')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Top 10 prodotti meno costosi', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def alimenti_porzionati_piu_costosi_window(alimenti):
    table = sg.Table(values=alimenti, headings=[
                     'Codice', 'Nome', 'Provenienza', 'Scadenza', 'Ingredienti', 'Allergeni', 'Prezzo Porzionato', 'Prezzo confezionato'])

    layout = [
        [sg.Text('Top 10 alimenti porzionati più costosi')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Top 10 alimenti porzionati più costosi', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def alimenti_porzionati_meno_costosi_window(alimenti):
    table = sg.Table(values=alimenti, headings=[
                     'Codice', 'Nome', 'Provenienza', 'Scadenza', 'Ingredienti', 'Allergeni', 'Prezzo Porzionato', 'Prezzo confezionato'])

    layout = [
        [sg.Text('Top 10 alimenti porzionati meno costosi')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Top 10 alimenti porzionati meno costosi', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def alimenti_confezionati_piu_costosi_window(alimenti):
    table = sg.Table(values=alimenti, headings=[
                     'Codice', 'Nome', 'Provenienza', 'Scadenza', 'Ingredienti', 'Allergeni', 'Prezzo Porzionato', 'Prezzo confezionato'])

    layout = [
        [sg.Text('Top 10 alimenti confezionati più costosi')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Top 10 alimenti confezionati più costosi', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def alimenti_confezionati_meno_costosi_window(alimenti):
    table = sg.Table(values=alimenti, headings=[
                     'Codice', 'Nome', 'Provenienza', 'Scadenza', 'Ingredienti', 'Allergeni', 'Prezzo Porzionato', 'Prezzo confezionato'])

    layout = [
        [sg.Text('Top 10 alimenti confezionati meno costosi')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Top 10 alimenti confezionati meno costosi', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def quantita_prodotto_magazzini_window(prodotti):
    table = sg.Table(key='quantita', values=[], headings=[
                     'Codice Negozio', 'Quantità'])

    layout = [
        [sg.Text('Quantità prodotto nei magazzini')],
        [sg.Combo(prodotti, key='prodotto', enable_events=True)],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Quantità prodotto nei magazzini', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def prodotti_terminati_window(quantita):
    table = sg.Table(values=quantita, headings=[
                     'Codice Negozio', 'Codice Prodotto', 'Nome Prodotto', 'Tipo'])

    layout = [
        [sg.Text('Prodotti terminati')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Prodotti terminati', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def personale_window(personale):
    table = sg.Table(values=personale, headings=[
                     'Codice Fiscale', 'Nome', 'Cognome'])

    layout = [
        [sg.Text('Personale')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Personale', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def prodotti_sconto_maggiore_window(prodotti):
    table = sg.Table(values=prodotti, headings=[
                     'Codice', 'Tipo', 'Nome', 'Codice Sconto', 'Percentuale Sconto'])

    layout = [
        [sg.Text('Top 10 prodotti con sconto maggiore')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Top 10 prodotti con sconto maggiore', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def ordini_data_window():
    table = sg.Table(key='ordini', values=[], headings=['Codice Ordine', 'Data effettuazione', 'Costo totale',
                     'Peso totale', 'Data arrivo', 'Codice Fiscale Cliente', 'Codice Fiscale tecnico commerciale'])

    layout = [
        [sg.Text('Ordini da una data')],
        [sg.In(key='-CAL-', enable_events=True, disabled=True),
         sg.CalendarButton('Data', target='-CAL-', format='%Y-%m-%d')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Ordini da una data', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def ordini_costosi_window(ordini):
    table = sg.Table(values=ordini, headings=['Codice Ordine', 'Data effettuazione', 'Costo totale',
                     'Peso totale', 'Data arrivo', 'Codice Fiscale Cliente', 'Codice Fiscale tecnico commerciale'])

    layout = [
        [sg.Text('Top 10 Ordini più costosi')],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Top 10 ordini più costosi', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def ordini_costosi_cliente_window(clienti):
    table = sg.Table(key='ordini', values=[], headings=['Codice Ordine', 'Data effettuazione', 'Costo totale',
                     'Peso totale', 'Data arrivo', 'Codice Fiscale Cliente', 'Codice Fiscale tecnico commerciale'])

    layout = [
        [sg.Text('Top 10 ordini più costosi di un cliente')],
        [sg.Combo(clienti, key='cliente', enable_events=True)],
        [table],
        [sg.Button('Indietro')]
    ]

    return sg.Window('Top 10 ordini più costosi di un cliente', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_alimento_window():
    layout = [
        [sg.Text('Aggiungi alimento')],
        [sg.Text('Nome'), sg.Input(key='nome')],
        [sg.Text('Provenienza'), sg.Input(key='provenienza')],
        [sg.Text('Scadenza'), sg.Input(key='scadenza')],
        [sg.Text('Ingredienti'), sg.Input(key='ingredienti')],
        [sg.Text('Allergeni'), sg.Input(key='allergeni')],
        [sg.Text('Prezzo Porzionato'), sg.Input(key='prezzo_porzionato')],
        [sg.Text('Prezzo confezionato'), sg.Input(key='prezzo_confezionato')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi alimento', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_composizione_window(prodotti):
    layout = [
        [sg.Text('Aggiungi composizione')],
        [sg.Text('Nome'), sg.Input(key='nome')],
        [sg.Text('Prodotti')],
        [sg.Listbox(values=prodotti, select_mode='extended',
                    key='prodotti', size=(30, 10))],
        [sg.Text('Quantità prodotti (10,4,...):'),
         sg.InputText(key='quantita')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi composizione', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_sconto_window(storico_sconti):
    layout = [
        [sg.Text('Aggiungi sconto')],
        [sg.Text('Percentuale'), sg.Input(key='percentuale')],
        [sg.Text('Storico sconto'), sg.Combo(storico_sconti, key='storico')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi sconto', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_storico_sconto_window():
    layout = [
        [sg.Text('Aggiungi storico sconto')],
        [sg.Text('Data inizio'), sg.In(key='-DATA INIZIO-', enable_events=True, disabled=True),
         sg.CalendarButton('Data inizio', target='-DATA INIZIO-', format='%m-%d')],
        [sg.Text('Data fine'), sg.In(key='-DATA FINE-', enable_events=True, disabled=True),
         sg.CalendarButton('Data fine', target='-DATA FINE-', format='%m-%d')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi storico sconto', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_orario_window():
    layout = [
        [sg.Text('Aggiungi orario')],
        [sg.Text('Giorni'), sg.InputText()],
        [sg.Text('Ore inizio'), sg.InputText()],
        [sg.Text('Ore fine'), sg.InputText()],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi orario', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_confezione_window(negozi, alimenti):
    layout = [
        [sg.Text('Aggiungi confezione')],
        [sg.Text('Negozio'), sg.Combo(negozi, key='negozio')],
        [sg.Text('Alimenti'), sg.Combo(alimenti, key='alimento', size=(60, 1))],
        [sg.Text('Quantità'), sg.InputText(key='quantita')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi confezione', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_porzione_window(negozi, alimenti):
    layout = [
        [sg.Text('Aggiungi porzione')],
        [sg.Text('Negozio'), sg.Combo(negozi, key='negozio')],
        [sg.Text('Alimenti'), sg.Combo(alimenti, key='alimento', size=(60, 1))],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi porzione', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_colorazione_window(colori, prodotti):
    layout = [
        [sg.Text('Aggiungi colorazione')],
        [sg.Text('Colori'), sg.Combo(colori, key='colore')],
        [sg.Text('Prodotti'), sg.Combo(prodotti, key='prodotto')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi colorazione', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def licenzia_personale_window(manager, amministratori, tecnici, tecnici_commerciali):
    layout = [
        [sg.Text('Licenzia personale')],
        [sg.Text('Manager'), sg.Listbox(values=manager,
                                        select_mode='extended', key='manager', size=(0, 10))],
        [sg.Text('Amministratori'), sg.Listbox(values=amministratori,
                                               select_mode='extended', key='amministratore', size=(0, 10))],
        [sg.Text('Tecnici'), sg.Listbox(values=tecnici,
                                        select_mode='extended', key='tecnico', size=(0, 10))],
        [sg.Text('Tecnici commerciali'), sg.Listbox(
            values=tecnici_commerciali, select_mode='extended', key='tecnico commerciale', size=(0, 10))],
        [sg.Button('Licenzia'), sg.Button('Annulla')]
    ]

    return sg.Window('Licenzia personale', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_colore_window(colori):
    table = sg.Table(values=colori, headings=['Codice', 'Nome'])

    layout = [
        [sg.Text('Aggiungi colore')],
        [sg.Text('Colori esistenti')],
        [table],
        [sg.Text('Nome'), sg.InputText(key='nome')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi colore', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def esponi_composizione_window(composizioni, negozi):
    table = sg.Table(values=composizioni, headings=['Codice', 'Nome'])

    layout = [
        [sg.Text('Esponi composizione')],
        [sg.Text('Composizioni'), sg.Combo(composizioni, key='composizione')],
        [sg.Text('Negozio'), sg.Combo(negozi, key='negozio')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Esponi composizione', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def restock_prodotto_window(prodotti, negozi):
    layout = [
        [sg.Text('Restock prodotto')],
        [sg.Text('Prodotti'), sg.Combo(prodotti, key='prodotto')],
        [sg.Text('Negozio'), sg.Combo(negozi, key='negozio')],
        [sg.Text('Quantità'), sg.InputText(key='quantita')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Restock prodotto', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)


def aggiungi_acquirente_window():
    layout = [
        [sg.Text('Aggiungi acquirente')],
        [sg.Text('Codice fiscale'), sg.InputText(key='codice_fiscale')],
        [sg.Text('Nome'), sg.InputText(key='nome')],
        [sg.Text('Cognome'), sg.InputText(key='cognome')],
        [sg.Text('Indirizzo'), sg.InputText(key='indirizzo')],
        [sg.Text('Telefono'), sg.InputText(key='telefono')],
        [sg.Text('Email'), sg.InputText(key='email')],
        [sg.Text('Via'), sg.InputText(key='via')],
        [sg.Text('Civico'), sg.InputText(key='civico')],
        [sg.Text('CAP'), sg.InputText(key='cap')],
        [sg.Text('Città'), sg.InputText(key='citta')],
        [sg.Button('Conferma'), sg.Button('Annulla')]
    ]

    return sg.Window('Aggiungi acquirente', layout, margins=MARGINS, element_justification='c', resizable=False, finalize=True)
