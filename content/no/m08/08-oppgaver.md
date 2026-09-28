# M8.8 – Oppgaver og mini-prosjekt

Nå skal du bruke det du har lært i M8 samlet.

Målet er ikke å lære mange nye Python-funksjoner. Målet er å øve på å sette kjente deler sammen.

## Oppgave 1 – Les hele filen

Lag en tekstfil med tre korte linjer.

Skriv et program som:

1. åpner filen med \`"r"\`
2. bruker UTF-8
3. leser hele innholdet med \`read()\`
4. skriver innholdet til skjermen

Forklar for deg selv hvorfor \`with open(...)\` er nyttig.

## Oppgave 2 – Linje for linje

Lag en fil med fire heltall, ett tall per linje.

Les filen med en \`for\`-løkke.

For hver linje:

1. bruk \`strip()\`
2. konverter teksten med \`int()\`
3. skriv tallet til skjermen

Tell samtidig hvor mange tall filen inneholder.

## Oppgave 3 – Finn feilen

Programmet skal lese \`data/navn.txt\`, men gir:

```text
FileNotFoundError
```

Undersøk i denne rekkefølgen:

1. filnavnet
2. filendelsen
3. store og små bokstaver
4. om \`data\`-mappen finnes
5. hvilken sti programmet faktisk bruker

Ikke legg inn en generell \`except\` bare for å få feilmeldingen bort.

## Oppgave 4 – Write eller append?

Velg riktig modus.

A. En rapport skal bygges helt på nytt hver gang.

B. En logg skal beholde gamle hendelser og få en ny linje.

C. En eksisterende tekstfil skal bare leses.

Svar med én av:

```text
"r"
"w"
"a"
```

Forklar hvorfor.

## Oppgave 5 – Hva blir resultatet?

Filen inneholder først:

```text
Start
```

Programmet kjører:

```python
with open("logg.txt", "a", encoding="utf-8") as fil:
    fil.write("Kontroll\n")

with open("logg.txt", "a", encoding="utf-8") as fil:
    fil.write("Ferdig\n")
```

Skriv ned hva du tror filen inneholder etterpå.

Kjør deretter programmet og kontroller svaret.

## Oppgave 6 – Funksjoner

Lag:

```python
def les_tall(filsti):
    ...
```

Funksjonen skal lese ett heltall per linje og returnere en liste.

Lag deretter:

```python
def beregn_total(tall):
    ...
```

Den skal returnere summen uten å lese noen fil.

Hvorfor kan det være nyttig at beregningsfunksjonen ikke kjenner filnavnet?

# Mini-prosjekt – Målearkiv

Vi skal lage et lite program som lagrer målinger over tid.

Programmet bruker en kontrollert tekstfil som tilhører prosjektet.

Hver linje inneholder ett heltall:

```text
12
15
11
14
```

## Del 1 – Finn filene

Bruk \`Path\`:

```python
from pathlib import Path

programmappe = Path(__file__).parent
datafil = programmappe / "data" / "målinger.txt"
rapportfil = programmappe / "rapport.txt"
```

## Del 2 – Les historikken

Lag:

```python
def les_målinger(filsti):
    ...
```

Funksjonen skal:

- åpne filen med \`"r"\`
- lese linje for linje
- bruke \`strip()\`
- konvertere med \`int()\`
- legge verdiene i en liste
- returnere listen

## Del 3 – Legg til en ny måling

Lag:

```python
def legg_til_måling(filsti, verdi):
    ...
```

Bruk \`"a"\`.

Husk at \`write()\` trenger tekst og at hver måling skal få sin egen linje.

## Del 4 – Beregn

Lag en funksjon som beregner totalen av målingene.

Du kan også lage en funksjon som teller dem med \`len()\`.

Hold beregningen adskilt fra filinnlesingen.

## Del 5 – Skriv en rapport

Lag:

```python
def skriv_rapport(filsti, antall, total):
    ...
```

Rapporten kan for eksempel bli:

```text
Antall målinger: 5
Total: 65
```

Rapporten representerer gjeldende resultat og kan derfor skrives med \`"w"\`.

Historikkfilen og rapportfilen har altså forskjellige behov:

```text
målinger.txt → "a" → behold historikken
rapport.txt  → "w" → bygg gjeldende rapport på nytt
```

## Del 6 – Les rapporten tilbake

Åpne rapportfilen med \`"r"\` og skriv den til skjermen.

Da kontrollerer programmet at resultatet faktisk ble lagret.

## Del 7 – Test med vilje

Test minst disse situasjonene:

- vanlig datafil
- én ny måling
- kjør append-delen en gang til
- feil navn på datafilen
- en linje som ikke kan konverteres til heltall

Les hvilken feil Python gir.

Rett deretter årsaken.

## Debugging-oppgave

Dette programmet har en logisk feil:

```python
def lagre(filsti, verdi):
    with open(filsti, "w", encoding="utf-8") as fil:
        fil.write(str(verdi) + "\n")
```

Programmet kaller \`lagre()\` hver gang en ny historisk måling kommer.

Hvorfor forsvinner de gamle målingene?

Hvilken modus passer bedre når historikken skal bevares?

## Før du går videre

Du bør nå kunne forklare forskjellen mellom:

```text
filinnhold
filsti
arbeidsmappe
programmets mappe
"r"
"w"
"a"
read()
write()
FileNotFoundError
ValueError
```

Du trenger ikke huske all syntaks utenat.

Det viktige er at du kjenner igjen delene, forstår hva de gjør og vet hvordan du kan undersøke en feil.

## M8 fullført

Du har nå gått fra data som bare finnes mens programmet kjører, til programmer som kan lagre og hente data.

Du kan:

- lese hele tekstfiler
- behandle filer linje for linje
- skrive nye filer
- legge til historikk
- velge mellom \`"r"\`, \`"w"\` og \`"a"\`
- lese og forstå vanlige filfeil
- bruke mapper og relative stier
- bygge robuste stier med \`Path\`
- kombinere filer, lister, løkker og funksjoner
- skille innlesing, behandling og utskrift/lagring
- bygge et lite program med varige data

Neste milepæl er M9, der vi arbeider med strukturerte tabelldata og CSV.
