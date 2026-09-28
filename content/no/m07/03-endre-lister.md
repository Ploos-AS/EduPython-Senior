# M7.3 – Endre en liste

Lister kan endres etter at de er laget.

Vi begynner med to vanlige operasjoner:

1. erstatte en verdi som allerede finnes
2. legge til en ny verdi på slutten

## Prøv det – erstatt en verdi

\`\`\`python
temperaturer = [18, 20, 17]

temperaturer[1] = 21

print(temperaturer)
\`\`\`

Resultat:

\`\`\`text
[18, 21, 17]
\`\`\`

Indeks 1 var den andre verdien.

Vi erstattet 20 med 21.

## Les tilordningen

Denne linjen:

\`\`\`python
temperaturer[1] = 21
\`\`\`

kan leses som:

> sett verdien på indeks 1 i temperaturer til 21

Vi bruker samme indeksmodell som i forrige leksjon:

\`\`\`text
indeks:    0    1    2
før:      18   20   17
etter:    18   21   17
\`\`\`

Listen er den samme listen, men innholdet er endret.

## Indeksen må finnes

Hvis listen er:

\`\`\`python
temperaturer = [18, 20, 17]
\`\`\`

kan vi endre indeks 0, 1 eller 2.

Dette virker ikke:

\`\`\`python
temperaturer[3] = 25
\`\`\`

Python gir:

\`\`\`text
IndexError: list assignment index out of range
\`\`\`

Indeks 3 finnes ikke ennå.

For å legge til en ny verdi bruker vi \`append()\`.

## Legg til med append

\`\`\`python
temperaturer = [18, 20, 17]

temperaturer.append(21)

print(temperaturer)
\`\`\`

Resultat:

\`\`\`text
[18, 20, 17, 21]
\`\`\`

\`append()\` legger én ny verdi på slutten av listen.

## Punktumet betyr at vi gjør noe med listen

Se på:

\`\`\`python
temperaturer.append(21)
\`\`\`

Her ber vi listen \`temperaturer\` om å utføre operasjonen \`append\`.

Python har mange slike operasjoner for lister. De kalles **metoder**.

Du trenger ikke lære mange metoder nå. I denne leksjonen bruker vi bare \`append()\`.

## Start med en tom liste

En liste kan bygges opp etter hvert:

\`\`\`python
målinger = []

målinger.append(12)
målinger.append(15)
målinger.append(11)

print(målinger)
\`\`\`

Resultat:

\`\`\`text
[12, 15, 11]
\`\`\`

Dette er nyttig når vi ikke kjenner alle verdiene når programmet starter.

## Bygg en liste i en løkke

Vi kan kombinere \`append()\` med \`for\`:

\`\`\`python
doble_tall = []

for tall in [2, 4, 6]:
    doble_tall.append(tall * 2)

print(doble_tall)
\`\`\`

Resultat:

\`\`\`text
[4, 8, 12]
\`\`\`

Følg listen:

\`\`\`text
start:       []
etter 2:     [4]
etter 4:     [4, 8]
etter 6:     [4, 8, 12]
\`\`\`

Listen endres for hver runde i løkka.

## Erstatte eller legge til?

Bruk:

\`\`\`python
liste[indeks] = verdi
\`\`\`

når du vil **erstatte en verdi på en plass som allerede finnes**.

Bruk:

\`\`\`python
liste.append(verdi)
\`\`\`

når du vil **legge en ny verdi på slutten**.

## Endre det

Start med:

\`\`\`python
steder = ["Tonstad", "Grimstad", "Oslo"]
\`\`\`

Erstatt den andre verdien med et annet sted.

Legg deretter til et fjerde sted med \`append()\`.

Skriv ut listen etter hver endring.

## Lag det selv

Start med en tom liste.

Legg til minst fire relaterte verdier med \`append()\`.

Endre deretter én av verdiene ved hjelp av en indeks.

Bruk en \`for\`-løkke til å skrive ut den ferdige listen én verdi om gangen.

## Dette har du lært

Du kan nå:

- erstatte et eksisterende listeelement
- forklare at indeksen må finnes før den kan erstattes
- kjenne igjen \`IndexError\` ved ugyldig tilordning
- legge til en verdi med \`append()\`
- forklare enkelt hva en listemetode er
- bygge opp en tom liste
- bruke \`append()\` i en løkke
- velge mellom å erstatte og å legge til

Neste leksjon handler om hvor mange elementer en liste inneholder og hvordan vi kan bruke lengden på en trygg måte.
