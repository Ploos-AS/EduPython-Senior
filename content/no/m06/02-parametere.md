# M6.2 – Gi funksjonen informasjon med parametere

En funksjon blir enda mer nyttig når den kan få informasjon utenfra.

Denne informasjonen kalles en **parameter**.

## Prøv det

\`\`\`python
def si_hei(navn):
    print("Hei,", navn)

si_hei("Anna")
si_hei("Bjørn")
\`\`\`

Den samme funksjonen kan brukes med forskjellige navn.

## Hva er parameteren?

I:

\`\`\`python
def si_hei(navn):
\`\`\`

er \`navn\` parameteren.

Når vi skriver:

\`\`\`python
si_hei("Anna")
\`\`\`

er \`"Anna"\` verdien vi sender inn til funksjonen.

Du kan tenke slik:

**parameter = plass for informasjon**

**argument = informasjonen vi faktisk sender inn**

Vi bruker gjerne «verdi» når vi vil holde forklaringen enkel.

## Flere parametere

En funksjon kan få flere verdier:

\`\`\`python
def vis_person(navn, alder):
    print(navn, "er", alder, "år.")

vis_person("Anna", 72)
vis_person("Bjørn", 68)
\`\`\`

Rekkefølgen betyr noe.

\`navn\` får første verdi, og \`alder\` får andre verdi.

## Følg verdiene

Når vi skriver:

\`\`\`python
vis_person("Anna", 72)
\`\`\`

kan du lese det som:

- \`navn\` blir \`"Anna"\`
- \`alder\` blir \`72\`
- funksjonen kjører med disse verdiene

Neste kall kan bruke helt andre verdier.

## Funksjonen kan gjøre beregninger

\`\`\`python
def vis_dobbelt(tall):
    dobbelt = tall * 2
    print("Dobbelt:", dobbelt)

vis_dobbelt(5)
vis_dobbelt(12)
\`\`\`

Parameteren brukes akkurat som en vanlig variabel inne i funksjonen.

## En vanlig feil

Hvis funksjonen trenger én parameter:

\`\`\`python
def si_hei(navn):
    print("Hei,", navn)
\`\`\`

må vi sende inn en verdi:

\`\`\`python
si_hei("Anna")
\`\`\`

Et kall uten verdi:

\`\`\`python
si_hei()
\`\`\`

gir en feil fordi funksjonen mangler den nødvendige informasjonen.

## Parametere gjør funksjoner gjenbrukbare

Uten parameter kunne vi skrevet:

\`\`\`python
def si_hei_anna():
    print("Hei, Anna")
\`\`\`

Men da er funksjonen bundet til ett navn.

Med parameter:

\`\`\`python
def si_hei(navn):
    print("Hei,", navn)
\`\`\`

kan den brukes med mange navn.

## Endre det

Lag en funksjon med én parameter.

Prøv å sende inn:

- tekst
- et annet tekststykke
- et tall

Pass på at operasjonen inne i funksjonen passer til typen verdi du sender inn.

## Lag det selv

Lag en funksjon som:

- har minst én parameter
- bruker parameteren inne i funksjonen
- kalles minst tre ganger
- får forskjellige verdier i kallene

Lag gjerne en funksjon som beregner eller viser noe praktisk.

## Dette har du lært

Du kan nå:

- definere en funksjon med parameter
- sende en verdi til en funksjon
- bruke parameteren inne i funksjonen
- bruke flere parametere
- forklare hvorfor rekkefølgen på verdiene betyr noe
- lage mer gjenbrukbare funksjoner

Neste leksjon handler om returverdier: når funksjonen skal gi et resultat tilbake til resten av programmet.
