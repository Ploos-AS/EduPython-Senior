# M8.3 – Skriv en tekstfil

Vi har lest filer.

Nå skal programmet lage en fil.

## Viktig før vi begynner

Når vi åpner en fil med:

\`\`\`python
"w"
\`\`\`

betyr det **write** – skriv.

Hvis filen ikke finnes, opprettes den.

Hvis filen allerede finnes, blir det gamle innholdet erstattet.

Derfor bruker vi i denne leksjonen bare en egen kursfil som det er trygt å lage på nytt.

Ikke bruk navnet på et viktig dokument når du eksperimenterer med \`"w"\`.

## Prøv det

\`\`\`python
with open("resultat.txt", "w", encoding="utf-8") as fil:
    fil.write("Dette er skrevet av Python.\n")
\`\`\`

Når programmet er ferdig, finnes filen \`resultat.txt\`.

Åpne den i en teksteditor.

Du skal se:

\`\`\`text
Dette er skrevet av Python.
\`\`\`

## Samme mønster som ved lesing

Ved lesing brukte vi:

\`\`\`python
with open("sample.txt", "r", encoding="utf-8") as fil:
\`\`\`

Ved skriving bruker vi:

\`\`\`python
with open("resultat.txt", "w", encoding="utf-8") as fil:
\`\`\`

Forskjellen er modusen:

\`\`\`text
"r" → read  → les
"w" → write → skriv
\`\`\`

## write()

Denne linjen:

\`\`\`python
fil.write("Dette er skrevet av Python.\n")
\`\`\`

skriver tekst til filen.

Legg merke til escape-sekvensen for linjeskift.

\`write()\` legger ikke automatisk til et linjeskift slik \`print()\` vanligvis gjør.

Hvis vi vil starte en ny linje, må vi derfor skrive linjeskiftet selv.

## Skriv flere linjer

\`\`\`python
with open("resultat.txt", "w", encoding="utf-8") as fil:
    fil.write("Mandag\n")
    fil.write("Tirsdag\n")
    fil.write("Onsdag\n")
\`\`\`

Filen blir:

\`\`\`text
Mandag
Tirsdag
Onsdag
\`\`\`

## Skriv verdier fra en liste

Vi kan kombinere filskriving med det vi lærte i M7:

\`\`\`python
steder = ["Tonstad", "Grimstad", "Oslo"]

with open("steder.txt", "w", encoding="utf-8") as fil:
    for sted in steder:
        fil.write(sted + "\n")
\`\`\`

Nå blir hvert element skrevet på sin egen linje.

## Tall må bli tekst

\`write()\` skriver tekst.

Dette virker derfor ikke:

\`\`\`python
antall = 3
fil.write(antall)
\`\`\`

Vi må konvertere tallet:

\`\`\`python
antall = 3
fil.write(str(antall))
\`\`\`

Dette er samme idé som tidligere: Python skiller mellom tall og tekst.

## Skriv og les tilbake

En nyttig måte å kontrollere et lite program på er:

1. skriv filen
2. åpne den for lesing
3. se hva som faktisk ble lagret

\`\`\`python
with open("resultat.txt", "w", encoding="utf-8") as fil:
    fil.write("Linje én\n")
    fil.write("Linje to\n")

with open("resultat.txt", "r", encoding="utf-8") as fil:
    innhold = fil.read()

print(innhold)
\`\`\`

Den første \`with\`-blokken skriver.

Den andre leser.

## Hva skjer hvis filen allerede finnes?

Tenk at \`resultat.txt\` inneholder:

\`\`\`text
Gammel tekst
\`\`\`

Så kjører vi:

\`\`\`python
with open("resultat.txt", "w", encoding="utf-8") as fil:
    fil.write("Ny tekst\n")
\`\`\`

Etterpå inneholder filen:

\`\`\`text
Ny tekst
\`\`\`

Den gamle teksten er borte.

Det er derfor vi må vite hvilken fil vi åpner før vi bruker \`"w"\`.

## En enkel sikkerhetsregel

Mens du lærer:

**Bruk \`"w"\` bare på filer du selv har laget for øvelsen.**

Vi skal ikke skrive til dokumenter, bilder, konfigurasjonsfiler eller andre viktige filer.

Senere lærer vi hvordan vi kan legge til innhold uten å erstatte det gamle.

## Endre det

Lag en liste:

\`\`\`python
oppgaver = ["Handle", "Ringe banken", "Lese"]
\`\`\`

Skriv hvert element til \`oppgaver.txt\`, ett element per linje.

Åpne filen etterpå og kontroller innholdet.

Endre deretter listen og kjør programmet igjen.

Legg merke til at filen bygges på nytt fra listen.

## Lag det selv

Lag et program som:

1. har en liste med minst tre tekstverdier
2. åpner en ny øvingsfil med \`"w"\`
3. bruker en \`for\`-løkke
4. skriver én verdi per linje
5. åpner filen igjen med \`"r"\`
6. skriver det lagrede innholdet til skjermen

Bruk bare en fil du har laget spesielt til øvelsen.

## Dette har du lært

Du kan nå:

- åpne en fil med \`"w"\`
- forklare at \`"w"\` oppretter eller erstatter en fil
- skrive tekst med \`write()\`
- legge til linjeskift med escape-sekvensen for linjeskift
- konvertere tall til tekst før skriving
- skrive elementer fra en liste
- lese en skrevet fil tilbake for kontroll
- forklare hvorfor filnavnet må kontrolleres før \`"w"\` brukes

Neste leksjon handler om å legge til nye data uten å erstatte det gamle innholdet.
