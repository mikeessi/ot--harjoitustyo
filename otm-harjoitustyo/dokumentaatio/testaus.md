# Testausdokumentti

Ohjelmaa on testattu unittestin avulla sekä yksikkötestein, että integraatiotestein. Ohjelmaa on myös testattu manuaalisesti järjestelmätasolla.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaavat luokat hakemistossa [deck](../src/deck/) on testattu niitä vastaavilla [testiluokilla](../src/tests/). Ainoat sovelluslogiikan luokat, joilla yksikkötestausta ei ole, ovat luokat [Endpile](../src/deck/endpile.py), sekä [Tableau](../src/deck/tableau.py), mutta näitäkin luokkia testataan integraatiotesteissä.


