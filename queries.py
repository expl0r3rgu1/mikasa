QUERIES = {
    'Visualizza clienti' : 'SELECT P.*, C.socio FROM clienti C, persone P WHERE C.cf_cliente = P.cf',
    'Aggiungi cliente' : 'INSERT INTO clienti (cf_cliente, socio) VALUES (%s, 0)',
    'Aggiungi persona' : 'INSERT INTO persone (cf, nome, cognome, telefono, email, via, civico, cap, città) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
    'Aggiungi personale' : 'INSERT INTO personale (cf_personale, salario, cod_orario) VALUES (%s, %s, %s)',
    'Aggiungi manager' : 'INSERT INTO manager(cf_manager, cod_negozio) VALUES (%s, %s)',
    'Aggiungi impiegati' : 'INSERT INTO impiegati(cf_impiegato) VALUES (%s)',
    'Aggiungi amministratori' : 'INSERT INTO amministratori(cf_amministratore, cod_zona, cod_negozio) VALUES (%s, %s, %s)',
    'Aggiungi tecnico' : 'INSERT INTO tecnici(cf_tecnico, cod_negozio, cod_magazzino) VALUES (%s, %s,%s)',
    'Aggiungi tecnico commerciale': 'INSERT INTO tecnici_commerciali(cf_tecnico_commerciale, cod_negozio, cod_alimentari, cod_ristoro) VALUES (%s, %s, %s, %s)',
    'Aggiungi negozio' : 'INSERT INTO negozi (cf_negozio, via, civico, cap, città) VALUES (%s, %s, %s, %s, %s)',
    'Rendi socio un cliente' : 'UPDATE clienti SET socio = 1 WHERE cf_cliente = %s',
    'Rendi non socio un cliente' : 'UPDATE clienti SET socio = 0 WHERE cf_cliente = %s',
    'Effettuazione ordine' : 'INSERT INTO ordini (cod_ordine, data_effetuazione, costo_totale, peso_totale, sconto_totale, data_arrivo, cod_cliente, cod_tecnico_commerciale) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    'Effettuazione ordine senza spedizione' : 'INSERT INTO ordini_no_spedizione(cod_ordine, cod_negozio) VALUES (%s, %s)',
    'Effettuazione ordine con spedizione' : 'INSERT INTO ordini_con_spedizione(cod_ordine, indirizzo, cf_tecnico) VALUES (%s, %s, %s)',
    'Effettuazione ordini con montaggio' : 'INSERT INTO ordini_con_montaggio(cod_ordine, indirizzo, cf_tecnico) VALUES (%s, %s, %s)',
    'Effettuazione ordini senza montaggio' : 'INSERT INTO ordini_no_montaggio(cod_ordine) VALUES (%s)',
    'Aggiungere prodotto' : 'INSERT INTO prodotti(cod_prodotto, nome, prezzo, altezza, larghezza, profondità, peso, cod_sconto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    'Aggiungere accessorio' : 'INSERT INTO accessori(cod_prodotto) VALUES (%s)',
    'Aggiungere mobili' : 'INSERT INTO mobili(cod_prodotto) VALUES (%s)',
    'Aggiungere elettrodomestici' : 'INSERT INTO elettrodomestici(cod_prodotto) VALUES (%s)',
    'Aggiungere alimento' : 'INSERT INTO alimenti(cod_alimento, nome, provenienza, scadenza, ingredienti, allergeni, prezzo_porzionato, prezzo_confezionato) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    'Aggiungere composizione' : 'INSERT INTO composizioni(cod_composizione, nome, num_prodotti, peso) VALUES (%s, %s, %s, %s)',
    'Aggiungere composta' : 'INSERT INTO composte(cod_negozio, cod_esposizione, cod_composizione, cod_prodotto) VALUES (%s, %s, %s, %s)',

}