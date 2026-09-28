# M7.6 – Endre en ordbok

Ordbøker kan endres etter at de er laget.

Vi bruker samme grunnform både når vi:

- endrer en verdi som allerede finnes
- legger til en ny nøkkel og verdi

## Prøv det – endre en eksisterende verdi

\`\`\`python
person = {
    "navn": "Anna",
    "alder": 72
}

person["alder"] = 73

print(person)
\`\`\`

Resultatet inneholder nå:

\`\`\`text
'alder': 73
\`\`\`

Nøkkelen \`"alder"\` fantes allerede, så verdien ble erstattet.

## Les tilordningen

Denne linjen:

\`\`\`python
person["alder"] = 73
\`\`\`

kan leses som:

> sett verdien for nøkkelen "alder" i person til 73

Dette ligner på hvordan vi endret en liste:

\`\`\`python
temperaturer[1] = 21
\`\`\`

Forskjellen er hva som står mellom klammeparentesene:

- liste: indeks
- ordbok: nøkkel

## Legg til en ny nøkkel

Hvis nøkkelen ikke finnes, opprettes den:

\`\`\`python
person = {
    "navn": "Anna",
    "alder": 72
}

person["sted"] = "Grimstad"

print(person)
\`\`\`

Nå inneholder ordboken også:

\`\`\`text
'sted': 'Grimstad'
\`\`\`

Vi brukte nøyaktig samme syntaks:

\`\`\`python
ordbok[nøkkel] = verdi
\`\`\`

## Eksisterende eller ny nøkkel?

Se på:

\`\`\`python
person["alder"] = 73
person["sted"] = "Grimstad"
\`\`\`

Hvis nøkkelen finnes:

**verdien oppdateres**

Hvis nøkkelen ikke finnes:

**et nytt nøkkel/verdi-par legges til**

## Bygg opp en tom ordbok

Vi kan starte med:

\`\`\`python
bok = {}
\`\`\`

og legge til opplysninger etter hvert:

\`\`\`python
bok["tittel"] = "Python for alle"
bok["sider"] = 200
bok["språk"] = "norsk"

print(bok)
\`\`\`

Dette er nyttig når opplysningene blir tilgjengelige på forskjellige tidspunkt i programmet.

## Bruk en variabel som verdi

Verdien trenger ikke stå direkte i tilordningen:

\`\`\`python
person = {
    "navn": "Anna"
}

ny_alder = 73
person["alder"] = ny_alder

print(person["alder"])
\`\`\`

Resultat:

\`\`\`text
73
\`\`\`

## Bruk en funksjon

En funksjon kan lese fra en ordbok:

\`\`\`python
def vis_person(person):
    print("Navn:", person["navn"])
    print("Sted:", person["sted"])


person = {
    "navn": "Anna",
    "sted": "Grimstad"
}

vis_person(person)
\`\`\`

Her sendes hele ordboken inn som argument.

Parameteren \`person\` viser til ordboken mens funksjonen kjører.

## En funksjon kan returnere en verdi fra ordboken

\`\`\`python
def hent_navn(person):
    return person["navn"]


person = {
    "navn": "Anna",
    "alder": 72
}

navn = hent_navn(person)
print(navn)
\`\`\`

Resultat:

\`\`\`text
Anna
\`\`\`

Dette kobler ordbøker til det du lærte om funksjoner i M6.

## Vær nøye med nøkkelnavn

Disse er forskjellige:

\`\`\`python
person["navn"]
person["Navn"]
\`\`\`

Hvis bare \`"navn"\` finnes, vil \`"Navn"\` gi \`KeyError\`.

Når du oppdaterer en ordbok, er det derfor viktig å skrive nøkkelen nøyaktig slik du mener.

## Endre det

Start med:

\`\`\`python
bok = {
    "tittel": "Python for alle",
    "sider": 200
}
\`\`\`

Gjør følgende:

1. endre \`"sider"\` til en annen verdi
2. legg til nøkkelen \`"språk"\`
3. skriv ut hver av de tre verdiene
4. skriv ut hele ordboken

## Lag det selv

Start med en tom ordbok.

Legg inn minst tre nøkkel/verdi-par.

Endre deretter verdien til én nøkkel som allerede finnes.

Lag en liten funksjon som tar imot ordboken og skriver ut eller returnerer minst én av verdiene.

## Dette har du lært

Du kan nå:

- endre verdien til en eksisterende nøkkel
- legge til en ny nøkkel og verdi
- forklare at begge bruker \`ordbok[nøkkel] = verdi\`
- bygge opp en tom ordbok
- bruke variabler som nye verdier
- sende en ordbok til en funksjon
- lese og returnere ordbokverdier fra en funksjon
- være oppmerksom på nøyaktige nøkkelnavn

Neste leksjon kombinerer lister og ordbøker i et praktisk eksempel.
