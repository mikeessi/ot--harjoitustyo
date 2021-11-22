# Ohjelmistotekniikka, harjoitustyö

Sovelluksen tarkoitus on toimia digitaalisena versiona tunnetusta pasianssin Klondike-versiosta.

- [Vaatimusmäärittely](./otm-harjoitustyo/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](./otm-harjoitustyo/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Siirry kansioon `/otm-harjoitustyo`

2. Asenna riippuvuudet komennolla:

```bash
poetry install
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suoritus

Ohjelma käynnistyy komennolla:

```bash
poetry run invoke start
```

### Ohjelman testaus

Testaus onnistuu komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin saa generoitua komennolla:

```bash
poetry run invoke coverage-report
```
