# M9.4 — Tall og beregninger fra CSV

I M9.3 kunne vi hente strømforbruket med:

```python
row["kwh"]
```

Men verdien er fortsatt tekst. For eksempel er `"820"` en streng. Hvis vi vil summere og beregne med verdiene, må vi først gjøre dem om til tall.

## Fra tekst til heltall

Vi kjenner allerede `int()`:

```python
kwh = int(row["kwh"])
```

Nå er `kwh` tallet `820`, ikke teksten `"820"`.

Dette er en viktig regel når du arbeider med CSV:

> Les først dataene som tekst. Konverter bare feltene du vet skal være tall.

## Samle tallene

Vi kan lese alle målingene inn i en liste:

```python
values = []

for row in reader:
    kwh = int(row["kwh"])
    values.append(kwh)
```

Etterpå inneholder listen:

```python
[820, 760, 640, 510]
```

Nå kan Python regne med verdiene.

## Antall og total

```python
count = len(values)
total = sum(values)
```

For eksempeldataene får vi:

```text
Antall måneder: 4
Totalt: 2730 kWh
```

`len()` kjenner du fra lister. `sum()` legger sammen tallene i listen.

## Minimum og maksimum

Python har også:

```python
lowest = min(values)
highest = max(values)
```

Da finner vi den laveste og høyeste verdien i listen.

## Gjennomsnitt

Gjennomsnittet er totalen delt på antallet:

```python
average = total / count
```

Med datasettet vårt blir det:

```text
Gjennomsnitt: 682.5 kWh
```

Dette er vanlig divisjon fra tidligere i kurset. Vi bruker ingen avansert statistikk.

## Hele programmet

Kjør `examples/m09/energy_summary.py`.

Programmet:

1. åpner CSV-filen
2. bruker `DictReader`
3. konverterer `kwh` til `int`
4. legger tallene i en liste
5. beregner antall, total, minimum, maksimum og gjennomsnitt

Dette kombinerer kunnskap fra flere tidligere milepæler.

## En viktig forutsetning

`min()`, `max()` og divisjonen for gjennomsnitt trenger minst én verdi.

Eksempelfilen har data, så programmet kan bruke dem direkte. I senere programmer skal vi også tenke på tomme og ufullstendige datasett.

## Prøv det

Kjør:

```text
python examples/m09/energy_summary.py
```

Kontroller at du får:

```text
Count: 4
Total: 2730 kWh
Minimum: 510 kWh
Maximum: 820 kWh
Average: 682.5 kWh
```

## Endre det

Legg til:

```text
May,430
```

i `energy.csv`.

Før du kjører programmet, prøv å regne ut den nye totalen selv. Kjør deretter programmet og sammenlign.

## Lag det selv

Lag en CSV-fil med en tekstkolonne og en tallkolonne, for eksempel:

```text
place,temperature
Grimstad,18
Tonstad,14
Kristiansand,17
```

Les tallkolonnen, konverter den med `int()`, og finn total, minimum, maksimum og gjennomsnitt.

### Husk

CSV-verdier starter som tekst. Når du vet at et felt representerer et heltall, kan du konvertere det eksplisitt med `int()` og deretter bruke vanlige Python-beregninger.
