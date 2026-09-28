# M4.5 – Et praktisk beslutningsprogram

Nå setter vi sammen det du har lært om input, tall og beslutninger.

Vi lager et program som beskriver en temperatur.

## Prøv det

```python
temperatur = float(input("Temperatur: "))

if temperatur < 0:
    melding = "Under null"
elif temperatur >= 0 and temperatur < 10:
    melding = "Kjølig"
elif temperatur >= 10 and temperatur < 20:
    melding = "Mildt"
else:
    melding = "20 eller høyere"

print("Vurdering:")
print(melding)
```

Programmet:

1. leser data
2. konverterer teksten til et tall
3. tester betingelser
4. velger én melding
5. skriver resultatet

Legg merke til at grenene lagrer en verdi i `melding`. Selve utskriften skjer bare én gang etter beslutningen.

## Følg én verdi gjennom programmet

Anta at brukeren skriver `12`.

Python tester:

```python
temperatur < 0
```

Usant.

Deretter:

```python
temperatur >= 0 and temperatur < 10
```

Usant.

Deretter:

```python
temperatur >= 10 and temperatur < 20
```

Sant.

Da blir:

```python
melding = "Mildt"
```

Resten av grenene hoppes over.

## Test grensene

Et beslutningsprogram bør ikke bare testes med tilfeldige tall.

Prøv:

- `-1`
- `0`
- `9.9`
- `10`
- `19.9`
- `20`

For hver verdi: bestem først hvilken melding du forventer, og kjør deretter programmet.

Dette er en enkel form for systematisk testing.

## Kan betingelsene forenkles?

Fordi tidligere grener allerede har utelukket lavere verdier, kunne noen av betingelsene skrives kortere.

Men den eksplisitte formen:

```python
temperatur >= 10 and temperatur < 20
```

viser området tydelig mens vi lærer.

Lesbar kode er viktigere enn å gjøre hver linje så kort som mulig.

## Endre det

Lag dine egne grenser og meldinger.

Skriv ned grensene før du endrer koden. Test deretter:

- rett under hver grense
- nøyaktig på hver grense
- rett over hver grense

## Lag det selv

Lag et beslutningsprogram for et annet tema.

Krav:

- minst én verdi fra `input()`
- nødvendig konvertering
- `if`
- minst én `elif`
- `else`
- minst én sammenligning
- minst én tydelig resultatvariabel
- test av grenseverdier

Mulige temaer er tidsbruk, strømforbruk, avstand, poeng eller et eget numerisk område.

## Dette har du lært

Du kan nå sette sammen:

**data inn → konvertering → beslutning → resultat**

Du kan også teste et beslutningsprogram systematisk rundt grensene.

Neste del trener på hele M4 med oppgaver og feilsøking.
