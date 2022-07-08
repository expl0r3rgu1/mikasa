QUERIES = {
    'Visualizza clienti': 'SELECT * FROM clienti',
    'Aggiungi cliente': 'INSERT INTO clienti(cf_cliente, nome, cognome, telefono, email, via, civico, cap, città, socio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 0)',
    'Aggiungi manager': 'INSERT INTO manager(cf_manager, nome, cognome, telefono, email, via, civico, cap, città, salario, cod_negozio, cod_orario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
    'Aggiungi amministratore': 'INSERT INTO amministratori(cf_amministratore, nome, cognome, telefono, email, via, civico, cap, città, salario, cod_orario, cod_negozio, cod_zona) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
    'Aggiungi tecnico': 'INSERT INTO tecnici(cf_tecnico, nome, cognome, telefono, email, via, civico, cap, città, salario, cod_orario, cod_negozio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
    'Aggiungi tecnico commerciale': 'INSERT INTO tecnici_commerciali(cf_tecnico_commerciale, nome, cognome, telefono, email, via, civico, cap, città, salario, cod_orario, cod_negozio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
    'Aggiungi negozio': 'INSERT INTO negozi(via, civico, cap, città, data_inaugurazione, cf_acquirente, cod_orario, num_posti_ristoro, num_composizioni) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
    'Rendi socio un cliente': 'UPDATE clienti SET socio = 1 WHERE cf_cliente = %s',
    'Rendi non socio un cliente': 'UPDATE clienti SET socio = 0 WHERE cf_cliente = %s',
    'Effettua ordine' : 'INSERT INTO ordini(data_effettuazione, costo_totale, peso_totale, data_arrivo, cf_cliente, cf_tecnico_commerciale) VALUES (%s, %s, %s, %s, %s, %s)',
    'Aggiungi spedizione': 'INSERT INTO spedizioni(cod_ordine, indirizzo, cf_tecnico) VALUES (%s, %s, %s)',
    'Aggiungi montaggio': 'INSERT INTO montaggi(cod_ordine) VALUES (%s)',
    'Aggiungi dettaglio montaggio' : 'INSERT INTO dettagli_montaggio(cf_tecnico, cod_ordine) VALUES (%s, %s)',
    'Aggiungi dettaglio prodotto' : 'INSERT INTO dettagli_prodotto (cod_ordine, cod_prodotto, quantità, prezzo_totale, peso_totale) VALUES ',
    'Aggiungi dettaglio composizione' : 'INSERT INTO dettagli_composizione (cod_ordine, cod_composizione, quantità, prezzo_totale, peso_totale) VALUES ',
    'Aggiungi prodotto': 'INSERT INTO prodotti(nome, prezzo, altezza, larghezza, profondità, peso, cod_sconto, tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    'Aggiungi alimento': 'INSERT INTO alimenti(nome, provenienza, scadenza, ingredienti, allergeni, prezzo_porzionato, prezzo_confezionato) VALUES (%s, %s, %s, %s, %s, %s, %s)',
    'Aggiungi composizione': 'INSERT INTO composizioni(nome, num_prodotti, peso) VALUES (%s, %s, %s)',
    'Aggiungi composta': 'INSERT INTO composte(cod_composizione, cod_prodotto) VALUES (%s, %s)',
    'Aggiungi sconto': 'INSERT INTO sconti(percentuale, cod_storico) VALUES (%s, %s)',
    'Aggiungi storico sconti': 'INSERT INTO storico_sconti(inizio, fine) VALUES (%s, %s)',
    'Visualizza se cliente è socio' : 'SELECT c.socio FROM clienti c WHERE c.cf_cliente = %s',
    'Visualizza ordini in un mese': 'SELECT * FROM ordini WHERE YEAR(data_effettuazione) = %s AND MONTH(data_effettuazione) = %s',
    'Visualizza ordini di un cliente': 'SELECT * FROM ordini WHERE cf_cliente = %s',
    'Visualizza ritiri' : 'SELECT s.cod_ordine, s.cod_negozio, o.data_effettuazione FROM spedizioni s, ordini o WHERE NOT EXISTS s.cod_ordine = o.cod_ordine',
    'Visualizza spedizioni in un mese': 'SELECT s.cod_ordine, s.indirizzo, s.cf_tecnico, o.data_effettuazione, o.data_arrivo FROM spedizioni s, ordini o WHERE YEAR(o.data_effettuazione) = %s AND MONTH(o.data_effettuazione) = %s AND o.cod_ordine = s.cod_ordine',
    'Visualizza montaggi in un mese': 'SELECT m.cod_ordine, o.data_arrivo FROM montaggi m, ordini o, spedizioni s WHERE YEAR(o.data_arrivo) = %s AND MONTH(o.data_arrivo) = %s AND o.cod_ordine = s.cod_ordine AND s.cod_ordine = m.cod_ordine',
    'Visualizza 10 prodotti più acquistati' : 'SELECT p.*, SUM(CASE WHEN p.cod_prodotto = d.cod_prodotto THEN d.quantità ELSE 0 END) AS quantità FROM prodotti p, dettagli_prodotto d WHERE p.cod_prodotto = d.cod_prodotto GROUP BY p.cod_prodotto ORDER BY quantità DESC LIMIT 10',
    'Visualizza 10 prodotti meno acquistati' : 'SELECT p.*, SUM(CASE WHEN p.cod_prodotto = d.cod_prodotto THEN d.quantità ELSE 0 END) AS quantità FROM prodotti p, dettagli_prodotto d WHERE p.cod_prodotto = d.cod_prodotto GROUP BY p.cod_prodotto ORDER BY quantità ASC LIMIT 10',
    'Visualizza 10 prodotti più costosi' : 'SELECT p.* FROM prodotti p ORDER BY prezzo DESC LIMIT 10',
    'Visualizza 10 prodotti meno costosi' : 'SELECT p.* FROM prodotti p ORDER BY prezzo ASC LIMIT 10',
    'Visualizza 10 alimenti porzionati più costosi' : 'SELECT a.* FROM alimenti a ORDER BY prezzo_porzionato DESC LIMIT 10',
    'Visualizza 10 alimenti confezionati più costosi' : 'SELECT a.* FROM alimenti a ORDER BY prezzo_confezionato DESC LIMIT 10',
    'Visualizza quantità magazzini prodotto': 'SELECT cod_negozio, quantità FROM quantità WHERE cod_prodotto = %s',
    'Visualizza prodotti terminati': 'SELECT q.cod_negozio, q.cod_prodotto, p.nome FROM quantità q, prodotti p WHERE q.cod_prodotto = p.cod_prodotto AND q.quantità = 0',
    'Visualizza personale': 'SELECT a.*, t.*, c.* FROM amministratori a, tecnici t, tecnici_commerciali c',
    'Visualizza 10 prodotti con sconto maggiore': 'SELECT p.cod_prodotto, p.nome, s.cod_sconto, s.percentuale FROM sconti s, prodotti p WHERE p.cod_sconto = s.cod_sconto GROUP BY p.cod_sconto ORDER BY s.percentuale DESC LIMIT 10',
    'Visualizza ordini dopo data': 'SELECT cod_ordine, cf_cliente, data_effettuazione, costo_totale FROM ordini WHERE data_effettuazione > %s',
    'Visualizza 10 ordini più costosi': 'SELECT cod_ordine, costo_totale FROM ordini ORDER BY costo_totale DESC LIMIT 10',
    'Visualizza 10 ordini più costosi cliente': 'SELECT c.cf_cliente, o.cod_ordine, o.costo_totale FROM clienti c, ordini o WHERE c.cf_cliente = %s AND c.cf_cliente = o.cf_cliente ORDER BY costo_totale DESC LIMIT 10',
    'Visualizza sconti' : 'SELECT * FROM sconti',
    'Visualizza negozi' : 'SELECT * FROM negozi',
    'Visualizza acquirenti' : 'SELECT * FROM acquirenti',
    'Visualizza tecnici' : 'SELECT * FROM tecnici',
    'Visualizza tecnici commerciali' : 'SELECT * FROM tecnici_commerciali',
    'Visualizza percentuale sconto di uno sconto' : 'SELECT s.percentuale FROM sconti s WHERE s.cod_sconto = %s',
    'Visualizza prodotti in composizione' : 'SELECT p.* FROM prodotti p WHERE EXISTS (SELECT * FROM composte WHERE cod_composizione = %s AND p.cod_prodotto = cod_prodotto)',
    'Visualizza prodotti' : 'SELECT * FROM prodotti',
    'Visualizza composizioni' : 'SELECT * FROM composizioni',
    'Visualizza colori': 'SELECT * FROM colori',
    'Aggiungi orario': 'INSERT INTO orari(giorni, oreinizio, orefine) VALUES (%s, %s, %s)',
    'Aggiungi colorazione': 'INSERT INTO colorazione(cod_colore, cod_prodotto) VALUES (%s, %s)',
    'Ristock prodotto negozio': 'UPDATE quantità SET quantità = %s WHERE cod_prodotto = %s AND cod_negozio = %s',
    'Aggiungi confezione': 'INSERT INTO confezioni(cod_negozio, cod_alimento, quantità, prezzo_totale) VALUES (%s, %s, %s, %s)',
    'Aggiungi porzione': 'INSERT INTO porzione(cod_negozio, cod_alimento)VALUES (%s, %s)',
    'Aggiungi esposta': 'INSERT INTO esposte(cod_composizione, cod_negozio) VALUES (%s, %s)',
    'Licenzia personale': 'DELETE FROM personale WHERE cf_personale = %s',
}
