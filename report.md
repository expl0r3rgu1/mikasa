<div>
<h1 style="text-align: center">Elaborato per il corso</h1>
<h1 style="text-align: center">di basi di dati</h1>
<h3 style="text-align: center">2021/2022</h3>
<br><br>
<h1 style="text-align: center">MiKasa</h1>
<br><br>
</div>

	
### Componenti

Salvatore Antonio Addimando, matricola : 0000970539<br>
Benedetta Pacilli, matricola: 0000975296<br>
Valentina Pieri, matricola: 0000974789


# Indice


# Capitolo 1 - Analisi dei requisiti

## Intervista

Si vuole tenere traccia di una catena di negozi simil-Ikea.
Per ogni negozio si tiene traccia del luogo e della data di inaugurazione, dell'orario di apertura e del suo codice negozio.
Ogni negozio viene suddiviso in zone, ognuna con un suo codice zona. Vi sono 4 tipi di zone: shop alimentari, ristoro, esposizione e magazzino.
La zona delle esposizioni è formata da tante composizioni di mobili, come ad esempio: cucina, bagno, ufficio, camera da letto, ecc...
Per ogni composizione viene salvato il nome, il numero di prodotti al suo interno e il suo codice composizione.
Una composizione è formata da più prodotti e ogni prodotto appartiene ad una sola composizione. Per ogni prodotto vengono salvati: il nome, il prezzo, le dimensioni, il peso e il codice prodotto. Ci sono 3 tipi di prodotti: i mobili, gli accessori e gli elettrodomestici.
Ad ogni prodotto viene inoltre associato uno o più colori e ogni colore può essere di più prodotti. Per ogni colore vengono salvati il nome e il codice colore.
Per i prodotti si mantiene uno storico sconti: a ogni prodotto possono essere applicati più sconti in base al periodo dell'anno. Il periodo di validità di uno sconto viene mantenuto tramite lo storico sconti. Ogni sconto può essere applicato a più prodotti. Per lo sconto vengono salvati una percentuale conto e un codice sconto, mentre, per lo storico sconti vengono salvati il periodo di sconto e il codice dello storico.
Tutti i prodotti vengono stockati nei magazzini dei vari negozi. In ogni magazzino ci sono da zero a N prodotti e, allo stesso tempo, ogni prodotto può essere presente in uno, nessuno o tanti magazzini. Per lo stockaggio dei prodotti vengono salvati la locazione del prodotto nel magazzino e la quantità di prodotto presente.
Per quanto riguarda lo shop alimentari e la zona di ristoro, questi vendono diversi alimenti. La zona ristoro vende gli alimenti al dettaglio mentre, la zona dello shop li vende all'ingrosso. Per entrambe le vendite vengono mantenuti i prezzi, al pezzo da una parte e all'ingrosso dall'altra. Inoltre, nella vendita all'ingrosso viene mantenuto il numero di pezzi venduti per ogni prodotto. Per i vari alimenti vengono salvati: il nome, gli ingredienti con i relativi allergeni, la provenienza, la scadenza e il codice a barre.
In questo database vi sono anche diversi tipi di persone. Per ogni persona vengono salvati: il nome, il cognome, il numero di telefono, l'indirizzo email, l'indirizzo e il codice fiscale. Ci sono 3 tipi di persone: clienti, personale e acquirenti. Ogni acquirente può aprire diversi negozi della catena mentre, ogni negozio ha un solo acquirente.
Per il personale vengono salvati: il salario, l'orario lavorativo e il codice personale. Il personale si divide tra impiegati e manager.
Ogni manager si occupa di un solo negozio e ogni negozio ha un solo manager.
Ci sono diversi tipi di impiegati: i tecnici, i tecnici commerciali e gli amministratori. Ogni amministratore gestisce una sola zona di un negozio mentre, ogni zona può avere più amministratori.
Ogni tecnico commerciale può occuparsi: di uno o nessuno shop, di uno o nessun alimentari, di zero/N ordini. Per quanto riguarda l'alimentari e il ristoro, questi possono avere da 1 a N tecnici commerciali mentre, ogni ordine è gestito da un solo tecnico commerciale.
Gli ordini vengono effettuati dai clienti: ogni cliente può fare più ordini e ogni ordine è relativo ad un solo cliente. Il singolo ordine è formato da zero/N dettagli ordine per prodotto/composizione. Un dettaglio ordine tiene conto della quantità acquistata di ogni singolo/a prodotto/composizione ordinato/a. Oltre alla quantità, un dettaglio ordine mantiene il prezzo totale per quel/la prodotto/composizione. Per ogni ordine vengono mantenuti: la data di effettuazione, il costo totale, il peso totale, lo sconto totale dell'ordine, la data di arrivo e il codice ordine. Un cliente può essere socio o meno; in caso sia socio ha diritto ad uno sconto sull'ordine totale. Gli ordini si dividono in due categorie: con e senza spedizione. Di un ordine spedizione si può fare il ritiro in un solo negozio, in ogni negozio vengono spediti più ordini. Per la spedizione, di un ordine con spedizione, viene mantenuto l'indirizzo di spedizione e il codice spedizione. Ogni spedizione viene consegnata da uno o più tecnici e ogni tecnico si può occupare di zero/N spedizioni.
Per un ordine con spedizione si può richiedere il montaggio. L'assemblaggio viene gestito da uno o più tecnici e ogni tecnico può occuparsi di zero/N assemblaggi. Infine, un tecnico può lavorare o meno come magazziniere nel magazzino di un negozio, ogni magazzino ha uno o più tecnici che vi lavorano.