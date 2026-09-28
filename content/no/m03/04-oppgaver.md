# M3.4 – Oppgaver og feilsøking

Disse oppgavene samler M3. Prøv selv før du leser veiledningen.

## 1. Hva lagres?

Se på:

```python
svar = input("Skriv 25: ")
```

Hvis brukeren skriver `25`, er `svar` tekst eller et tall?

**Veiledning:** Tenk på hva `input()` alltid returnerer.

**Svar:** `svar` inneholder teksten `"25"`.

## 2. Gjør teksten om til et heltall

Fullfør:

```python
antall_tekst = input("Antall: ")
antall = __________

print(antall + 1)
```

**Mulig løsning:**

```python
antall = int(antall_tekst)
```

## 3. Velg int eller float

Hvilken konvertering passer best?

- antall bøker
- temperatur
- antall dager
- pris per kWh
- avstand i kilometer

**Veiledning:** Verdier som kan trenge desimaler passer ofte med `float()`. Hele antall passer ofte med `int()`.

En mulig vurdering er:

- antall bøker → `int()`
- temperatur → `float()`
- antall dager → `int()`
- pris per kWh → `float()`
- avstand → `float()`

## 4. Finn feilen

Programmet skal legge én til brukerens tall:

```python
tall = input("Tall: ")
resultat = tall + 1
print(resultat)
```

Hvorfor virker det ikke?

**Svar:** `tall` er tekst. Konverter først:

```python
tall = int(input("Tall: "))
resultat = tall + 1
print(resultat)
```

## 5. Les ValueError

Programmet er:

```python
pris = float(input("Pris: "))
print(pris)
```

Brukeren skriver:

```text
billig
```

Python stopper med `ValueError`.

Forklar med egne ord hvorfor.

**Svar:** `float()` fikk tekst som ikke representerer et gyldig tall. Python fikk en verdi, men kunne ikke konvertere den slik programmet ba om.

## 6. Regn med to brukerverdier

Lag et program som spør etter:

- antall
- pris per stykk

Beregn total pris og skriv den ut.

**Mulig løsning:**

```python
antall = int(input("Antall: "))
pris = float(input("Pris per stykk: "))

total = antall * pris

print("Total:")
print(total)
```

## 7. Mini-prosjekt

Lag din egen interaktive kalkulator.

Krav:

- minst to `input()`
- tydelige variabelnavn
- riktig bruk av `int()` eller `float()`
- minst én beregning
- resultatet lagres i en variabel
- forklarende tekst skrives ut
- programmet skal kunne kjøres flere ganger med forskjellige gyldige verdier uten at kildekoden endres

Mulige temaer er avstand, tid, pris, strømforbruk, temperatur eller noe annet du selv velger.

## Før du går videre

Du bør nå kunne forklare:

- hvorfor `input()` returnerer tekst
- hvordan tekst konverteres til heltall
- hvordan tekst konverteres til desimaltall
- hvorfor ugyldig talltekst kan gi `ValueError`
- hvordan brukerdata kan inngå i en beregning

Neste milepæl introduserer valg: programmet skal kunne gjøre forskjellige ting avhengig av en betingelse.
