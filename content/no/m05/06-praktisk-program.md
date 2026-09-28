# M5.6 – Et praktisk program med flere målinger

Nå setter vi sammen løkker, input, beslutninger og et resultat som bygges opp over flere runder.

Vi lager et lite program for strømforbruk.

## Målet

Programmet skal spørre om strømforbruk for tre dager.

For hver dag skal det:

- lese forbruket
- legge det til totalen
- gi en enkel melding hvis forbruket er høyt

Til slutt skal det skrive totalforbruket.

## Prøv det

```python
total_kwh = 0

for dag in range(1, 4):
    print("Dag", dag)
    kwh = float(input("Forbruk i kWh: "))

    total_kwh = total_kwh + kwh

    if kwh > 20:
        print("Denne dagen var forbruket over 20 kWh.")
    else:
        print("Denne dagen var forbruket 20 kWh eller lavere.")

print("Totalt forbruk:", total_kwh, "kWh")
```

## Se strukturen

Før løkka:

```python
total_kwh = 0
```

Her opprettes resultatet som skal bygges opp.

Løkka:

```python
for dag in range(1, 4):
```

gir tre runder: 1, 2 og 3.

I hver runde leses én måling:

```python
kwh = float(input("Forbruk i kWh: "))
```

Så legges den til totalen:

```python
total_kwh = total_kwh + kwh
```

Deretter vurderes akkurat denne målingen med `if`.

Etter løkka skrives sluttresultatet én gang.

## Følg et eksempel

Anta at brukeren skriver:

```text
10
25
15
```

Totalen utvikler seg slik:

```text
start: 0
dag 1: 0 + 10 = 10
dag 2: 10 + 25 = 35
dag 3: 35 + 15 = 50
```

Bare dag 2 gir meldingen om forbruk over 20 kWh.

Sluttresultatet blir 50 kWh.

## Hvorfor ligger input inne i løkka?

Vi trenger en ny måling for hver dag.

Hvis `input()` lå før løkka, ville programmet bare lest én verdi og brukt den samme verdien flere ganger.

Plasseringen av en instruksjon avgjør **når** og **hvor ofte** den kjøres.

## Hvorfor ligger totalen utenfor?

Hvis vi skrev:

```python
for dag in range(1, 4):
    total_kwh = 0
```

ville totalen blitt nullstilt for hver dag.

Startverdien må opprettes én gang før løkka.

## Test systematisk

Prøv blant annet:

- alle målinger under 20
- én måling nøyaktig 20
- én måling over 20
- desimaltall, for eksempel 12.5

Forutsi både meldingene og totalen før du kjører programmet.

## Endre det

Endre programmet til fem dager.

Hvilken del må endres?

Endre også grensen for «høyt forbruk» fra 20 til en annen verdi.

## Lag det selv

Lag et program som behandler flere målinger.

Det skal:

- bruke `for`
- lese en ny numerisk verdi i hver runde
- bygge opp en total eller en teller
- bruke `if` på hver måling
- skrive et sluttresultat etter løkka

Mulige temaer er kostnader, kilometer, minutter, poeng eller andre målinger.

## Dette har du lært

Du kan nå kombinere:

**startverdi → løkke → input → oppdatering → beslutning → sluttresultat**

Du kan også forklare hvorfor noen instruksjoner må stå før, inne i eller etter løkka.

Neste del samler hele M5 med oppgaver og feilsøking.
