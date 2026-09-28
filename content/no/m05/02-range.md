# M5.2 – Gjenta et bestemt antall ganger med range()

I forrige leksjon gikk `for` gjennom verdier vi allerede hadde skrevet opp.

Noen ganger vil vi ganske enkelt gjenta noe et bestemt antall ganger. Da er `range()` nyttig.

## Prøv det

```python
for nummer in range(5):
    print(nummer)
```

Programmet skriver:

```text
0
1
2
3
4
```

`range(5)` gir løkka fem tall: fra `0` til `4`.

## Hvorfor stopper den på 4?

I:

```python
range(5)
```

er `5` **stoppunktet**, men selve stoppunktet er ikke med.

Det betyr:

- start på 0
- fortsett mens tallet er mindre enn 5
- resultatet blir 0, 1, 2, 3, 4

Dette kan virke uvant. Test små verdier og se mønsteret.

## Gjenta fem ganger uten å bry deg om tallet

```python
for nummer in range(5):
    print("Dette skjer fem ganger")
```

Variabelen `nummer` får fortsatt verdiene 0 til 4, selv om vi ikke bruker den inne i blokken.

Senere vil du møte en vanlig skrivemåte for løkker der selve verdien ikke brukes. Foreløpig beholder vi et tydelig variabelnavn.

## Velg start og stopp

`range()` kan også få to tall:

```python
for nummer in range(1, 6):
    print(nummer)
```

Dette skriver:

```text
1
2
3
4
5
```

Les:

```python
range(1, 6)
```

som:

**start på 1, stopp før 6.**

## Forutsi før du kjører

Hva skriver dette?

```python
for nummer in range(3, 7):
    print(nummer)
```

Forutsi først.

Svaret er:

```text
3
4
5
6
```

## Bruk tallet i en beregning

```python
for nummer in range(1, 6):
    dobbelt = nummer * 2
    print(nummer, dobbelt)
```

Hver runde bruker den aktuelle verdien av `nummer`.

## En vanlig tankefeil

Hvis du vil skrive tallene 1 til og med 10, er dette:

```python
range(1, 10)
```

ikke nok. Det stopper før 10.

Bruk:

```python
range(1, 11)
```

## Endre det

Start med:

```python
for nummer in range(1, 4):
    print("Runde", nummer)
```

Endre stoppverdien. Forutsi hvor mange linjer som kommer før du kjører programmet.

## Lag det selv

Lag et program som:

- bruker `for` og `range()`
- starter på 1
- kjører minst fem runder
- bruker løkkevariabelen i en beregning
- skriver resultatet i hver runde

## Dette har du lært

Du kan nå:

- bruke `range(stop)`
- forklare at `range()` stopper **før** stoppverdien
- bruke `range(start, stop)`
- forutsi hvilke tall en enkel `range()` lager
- bruke løkkevariabelen i beregninger

Neste leksjon kombinerer løkker med beslutninger.
