# M6.5 – Et lite program med flere funksjoner

Funksjoner er mest nyttige når de gjør et program lettere å forstå.

Nå lager vi et lite program som beregner kostnaden for en tur.

Vi deler arbeidet i små funksjoner.

## Prøv det

\`\`\`python
def beregn_kostnad(kilometer, pris_per_km):
    return kilometer * pris_per_km


def vis_resultat(kilometer, kostnad):
    print("Kjørelengde:", kilometer, "km")
    print("Kostnad:", kostnad, "kr")


kilometer = 120
pris_per_km = 1.50

kostnad = beregn_kostnad(kilometer, pris_per_km)
vis_resultat(kilometer, kostnad)
\`\`\`

Programmet har to tydelige oppgaver:

- \`beregn_kostnad()\` gjør beregningen
- \`vis_resultat()\` viser resultatet

## Følg dataene

Start:

\`\`\`text
kilometer = 120
pris_per_km = 1.50
\`\`\`

Deretter:

\`\`\`python
kostnad = beregn_kostnad(kilometer, pris_per_km)
\`\`\`

Funksjonen regner:

\`\`\`text
120 × 1.50 = 180
\`\`\`

og returnerer 180.

Variabelen \`kostnad\` får derfor verdien 180.

Til slutt sender vi verdiene til:

\`\`\`python
vis_resultat(kilometer, kostnad)
\`\`\`

## Hvorfor dele programmet opp?

Vi kunne skrevet alt i én lang blokk.

Men med funksjoner kan vi gi delene navn:

**beregn** og **vis**.

Det gjør det lettere å lese programmet.

Hvis beregningen må endres, vet vi hvor vi skal lete.

## En funksjon bør ha en tydelig oppgave

Sammenlign:

\`\`\`python
def beregn_kostnad(kilometer, pris_per_km):
    return kilometer * pris_per_km
\`\`\`

med en funksjon som både:

- spør brukeren om mange ting
- gjør flere forskjellige beregninger
- skriver mange meldinger
- lagrer data
- og avslutter programmet

Den første er enklere å forstå fordi oppgaven er tydelig.

## Funksjoner kan brukes flere ganger

\`\`\`python
kostnad1 = beregn_kostnad(50, 1.50)
kostnad2 = beregn_kostnad(200, 1.50)

print(kostnad1)
print(kostnad2)
\`\`\`

Samme beregning kan brukes med forskjellige verdier.

## Funksjoner kan bruke andre funksjoner

Dette kommer vi tilbake til senere, men du kan allerede se mønsteret:

\`\`\`python
kostnad = beregn_kostnad(kilometer, pris_per_km)
vis_resultat(kilometer, kostnad)
\`\`\`

Den ene funksjonen lager et resultat som den andre funksjonen bruker.

## Endre det

Endre:

\`\`\`python
kilometer = 120
\`\`\`

til en annen avstand.

Endre også \`pris_per_km\`.

Forutsi kostnaden før du kjører programmet.

## Lag det selv

Lag et lite program med minst to funksjoner.

Den ene funksjonen skal:

- ta imot verdier
- beregne noe
- returnere resultatet

Den andre skal:

- ta imot et resultat
- vise det på en ryddig måte

Bruk begge funksjonene fra hoveddelen av programmet.

## Dette har du lært

Du kan nå:

- dele et program opp i funksjoner
- gi hver funksjon en tydelig oppgave
- sende data fra én del av programmet til en funksjon
- returnere data fra en funksjon
- sende et returnert resultat videre
- gjenbruke funksjoner med forskjellige verdier

Neste leksjon handler om hvordan funksjoner kan gjøre kode lettere å teste og feilsøke.
