# M5.7 – Oppgaver og feilsøking

Disse oppgavene samler hele M5. Forutsi gjerne resultatet før du kjører kode.

## 1. Hvor mange runder?

```python
for tall in range(4):
    print(tall)
```

Hvor mange ganger kjøres `print()`, og hvilke tall skrives?

**Svar:** Fire ganger: `0`, `1`, `2`, `3`.

Stoppverdien `4` er ikke med.

## 2. Start og stopp

Hva skriver dette?

```python
for tall in range(2, 6):
    print(tall)
```

**Svar:**

```text
2
3
4
5
```

## 3. Finn innrykksfeilen

```python
for tall in range(1, 4):
print(tall)
```

**Svar:** Løkka trenger en innrykket blokk:

```python
for tall in range(1, 4):
    print(tall)
```

## 4. Inne i eller etter løkka?

```python
for tall in range(1, 4):
    print("Runde", tall)

print("Ferdig")
```

Hvor mange ganger skrives `Ferdig`?

**Svar:** Én gang. Linjen er ikke innrykket og ligger derfor etter løkka.

## 5. Beslutning i hver runde

```python
for tall in range(1, 5):
    if tall >= 3:
        print(tall)
```

Hva skrives?

**Svar:** `3` og `4`.

Betingelsen testes på nytt for hver verdi.

## 6. Hvorfor blir totalen feil?

```python
for tall in range(1, 4):
    total = 0
    total = total + tall

print(total)
```

**Svar:** `total` nullstilles i hver runde. Etter siste runde er den derfor bare `3`.

Flytt startverdien før løkka:

```python
total = 0

for tall in range(1, 4):
    total = total + tall

print(total)
```

Nå blir resultatet `6`.

## 7. Tell hendelser

Hva blir `antall`?

```python
antall = 0

for tall in range(1, 8):
    if tall > 4:
        antall = antall + 1

print(antall)
```

**Svar:** `3`, fordi 5, 6 og 7 er større enn 4.

## 8. Spor en while-løkke

```python
tall = 2

while tall <= 6:
    print(tall)
    tall = tall + 2
```

Hva skrives?

**Svar:** `2`, `4`, `6`.

Etterpå blir `tall` 8, og betingelsen blir usann.

## 9. Finn den uendelige løkka

```python
tall = 1

while tall < 5:
    print(tall)
```

Hvorfor stopper den ikke?

**Svar:** Ingenting endrer `tall`. Betingelsen `1 < 5` forblir sann.

En mulig rettelse:

```python
tall = 1

while tall < 5:
    print(tall)
    tall = tall + 1
```

## 10. for eller while?

Velg den enkleste løkketypen.

A. Skriv ut tallene 1 til 10.

B. Fortsett å spørre om input så lenge brukeren skriver `ja`.

**Svar:** En `for`-løkke passer naturlig til A. En `while`-løkke passer naturlig til B.

## 11. Mini-prosjekt

Lag et program som behandler flere målinger.

Krav:

- bruk en `for`- eller `while`-løkke
- bruk minst én verdi som endres gjennom programmet
- bruk en beslutning inne i løkka
- bygg opp en total eller teller
- skriv sluttresultatet etter løkka
- forutsi minst ett testresultat før du kjører programmet

Hvis du bruker `while`, skal du også kunne forklare nøyaktig hvorfor løkka stopper.

## Før du går videre

Du bør nå kunne forklare:

- hva en løkke er
- hvordan `for` går gjennom verdier
- hvordan `range()` bestemmer en tallsekvens
- at stoppverdien i `range()` ikke er med
- hvordan en beslutning kan ligge inne i en løkke
- hvordan et resultat kan bygges opp over flere runder
- forskjellen mellom kode før, inne i og etter en løkke
- hvordan `while` styres av en betingelse
- hvorfor en `while`-løkke kan bli uendelig
- når enkel `for` eller `while` er et naturlig valg

Neste milepæl handler om funksjoner: å gi en gruppe instruksjoner et navn slik at den kan brukes på en ryddig måte.
