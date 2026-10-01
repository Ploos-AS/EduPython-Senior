# M9.8 — Praktisk prosjekt: strømrapport

Nå skal vi samle det viktigste fra M9 i ett program.

Programmet skal:

1. lese en CSV-fil
2. bruke kolonnenavn
3. kontrollere manglende og ugyldige verdier
4. konvertere gyldige tall
5. lagre strukturerte data
6. beregne en oppsummering
7. filtrere etter en grense

Dette er ikke en ny teknikk. Det er trening i å sette sammen det du allerede kan.

## Datasettet

`examples/m09/energy_report.csv` inneholder både gyldige og ugyldige rader.

Noen verdier mangler eller kan ikke konverteres til heltall. Programmet skal rapportere disse radene og fortsette med de gyldige.

## Del opp arbeidet med funksjoner

Vi lager én funksjon for å lese og validere:

```python
def read_measurements(path):
```

Den returnerer en liste med ordbøker der `kwh` allerede er et heltall.

Dermed slipper resten av programmet å spørre om verdien fortsatt er tekst eller om den er gyldig.

## En tydelig datastruktur

En gyldig rad lagres slik:

```python
{"month": month, "kwh": kwh}
```

Dette bruker lister og ordbøker fra M7.

## Oppsummeringen

Den andre funksjonen får de validerte målingene:

```python
def print_report(measurements, limit):
```

Den beregner:

- antall gyldige målinger
- total
- minimum
- maksimum
- gjennomsnitt

Deretter viser den bare målinger som er minst like store som `limit`.

## Tomt datasett

Denne gangen håndterer vi også tilfellet der ingen gyldige målinger finnes:

```python
if len(measurements) == 0:
    print("No valid measurements")
    return
```

Da unngår vi å bruke `min()`, `max()` eller divisjon på en tom samling.

## Kjør programmet

```text
python examples/m09/energy_report.py
```

Studer utskriften i denne rekkefølgen:

1. hvilke rader ble hoppet over?
2. hvor mange gyldige målinger finnes?
3. stemmer totalen?
4. hvilke måneder passerer grensen på 700 kWh?

Prøv å svare før du endrer programmet.

## Endre det

Endre grensen fra:

```python
print_report(measurements, 700)
```

til:

```python
print_report(measurements, 500)
```

Forutsi hvilke måneder som nå vises i den filtrerte delen.

## Lag det selv — kumulativt M9-prosjekt

Velg et lite datasett som er nyttig eller interessant for deg. Det kan for eksempel være:

- månedlige utgifter
- temperaturmålinger
- bøker og sidetall
- reiselengder
- tidsbruk på aktiviteter

Lag minst to kolonner: én tekstkolonne og én tallkolonne.

Programmet ditt skal:

1. lese CSV-filen med `DictReader`
2. konvertere tallfeltet eksplisitt
3. oppdage tomme og ugyldige tall
4. lagre gyldige rader
5. beregne minst total og gjennomsnitt
6. filtrere etter en grense du velger
7. skrive forståelig resultat til skjermen

### Ekstra utfordring

Skriv de validerte radene til en ny CSV-fil med `DictWriter`.

Bruk en ny fil. Ikke overskriv originaldataene mens du arbeider med prosjektet.

## Kontroller arbeidet ditt

Før du regner prosjektet som ferdig, prøv minst disse tilfellene:

- alle rader er gyldige
- ett tallfelt er tomt
- ett tallfelt inneholder tekst
- ingen rader passerer filteret

Programmet skal gi forståelig resultat uten at du trenger å redigere Python-koden mellom testene, bortsett fra dataene eller grensen du bevisst vil prøve.

## Hva du nå kan

Etter M9 kan du bruke Python til å arbeide med enkle tabulære data uten ekstra biblioteker.

Du kan lese, kontrollere, konvertere, oppsummere, filtrere og skrive CSV. Like viktig: du kan kombinere filer, funksjoner, lister, ordbøker, løkker og beslutninger i ett sammenhengende program.

Det er et stort steg fra de første `print()`-linjene i kurset.
