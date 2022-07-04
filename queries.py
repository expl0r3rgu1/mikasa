QUERIES = {
    'Visualizza clienti': 'SELECT p.*, c.socio FROM clienti c, persone p WHERE c.cf_cliente = p.cf',
    'Aggiungi cliente': 'INSERT INTO clienti (cf_cliente, socio) VALUES (%s, 0)',
    'Aggiungi persona': 'INSERT INTO persone (cf, nome, cognome, telefono, email, via, civico, cap, città) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
    'Aggiungi personale': 'INSERT INTO personale (cf_personale, salario, cod_orario) VALUES (%s, %s, %s)',
    'Aggiungi manager': 'INSERT INTO manager(cf_manager, cod_negozio) VALUES (%s, %s)',
    'Aggiungi impiegato': 'INSERT INTO impiegati(cf_impiegato) VALUES (%s)',
    'Aggiungi amministratore': 'INSERT INTO amministratori(cf_amministratore, cod_zona, cod_negozio) VALUES (%s, %s, %s)',
    'Aggiungi tecnico': 'INSERT INTO tecnici(cf_tecnico, cod_negozio, cod_magazzino) VALUES (%s, %s,%s)',
    'Aggiungi tecnico commerciale': 'INSERT INTO tecnici_commerciali(cf_tecnico_commerciale, cod_negozio, cod_alimentari, cod_ristoro) VALUES (%s, %s, %s, %s)',
    'Aggiungi negozio': 'INSERT INTO negozi (via, civico, cap, città, data_inaugurazione, cf_acquirente, cod_orario) VALUES (%s, %s, %s, %s, %s, %s, %s)',
    'Rendi socio un cliente': 'UPDATE clienti SET socio = 1 WHERE cf_cliente = %s',
    'Rendi non socio un cliente': 'UPDATE clienti SET socio = 0 WHERE cf_cliente = %s',
    'Effettua ordine': 'INSERT INTO ordini (data_effetuazione, costo_totale, peso_totale, sconto_totale, data_arrivo, cf_cliente, cf_tecnico_commerciale) VALUES (%s, %s, %s, %s, %s, %s, %s)',
    'Effettua ordine senza spedizione': 'INSERT INTO ordini_no_spedizione(cod_ordine, cod_negozio) VALUES (%s, %s)',
    'Effettua ordine con spedizione': 'INSERT INTO ordini_spedizione(cod_ordine, indirizzo, cf_tecnico) VALUES (%s, %s, %s)',
    'Effettua ordine con montaggio': 'INSERT INTO ordini_montaggio(cod_ordine, indirizzo, cf_tecnico) VALUES (%s, %s, %s)',
    'Effettua ordine senza montaggio': 'INSERT INTO ordini_no_montaggio(cod_ordine) VALUES (%s)',
    'Aggiungi prodotto': 'INSERT INTO prodotti(nome, prezzo, altezza, larghezza, profondità, peso, cod_sconto) VALUES (%s, %s, %s, %s, %s, %s, %s)',
    'Aggiungi accessorio': 'INSERT INTO accessori(cod_prodotto) VALUES (%s)',
    'Aggiungi mobile': 'INSERT INTO mobili(cod_prodotto) VALUES (%s)',
    'Aggiungi elettrodomestico': 'INSERT INTO elettrodomestici(cod_prodotto) VALUES (%s)',
    'Aggiungi alimento': 'INSERT INTO alimenti(cod_alimento, nome, provenienza, scadenza, ingredienti, allergeni, prezzo_porzionato, prezzo_confezionato) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    'Aggiungi composizione': 'INSERT INTO composizioni(cod_composizione, nome, num_prodotti, peso) VALUES (%s, %s, %s, %s)',
    'Aggiungi composta': 'INSERT INTO composte(cod_negozio, cod_esposizione, cod_composizione, cod_prodotto) VALUES (%s, %s, %s, %s)',
    'Aggiungi sconto': 'INSERT INTO sconti(cod_sconto, percentuale, cod_storico) VALUES (%s, %s, %s)',
    'Aggiungi storico sconti': 'INSERT INTO storico_sconti(cod_storico, inizio, fine) VALUES (%s, %s)',
    'Visualizza ordini in un mese': 'SELECT * FROM ordini WHERE YEAR(data_effettuazione) = %s AND MONTH(data_effettuazione) = %s',
    'Visualizza ordini di un cliente': 'SELECT * FROM ordini WHERE cf_cliente = %s',
    'Visualizza spedizioni in un mese': 'SELECT s.cod_ordine, s.indirizzo, s.cf_tecnico, o.data_effettuazione, o.data_arrivo FROM ordini_spedizione s, ordini o WHERE YEAR(data_effettuazione) = %s AND MONTH(o.data_effettuazione) = %s AND o.cod_ordine = s.cod_ordine',
    'Visualizza montaggi in un mese': 'SELECT m.cod_ordine, o.data_arrivo FROM ordini_montaggio m, ordini o, ordini_spedizione s WHERE YEAR(o.data_arrivo) = %s AND MONTH(o.data_arrivo)  = %s AND o.cod_ordine = s.cod_ordine AND s.cod_ordine = m.cod_ordine',
    'Visualizza prodotto più acquistato': 'SELECT p.*, SUM(CASE WHEN p.cod_prodotto = d.cod_prodotto THEN d.quantità ELSE 0 END) AS quantità FROM prodotti p, dettagli_prodotto d WHERE p.cod_prodotto = d.cod_prodotto GROUP BY p.cod_prodotto ORDER BY quantità DESC LIMIT 1',
    'Visualizza 10 prodotti più acquistati' : 'SELECT p.*, SUM(CASE WHEN p.cod_prodotto = d.cod_prodotto THEN d.quantità ELSE 0 END) AS quantità FROM prodotti p, dettagli_prodotto d WHERE p.cod_prodotto = d.cod_prodotto GROUP BY p.cod_prodotto ORDER BY quantità DESC LIMIT 10',
    'Visualizza prodotto meno acquistato': 'SELECT p.*, SUM(CASE WHEN p.cod_prodotto = d.cod_prodotto THEN d.quantità ELSE 0 END) AS quantità FROM prodotti p, dettagli_prodotto d WHERE p.cod_prodotto = d.cod_prodotto GROUP BY p.cod_prodotto ORDER BY quantità ASC LIMIT 1',
    'Visualizza prodotto più costoso': 'SELECT p.* FROM prodotti p ORDER BY prezzo DESC LIMIT 1',
    'Visualizza prodotto meno costoso': 'SELECT p.* FROM prodotti p ORDER BY prezzo DESC LIMIT 1',
    'Visualizza alimento porzionato più costoso': 'SELECT a.* FROM alimenti a ORDER BY prezzo_porzionato DESC LIMIT 1',
    'Visualizza alimento confezionato più costoso': 'SELECT a.* FROM alimenti a ORDER BY prezzo_confezionato DESC LIMIT 1',
    'Visualizza quantità presente nei magazzini di un prodotto': 'SELECT cod_negozio, quantità FROM quantità WHERE cod_prodotto = %s',
    'Visualizza prodotti terminati': 'SELECT q.cod_negozio, q.cod_prodotto, p.nome FROM quantità q, prodotti p WHERE q.cod_prodotto = p.cod_prodotto AND q.quantità = 0',
    'Visualizza personale': 'SELECT p.* FROM personale e, persone p WHERE e.cf_personale = p.cf',
    'Visualizza prodotto con sconto maggiore': 'SELECT p.cod_prodotto, p.nome, s.cod_sconto, s.percentuale FROM sconti s, prodotti p WHERE p.cod_sconto = s.cod_sconto GROUP BY p.cod_sconto ORDER BY s.percentuale DESC LIMIT 1',
    'Visualizza ordini effettuati dopo una certa data': 'SELECT cod_ordine, cf_cliente, data_effettuazione, costo_totale FROM ordini WHERE data_effettuazione > %s',
    'Visualizza ordine più costoso': 'SELECT cod_ordine, costo_totale FROM ordini ORDER BY costo_totale DESC LIMIT 1',
    'Visualizza ordine più costoso di un cliente': 'SELECT c.cf_cliente, o.cod_ordine, o.costo_totale FROM clienti c, ordini o WHERE c.cf_cliente = %s AND c.cf_cliente = o.cf_cliente ORDER BY costo_totale DESC LIMIT 1',
    'Aggiungi orario': 'INSERT INTO orari(cod_orario, giorni, oreinizio, orefine) VALUES (%s, %s, %s, %s)',
    'Aggiungi colorazione': 'INSERT INTO colorazione(cod_colore, cod_prodotto) VALUES (%s, %s)',
    'Ristock prodotto in un negozio': 'UPDATE quantità SET quantità = %s WHERE cod_prodotto = %s AND cod_zona = %s AND cod_negozio = %s',
    'Aggiungi confezione': 'INSERT INTO confezioni(cod_negozio, cod_alimentari, cod_alimento, quantità, prezzo_totale) VALUES (%s, 1, %s, %s, %s)',
    'Aggiungi porzione': 'INSERT INTO porzione(cod_negozio, cod_ristoro, cod_alimento)VALUES (%s, 2, %s)',
    'Aggiungi esposta': 'INSERT INTO esposte(cod_composizione, cod_negozio, cod_esposizione) VALUES (%s, %s, 3)',
    'Visualizza colori': 'SELECT * FROM colori',
    'Licenzia personale': 'DELETE FROM personale WHERE cf_personale = %s',
}
