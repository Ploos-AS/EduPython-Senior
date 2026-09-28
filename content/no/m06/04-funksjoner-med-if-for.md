# M6.4 – Funksjoner sammen med if og for

Nå kan vi kombinere funksjoner med beslutninger og løkker.

Dette er et viktig steg: funksjonen kan ta imot verdier, arbeide med dem og returnere et resultat.

## Prøv det – funksjon med if

\`\`\`python
def temperatur_melding(temperatur):
    if temperatur < 0:
        return "Under null"
    elif temperatur < 20:
        return "Mellom 0 og under 20"
    else:
        return "20 eller høyere"

print(temperatur_melding(-5))
print(temperatur_melding(12))
print(temperatur_melding(25))
\`\`\`

Funksjonen får én verdi og velger riktig resultat.

Legg merke til at vi ikke trenger å skrive tre forskjellige temperaturprogrammer. Funksjonen kan brukes med mange verdier.

## Følg ett kall

Når vi skriver:

\`\`\`python
temperatur_melding(12)
\`\`\`

blir parameteren:

\`\`\`text
temperatur = 12
\`\`\`

Python tester første betingelse:

\`\`\`text
12 < 0
\`\`\`

Den er usann.

Så testes:

\`\`\`text
12 < 20
\`\`\`

Den er sann.

Funksjonen returnerer:

\`\`\`text
"Mellom 0 og under 20"
\`\`\`

## Funksjon inne i en for-løkke

Funksjonen kan også brukes for hver verdi i en løkke:

\`\`\`python
def temperatur_melding(temperatur):
    if temperatur < 0:
        return "Under null"
    elif temperatur < 20:
        return "Mellom 0 og under 20"
    else:
        return "20 eller høyere"

temperaturer = [-5, 4, 18, 23]

for temperatur in temperaturer:
    melding = temperatur_melding(temperatur)
    print(temperatur, ":", melding)
\`\`\`

Her skjer det samme arbeidet flere ganger, men selve beslutningslogikken ligger ett sted.

## Hvorfor er dette nyttig?

Uten funksjonen kunne vi skrevet hele \`if\`-strukturen på nytt hver gang.

Med funksjonen har vi:

**én regel → mange brukere av regelen**

Hvis regelen endres, kan vi endre funksjonen på ett sted.

## En funksjon kan bruke en løkke

Det kan også gå andre veien:

\`\`\`python
def summer_tall(start, stopp):
    total = 0

    for tall in range(start, stopp):
        total = total + tall

    return total

print(summer_tall(1, 6))
\`\`\`

Her ligger \`for\`-løkken inne i funksjonen.

Funksjonen summerer 1 til 5 og returnerer resultatet.

## Følg dataflyten

Når vi skriver:

\`\`\`python
summer_tall(1, 6)
\`\`\`

kan vi følge:

1. \`start\` blir 1
2. \`stopp\` blir 6
3. \`total\` starter på 0
4. løkka går gjennom 1, 2, 3, 4 og 5
5. \`total\` bygges opp
6. funksjonen returnerer 15

## Ikke gjør funksjonen unødvendig stor

En funksjon bør helst ha en tydelig oppgave.

Denne er lett å forstå:

\`\`\`python
def beregn_total(pris, antall):
    return pris * antall
\`\`\`

En funksjon som både leser mange inputverdier, skriver lange meldinger, gjør mange beslutninger og beregner flere forskjellige ting kan bli vanskeligere å forstå.

Vi lærer mer om dette senere.

## Endre det

Endre temperaturfunksjonen slik at grensene passer til dine egne kategorier.

Test flere verdier.

Prøv også å endre listen med temperaturer uten å endre selve funksjonen.

## Lag det selv

Lag en funksjon som:

- har minst én parameter
- bruker \`if\` eller \`elif\`
- returnerer et resultat
- kalles fra en \`for\`-løkke

Eller lag en funksjon som selv inneholder en \`for\`-løkke og returnerer et samlet resultat.

## Dette har du lært

Du kan nå:

- bruke \`if\` inne i en funksjon
- bruke \`for\` inne i en funksjon
- kalle en funksjon fra en løkke
- returnere forskjellige resultater fra beslutninger
- følge data fra parameter til resultat
- gjenbruke én regel på mange verdier

Neste leksjon viser hvordan funksjoner kan gjøre et helt lite program ryddigere.
