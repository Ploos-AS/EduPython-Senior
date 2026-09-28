# M8.4 – Legg til tekst med append

I forrige leksjon brukte vi:

\`\`\`python
"w"
\`\`\`

Da blir filen opprettet eller erstattet.

Noen ganger vil vi beholde det som allerede står i filen og legge til noe nytt.

Da kan vi bruke:

\`\`\`python
"a"
\`\`\`

\`"a"\` betyr **append** – legg til på slutten.

## Prøv det

Først lager vi en øvingsfil:

\`\`\`python
with open("logg.txt", "w", encoding="utf-8") as fil:
    fil.write("Programmet startet\n")
\`\`\`

Så åpner vi den med \`"a"\`:

\`\`\`python
with open("logg.txt", "a", encoding="utf-8") as fil:
    fil.write("Første oppgave er ferdig\n")
\`\`\`

Filen inneholder nå:

\`\`\`text
Programmet startet
Første oppgave er ferdig
\`\`\`

Den første linjen ble beholdt.

## Tre moduser

Vi kjenner nå tre filmoduser:

\`\`\`text
"r" → read   → les eksisterende innhold
"w" → write  → skriv, og erstatt gammelt innhold
"a" → append → legg til etter eksisterende innhold
\`\`\`

Det er viktig å velge riktig modus før filen åpnes.

## Legg til flere ganger

\`\`\`python
with open("logg.txt", "a", encoding="utf-8") as fil:
    fil.write("Andre oppgave er ferdig\n")

with open("logg.txt", "a", encoding="utf-8") as fil:
    fil.write("Programmet avsluttes\n")
\`\`\`

Nå inneholder filen flere oppføringer.

Hver bruk av \`"a"\` legger ny tekst på slutten.

## Husk linjeskiftet

Dette:

\`\`\`python
fil.write("Ny oppføring")
\`\`\`

legger ikke automatisk til et linjeskift.

Hvis neste oppføring også mangler \`\n\`, kan resultatet bli:

\`\`\`text
Ny oppføringNeste oppføring
\`\`\`

For én oppføring per linje bruker vi:

\`\`\`python
fil.write("Ny oppføring\n")
\`\`\`

## Append oppretter også filen

Hvis filen ikke finnes, vil \`"a"\` normalt opprette den.

Det betyr at:

\`\`\`python
with open("notater.txt", "a", encoding="utf-8") as fil:
    fil.write("Første notat\n")
\`\`\`

kan brukes selv om \`notater.txt\` ikke eksisterte fra før.

Forskjellen fra \`"w"\` blir viktig når filen allerede finnes:

- \`"w"\` erstatter innholdet
- \`"a"\` beholder innholdet og legger til nytt

## Et lite loggmønster

En logg er en fil der nye hendelser legges til etter hvert.

\`\`\`python
def legg_til_logg(melding):
    with open("logg.txt", "a", encoding="utf-8") as fil:
        fil.write(melding + "\n")
\`\`\`

Vi kan bruke funksjonen flere ganger:

\`\`\`python
legg_til_logg("Start")
legg_til_logg("Kontroll utført")
legg_til_logg("Ferdig")
\`\`\`

Dette kombinerer M6-funksjoner med M8-filer.

## Les loggen tilbake

\`\`\`python
with open("logg.txt", "r", encoding="utf-8") as fil:
    for linje in fil:
        print(linje.strip())
\`\`\`

Nå bruker vi tre tidligere ideer sammen:

- append for å lagre nye oppføringer
- read for å lese
- for for å behandle én linje om gangen

## Når passer "a"?

Append passer når hver ny oppføring skal komme etter de gamle.

Eksempler kan være:

- en enkel logg
- en liste med nye notater
- målinger som registreres etter hverandre
- en enkel historikk

Men append er ikke riktig hvis hele filen skal representere én oppdatert versjon av dataene.

Da kan det være bedre å bygge innholdet på nytt og skrive en ny fil med \`"w"\`.

## Ikke bruk append ukritisk

Hvis du kjører dette programmet tre ganger:

\`\`\`python
with open("logg.txt", "a", encoding="utf-8") as fil:
    fil.write("Programmet kjørte\n")
\`\`\`

får du tre nye linjer.

Det er riktig hvis du ønsker historikk.

Det er feil hvis du forventet at filen bare skulle inneholde én linje.

Spør derfor:

**Skal gammelt innhold beholdes?**

Hvis ja, kan \`"a"\` passe.

## Endre det

Lag først \`notater.txt\` med \`"w"\` og én linje.

Legg deretter til to nye linjer med \`"a"\`.

Les filen tilbake og kontroller at alle tre linjene finnes.

Kjør append-delen én gang til og se hva som skjer.

## Lag det selv

Lag en funksjon:

\`\`\`python
def legg_til_notat(notat):
    # skriv notatet til filen
\`\`\`

Funksjonen skal:

1. åpne en egen øvingsfil med \`"a"\`
2. skrive notatet
3. legge til \`\n\`

Kall funksjonen minst tre ganger.

Les deretter filen linje for linje og skriv ut notatene.

## Dette har du lært

Du kan nå:

- forklare forskjellen mellom \`"r"\`, \`"w"\` og \`"a"\`
- legge til tekst uten å erstatte eksisterende innhold
- forstå at append også kan opprette en fil
- bruke linjeskift mellom oppføringer
- lage en enkel loggfunksjon
- lese en append-fil tilbake
- velge mellom å erstatte og å bevare gammelt innhold

Neste leksjon handler mer systematisk om filfeil og hvordan vi kan forstå dem.
