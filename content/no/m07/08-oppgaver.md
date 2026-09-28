# M7.8 – Oppgaver og mini-prosjekt

Nå skal du bruke lister og ordbøker uten at hvert steg blir vist på forhånd.

Arbeid gjerne i denne rekkefølgen:

1. forutsi hva programmet gjør
2. kjør programmet
3. sammenlign resultatet med forutsigelsen
4. undersøk eventuelle feil
5. endre programmet

## Oppgave 1 – Les en liste

Hva skriver dette programmet ut?

\`\`\`python
priser = [12, 18, 25, 9]

print(priser[0])
print(priser[2])
print(len(priser))
\`\`\`

Forutsi resultatet før du kjører programmet.

## Oppgave 2 – Finn feilen

\`\`\`python
steder = ["Tonstad", "Grimstad", "Oslo"]

print(steder[3])
\`\`\`

Kjør programmet og les feilmeldingen.

Svar på:

- hvilken type feil får du?
- hvor mange elementer finnes?
- hvilke indekser er gyldige?
- hvilken indeks må brukes for å hente Oslo?

Rett programmet.

## Oppgave 3 – Endre listen

Start med:

\`\`\`python
temperaturer = [17, 19, 18]
\`\`\`

Gjør følgende:

1. endre den andre verdien til 20
2. legg til 21 med \`append()\`
3. skriv ut antall elementer med \`len()\`
4. bruk en \`for\`-løkke til å skrive ut alle temperaturene

## Oppgave 4 – Les en ordbok

Hva skriver programmet ut?

\`\`\`python
bok = {
    "tittel": "Python i praksis",
    "sider": 240,
    "språk": "norsk"
}

print(bok["tittel"])
print(bok["sider"])
\`\`\`

Endre deretter sidetallet og legg til nøkkelen \`"år"\`.

## Oppgave 5 – Finn KeyError

Programmet har en feil:

\`\`\`python
avtale = {
    "dag": "fredag",
    "tid": "14:00"
}

print(avtale["klokkeslett"])
\`\`\`

Kjør programmet.

Les \`KeyError\` og sammenlign nøkkelen i feilmeldingen med nøklene som faktisk finnes.

Rett programmet uten å endre ordboken.

## Oppgave 6 – Liste eller ordbok?

Velg hvilken datastruktur som passer best.

A. Temperaturmålinger i rekkefølge.

B. Opplysninger om én bok: tittel, forfatter og sidetall.

C. Navn på fem steder du vil behandle ett etter ett.

D. Opplysninger om én avtale: dato, klokkeslett og sted.

Forklar valget ditt med egne ord.

## Oppgave 7 – Følg strukturen

\`\`\`python
målinger = [
    {"dag": "mandag", "kwh": 10},
    {"dag": "tirsdag", "kwh": 12}
]

første = målinger[0]
print(første["dag"])
print(første["kwh"])
\`\`\`

Forklar hva som skjer i to steg:

1. Hva inneholder \`første\`?
2. Hva gjør \`første["dag"]\`?

## Oppgave 8 – Beregn totalen

Fullfør funksjonen:

\`\`\`python
def beregn_total(målinger):
    total = 0

    for måling in målinger:
        # legg kWh-verdien til total her

    return total
\`\`\`

Test den med:

\`\`\`python
målinger = [
    {"dag": "mandag", "kwh": 10},
    {"dag": "tirsdag", "kwh": 12},
    {"dag": "onsdag", "kwh": 9}
]

print(beregn_total(målinger))
\`\`\`

Forventet resultat:

\`\`\`text
31
\`\`\`

## Mini-prosjekt – Et lite utgiftsregister

Lag et program som holder oversikt over noen utgifter.

Start med:

\`\`\`python
utgifter = [
    {"beskrivelse": "Buss", "beløp": 45},
    {"beskrivelse": "Kaffe", "beløp": 38},
    {"beskrivelse": "Bok", "beløp": 249}
]
\`\`\`

Programmet skal:

1. skrive ut hver beskrivelse og hvert beløp
2. beregne totalbeløpet i en funksjon
3. returnere totalen fra funksjonen
4. skrive ut totalen
5. legge til én ny utgift med \`append()\`
6. beregne og skrive ut den nye totalen

Eksempel på funksjonens form:

\`\`\`python
def beregn_total(utgifter):
    total = 0

    for utgift in utgifter:
        total = total + utgift["beløp"]

    return total
\`\`\`

Prøv først å skrive resten selv.

## Utvid mini-prosjektet

Når grunnversjonen virker, kan du prøve én eller flere endringer:

- endre beløpet til en eksisterende utgift
- skriv ut hvor mange utgifter som finnes
- legg til en ny nøkkel, for eksempel \`"kategori"\`
- bruk \`if\` i løkka for å skrive ut bare utgifter over et valgt beløp

Gjør én endring om gangen og kjør programmet etter hver endring.

## Feilsøkingsrunde

Hvis programmet stopper, se først på navnet til feilen.

\`IndexError\`:

- undersøk listeindeksen
- husk at første indeks er 0
- sammenlign indeksen med \`len(liste)\`

\`KeyError\`:

- undersøk nøkkelen
- sammenlign stavemåten med nøklene i ordboken

Hvis programmet kjører, men resultatet er feil:

- følg én runde i løkka om gangen
- skriv eventuelt ut \`total\` underveis
- kontroller hvilken verdi som hentes fra hver ordbok

## M7 er fullført når du kan

- lage og lese lister
- bruke indekser
- forstå forholdet mellom \`len()\` og indekser
- endre og utvide lister
- lage og lese ordbøker
- bruke nøkkel/verdi-par
- endre og utvide ordbøker
- kjenne igjen \`IndexError\` og \`KeyError\`
- kombinere lister og ordbøker
- bruke samlinger sammen med løkker og funksjoner
- bygge et lite program med strukturerte data

Neste milepæl handler om filer og mapper.
