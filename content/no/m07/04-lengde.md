# M7.4 – Hvor lang er listen?

Ofte trenger vi å vite hvor mange elementer en liste inneholder.

Python har funksjonen \`len()\`.

## Prøv det

\`\`\`python
temperaturer = [18, 20, 17, 21]

antall = len(temperaturer)

print("Antall:", antall)
\`\`\`

Resultat:

\`\`\`text
Antall: 4
\`\`\`

\`len\` er en forkortelse for *length*, som betyr lengde.

## len() gir antall elementer

Listen:

\`\`\`python
temperaturer = [18, 20, 17, 21]
\`\`\`

har fire elementer.

Derfor:

\`\`\`python
len(temperaturer)
\`\`\`

gir \`4\`.

## Antall og siste indeks er forskjellige

Dette er viktig.

For listen:

\`\`\`python
dager = ["mandag", "tirsdag", "onsdag"]
\`\`\`

er:

\`\`\`text
antall elementer: 3
gyldige indekser: 0, 1, 2
siste indeks:      2
\`\`\`

Dermed:

\`\`\`python
len(dager)
\`\`\`

gir 3, men:

\`\`\`python
dager[2]
\`\`\`

henter siste element.

## Siste indeks med len()

Når listen ikke er tom, er siste gyldige indeks:

\`\`\`python
len(dager) - 1
\`\`\`

Eksempel:

\`\`\`python
dager = ["mandag", "tirsdag", "onsdag"]

siste_indeks = len(dager) - 1

print(dager[siste_indeks])
\`\`\`

Resultat:

\`\`\`text
onsdag
\`\`\`

Vi lærer senere en kortere Python-måte å hente siste element på. Akkurat nå bruker vi dette for å gjøre forholdet mellom lengde og indeks tydelig.

## Hva med en tom liste?

\`\`\`python
verdier = []

print(len(verdier))
\`\`\`

Resultat:

\`\`\`text
0
\`\`\`

En tom liste har lengde 0.

Men da finnes det ingen gyldig indeks.

Hvis vi regner:

\`\`\`python
len(verdier) - 1
\`\`\`

får vi \`-1\`, men dette betyr ikke at listen plutselig har et element.

Vi skal lære mer om negative indekser senere.

## Sjekk før du henter

Vi kan bruke det vi lærte om \`if\`:

\`\`\`python
verdier = []

if len(verdier) > 0:
    siste_indeks = len(verdier) - 1
    print(verdier[siste_indeks])
else:
    print("Listen er tom.")
\`\`\`

Resultat:

\`\`\`text
Listen er tom.
\`\`\`

Nå prøver programmet bare å hente et element når listen faktisk inneholder noe.

## len() etter append()

Lengden endrer seg når vi legger til verdier:

\`\`\`python
målinger = []

print(len(målinger))

målinger.append(12)
print(len(målinger))

målinger.append(15)
print(len(målinger))
\`\`\`

Resultat:

\`\`\`text
0
1
2
\`\`\`

Dette viser at listen endres mens programmet kjører.

## Bruk len() i en funksjon

\`\`\`python
def vis_antall(verdier):
    print("Listen har", len(verdier), "elementer.")

vis_antall([10, 20, 30])
\`\`\`

Resultat:

\`\`\`text
Listen har 3 elementer.
\`\`\`

Her kombinerer vi lister med funksjoner fra M6.

## Endre det

Start med:

\`\`\`python
steder = ["Tonstad", "Grimstad", "Oslo", "Bergen"]
\`\`\`

Skriv ut:

- hele listen
- antall elementer
- siste gyldige indeks
- elementet på siste gyldige indeks

Legg deretter til et nytt sted med \`append()\` og gjør det samme igjen.

## Lag det selv

Lag en liste med minst fem verdier.

Bruk \`len()\` til å finne antallet.

Lag deretter en tom liste og bruk \`if\` til å kontrollere at den har minst ett element før du prøver å hente det siste.

## Dette har du lært

Du kan nå:

- bruke \`len()\` for å finne antall elementer
- skille mellom antall elementer og siste indeks
- finne siste indeks i en ikke-tom liste med \`len(liste) - 1\`
- forklare hvorfor en tom liste krever ekstra omtanke
- bruke \`if\` før du henter et element
- se at lengden endres når listen endres
- bruke \`len()\` sammen med funksjoner

Neste leksjon introduserer dictionaries: samlinger der vi finner verdier ved hjelp av navn i stedet for nummererte posisjoner.
