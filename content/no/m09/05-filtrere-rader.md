# M9.5 — Filtrere rader

Et datasett inneholder ofte flere rader enn vi trenger akkurat nå. Da kan vi **filtrere**: velge bare radene som oppfyller en betingelse.

Dette bygger direkte på `if` fra M4.

## Velg høyt forbruk

Vi vil finne måneder der strømforbruket er minst 700 kWh.

```python
for row in reader:
    kwh = int(row["kwh"])

    if kwh >= 700:
        print(row["month"], kwh)
```

Med `energy.csv` blir resultatet:

```text
January 820
February 760
```

Programmet leser alle radene, men skriver bare ut radene som passer til betingelsen.

## Rekkefølgen er viktig

CSV-verdien starter som tekst:

```python
row["kwh"]
```

Før vi sammenligner den med tallet `700`, konverterer vi:

```python
kwh = int(row["kwh"])
```

Deretter gir denne sammenligningen mening:

```python
if kwh >= 700:
```

Vi sammenligner tall med tall.

## Lagre de valgte radene

Vi kan også samle resultatene i en liste:

```python
selected = []

for row in reader:
    kwh = int(row["kwh"])

    if kwh >= 700:
        selected.append(row)
```

Nå inneholder `selected` bare ordbøkene som oppfylte betingelsen.

Dette kombinerer:

- CSV-filer
- ordbøker
- løkker
- `int()`
- `if`
- lister

## En grense som variabel

Det er tydeligere å gi grensen et navn:

```python
limit = 700
```

Deretter:

```python
if kwh >= limit:
```

Nå kan vi endre én verdi hvis vi vil prøve en annen grense.

## Prøv det

Kjør:

```text
python examples/m09/filter_energy.py
```

Programmet skriver ut måneder med minst 700 kWh.

## Endre det

Endre:

```python
limit = 700
```

til:

```python
limit = 600
```

Før du kjører programmet, prøv å finne ut hvilke måneder som nå skal bli valgt.

## Lag det selv

Endre betingelsen slik at programmet i stedet finner måneder med **mindre enn 700 kWh**.

Prøv deretter to grenser:

```python
minimum = 600
maximum = 800
```

Du kan bruke det du lærte om `and` i M4:

```python
if kwh >= minimum and kwh <= maximum:
```

Hvilke rader blir valgt?

### Husk

Filtrering betyr ikke at CSV-filen endres. Programmet leser dataene og velger hvilke rader det vil arbeide videre med.
