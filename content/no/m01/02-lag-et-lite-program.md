# M1.2 – Lag et lite program

Nå skal du sette sammen det du allerede kan til et lite program.

Vi bruker strømforbruk som eksempel, men poenget er Python-koden. Du kan senere bytte eksemplet med noe du selv er interessert i.

## Prøv det

Et apparat bruker 1000 watt i 3 timer. Det tilsvarer 3 kilowattimer (kWh).

Hvis én kWh koster 1,20 kroner, kan Python regne ut energikostnaden:

```python
print("En enkel energiberegning")
print("Forbruk i kWh:")
print(3)
print("Pris i kroner:")
print(3 * 1.20)
```

Kjør programmet og se på resultatet.

Python skiller mellom teksten som forklarer resultatet og tallene den regner med.

## La Python gjøre mer av regningen

Vi kan skrive selve beregningen direkte:

```python
print("Tre timer med 1000 watt gir:")
print(1000 / 1000 * 3)
print("kWh")
```

Python følger vanlige regneregler.

Parenteser kan gjøre hensikten tydeligere:

```python
print((1000 / 1000) * 3)
```

Begge uttrykkene gir samme resultat.

## Endre det

Prøv å endre tallene.

Hva koster 5 kWh hvis prisen er 1,50 kroner per kWh?

```python
print(5 * 1.50)
```

Hva blir resultatet for 8 kWh til 0,90 kroner?

Skriv uttrykket selv før du kjører programmet.

## Et program kan forklare resultatet

Et nyttig program viser ikke bare et ensomt tall.

Sammenlign:

```python
print(7.5)
```

med:

```python
print("Beregnet kostnad i kroner:")
print(5 * 1.50)
```

Den andre versjonen er lettere å forstå når du åpner programmet igjen senere.

## En ny feil å kjenne igjen

Prøv:

```python
print(10 / 0)
```

Python svarer med en feilmelding som ender med:

```text
ZeroDivisionError: division by zero
```

Dette er ikke en syntaksfeil. Python forstår instruksjonen, men selve regnestykket kan ikke utføres.

Det er nyttig å skille mellom:

- **SyntaxError** – Python klarer ikke å tolke hvordan koden er skrevet.
- **ZeroDivisionError** – koden er gyldig Python, men operasjonen kan ikke utføres.

Feiltypen nederst i meldingen er ofte et godt sted å begynne.

## Lag det selv

Lag et program som fungerer som en liten kalkulatorrapport.

Programmet skal:

1. skrive ut en overskrift
2. forklare hva som beregnes
3. utføre minst tre forskjellige regnestykker
4. skrive tekst som gjør resultatene forståelige

Du kan bruke strøm, reiseavstand, oppskrifter, temperaturer eller noe helt annet som eksempel.

Ikke bruk variabler ennå. Det kommer i neste milepæl.

## Utfordring

Kan du forutsi resultatet før du kjører dette?

```python
print(10 + 2 * 3)
print((10 + 2) * 3)
```

Kjør deretter programmet og sammenlign.

Parenteser kan endre rekkefølgen på beregningen, akkurat som i vanlig matematikk.

## Dette har du lært

Du har nå brukt flere Python-instruksjoner sammen til et lite program. Du kan kombinere forklarende tekst med beregninger, og du har møtt to forskjellige typer feil.

I M2 gjør vi programmene langt mer fleksible ved å lagre verdier i **variabler (variables)**.
