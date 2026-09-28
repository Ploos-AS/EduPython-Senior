# M8.6 – Mapper og relative stier

En fil ligger et sted.

For å åpne riktig fil må programmet vite **stien** til den.

Så langt har vi brukt enkle stier som:

```text
sample.txt
```

Nå skal vi også bruke mapper.

## En enkel mappestruktur

Tenk at prosjektet ser slik ut:

```text
mitt-program/
├── program.py
└── data/
    └── steder.txt
```

Python-filen heter \`program.py\`.

Tekstfilen ligger i undermappen \`data\`.

En relativ sti til tekstfilen kan skrives:

```text
data/steder.txt
```

## Hva betyr relativ sti?

En **relativ sti** beskriver et sted i forhold til et annet sted.

Dette:

```text
data/steder.txt
```

betyr omtrent:

> gå til mappen \`data\`, og finn filen \`steder.txt\`

Men det finnes et viktig spørsmål:

**I forhold til hvilken mappe?**

## Arbeidsmappen

Når Python starter et program, har prosessen en **nåværende arbeidsmappe**.

Et enkelt kall som:

```python
open("data/steder.txt", "r", encoding="utf-8")
```

tolkes i forhold til denne arbeidsmappen.

Arbeidsmappen er ikke nødvendigvis den samme mappen som Python-filen ligger i.

Dette er en vanlig årsak til \`FileNotFoundError\`.

## En mer robust kursmåte

Python har standardbiblioteket \`pathlib\`.

Der finner vi \`Path\`.

```python
from pathlib import Path
```

Vi kan finne mappen der selve Python-filen ligger:

```python
programmappe = Path(__file__).parent
```

Du trenger ikke kunne alle detaljene i \`__file__\` nå.

I dette mønsteret betyr det ganske enkelt:

> start med plasseringen til Python-filen

## Bygg en sti

Vi kan kombinere mapper og filnavn med \`/\`:

```python
from pathlib import Path

programmappe = Path(__file__).parent
filsti = programmappe / "data" / "steder.txt"
```

Dette bygger stien lag for lag:

```text
programmappe
    │
    └── data
         │
         └── steder.txt
```

\`/\` betyr her ikke divisjon.

Når vi arbeider med \`Path\`, brukes det til å kombinere deler av en sti.

## Les filen

```python
from pathlib import Path

programmappe = Path(__file__).parent
filsti = programmappe / "data" / "steder.txt"

with open(filsti, "r", encoding="utf-8") as fil:
    for linje in fil:
        print(linje.strip())
```

Programmet finner nå datafilen ut fra hvor \`program.py\` ligger, ikke ut fra hvilken arbeidsmappe vi tilfeldigvis startet Python fra.

## Hvorfor er dette nyttig?

Tenk at programmet ligger i:

```text
kurs/m08/program.py
```

Du kan starte det fra forskjellige steder.

Hvis filstien bygges fra \`Path(__file__).parent\`, kan programmet fortsatt finne datafilen som ligger ved siden av programmet i prosjektstrukturen.

Dette gjør eksempler og små prosjekter mer forutsigbare.

## Path er en stiverdi

Variabelen:

```python
filsti = programmappe / "data" / "steder.txt"
```

inneholder et \`Path\`-objekt.

\`open()\` kan bruke dette direkte:

```python
open(filsti, "r", encoding="utf-8")
```

Vi trenger altså ikke konvertere stien til tekst først.

## parent

I:

```python
Path(__file__).parent
```

betyr \`.parent\` mappen som inneholder filen.

Hvis Python-filen er:

```text
/home/anna/kurs/program.py
```

er parent-mappen:

```text
/home/anna/kurs
```

Den nøyaktige stien vil naturligvis være forskjellig på forskjellige maskiner.

Det er nettopp derfor vi ikke skriver en bestemt brukers komplette sti inn i programmet.

## Unngå hardkodede personlige stier

Dette kan virke på én bestemt maskin:

```python
open("/home/anna/kurs/data/steder.txt", "r", encoding="utf-8")
```

men programmet blir bundet til den plasseringen.

På en annen maskin kan brukernavnet, operativsystemet eller mappestrukturen være annerledes.

Når datafilen følger programmet, er det ofte bedre å bygge stien relativt til programfilen.

## Mapper kan også mangle

Hvis vi bygger:

```python
filsti = programmappe / "data" / "steder.txt"
```

men \`data\`-mappen eller filen ikke finnes, kan lesing fortsatt gi:

```text
FileNotFoundError
```

En korrekt Python-sti kan altså fortsatt peke til noe som ikke finnes.

Bruk feilsøkingen fra M8.5.

## Endre det

Lag denne strukturen:

```text
øvelse/
├── program.py
└── data/
    └── navn.txt
```

Legg noen navn i \`navn.txt\`.

Bruk:

```python
from pathlib import Path

programmappe = Path(__file__).parent
filsti = programmappe / "data" / "navn.txt"
```

Les filen linje for linje.

## Lag det selv

Lag en ny undermappe ved siden av programmet, for eksempel:

```text
notater/
```

Legg en tekstfil i mappen.

Bygg stien med \`Path(__file__).parent\` og \`/\`.

Programmet skal:

1. bygge stien
2. åpne filen med \`"r"\`
3. lese den linje for linje
4. bruke \`strip()\`
5. skrive ut innholdet

## Dette har du lært

Du kan nå:

- forklare hva en mappe og filsti beskriver
- kjenne igjen en relativ sti
- forstå at arbeidsmappen og programmappen kan være forskjellige
- importere \`Path\` fra \`pathlib\`
- finne programmappen med \`Path(__file__).parent\`
- bygge en sti med \`/\`
- åpne en \`Path\` direkte med \`open()\`
- unngå å hardkode en bestemt brukers komplette sti
- bruke \`FileNotFoundError\`-kunnskapen når en mappe eller fil mangler

Neste leksjon kombinerer filer med lister og funksjoner.
