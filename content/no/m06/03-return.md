# M6.3 – Få et resultat tilbake med return

En funksjon kan skrive ut noe med \`print()\`. Men ofte vil vi at funksjonen skal **gi et resultat tilbake** slik at resten av programmet kan bruke det.

Da bruker vi \`return\`.

## Først med print

\`\`\`python
def vis_dobbelt(tall):
    print(tall * 2)

vis_dobbelt(5)
\`\`\`

Dette viser resultatet på skjermen.

Men hva hvis vi vil lagre resultatet?

## Bruk return

\`\`\`python
def beregn_dobbelt(tall):
    return tall * 2

resultat = beregn_dobbelt(5)

print("Resultat:", resultat)
\`\`\`

Funksjonen regner ut \`10\` og **returnerer** verdien til stedet der funksjonen ble kalt.

## print og return er ikke det samme

Dette:

\`\`\`python
def med_print(tall):
    print(tall * 2)
\`\`\`

viser et resultat.

Dette:

\`\`\`python
def med_return(tall):
    return tall * 2
\`\`\`

gir resultatet tilbake.

En funksjon med \`return\` trenger ikke skrive noe på skjermen.

## Bruk resultatet videre

Når en funksjon returnerer en verdi, kan vi bruke den som en vanlig verdi:

\`\`\`python
def beregn_dobbelt(tall):
    return tall * 2

resultat = beregn_dobbelt(5)
ny_verdi = resultat + 3

print(ny_verdi)
\`\`\`

Her blir resultatet 10, og deretter 13.

## return avslutter funksjonen

Når Python møter \`return\`, forlater den funksjonen med én gang.

\`\`\`python
def test():
    print("Før")
    return 10
    print("Etter")
\`\`\`

\`Etter\` blir aldri skrevet.

Dette er nyttig når funksjonen har funnet resultatet den skal gi tilbake.

## Flere return-punkter kommer senere

Det er mulig å ha flere \`return\`-linjer i en funksjon, ofte sammen med \`if\`.

Vi venter med slike eksempler til beslutninger inne i funksjoner er godt etablert.

## Praktisk eksempel

\`\`\`python
def beregn_total(pris, antall):
    return pris * antall

total = beregn_total(25, 4)

print("Total:", total, "kr")
\`\`\`

Funksjonen kjenner ikke resten av programmet. Den gjør én bestemt beregning og gir resultatet tilbake.

Dette gjør den enkel å teste og gjenbruke.

## Funksjon med tekst

\`\`\`python
def lag_hilsen(navn):
    return "Hei, " + navn + "!"

melding = lag_hilsen("Anna")
print(melding)
\`\`\`

\`return\` kan gi tilbake tekst, ikke bare tall.

## Endre det

Lag en funksjon som tar inn en verdi og returnerer et beregnet resultat.

Lagre resultatet i en variabel.

Bruk deretter variabelen i en ny beregning eller skriv den ut.

## Lag det selv

Lag en funksjon som:

- har minst én parameter
- bruker parameteren i en beregning
- bruker \`return\`
- kalles minst to ganger
- lagrer minst ett av resultatene i en variabel

## Dette har du lært

Du kan nå:

- forklare hva \`return\` gjør
- skille mellom \`print()\` og \`return\`
- lagre en returnert verdi
- bruke resultatet videre i programmet
- forklare at \`return\` avslutter funksjonen
- lage funksjoner som beregner og returnerer både tall og tekst

Neste leksjon kombinerer funksjoner med \`if\` og \`for\`.
