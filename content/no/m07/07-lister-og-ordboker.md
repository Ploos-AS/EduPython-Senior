# M7.7 – Kombiner lister og ordbøker

Vi har lært at:

- en liste samler flere verdier i en rekkefølge
- en ordbok samler navngitte opplysninger om én ting

Nå kombinerer vi dem.

## Problemet

Tenk at vi vil lagre flere strømmålinger.

Én måling kan beskrives slik:

\`\`\`python
måling = {
    "dag": "mandag",
    "kwh": 12.4
}
\`\`\`

Men vi har flere dager.

Da kan vi lage en **liste med ordbøker**.

## Prøv det

\`\`\`python
målinger = [
    {"dag": "mandag", "kwh": 12.4},
    {"dag": "tirsdag", "kwh": 10.8},
    {"dag": "onsdag", "kwh": 13.1}
]

print(målinger)
\`\`\`

Den ytre strukturen er en liste:

\`\`\`text
[ ... ]
\`\`\`

Hvert element i listen er en ordbok:

\`\`\`text
{ ... }
\`\`\`

## Se strukturen lag for lag

\`\`\`text
liste
│
├── ordbok: dag → mandag,  kwh → 12.4
├── ordbok: dag → tirsdag, kwh → 10.8
└── ordbok: dag → onsdag,  kwh → 13.1
\`\`\`

Vi trenger ikke forstå alt på én gang.

Først henter vi ett element fra listen.

## Hent én ordbok fra listen

\`\`\`python
første = målinger[0]

print(første)
\`\`\`

Resultatet er den første ordboken:

\`\`\`text
{'dag': 'mandag', 'kwh': 12.4}
\`\`\`

Nå kan vi hente en verdi fra den:

\`\`\`python
print(første["dag"])
print(første["kwh"])
\`\`\`

## To steg

Dette:

\`\`\`python
første = målinger[0]
print(første["dag"])
\`\`\`

gjør to ting:

1. hent element 0 fra listen
2. hent verdien med nøkkelen \`"dag"\` fra ordboken

Vi kan senere skrive dette kortere, men to steg gjør datastrukturen lettere å følge.

## Gå gjennom alle oppføringene

Vi kjenner allerede \`for\`:

\`\`\`python
for måling in målinger:
    print(måling)
\`\`\`

For hver runde viser \`måling\` til én ordbok.

Derfor kan vi skrive:

\`\`\`python
for måling in målinger:
    print(måling["dag"], måling["kwh"])
\`\`\`

Resultat:

\`\`\`text
mandag 12.4
tirsdag 10.8
onsdag 13.1
\`\`\`

## Følg løkka

Første runde:

\`\`\`python
måling = {"dag": "mandag", "kwh": 12.4}
\`\`\`

Andre runde:

\`\`\`python
måling = {"dag": "tirsdag", "kwh": 10.8}
\`\`\`

Tredje runde:

\`\`\`python
måling = {"dag": "onsdag", "kwh": 13.1}
\`\`\`

Det er den samme \`for\`-ideen som før. Det nye er bare at hver verdi i listen nå er en ordbok.

## Regn med verdiene

Vi kan summere målingene:

\`\`\`python
total = 0

for måling in målinger:
    total = total + måling["kwh"]

print("Totalt:", total)
\`\`\`

Her kombinerer vi:

- liste
- ordbok
- \`for\`
- variabel
- beregning

Alle delene er kjent hver for seg.

## Bruk en funksjon

Vi kan flytte beregningen inn i en funksjon:

\`\`\`python
def beregn_total(målinger):
    total = 0

    for måling in målinger:
        total = total + måling["kwh"]

    return total
\`\`\`

Og bruke den slik:

\`\`\`python
total = beregn_total(målinger)
print("Totalt:", total)
\`\`\`

Funksjonen tar imot hele listen.

Løkka går gjennom ordbøkene én etter én.

## Legg til en ny oppføring

Vi kjenner allerede \`append()\`:

\`\`\`python
ny_måling = {
    "dag": "torsdag",
    "kwh": 11.7
}

målinger.append(ny_måling)
\`\`\`

Nå har listen fire ordbøker.

Vi bruker altså de samme operasjonene som tidligere. Verdiene er bare blitt mer strukturerte.

## Endre det

Start med tre målinger.

1. Endre én \`kwh\`-verdi.
2. Legg til en fjerde måling med \`append()\`.
3. Bruk en \`for\`-løkke til å skrive ut dag og kWh.
4. Beregn totalen.

Følg gjerne innholdet i listen etter hver endring.

## Lag det selv

Lag en liste med minst tre ordbøker som beskriver samme type ting.

Det kan for eksempel være:

- bøker med tittel og sidetall
- avtaler med dag og klokkeslett
- steder med navn og temperatur
- utgifter med beskrivelse og beløp

Lag en funksjon som tar imot listen og bruker minst én verdi fra hver ordbok.

## Dette har du lært

Du kan nå:

- forklare hva en liste med ordbøker er
- lese en sammensatt datastruktur lag for lag
- hente én ordbok fra en liste
- hente en verdi fra ordboken
- gå gjennom flere ordbøker med \`for\`
- beregne med verdier fra ordbøkene
- sende en liste med ordbøker til en funksjon
- legge til en ny strukturert oppføring med \`append()\`

Dette mønsteret blir viktig senere når vi arbeider med tabeller og CSV-filer.

Neste leksjon samler M7 med oppgaver og feilsøking.
