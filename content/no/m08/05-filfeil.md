# M8.5 – Filfeil og feilsøking

Når vi arbeider med filer, kan programmet be om en fil som ikke finnes der vi forventer.

Python forteller oss dette med en feilmelding.

Målet er ikke å unngå alle feil. Målet er å kunne lese dem og finne årsaken.

## FileNotFoundError

Dette programmet prøver å lese en fil:

```python
with open("målinger.txt", "r", encoding="utf-8") as fil:
    innhold = fil.read()
```

Hvis Python ikke finner filen, kan feilmeldingen inneholde:

```text
FileNotFoundError
```

Navnet sier mye:

```text
File     Not Found     Error
fil      ikke funnet   feil
```

Programmet ba om en fil som Python ikke fant på den oppgitte stien.

## Kontroller det enkle først

Når du ser \`FileNotFoundError\`, kontroller:

1. Er filnavnet riktig?
2. Er filendelsen riktig, for eksempel \`.txt\`?
3. Er store og små bokstaver riktige?
4. Finnes filen faktisk?
5. Kjører programmet fra mappen du forventer?

En liten skrivefeil er nok:

```python
open("temperatur.txt", "r", encoding="utf-8")
```

hvis filen egentlig heter:

```text
temperaturer.txt
```

## Stien er en del av feilen

Python leter ikke etter filen «overalt».

Filnavnet eller stien forteller hvor programmet forventer å finne den.

Et enkelt navn:

```text
temperaturer.txt
```

er en relativ sti.

Den tolkes i forhold til programmets **nåværende arbeidsmappe**.

Det er derfor samme kode kan finne filen i én situasjon og ikke i en annen hvis arbeidsmappen har endret seg.

Vi lærer mer om mapper og stier i neste leksjon.

## Les hele feilmeldingen

Ikke stopp ved ordet \`Error\`.

Se etter:

- typen feil
- filnavnet Python prøvde å åpne
- linjen i programmet der feilen skjedde

Feilmeldingen er informasjon til deg.

## Når feilen er forventet

Noen programmer må kunne håndtere at en fil mangler.

Da kan vi bruke \`try\` og \`except\`.

```python
try:
    with open("notater.txt", "r", encoding="utf-8") as fil:
        innhold = fil.read()

    print(innhold)
except FileNotFoundError:
    print("Fant ikke notater.txt")
```

Python prøver først koden under \`try\`.

Hvis akkurat en \`FileNotFoundError\` oppstår, kjører koden under:

```python
except FileNotFoundError:
```

## Hvorfor skriver vi feiltypen?

Vi bruker:

```python
except FileNotFoundError:
```

ikke bare en generell regel som skjuler alle feil.

Hvis programmet har en annen feil, vil vi fortsatt se den og kunne rette den.

Det er nyttig når vi lærer og nyttig i virkelige programmer.

## Ikke bruk except for å skjule en skrivefeil

Hvis filen skal finnes, men du skrev feil navn, er den beste løsningen vanligvis å rette filnavnet.

\`try/except\` er nyttig når en manglende fil er en situasjon programmet faktisk forventer.

Spør:

**Er det normalt at denne filen kan mangle?**

Hvis nei, undersøk hvorfor den mangler.

## En funksjon som leser en fil

Vi kan kombinere dette med funksjoner:

```python
def les_notater():
    try:
        with open("notater.txt", "r", encoding="utf-8") as fil:
            return fil.read()
    except FileNotFoundError:
        return "Ingen notatfil funnet."
```

Funksjonen returnerer enten filinnholdet eller en tydelig melding.

## Andre filfeil finnes også

Filer kan gi andre feil, for eksempel hvis programmet ikke har tillatelse til å lese eller skrive et sted.

Vi trenger ikke lære alle feiltypene nå.

Det viktige er:

- les hvilken feil Python faktisk viser
- ikke anta at alle filproblemer er \`FileNotFoundError\`
- ikke skjul ukjente feil med en altfor bred \`except\`

## Endre det

Lag en kopi av et leseprogram.

1. Bruk først riktig filnavn.
2. Endre én bokstav i filnavnet.
3. Kjør programmet og les \`FileNotFoundError\`.
4. Rett filnavnet.
5. Legg deretter inn en \`try/except FileNotFoundError\` og prøv et manglende filnavn igjen.

Sammenlign forskjellen mellom en ubehandlet feil og en forventet feil som programmet håndterer.

## Lag det selv

Lag en funksjon som prøver å lese en egen øvingsfil.

Hvis filen finnes, skal funksjonen returnere innholdet.

Hvis filen mangler, skal den returnere en kort og forståelig melding.

Bruk bare:

```python
except FileNotFoundError:
```

ikke en generell \`except\`.

## Dette har du lært

Du kan nå:

- kjenne igjen \`FileNotFoundError\`
- kontrollere filnavn, filendelse og plassering
- forstå at relative stier avhenger av arbeidsmappen
- bruke feilmeldingen som informasjon
- skille mellom en feil som bør rettes og en forventet situasjon
- bruke \`try/except FileNotFoundError\`
- forstå hvorfor vi ikke skjuler alle feil med en generell \`except\`

Neste leksjon handler om mapper og relative stier.
