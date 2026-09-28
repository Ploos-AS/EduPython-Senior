# M2.1 – Gi verdier navn

I M1 skrev vi tall og tekst direkte i instruksjonene. Det fungerer, men et program blir raskt vanskelig å endre hvis den samme verdien brukes flere steder.

En **variabel (variable)** gir en verdi et navn.

## Hvorfor bruke variabler?

Sammenlign:

```python
print(5 * 1.50)
```

med:

```python
antall = 5
pris = 1.50
print(antall * pris)
```

Begge beregner det samme. Den andre versjonen forteller oss hva tallene betyr.

## Prøv det

Skriv:

```python
navn = "Ada"
alder = 70

print(navn)
print(alder)
```

Python lagrer teksten `"Ada"` under navnet `navn`, og tallet `70` under navnet `alder`.

Når `print(navn)` kjøres, finner Python verdien som variabelen `navn` viser til.

## Hva betyr =?

I Python betyr:

```python
pris = 1.50
```

omtrent «la `pris` få verdien `1.50`».

Dette kalles **tilordning (assignment)**.

Det er ikke helt det samme som likhetstegnet i matematikk. Python bruker `=` for å tilordne en verdi til et navn.

## Bruk variabler i beregninger

```python
forbruk = 5
pris_per_kwh = 1.50

print("Kostnad:")
print(forbruk * pris_per_kwh)
```

Nå kan du endre `forbruk` eller `pris_per_kwh` ett sted og kjøre programmet på nytt.

## Endre det

Prøv:

```python
forbruk = 8
pris_per_kwh = 0.90

print(forbruk * pris_per_kwh)
```

Bytt verdiene og se hvordan resultatet endres.

## En variabel kan få en ny verdi

```python
temperatur = 18
print(temperatur)

temperatur = 21
print(temperatur)
```

Den andre tilordningen gjør at `temperatur` nå viser til `21`.

Dette er en viktig forskjell fra hvordan bokstaver ofte brukes i matematikk.

## Gode navn hjelper deg

Dette virker:

```python
x = 5
y = 1.50
print(x * y)
```

Men dette er lettere å forstå:

```python
antall = 5
pris = 1.50
print(antall * pris)
```

Velg navn som beskriver hva verdien betyr.

Variabelnavn kan blant annet inneholde bokstaver, tall og understrek, men kan ikke begynne med et tall.

```python
pris_per_kwh = 1.50
```

er et vanlig og tydelig Python-navn.

## Når Python ikke kjenner navnet

Prøv med vilje:

```python
print(kostnad)
```

hvis du ikke først har laget en variabel som heter `kostnad`.

Python vil rapportere:

```text
NameError: name 'kostnad' is not defined
```

**NameError** betyr her at Python ikke finner navnet du ba den bruke.

Se etter:

1. Har variabelen fått en verdi før den brukes?
2. Er navnet skrevet likt begge steder?
3. Har du kanskje skrevet en bokstav feil?

## Lag det selv

Lag et program med minst tre variabler:

- én som inneholder tekst
- én som inneholder et heltall
- én som inneholder et desimaltall

Skriv ut variablene og bruk minst to av tallvariablene i en beregning.

Endre deretter én verdi og kjør programmet igjen.

## Dette har du lært

Du kan nå:

- forklare hvorfor variabler er nyttige
- tilordne verdier med `=`
- bruke variabler i `print()` og beregninger
- endre verdien til en variabel
- velge tydelige variabelnavn
- kjenne igjen en enkel `NameError`

Neste leksjon bruker variabler til å bygge et mer praktisk program.
