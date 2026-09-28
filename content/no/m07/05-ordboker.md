# M7.5 – Finn verdier med navn: ordbøker

En liste passer godt når vi har flere verdier i en rekkefølge.

Men noen ganger beskriver verdiene forskjellige ting.

Se på denne listen:

\`\`\`python
person = ["Anna", 72, "Grimstad"]
\`\`\`

Hva betyr indeks 0, 1 og 2?

Vi kan lære oss at:

- 0 er navn
- 1 er alder
- 2 er sted

Men Python har en samlingstype der vi kan bruke **navn** i stedet.

Den heter en **dictionary**. På norsk kan vi kalle den en **ordbok**.

## Prøv det

\`\`\`python
person = {
    "navn": "Anna",
    "alder": 72,
    "sted": "Grimstad"
}

print(person)
\`\`\`

Ordboken inneholder tre opplysninger om personen.

## Nøkkel og verdi

Se på:

\`\`\`python
"navn": "Anna"
\`\`\`

Her er:

\`\`\`text
"navn"  → nøkkel
"Anna"  → verdi
\`\`\`

Et slikt par kalles et **nøkkel/verdi-par**.

Ordboken:

\`\`\`python
person = {
    "navn": "Anna",
    "alder": 72,
    "sted": "Grimstad"
}
\`\`\`

kan leses som:

\`\`\`text
navn  → Anna
alder → 72
sted  → Grimstad
\`\`\`

## Hent en verdi med nøkkelen

For å hente navnet:

\`\`\`python
print(person["navn"])
\`\`\`

Resultat:

\`\`\`text
Anna
\`\`\`

For å hente alderen:

\`\`\`python
print(person["alder"])
\`\`\`

Resultat:

\`\`\`text
72
\`\`\`

Vi bruker fortsatt klammeparenteser, men nå står det en **nøkkel** inni dem, ikke en nummerert indeks.

## Liste og ordbok løser forskjellige problemer

Liste:

\`\`\`python
temperaturer = [18, 20, 17]
\`\`\`

Her er rekkefølgen viktig, og vi kan bruke indekser:

\`\`\`python
temperaturer[0]
\`\`\`

Ordbok:

\`\`\`python
person = {
    "navn": "Anna",
    "alder": 72
}
\`\`\`

Her finner vi verdier med beskrivende nøkler:

\`\`\`python
person["navn"]
\`\`\`

Det er ikke et spørsmål om at én type alltid er bedre. De beskriver forskjellige slags data.

## Krøllparenteser

Lister bruker:

\`\`\`text
[ ]
\`\`\`

Ordbøker bruker:

\`\`\`text
{ }
\`\`\`

Eksempel:

\`\`\`python
bok = {
    "tittel": "Python",
    "sider": 250
}
\`\`\`

Kolonet \`:\` skiller nøkkelen fra verdien.

Komma skiller nøkkel/verdi-parene.

## Hva skjer hvis nøkkelen ikke finnes?

\`\`\`python
person = {
    "navn": "Anna",
    "alder": 72
}

print(person["telefon"])
\`\`\`

Python gir en feil som blant annet inneholder:

\`\`\`text
KeyError: 'telefon'
\`\`\`

Det betyr at programmet prøvde å hente en nøkkel som ikke finnes i ordboken.

## Les KeyError

Når du ser \`KeyError\`, spør:

1. Hvilken ordbok bruker jeg?
2. Hvilken nøkkel prøver jeg å hente?
3. Finnes nøkkelen i ordboken?
4. Er nøkkelen skrevet nøyaktig likt?

For eksempel er:

\`\`\`text
"navn"
\`\`\`

og:

\`\`\`text
"Navn"
\`\`\`

to forskjellige tekstverdier.

## En tom ordbok

Vi kan også lage en tom ordbok:

\`\`\`python
opplysninger = {}

print(opplysninger)
\`\`\`

Resultat:

\`\`\`text
{}
\`\`\`

I neste leksjon skal vi lære å legge inn og endre nøkkel/verdi-par.

## Endre det

Start med:

\`\`\`python
bok = {
    "tittel": "Python for alle",
    "sider": 200,
    "språk": "norsk"
}
\`\`\`

Skriv ut:

- hele ordboken
- tittelen
- antall sider
- språket

Prøv deretter med vilje en nøkkel som ikke finnes. Les \`KeyError\`, rett nøkkelen og kjør igjen.

## Lag det selv

Lag en ordbok som beskriver én ting, for eksempel en bok, en avtale, en by eller en måling.

Bruk minst tre nøkkel/verdi-par.

Skriv ut hele ordboken og deretter hver verdi ved hjelp av nøkkelen.

## Dette har du lært

Du kan nå:

- forklare forskjellen mellom en listeindeks og en ordboknøkkel
- lage en ordbok med \`{\` og \`}\`
- kjenne igjen et nøkkel/verdi-par
- hente en verdi ved hjelp av en nøkkel
- forklare hvorfor beskrivende nøkler kan gjøre data lettere å forstå
- kjenne igjen og undersøke \`KeyError\`
- lage en tom ordbok

Neste leksjon handler om å endre eksisterende verdier og legge til nye nøkler.
