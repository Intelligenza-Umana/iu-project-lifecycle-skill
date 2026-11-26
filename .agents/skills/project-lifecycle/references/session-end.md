# Fine sessione
Controlla diff e test. Aggiorna HANDOFF con data, obiettivo, risultati verificati, file modificati, decisioni, blocchi, attività aperte e prossimo passo concreto. Archivia sessioni significative in sessions/ con data e identificatore univoco se utile. Non salvare trascrizioni integrali o segreti. Non dichiarare commit o test non effettuati.

Applica [integrità del contesto](context-integrity.md); registra documenti aggiornati e verificati invariati.

## Verifica dei test

- Individua i comandi previsti dal progetto nelle istruzioni locali, negli script o nella CI. Esegui i test pertinenti sullo stato finale della modifica, oppure consulta il risultato del job di test per la stessa revisione. Le modifiche locali successive richiedono una nuova verifica dei test interessati.
- Per ogni suite riporta comando o link al job, ambito e risultato osservato nel riepilogo e nell'eventuale HANDOFF. Leggi il riepilogo del runner anche quando il comando termina con successo. Indica i test saltati e distingui una suite parziale da quella completa.
- Se un test fallisce, riporta il caso e l'errore essenziale. Se la suite è bloccata, assente o non raccoglie test, registra il motivo e cosa resta da verificare. Tieni build, lint e controlli manuali distinti dai test eseguiti.
