# M4.3 – Flere veier med elif

Med `if` og `else` kan programmet velge mellom to veier. Noen ganger trenger vi flere.

Da bruker vi `elif`, som kan leses som **ellers hvis**.

## Prøv det

```python
temperatur = float(input("Temperatur: "))

if temperatur < 0:
    print("Under null.")
elif temperatur < 20:
    print("Mellom 0 og under 20.")
else:
    print("20 eller høyere.")
```

Programmet velger én av tre veier.

## Python tester ovenfra og ned

Python gjør dette:

1. tester `temperatur < 0`
2. hvis den er sann, kjøres den blokken og resten hoppes over
3. ellers testes `temperatur < 20`
4. hvis også den er usann, kjøres `else`

Bare den **første sanne grenen** kjøres.

## Hvorfor betyr rekkefølgen noe?

Se på:

```python
if temperatur < 20:
    print("Under 20")
elif temperatur < 0:
    print("Under null")
```

Hvis temperaturen er `-5`, er allerede `temperatur < 20` sann. Python kjører den første blokken og kommer aldri til testen `temperatur < 0`.

Når betingelser overlapper, må de derfor stå i en fornuftig rekkefølge.

## Grensene igjen

I det første programmet:

- `-1` går til første gren
- `0` går til `elif`
- `19.9` går til `elif`
- `20` går til `else`

Test gjerne akkurat disse verdiene.

## Flere elif

Du kan ha mer enn én `elif`:

```python
poeng = int(input("Poeng: "))

if poeng < 25:
    print("Nivå 1")
elif poeng < 50:
    print("Nivå 2")
elif poeng < 75:
    print("Nivå 3")
else:
    print("Nivå 4")
```

Igjen testes grenene ovenfra og ned.

## else er fortsatt valgfri

En kjede trenger ikke alltid `else`:

```python
tall = int(input("Tall: "))

if tall < 0:
    print("Negativt")
elif tall == 0:
    print("Null")
```

Hvis tallet er positivt, skriver denne koden ingenting.

Bruk `else` når du faktisk trenger en siste vei for alle andre tilfeller.

## Endre det

Lag tre temperaturkategorier med andre grenser. Test:

- en verdi under første grense
- nøyaktig første grense
- en verdi mellom grensene
- nøyaktig andre grense
- en verdi over andre grense

## En vanlig tankefeil

Ikke spør bare «er hver betingelse riktig?». Spør også:

**Kan en tidligere betingelse allerede ha fanget denne verdien?**

Det er en viktig del av feilsøking av `if`/`elif`.

## Lag det selv

Lag et program med minst tre mulige utfall.

Programmet skal:

- lese én verdi med `input()`
- konvertere verdien
- bruke `if`, minst én `elif` og `else`
- skrive forskjellige meldinger for de forskjellige områdene
- testes ved grensene mellom områdene

## Dette har du lært

Du kan nå:

- bruke `elif`
- lage mer enn to mulige veier
- forklare at Python tester ovenfra og ned
- forklare at første sanne gren vinner
- ordne overlappende betingelser fornuftig
- teste grenseverdier systematisk

Neste leksjon kombinerer enkle betingelser med `and`, `or` og `not`.
