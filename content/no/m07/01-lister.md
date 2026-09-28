# M7.1 – Flere verdier i en liste

Til nå har variablene våre vanligvis hatt én verdi:

\`\`\`python
temperatur = 18
\`\`\`

Men hva hvis vi har flere temperaturmålinger?

Vi kunne lage mange variabler:

\`\`\`python
temperatur1 = 18
temperatur2 = 20
temperatur3 = 17
temperatur4 = 21
\`\`\`

Det virker for fire målinger, men blir fort upraktisk.

Python har **lister** for samlinger av verdier som hører sammen.

## Prøv det

\`\`\`python
temperaturer = [18, 20, 17, 21]

print(temperaturer)
\`\`\`

Resultatet blir:

\`\`\`text
[18, 20, 17, 21]
\`\`\`

Variabelen \`temperaturer\` inneholder nå en **liste** med fire verdier.

## Klammeparentesene lager listen

En liste skrives med \`[\` og \`]\`.

Verdiene skilles med komma:

\`\`\`python
temperaturer = [18, 20, 17, 21]
\`\`\`

Du kan lese dette som:

> temperaturer er en liste som inneholder 18, 20, 17 og 21

## En liste kan inneholde tekst

\`\`\`python
steder = ["Tonstad", "Kristiansand", "Oslo"]

print(steder)
\`\`\`

Resultat:

\`\`\`text
['Tonstad', 'Kristiansand', 'Oslo']
\`\`\`

Anførselstegnene viser at verdiene er tekst.

## En tom liste

En liste kan også starte uten innhold:

\`\`\`python
målinger = []

print(målinger)
\`\`\`

Resultat:

\`\`\`text
[]
\`\`\`

Dette kalles en **tom liste**.

Senere skal vi lære å legge verdier inn i listen.

## Listen har en rekkefølge

I denne listen:

\`\`\`python
dager = ["mandag", "tirsdag", "onsdag"]
\`\`\`

kommer \`mandag\` først, \`tirsdag\` etterpå og \`onsdag\` til slutt.

Rekkefølgen er en del av listen.

I neste leksjon lærer vi hvordan vi henter én bestemt verdi fra denne rekkefølgen.

## Bruk listen med det du allerede kan

Du lærte \`for\` i M5.

En \`for\`-løkke passer svært godt sammen med en liste:

\`\`\`python
temperaturer = [18, 20, 17, 21]

for temperatur in temperaturer:
    print("Temperatur:", temperatur)
\`\`\`

Resultat:

\`\`\`text
Temperatur: 18
Temperatur: 20
Temperatur: 17
Temperatur: 21
\`\`\`

Nå trenger vi ikke én variabel og én \`print()\` for hver måling.

## Følg løkka

Første gang gjennom løkka er:

\`\`\`text
temperatur = 18
\`\`\`

Neste gang:

\`\`\`text
temperatur = 20
\`\`\`

Deretter 17 og 21.

Listen beholder alle verdiene. Løkkevariabelen \`temperatur\` får én av dem om gangen.

## Hvorfor er lister nyttige?

Lister passer når vi har flere relaterte verdier, for eksempel:

- temperaturmålinger
- navn
- priser
- strømforbruk per dag
- filnavn
- avtaler eller oppgaver

Vi trenger ikke vite på forhånd alt vi senere skal gjøre med verdiene. Først lærer vi å samle dem på en ryddig måte.

## Endre det

Start med:

\`\`\`python
temperaturer = [18, 20, 17, 21]
\`\`\`

Endre noen av verdiene.

Legg til en femte verdi mellom klammeparentesene.

Kjør programmet igjen.

## Lag det selv

Lag en liste med minst fire relaterte verdier.

Skriv først ut hele listen.

Bruk deretter en \`for\`-løkke til å skrive ut én verdi om gangen.

## Dette har du lært

Du kan nå:

- forklare hvorfor en liste kan være bedre enn mange separate variabler
- lage en liste med \`[\` og \`]\`
- lage lister med tall eller tekst
- lage en tom liste
- forklare at en liste har en rekkefølge
- skrive ut hele listen
- gå gjennom en liste med \`for\`

Neste leksjon handler om hvordan vi henter én bestemt verdi fra en liste.
