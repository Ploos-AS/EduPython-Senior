# M9.7 — Skrive CSV

Så langt har vi lest CSV-filer. Nå skal vi lage en CSV-fil fra Python.

Vi bruker `csv.DictWriter` fordi vi allerede arbeider med kolonnenavn og ordbøker.

## Dataene våre

Vi starter med en liste av ordbøker:

```python
measurements = [
    {"month": "January", "kwh": 820},
    {"month": "February", "kwh": 760},
    {"month": "March", "kwh": 640},
]
```

Hver ordbok skal bli én datarad.

## Fortell hvilke kolonner filen skal ha

```python
fieldnames = ["month", "kwh"]
```

Rekkefølgen her bestemmer kolonnerekkefølgen i CSV-filen.

## Åpne filen for skriving

```python
with open(path, "w", encoding="utf-8", newline="") as file:
```

Som i M8 betyr `"w"` at filen opprettes eller overskrives.

Derfor skal du alltid kontrollere hvilken filsti du bruker før du skriver til en virkelig fil.

I kurseksemplet bruker vi bare en egen kontrollert fil som programmet rydder bort etterpå.

## Lag skriveren

```python
writer = csv.DictWriter(file, fieldnames=fieldnames)
```

Så skriver vi headeren:

```python
writer.writeheader()
```

og dataradene:

```python
writer.writerows(measurements)
```

Resultatet blir:

```text
month,kwh
January,820
February,760
March,640
```

## Les tilbake det du skrev

Et nyttig mønster er å kontrollere resultatet etter skriving.

Eksempelprogrammet åpner derfor filen på nytt med `DictReader` og skriver radene til skjermen.

Da ser vi hele kjeden:

```text
Python-data → CSV-fil → Python-data
```

## Hva med `csv.writer`?

Python har også `csv.writer`, som skriver sekvenser som lister:

```python
writer = csv.writer(file)
writer.writerow(["month", "kwh"])
writer.writerow(["January", 820])
```

Det er nyttig når dataene naturlig er lister. I dette kurset bruker vi hovedsakelig `DictWriter` når filen har navngitte kolonner, fordi navnene gjør koden lettere å lese.

## Prøv det

Kjør:

```text
python examples/m09/write_csv.py
```

Programmet skriver en kontrollert CSV-fil, leser den tilbake, viser innholdet og fjerner filen igjen.

## Endre det

Legg til:

```python
{"month": "April", "kwh": 510}
```

i listen.

Kjør programmet igjen og kontroller at den nye raden blir lest tilbake.

## Lag det selv

Lag en liste med minst tre ordbøker med feltene:

```text
title,year
```

Skriv dem til en CSV-fil med `DictWriter`.

Husk:

1. velg `fieldnames`
2. bruk `newline=""`
3. skriv headeren
4. skriv radene
5. les gjerne filen tilbake for å kontrollere resultatet

### Husk

`DictReader` leser navngitte CSV-rader inn som ordbøker. `DictWriter` gjør den motsatte veien og skriver ordbøker som navngitte CSV-rader.
