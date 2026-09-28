# M5.4 – Bygg opp et resultat i en løkke

En løkke kan ikke bare behandle hver verdi. Den kan også bygge opp et resultat litt etter litt.

Et vanlig eksempel er å summere flere tall.

## Prøv det

```python
total = 0

for tall in range(1, 6):
    total = total + tall
    print("Etter", tall, "er totalen", total)

print("Sluttresultat:", total)
```

Programmet legger sammen tallene 1 til 5.

## Tre deler

Mønsteret har tre viktige deler.

### 1. Startverdi

```python
total = 0
```

Før løkka begynner, trenger vi et sted å lagre resultatet.

### 2. Oppdatering

```python
total = total + tall
```

Denne linjen kan leses:

**Ta den gamle totalen, legg til det aktuelle tallet, og lagre den nye totalen.**

### 3. Sluttresultat

```python
print("Sluttresultat:", total)
```

Denne linjen står etter løkka og kjøres én gang.

## Følg verdien

Start:

```text
total = 0
```

Første runde, `tall = 1`:

```text
total = 0 + 1 = 1
```

Andre runde, `tall = 2`:

```text
total = 1 + 2 = 3
```

Tredje runde, `tall = 3`:

```text
total = 3 + 3 = 6
```

Verdien i `total` blir altså med videre til neste runde.

## Hvorfor må total ligge før løkka?

Dette er feil hvis målet er å samle resultatet:

```python
for tall in range(1, 6):
    total = 0
    total = total + tall
```

Her settes `total` tilbake til 0 i hver eneste runde. Tidligere arbeid forsvinner.

Startverdien må derfor stå før løkka:

```python
total = 0

for tall in range(1, 6):
    total = total + tall
```

## Tell hendelser

Samme mønster kan brukes til å telle:

```python
antall = 0

for tall in range(1, 11):
    if tall >= 7:
        antall = antall + 1

print("Antall:", antall)
```

Her økes `antall` bare når betingelsen er sann.

## En kortere skrivemåte kommer senere

Python kan også skrive enkelte oppdateringer kortere. Vi bruker foreløpig:

```python
total = total + tall
```

fordi den viser tydelig at den gamle verdien brukes til å lage den nye.

## Endre det

Endre:

```python
range(1, 6)
```

til et annet område.

Forutsi sluttresultatet før du kjører programmet.

## Lag det selv

Lag et program som:

- starter en variabel før løkka
- bruker en `for`-løkke
- oppdaterer variabelen i hver runde eller når en betingelse er sann
- skriver sluttresultatet etter løkka

Du kan summere tall eller telle hvor mange verdier som oppfyller en betingelse.

## Dette har du lært

Du kan nå:

- starte et resultat før en løkke
- oppdatere resultatet i hver runde
- forklare hvorfor startverdien ikke skal nullstilles inne i løkka
- summere verdier
- telle hendelser
- skille mellom mellomresultater og sluttresultat

Neste leksjon introduserer `while`: en løkke som fortsetter så lenge en betingelse er sann.
