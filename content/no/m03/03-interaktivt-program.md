# M3.3 – Et komplett interaktivt program

Nå setter vi sammen det du har lært om variabler, `input()`, `float()` og beregninger.

Vi lager en enkel kalkulator for energikostnad.

## Prøv det

```python
forbruk_tekst = input("Forbruk i kWh: ")
pris_tekst = input("Pris per kWh: ")

forbruk = float(forbruk_tekst)
pris = float(pris_tekst)

kostnad = forbruk * pris

print("Beregnet kostnad:")
print(kostnad)
```

Programmet har en tydelig rekkefølge:

1. spør brukeren
2. lagrer tekstsvarene
3. konverterer teksten til tall
4. utfører beregningen
5. skriver resultatet

Det er et lite program, men det følger samme grunnidé som langt større programmer: **data inn → behandling → resultat ut**.

## Hvorfor beholde tekstvariablene?

Vi kunne skrevet:

```python
forbruk = float(input("Forbruk i kWh: "))
```

Det er kortere. Men akkurat nå er den lengre varianten nyttig fordi du kan se hvert steg.

Når du blir mer erfaren, kan du selv velge hvilken form som er tydeligst.

## Endre det

Utvid programmet med antall dager:

```python
forbruk_per_dag = float(input("Forbruk per dag i kWh: "))
antall_dager = int(input("Antall dager: "))
pris = float(input("Pris per kWh: "))

total_forbruk = forbruk_per_dag * antall_dager
kostnad = total_forbruk * pris

print("Totalt forbruk:")
print(total_forbruk)
print("Beregnet kostnad:")
print(kostnad)
```

Legg merke til at `antall_dager` bruker `int()`, mens verdier som kan ha desimaler bruker `float()`.

## Hva skjer med ugyldig input?

Hvis programmet forventer et tall og brukeren skriver et ord, kan Python stoppe med `ValueError`.

Det er foreløpig forventet oppførsel. Målet i M3 er å forstå input og konvertering.

Senere lærer du å la programmet ta egne valg og håndtere flere situasjoner.

## Lag det selv

Velg én liten kalkulator, for eksempel:

- pris × antall
- kilometer per dag × antall dager
- timer × pris per time
- temperaturkonvertering
- enkel rente for ett år

Programmet skal:

- spørre etter minst to verdier
- bruke tydelige variabelnavn
- konvertere input til riktig talltype
- ha minst ett mellomresultat eller sluttresultat i en variabel
- skrive forklarende tekst sammen med resultatet

Kjør programmet flere ganger med forskjellige verdier.

## Tenk gjennom programmet

Før du går videre, skal du kunne peke på:

- hvor data kommer inn
- hvor tekst blir gjort om til tall
- hvor beregningen skjer
- hvor resultatet kommer ut

Dette mønsteret kommer igjen gjennom resten av kurset.
