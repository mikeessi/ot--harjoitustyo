# Arkkitehtuurikuvaus

## Sovelluslogiikka

Sovelluksen logiikka koostuu kortteja, korttipakkaa ja pelimatolla olevia pinoja mallintavat luokat:
- [Card](../src/deck/card.py), joka mallintaa kortteja.
- [Deck](../src/deck/deck.py), joka mallintaa korttipakkaa.
- [Discardpile](../src/deck/discardpile.py), joka mallintaa hylkypinoa.
- [Drawpile](../src/deck/drawpile.py), joka mallintaa nostopinoa.
- [Endpile](../src/deck/endpile.py), joka mallintaa loppupinoja.
![Luokkakaavio](./kuvat/luokkakaavio.png)
![Sekvenssikaavio](./kuvat/sekvenssikaavio.png)
