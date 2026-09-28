# M6.1 – Gi en gruppe instruksjoner et navn

Vi har nå laget programmer med variabler, beslutninger og løkker.

Etter hvert som programmer blir større, kan det være nyttig å samle instruksjoner som hører sammen.

En **funksjon** er en navngitt gruppe instruksjoner som kan brukes når vi trenger den.

## Prøv det

\`\`\`python
def vis_velkomst():
    print("Velkommen!")
    print("Dette er EduPython-Senior.")

vis_velkomst()
vis_velkomst()
\`\`\`

Funksjonen er definert med \`def\`, men instruksjonene kjøres først når vi **kaller** \`vis_velkomst()\`.

Det er viktig å skille mellom:

\`\`\`python
def vis_velkomst():
\`\`\`

som definerer funksjonen, og:

\`\`\`python
vis_velkomst()
\`\`\`

som ber Python kjøre den.

## Innrykk

Som med \`if\` og løkker viser innrykket hvilke linjer som hører til funksjonen:

\`\`\`python
def si_hei():
    print("Hei!")
    print("Ha en fin dag.")

print("Programmet starter")
si_hei()
print("Programmet fortsetter")
\`\`\`

De to første \`print()\`-linjene i funksjonen kjøres når funksjonen kalles.

## En vanlig misforståelse

Dette:

\`\`\`python
def vis_melding():
    print("Hei!")
\`\`\`

skriver ikke nødvendigvis \`Hei!\` når programmet starter. Funksjonen er bare definert.

Dette kaller den:

\`\`\`python
vis_melding()
\`\`\`

## Hvorfor er dette nyttig?

Hvis samme arbeid skal gjøres flere steder, skriver vi instruksjonene én gang:

\`\`\`python
def vis_melding():
    print("Husk å lagre arbeidet.")
\`\`\`

Deretter kan vi bruke:

\`\`\`python
vis_melding()
\`\`\`

flere steder i programmet.

Hvis meldingen skal endres, gjør vi det ett sted.

## Endre det

Lag en funksjon som skriver en kort melding du selv velger.

Kall den én gang, og deretter tre ganger.

## Lag det selv

Lag en funksjon som:

- har et tydelig navn
- inneholder minst to instruksjoner
- kalles minst to ganger

Skriv også litt kode utenfor funksjonen slik at forskjellen blir tydelig.

## Dette har du lært

Du kan nå:

- forklare hva en funksjon er
- definere en enkel funksjon med \`def\`
- kalle en funksjon
- forklare forskjellen mellom å definere og å kalle
- bruke innrykk til å vise funksjonsblokken
- bruke samme funksjon flere ganger

Neste leksjon gir funksjonen informasjon gjennom parametere.
