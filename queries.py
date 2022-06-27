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
}