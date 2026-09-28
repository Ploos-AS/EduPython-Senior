# M8.7 – Filer, lister og funksjoner

Vi har nå lært å:

- lese filer
- skrive filer
- legge til med append
- bruke mapper og stier
- bruke lister
- lage funksjoner

Nå setter vi delene sammen.

## En tydelig dataflyt

Et nyttig mønster er:

\`\`\`text
fil
 ↓
lesefunksjon
 ↓
liste
 ↓
behandling
 ↓
resultat
 ↓
skrivefunksjon
 ↓
ny fil
\`\`\`

Hver del har én tydelig oppgave.

## Datafilen

Tenk at \`målinger.txt\` inneholder:

\`\`\`text
12
15
11
14
\`\`\`

Vi vil:

1. lese tallene
2. lagre dem i en liste
3. beregne totalen
4. skrive resultatet til en ny fil

## Les filen inn i en liste

\`\`\`python
def les_målinger(filsti):
    målinger = []

    with open(filsti, "r", encoding="utf-8") as fil:
        for linje in fil:
            verdi = int(linje.strip())
            målinger.append(verdi)

    return målinger
\`\`\`

Følg dataene:

Først:

\`\`\`python
målinger = []
\`\`\`

Etter første linje:

\`\`\`python
målinger = [12]
\`\`\`

Etter andre:

\`\`\`python
målinger = [12, 15]
\`\`\`

Til slutt:

\`\`\`python
målinger = [12, 15, 11, 14]
\`\`\`

Funksjonen returnerer listen.

## Filstien er en parameter

Legg merke til:

\`\`\`python
def les_målinger(filsti):
\`\`\`

Funksjonen bestemmer ikke selv hvilket bestemt filnavn som skal brukes.

Den får stien som et argument.

Det gjør funksjonen lettere å bruke med andre øvingsfiler senere.

## Beregn med listen

Filbehandlingen trenger ikke være en del av beregningen.

\`\`\`python
def beregn_total(målinger):
    total = 0

    for måling in målinger:
        total = total + måling

    return total
\`\`\`

Denne funksjonen vet ingenting om filer.

Den får en liste og returnerer et tall.

Det gjør ansvaret tydelig:

\`\`\`text
les_målinger()   → fil til liste
beregn_total()   → liste til tall
\`\`\`

## Skriv resultatet

\`\`\`python
def skriv_resultat(filsti, total):
    with open(filsti, "w", encoding="utf-8") as fil:
        fil.write("Total: " + str(total) + "\n")
\`\`\`

Denne funksjonen har ett annet ansvar:

\`\`\`text
skriv_resultat() → verdi til fil
\`\`\`

## Sett delene sammen

Med \`Path\` kan hoveddelen av programmet se slik ut:

\`\`\`python
from pathlib import Path

programmappe = Path(__file__).parent
innfil = programmappe / "data" / "målinger.txt"
utfil = programmappe / "resultat.txt"

målinger = les_målinger(innfil)
total = beregn_total(målinger)
skriv_resultat(utfil, total)

print("Målinger:", målinger)
print("Total:", total)
\`\`\`

Dataflyten er:

\`\`\`text
målinger.txt
     ↓
[12, 15, 11, 14]
     ↓
52
     ↓
resultat.txt
\`\`\`

## Hvorfor bruke flere funksjoner?

Vi kunne skrevet alt i én lang blokk.

Men separate funksjoner gjør det lettere å svare på:

- Hvor leses filen?
- Hvor konverteres linjene til tall?
- Hvor beregnes totalen?
- Hvor skrives resultatet?

Hvis totalen er feil, kan vi undersøke \`beregn_total()\`.

Hvis filen ikke finnes, kan vi undersøke stien og \`les_målinger()\`.

Dette gjør feilsøking enklere.

## Kontroller mellomsteg

Vi kan skrive ut listen før beregningen:

\`\`\`python
målinger = les_målinger(innfil)
print(målinger)
\`\`\`

Hvis resultatet er:

\`\`\`text
[12, 15, 11, 14]
\`\`\`

vet vi at lesingen og konverteringen ser riktig ut.

Så kan vi undersøke neste steg.

Dette er en nyttig måte å feilsøke en dataflyt på: kontroller ett mellomresultat om gangen.

## Hva hvis en linje ikke er et tall?

Hvis filen inneholder:

\`\`\`text
12
femten
11
\`\`\`

vil:

\`\`\`python
int("femten")
\`\`\`

gi \`ValueError\`.

Det er ikke en filfeil.

Filen ble funnet og lest, men innholdet hadde ikke formatet programmet forventet.

Dette viser hvorfor det er nyttig å lese den faktiske feiltypen.

Vi legger ikke inn en bred \`except\` for å skjule problemet.

## Endre det

Bruk en fil med fire heltall.

1. Les dem inn i en liste med en funksjon.
2. Skriv ut listen.
3. Beregn totalen i en annen funksjon.
4. Endre ett tall i datafilen.
5. Kjør programmet igjen og følg hvordan resultatet endres.

## Lag det selv

Lag et lite program med tre funksjoner:

\`\`\`python
def les_data(filsti):
    ...

def beregn(data):
    ...

def skriv_resultat(filsti, resultat):
    ...
\`\`\`

Bruk en egen øvingsfil med ett heltall per linje.

Programmet skal:

1. bygge inn- og utstier med \`Path\`
2. lese tallene til en liste
3. gjøre en enkel beregning
4. skrive resultatet til en egen resultatfil
5. skrive resultatet til skjermen

Bruk bare en kontrollert øvingsfil som utfil.

## Dette har du lært

Du kan nå:

- lese filinnhold inn i en liste
- sende en filsti til en funksjon
- returnere en liste fra en funksjon
- skille filinnlesing fra beregning
- skrive et beregnet resultat til en ny fil
- bygge en enkel dataflyt fra fil til Python-data og tilbake til fil
- kontrollere mellomresultater under feilsøking
- skille \`FileNotFoundError\` fra \`ValueError\`

Neste leksjon samler M8 med oppgaver, feilsøking og et mini-prosjekt.
