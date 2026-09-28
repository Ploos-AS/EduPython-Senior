# M8.1 – Hvorfor trenger programmer filer?

Så langt har programmene våre laget data i variabler, lister og ordbøker.

Men hva skjer når programmet avsluttes?

## Data i programmet varer ikke automatisk

Se på:

\`\`\`python
navn = "Anna"
målinger = [12, 15, 11]

print(navn)
print(målinger)
\`\`\`

Mens programmet kjører, finnes verdiene i variablene.

Når programmet er ferdig, blir ikke disse variablene automatisk lagret til neste gang programmet starter.

Hvis vi vil beholde data, trenger vi et sted å lagre dem.

Et vanlig sted er en **fil**.

## En fil kan overleve programmet

Du kjenner allerede filer fra andre programmer:

- tekstdokumenter
- bilder
- regneark
- PDF-filer
- musikkfiler

Et Python-program kan også lese og skrive filer.

I denne leksjonen skal vi bare **lese** en tekstfil som følger med kurset.

Vi endrer eller sletter ingen filer.

## Kursfilen

Eksempelet bruker filen:

\`\`\`text
sample.txt
\`\`\`

Den inneholder vanlig tekst.

Tenk på den som en liten notatfil programmet skal lese.

## Prøv det

\`\`\`python
with open("sample.txt", "r", encoding="utf-8") as fil:
    innhold = fil.read()

print(innhold)
\`\`\`

Når eksempelet kjøres fra mappen der filen ligger, åpner Python \`sample.txt\`, leser teksten og legger den i variabelen \`innhold\`.

Deretter skriver programmet ut teksten.

## Les koden i små deler

Først:

\`\`\`python
open("sample.txt", "r", encoding="utf-8")
\`\`\`

Dette ber Python åpne filen.

\`"sample.txt"\` er navnet på filen.

\`"r"\` betyr **read** – les.

\`encoding="utf-8"\` forteller hvordan teksten i filen er kodet.

UTF-8 kan representere blant annet norske bokstaver som æ, ø og å.

## with open(...)

Hele starten er:

\`\`\`python
with open("sample.txt", "r", encoding="utf-8") as fil:
\`\`\`

Mens den innrykkede delen kjører, kan vi bruke filen gjennom navnet \`fil\`.

\`with\` sørger også for at filen blir lukket riktig når den innrykkede delen er ferdig.

Dette blir standardmåten vår å arbeide med filer på.

Du trenger ikke lære en separat \`close()\`-regel først.

## read()

Denne linjen:

\`\`\`python
innhold = fil.read()
\`\`\`

leser hele tekstinnholdet fra filen.

Resultatet er tekst, altså en streng.

Det betyr at \`innhold\` kan brukes som andre tekstverdier du allerede kjenner.

## Innrykk betyr noe igjen

Legg merke til:

\`\`\`python
with open("sample.txt", "r", encoding="utf-8") as fil:
    innhold = fil.read()

print(innhold)
\`\`\`

\`fil.read()\` står inni \`with\`-blokken.

\`print(innhold)\` står etter blokken.

Selve filen er da lukket, men teksten vi leste ligger fortsatt i variabelen \`innhold\`.

## Hva betyr filnavnet?

\`\`\`text
sample.txt
\`\`\`

er en **sti** til filen.

Her er stien svært enkel: bare filnavnet.

Det betyr at Python leter etter filen i programmets nåværende arbeidsmappe.

Vi skal lære mer om mapper og stier senere i M8.

## Hvis filen ikke finnes

Hvis Python ikke finner filen, får du vanligvis:

\`\`\`text
FileNotFoundError
\`\`\`

Det betyr ikke at Python er ødelagt.

Det betyr at programmet ba om en fil på et sted der Python ikke kunne finne den.

Når du ser denne feilen, kontroller:

1. filnavnet
2. stavemåten
3. hvilken mappe programmet kjører fra
4. om filen faktisk finnes der

Vi kommer tilbake til denne feilen senere.

## Endre det

Åpne kursfilen \`sample.txt\`.

Endre litt av teksten i filen, lagre den og kjør programmet igjen.

Se at Python nå leser den nye teksten.

Ikke endre filnavnet ennå.

## Lag det selv

Lag en ny vanlig tekstfil i samme mappe som programmet.

Skriv én eller to linjer i filen.

Lag deretter en kopi av leseprogrammet og endre filnavnet slik at det leser din fil.

Bruk fortsatt:

\`\`\`python
"r"
\`\`\`

slik at programmet bare åpner filen for lesing.

## Dette har du lært

Du kan nå:

- forklare hvorfor filer brukes til data som skal eksistere utenfor én programkjøring
- åpne en tekstfil for lesing
- bruke \`with open(...)\`
- lese hele filen med \`read()\`
- forklare hva \`"r"\` betyr
- kjenne igjen \`encoding="utf-8"\`
- forstå at et enkelt filnavn også er en sti
- kjenne igjen \`FileNotFoundError\`

Neste leksjon handler om å lese en tekstfil linje for linje.
