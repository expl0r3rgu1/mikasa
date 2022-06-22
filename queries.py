QUERIES = {
    'get_all_users': 'SELECT * FROM users',
    'Visualizza clienti' : 'SELECT P.*, C.socio FROM clienti C, persone P WHERE C.cf_cliente = P.cf',
    'Aggiungi cliente' : 'INSERT INTO clienti (cf_cliente, socio) VALUES (%s, 0)',
    'Aggiungi persona' : 'INSERT INTO persone (cf, nome, cognome, telefono, email, via, civico, cap, città) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
    'Rendi socio un cliente' : 'UPDATE clienti SET socio = 1 WHERE cf_cliente = %s',

}