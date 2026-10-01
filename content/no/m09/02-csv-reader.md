# M9.2 — Lese CSV med `csv.reader`

I forrige leksjon leste vi CSV-filen som vanlig tekst. Nå skal Python hjelpe oss med å dele filen i **rader og felt**.

Python har modulen `csv` i standardbiblioteket. Du trenger derfor ikke installere noe ekstra.

## Første CSV-leser

```python
import csv
from pathlib import Path

path = Path(__file__).with_name("energy.csv")

with open(path, "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Kjør `examples/m09/read_csv.py`.

Du får omtrent dette:

```text
['month', 'kwh']
['January', '820']
['February', '760']
['March', '640']
['April', '510']
```

## Hva gjør `csv.reader`?

`csv.reader(file)` lager en leser som forstår CSV-strukturen.

Når løkken ber om neste rad, deler leseren raden i felt. Hver rad blir en **liste**. Det passer godt med det du lærte om lister i M7.

Første rad blir:

```python
["month", "kwh"]
```

Andre rad blir:

```python
["January", "820"]
```

## Headeren er også en rad

`csv.reader` vet ikke automatisk at første rad er en overskrift. For leseren er den bare den første raden i filen.

Senere skal vi se på en annen CSV-leser som kan bruke kolonnenavnene direkte. Først er det nyttig å se den enkle strukturen tydelig.

## Alt er tekst ennå

Legg merke til:

```python
["January", "820"]
```

Verdien `"820"` har anførselstegn når listen vises. Det betyr at den er en streng, ikke tallet `820`.

CSV-filen lagrer tekst. Python gjetter ikke hvilke felt som skal være heltall, desimaltall, datoer eller noe annet. Vi skal gjøre slike konverteringer bevisst i en senere leksjon.

## Hvorfor `newline=""`?

Når Python-modulen `csv` arbeider med en fil, anbefales det å åpne filen med `newline=""`. Da får CSV-modulen håndtere linjeskiftene selv.

Du trenger ikke forstå alle detaljene nå. Bruk dette mønsteret når du åpner CSV-filer:

```python
with open(path, "r", encoding="utf-8", newline="") as file:
```

## Prøv det

Kjør:

```text
python examples/m09/read_csv.py
```

Finn igjen:

1. header-raden
2. raden for January
3. de to feltene i hver rad

## Endre det

Legg til:

```text
May,430
```

i `energy.csv` og kjør programmet igjen.

Deretter kan du endre utskriften til:

```python
for row in reader:
    print("Antall felt:", len(row), row)
```

Hver rad i dette datasettet skal ha to felt.

## Lag det selv

Lag en liten CSV-fil med tre kolonner. Les den med `csv.reader` og skriv ut hver rad.

Prøv deretter å skrive ut bare første felt:

```python
for row in reader:
    print(row[0])
```

Her bruker du både filer, løkker, lister og indeksering fra tidligere milepæler.

### Husk

`csv.reader` gjør hver CSV-rad om til en liste med tekstverdier. Det gjør CSV-data tilgjengelig med Python-verktøy du allerede kjenner.
