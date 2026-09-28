# M6.7 – Oppgaver og feilsøking

Disse oppgavene samler hele M6. Prøv å forutsi resultatet før du kjører koden.

## 1. Definisjon eller kall?

Hva gjør denne koden?

\`\`\`python
def si_hei():
    print("Hei!")
\`\`\`

**Svar:** Den definerer funksjonen. Den kaller den ikke.

For å kjøre funksjonen:

\`\`\`python
si_hei()
\`\`\`

## 2. Hvor mange ganger?

\`\`\`python
def vis_melding():
    print("Python")

vis_melding()
vis_melding()
vis_melding()
\`\`\`

Hvor mange ganger skrives \`Python\`?

**Svar:** Tre ganger.

## 3. Finn innrykksfeilen

\`\`\`python
def vis_navn():
print("Anna")
\`\`\`

**Svar:** Funksjonsblokken må rykkes inn:

\`\`\`python
def vis_navn():
    print("Anna")
\`\`\`

## 4. Følg parameteren

\`\`\`python
def vis_dobbelt(tall):
    print(tall * 2)

vis_dobbelt(7)
\`\`\`

Hva er verdien til \`tall\` inne i funksjonen?

**Svar:** \`7\`.

Hva skrives?

**Svar:** \`14\`.

## 5. Flere parametere

\`\`\`python
def beregn(pris, antall):
    return pris * antall

resultat = beregn(20, 3)
print(resultat)
\`\`\`

Hva blir resultatet?

**Svar:** \`60\`.

## 6. print eller return?

Se på:

\`\`\`python
def beregn(pris, antall):
    print(pris * antall)
\`\`\`

Funksjonen viser resultatet, men gir det ikke tilbake med \`return\`.

Hvis resten av programmet skal bruke resultatet, kan vi skrive:

\`\`\`python
def beregn(pris, antall):
    return pris * antall
\`\`\`

Forklar med egne ord forskjellen mellom å **vise** en verdi og å **returnere** en verdi.

## 7. Hva skjer etter return?

\`\`\`python
def test():
    print("A")
    return 5
    print("B")

resultat = test()
print(resultat)
\`\`\`

Hva skrives?

**Svar:**

\`\`\`text
A
5
\`\`\`

\`print("B")\` kjøres ikke fordi \`return\` avslutter funksjonen.

## 8. Finn den logiske feilen

Funksjonen skal beregne pris ganger antall:

\`\`\`python
def beregn_total(pris, antall):
    return pris + antall
\`\`\`

Koden er gyldig Python, men beregningen er feil.

**Rettelse:**

\`\`\`python
def beregn_total(pris, antall):
    return pris * antall
\`\`\`

## 9. Beslutning i en funksjon

\`\`\`python
def kategori(tall):
    if tall < 0:
        return "negativt"
    else:
        return "null eller positivt"

print(kategori(-2))
print(kategori(0))
\`\`\`

Hva skrives?

**Svar:**

\`\`\`text
negativt
null eller positivt
\`\`\`

## 10. Funksjon og løkke

\`\`\`python
def kvadrat(tall):
    return tall * tall

for tall in range(1, 4):
    print(kvadrat(tall))
\`\`\`

Hva skrives?

**Svar:**

\`\`\`text
1
4
9
\`\`\`

## 11. Test grenseverdier

Du har funksjonen:

\`\`\`python
def beregn_total(pris, antall):
    return pris * antall
\`\`\`

Lag minst tre tester.

Ta med:

- en vanlig verdi
- \`antall = 1\`
- \`antall = 0\`

Skriv forventet resultat før du kjører koden.

## 12. Mini-prosjekt

Lag et lite program med minst to funksjoner.

Krav:

- minst én funksjon har parameter
- minst én funksjon returnerer en verdi
- bruk en beslutning eller løkke i eller sammen med en funksjon
- bruk et returnert resultat videre i programmet
- test minst én funksjon separat med flere verdier
- gi funksjonene navn som beskriver oppgaven deres

Mulige temaer er kostnader, strømforbruk, avstander, tidsbruk eller andre enkle beregninger.

## Før du går videre

Du bør nå kunne forklare:

- hvorfor funksjoner er nyttige
- forskjellen mellom å definere og kalle en funksjon
- hva en parameter gjør
- hvordan verdier sendes inn i en funksjon
- forskjellen mellom \`print()\` og \`return\`
- hvordan et returnert resultat brukes videre
- at \`return\` avslutter funksjonen
- hvordan \`if\` og løkker kan brukes sammen med funksjoner
- hvorfor små funksjoner kan være lettere å teste
- hvordan en logisk feil kan finnes med kjente testverdier

Neste milepæl handler om lister og ordbøker: å arbeide med samlinger av data.
