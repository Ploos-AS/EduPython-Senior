# M9.3 — Kolonnenavn med `csv.DictReader`

Med `csv.reader` ble hver rad en liste:

```python
["January", "820"]
```

Da må vi huske at `row[0]` betyr måned og `row[1]` betyr strømforbruk. Det fungerer, men blir vanskeligere når en fil får flere kolonner.

Når CSV-filen har en header, kan `csv.DictReader` bruke kolonnenavnene for oss.

## Fra liste til ordbok

```python
import csv
from pathlib import Path

path = Path(__file__).with_name("energy.csv")

with open(path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

Kjør `examples/m09/read_csv_dict.py`.

En datarad inneholder nå navn og verdier omtrent slik:

```text
{'month': 'January', 'kwh': '820'}
```

Dette bygger direkte på ordbøkene du lærte om i M7.

## Headeren får en jobb

Filen starter med:

```text
month,kwh
```

`DictReader` bruker disse feltene som nøkler. Headeren blir derfor ikke levert som en vanlig datarad.

For raden:

```text
January,820
```

kan vi hente feltene med:

```python
print(row["month"])
print(row["kwh"])
```

Dette er ofte tydeligere enn:

```python
print(row[0])
print(row[1])
```

Kolonnenavnet forteller hva verdien betyr.

## Skriv ut en tydelig setning

Eksempelprogrammet bruker:

```python
for row in reader:
    print(row["month"], ":", row["kwh"], "kWh")
```

Resultatet blir:

```text
January : 820 kWh
February : 760 kWh
March : 640 kWh
April : 510 kWh
```

Legg merke til at `row["kwh"]` fortsatt er tekst. `DictReader` gir oss navn på feltene, men konverterer ikke datatypene.

## Hva hvis navnet er feil?

En ordbok krever riktig nøkkel. Hvis du skriver:

```python
row["energy"]
```

men headeren bare inneholder `month` og `kwh`, får du en `KeyError`.

Dette er samme type feil som du møtte med ordbøker i M7. Les feilmeldingen og sammenlign nøkkelen med headeren i CSV-filen.

## Prøv det

Kjør:

```text
python examples/m09/read_csv_dict.py
```

Sammenlign koden med `read_csv.py` fra forrige leksjon.

## Endre det

Endre utskriften slik at den begynner med teksten:

```text
Forbruk i January: 820 kWh
```

Du trenger ikke endre CSV-filen.

## Lag det selv

Lag en CSV-fil med headeren:

```text
title,year
```

Legg inn minst tre rader. Les filen med `csv.DictReader` og skriv ut `row["title"]` og `row["year"]`.

Prøv til slutt å bytte rekkefølgen på kolonnene i både headeren og dataradene. Når du bruker kolonnenavn, kan resten av programmet fortsatt være lett å forstå.

### Husk

`csv.DictReader` bruker headeren som nøkler og gjør hver datarad til en ordbok. Verdiene er fortsatt tekst.
