# Arkkitehtuurikuvaus

## Rakenne

Sovellus koostuu [interface](../src/interface/)-hakemistosta, jossa on käyttöliittymään liittyvät luokat, [deck](../src/deck/)-hakemistosta, jossa on sovelluslogiikan kannalta tärkeät luokat ja [data](../src/data/)-hakemistosta, jossa on tietokantaoperaatioihin liittyvät luokat, sekä tallennettu tietokanta. 

## Käyttöliittymä

Ohjelman käyttöliittymän voi jakaa menuun, ja itse peliin. Ohjelman menut on toteutettu omana [Menu](../src/interface/menu.py)-luokkana. Itse pelimaton käyttöliittymän toteuttaa pääasiassa luokat
- [Hitboxes](../src/interface/hitboxes.py), joka mallintaa pelimaton objektien hitboxeja ja tarkkailee, mihin hiirellä klikataan, sekä
- [Renderer](../src/interface/renderer.py), joka piirtää objektit pelimatolle.

## Sovelluslogiikka

Sovelluksen logiikka koostuu kortteja, korttipakkaa ja pelimatolla olevia pinoja mallintavat luokat:
- [Card](../src/deck/card.py), joka mallintaa kortteja.
- [Deck](../src/deck/deck.py), joka mallintaa korttipakkaa.
- [Discardpile](../src/deck/discardpile.py), joka mallintaa hylkypinoa.
- [Drawpile](../src/deck/drawpile.py), joka mallintaa nostopinoa.
- [Tableau](../src/deck/tableau.py), joka mallintaa pelipinoja.
- [Endpile](../src/deck/endpile.py), joka mallintaa loppupinoja.
- [Draggedcard](../src/deck/draggedcard.py), joka mallintaa tällä hetkellä valittua korttia/kortteja.

Alla olevassa kuvassa näkyy karkeasti luokkien yhteydet. Käytännössä luokka [Gameloop](../src/deck/gameloop.py) hoitaa eri luokkien väliset interaktiot, esimerkiksi korttien siirron ja siirtojen laillisuuden tarkistamisen.
![Luokkakaavio](./kuvat/luokkakaavio.png)

## Tietojen pysyväistallennus

Hakemiston _data_ luokka [Hiscores](../src/data/hiscores.py) on ainoa keino, jolla ohjelma tallentaa tietoa. Se tallentaa tiedot SQL-tietokantaan, ja toimii nimensä mukaisesti Hiscore-listana.

### Tiedostot

Sovelluksen ainoa tallennuskohde on _data_ hakemistoon luotava hiscores.db, jonka tauluun 'Hiscores' tulokset tallennetaan.

## Toiminnallisuus

Alla olevassa sekvenssikaaviossa kuvataan kortin nostamista pakasta ja sen siirtäminen pöydällä olevaan pelipinoon.

![Sekvenssikaavio](./kuvat/sekvenssikaavio.png)

