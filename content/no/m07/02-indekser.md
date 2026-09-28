# M7.2 – Hent én verdi fra en liste

En liste kan inneholde mange verdier. Noen ganger vil vi hente bare én av dem.

Da bruker vi verdien sin **indeks**.

## Prøv det

\`\`\`python
dager = ["mandag", "tirsdag", "onsdag"]

print(dager[0])
\`\`\`

Resultat:

\`\`\`text
mandag
\`\`\`

\`[0]\` betyr: hent den første verdien i listen.

## Python starter på 0

Dette er viktig:

| Plass | Indeks | Verdi |
|---|---:|---|
| første | 0 | mandag |
| andre | 1 | tirsdag |
| tredje | 2 | onsdag |

Derfor:

\`\`\`python
print(dager[0])
print(dager[1])
print(dager[2])
\`\`\`

gir:

\`\`\`text
mandag
tirsdag
onsdag
\`\`\`

## Hvorfor starter det på 0?

I Python, som i mange programmeringsspråk, brukes indeksen som en posisjon regnet fra starten av samlingen.

Den første verdien ligger **0 steg fra starten**.

Den neste ligger 1 steg fra starten.

Du trenger ikke bruke tid på å like dette. Det viktige er å huske:

> Første verdi har indeks 0.

## Se listen som to rader

\`\`\`text
indeks:   0          1          2
verdi:   mandag     tirsdag    onsdag
\`\`\`

Når du skriver:

\`\`\`python
dager[1]
\`\`\`

ser Python på indeks 1 og finner \`"tirsdag"\`.

## Indeks er ikke det samme som antall

Listen har tre verdier:

\`\`\`python
dager = ["mandag", "tirsdag", "onsdag"]
\`\`\`

Men siste indeks er 2.

Det er fordi indeksene er:

\`\`\`text
0, 1, 2
\`\`\`

Dette er en vanlig kilde til feil når man lærer programmering.

## Hva skjer med en indeks som ikke finnes?

Prøv:

\`\`\`python
dager = ["mandag", "tirsdag", "onsdag"]

print(dager[3])
\`\`\`

Python gir en feil som blant annet inneholder:

\`\`\`text
IndexError: list index out of range
\`\`\`

Dette betyr at programmet forsøkte å hente en plass som ikke finnes i listen.

Listen har tre verdier, men de gyldige indeksene er 0, 1 og 2.

## Les feilmeldingen

Når du ser:

\`\`\`text
IndexError
\`\`\`

spør:

1. Hvilken liste bruker jeg?
2. Hvilken indeks prøver jeg å hente?
3. Hvor mange verdier finnes i listen?
4. Starter jeg tellingen på 0?

Feilmeldingen er informasjon som hjelper oss å finne problemet.

## Bruk en variabel som indeks

Indeksen trenger ikke stå direkte i klammeparentesene:

\`\`\`python
dager = ["mandag", "tirsdag", "onsdag"]
indeks = 1

print(dager[indeks])
\`\`\`

Resultatet er:

\`\`\`text
tirsdag
\`\`\`

Python bruker verdien i \`indeks\`, som er 1.

## Endre det

Start med:

\`\`\`python
steder = ["Tonstad", "Grimstad", "Oslo", "Bergen"]
\`\`\`

Skriv ut:

- første verdi
- andre verdi
- fjerde verdi

Forutsi indeksene før du kjører programmet.

## Lag det selv

Lag en liste med minst fem verdier.

Skriv ut:

- første verdi
- en verdi fra midten
- siste verdi ved å bruke den konkrete indeksen

Prøv deretter med vilje en indeks som er for stor. Les \`IndexError\`, rett indeksen og kjør programmet igjen.

## Dette har du lært

Du kan nå:

- hente ett element fra en liste med en indeks
- forklare at første indeks er 0
- skille mellom antall elementer og siste indeks
- bruke en variabel som indeks
- kjenne igjen og undersøke \`IndexError: list index out of range\`

Neste leksjon handler om å endre en liste og legge til nye verdier.
