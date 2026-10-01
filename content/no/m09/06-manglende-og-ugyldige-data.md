# M9.6 — Manglende og ugyldige data

Virkelige data er ikke alltid perfekte. Et felt kan være tomt, eller inneholde tekst der programmet forventer et tall.

Det betyr ikke at vi skal ignorere feil. Vi skal **oppdage dem, forstå dem og håndtere de feilene vi forventer**.

## Et kontrollert eksempel

Filen `examples/m09/energy_with_errors.csv` inneholder:

```text
month,kwh
January,820
February,
March,unknown
April,510
```

Her har vi to forskjellige problemer:

- February mangler en verdi
- March har teksten `unknown` der vi forventer et heltall

Disse tilfellene bør behandles tydelig.

## Sjekk tom verdi først

Vi henter teksten og fjerner eventuelle mellomrom:

```python
text = row["kwh"].strip()
```

Så kan vi teste:

```python
if text == "":
    print(month, ": mangler verdi")
    continue
```

`continue` går videre til neste runde i løkken. Vi prøver dermed ikke å konvertere en tom streng med `int()`.

## Når teksten ikke er et tall

En ikke-tom verdi kan fortsatt være ugyldig:

```text
unknown
```

Denne koden gir `ValueError`:

```python
int("unknown")
```

Her vet vi nøyaktig hvilken feil som kan oppstå, så vi kan håndtere akkurat `ValueError`:

```python
try:
    kwh = int(text)
except ValueError:
    print(month, ": ugyldig tall:", text)
    continue
```

Vi bruker ikke en generell `except:`. Andre feil bør fortsatt bli synlige, slik at vi kan finne og rette dem.

## Behold de gyldige verdiene

Når konverteringen lykkes:

```python
valid_values.append(kwh)
```

Programmet kan dermed fortsette med gyldige data samtidig som det forteller hvilke rader som hadde problemer.

Kjør `examples/m09/read_imperfect_csv.py`.

Du skal se at January og April godtas, mens February og March får tydelige meldinger.

## Hvorfor ikke bare ignorere alt som går galt?

Hvis vi skjuler alle feil, kan programmet gi et resultat som ser riktig ut selv om viktige data mangler.

Et bedre mønster er:

1. sjekk forventede mangler
2. håndter den konkrete konverteringsfeilen
3. gjør problemet synlig
4. behold bare verdier du faktisk har validert

## Prøv det

Kjør:

```text
python examples/m09/read_imperfect_csv.py
```

Finn de to forskjellige feilsituasjonene i utskriften.

## Endre det

Endre `unknown` til `640` og kjør igjen.

Hvor mange gyldige verdier får programmet nå?

Deretter kan du gi February verdien `760`. Nå bør alle fire radene være gyldige.

## Lag det selv

Lag en CSV-fil med navn og alder. La én alder være tom og én inneholde tekst som ikke er et tall.

Skriv et program som:

- rapporterer tom alder
- fanger bare `ValueError` ved ugyldig tall
- skriver ut gyldige aldre
- teller hvor mange gyldige verdier det fant

### Husk

Robust kode betyr ikke å skjule feil. Den håndterer forventede problemer tydelig og lar uventede feil være synlige.
