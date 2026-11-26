# Test

Run `python3 -m unittest discover -s tests -v` for installer regression tests. The following agent workflow scenarios require a live host and have not been verified by the automated installer tests.

## Criteri di accettazione manuali
1. Bootstrap su repo vuota: documenti minimi e link validi.
2. Bootstrap ripetuto: nessun duplicato o sovrascrittura.
3. Migrazione con AGENTS esistente: regole preservate.
4. Resume con handoff obsoleto: discrepanza segnalata.
5. Audit: nessuna modifica senza mandato.
6. Handoff: su una fixture con un test superato, uno fallito e uno saltato, verificare che il resoconto riporti comando, ambito ed esiti osservati. Ripetere con zero test raccolti e controllare che il lavoro resti da verificare.
7. Segreti e modifiche locali: nessuna esposizione o perdita.

8. Modifica con impatto documentale: tutte le fonti pertinenti aggiornate o motivate come invariate.
9. Contesto indispensabile inaccessibile: blocco esplicito, nessun completamento inventato.
