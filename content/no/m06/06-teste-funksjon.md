# M6.6 – Test én funksjon om gangen

Når et program ikke virker som forventet, kan det være vanskelig å finne feilen hvis alt ligger i én stor kodeblokk.

Små funksjoner gjør det lettere å undersøke én del om gangen.

## Prøv det

Se på denne funksjonen:

\`\`\`python
def beregn_total(pris, antall):
    return pris * antall
\`\`\`

Vi kan teste den med kjente verdier:

\`\`\`python
print(beregn_total(10, 3))
print(beregn_total(25, 4))
\`\`\`

Vi forventer:

\`\`\`text
30
100
\`\`\`

Hvis resultatet er annerledes, vet vi at vi bør undersøke selve beregningen.

## Test med enkle verdier

Når du feilsøker, er det ofte nyttig å begynne med verdier der svaret er lett å regne ut selv.

For eksempel:

\`\`\`python
beregn_total(10, 3)
\`\`\`

er lett å kontrollere:

\`\`\`text
10 × 3 = 30
\`\`\`

Deretter kan vi prøve mer realistiske verdier.

## En funksjon kan ha en liten testdel

\`\`\`python
def beregn_total(pris, antall):
    return pris * antall


print("Test 1:", beregn_total(10, 3))
print("Test 2:", beregn_total(25, 4))
\`\`\`

Dette er ikke et avansert testverktøy. Det er bare en enkel måte å undersøke funksjonen på.

## Finn en logisk feil

Se på:

\`\`\`python
def beregn_total(pris, antall):
    return pris + antall
\`\`\`

Hvis vi tester:

\`\`\`python
print(beregn_total(10, 3))
\`\`\`

får vi 13.

Men hvis funksjonen skal beregne pris ganger antall, forventer vi 30.

Programmet kan altså være gyldig Python, men likevel ha feil logikk.

Riktig:

\`\`\`python
def beregn_total(pris, antall):
    return pris * antall
\`\`\`

## Test funksjonen før resten av programmet

Anta at hovedprogrammet er:

\`\`\`python
pris = 25
antall = 4

total = beregn_total(pris, antall)
print("Total:", total)
\`\`\`

Hvis totalen er feil, kan vi først teste:

\`\`\`python
print(beregn_total(25, 4))
\`\`\`

Da undersøker vi funksjonen uten resten av programmet.

## Test forskjellige typer situasjoner

For en enkel beregningsfunksjon kan vi teste:

**Vanlig verdi**

\`\`\`python
beregn_total(25, 4)
\`\`\`

**Én enhet**

\`\`\`python
beregn_total(25, 1)
\`\`\`

**Null**

\`\`\`python
beregn_total(25, 0)
\`\`\`

Det siste kan være nyttig fordi grenseverdier ofte avslører feil.

## Ikke stol på bare én test

Hvis én test virker, betyr det ikke nødvendigvis at funksjonen alltid virker.

Flere små tester gir bedre informasjon.

## Endre det

Lag en funksjon som gjør en enkel beregning.

Finn minst tre testverdier som du kan regne ut på forhånd.

Sammenlign Python-resultatet med det du forventet.

## Lag det selv

Lag en funksjon som:

- har minst én parameter
- returnerer et resultat
- testes med minst tre forskjellige kall
- har minst én test med en grenseverdi, for eksempel 0 eller 1

Skriv gjerne forventet resultat som kommentar før du kjører testen.

## Dette har du lært

Du kan nå:

- teste en funksjon separat
- bruke enkle verdier for å kontrollere en beregning
- skille mellom syntaksfeil og logiske feil
- bruke flere testverdier
- bruke grenseverdier i enkel testing
- finne feil i en liten funksjon før du undersøker resten av programmet

Neste leksjon samler M6 med oppgaver og feilsøking.
