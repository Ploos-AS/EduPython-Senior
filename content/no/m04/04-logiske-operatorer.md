# M4.4 – Kombiner betingelser

Noen valg avhenger av mer enn ett spørsmål. Python har ordene `and`, `or` og `not` for å kombinere eller snu betingelser.

## and – begge må være sanne

```python
temperatur = float(input("Temperatur: "))

if temperatur >= 0 and temperatur < 20:
    print("Temperaturen er fra 0 til under 20.")
```

Hele betingelsen er sann bare når **begge** delene er sanne.

For `10`:

- `temperatur >= 0` er sann
- `temperatur < 20` er sann
- hele uttrykket er derfor sant

For `25` er den andre delen usann, og blokken kjøres ikke.

## or – minst én må være sann

```python
temperatur = float(input("Temperatur: "))

if temperatur < 0 or temperatur > 30:
    print("Temperaturen er utenfor området 0 til 30.")
```

Her holder det at **minst én** av delene er sann.

## not – snu sant og usant

`not` snur resultatet av en betingelse.

```python
er_klar = input("Skriv ja når du er klar: ") == "ja"

if not er_klar:
    print("Du skrev ikke ja.")
```

Hvis `er_klar` er usann, gjør `not` uttrykket sant.

Dette eksemplet sammenligner teksten nøyaktig. `"Ja"` og `"ja"` er forskjellige tekster.

## Les uttrykket som en setning

Denne koden:

```python
if alder >= 18 and alder <= 100:
```

kan leses:

**Hvis alder er minst 18 og alder er høyst 100.**

Hvis et uttrykk blir vanskelig å lese, er det ofte bedre å gjøre programmet tydeligere enn å presse alt inn på én linje.

## Parenteser kan gjøre hensikten tydelig

Du kan skrive:

```python
if (temperatur < 0) or (temperatur > 30):
    print("Utenfor området")
```

Parentesene er ikke nødvendige i dette enkle uttrykket, men de kan gjøre de to delene lettere å se.

Vi holder kombinasjonene enkle foreløpig.

## Endre det

Prøv:

```python
tall = int(input("Tall: "))

if tall >= 10 and tall <= 20:
    print("Tallet er fra 10 til og med 20.")
else:
    print("Tallet er utenfor området.")
```

Test `9`, `10`, `15`, `20` og `21`.

## En vanlig feil med and

Dette er ikke riktig måte å skrive «mellom 10 og 20» på:

```python
if tall >= 10 and <= 20:
```

Hver sammenligning må være komplett:

```python
if tall >= 10 and tall <= 20:
```

Senere kan du møte andre gyldige Python-måter å uttrykke områder på. Her bruker vi formen som viser begge spørsmålene tydelig.

## Lag det selv

Lag et program som bruker minst én av:

- `and`
- `or`
- `not`

Test flere verdier og forklar for deg selv hvorfor hele betingelsen blir sann eller usann.

## Dette har du lært

Du kan nå:

- bruke `and` når begge betingelser må være sanne
- bruke `or` når minst én må være sann
- bruke `not` for å snu et sant/usant-resultat
- lese en kombinert betingelse som en setning
- holde logiske uttrykk enkle og lesbare

Neste del bruker beslutninger i et komplett praktisk program.
