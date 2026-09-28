# M1.1 – Gi datamaskinen instruksjoner

Et program er en serie instruksjoner. Python leser instruksjonene og utfører dem i den rekkefølgen de står.

Vi begynner med `print()`. Navnet kommer fra engelsk *print*, men her betyr det først og fremst «vis dette på skjermen».

## Prøv det

Skriv:

```python
print("Hei!")
```

Kjør programmet. Du skal se:

```text
Hei!
```

Teksten mellom anførselstegnene er en **tekststreng (string)**.

Prøv også flere instruksjoner:

```python
print("God morgen")
print("Jeg lærer Python")
print("Én instruksjon om gangen")
```

Python utfører dem ovenfra og ned.

## Endre det

Bytt ut teksten med noe du selv velger:

```python
print("Min første Python-tekst")
```

Legg deretter til en linje til. Hva skjer hvis du bytter om rekkefølgen på de to `print()`-linjene?

## Tall er ikke tekst

Python kan også skrive ut tall:

```python
print(42)
print(3.14)
```

Tall trenger ikke anførselstegn.

Det blir viktig senere fordi Python kan **regne** med tall:

```python
print(2 + 3)
print(10 - 4)
print(6 * 7)
print(20 / 4)
```

Python viser resultatet av hvert uttrykk.

## Tekst eller regnestykke?

Sammenlign:

```python
print(2 + 3)
print("2 + 3")
```

Den første linjen viser `5`. Den andre viser teksten `2 + 3`.

Anførselstegn forteller Python at innholdet skal behandles som tekst.

## Når Python sier fra om en feil

Feil er en normal del av programmering. Python prøver å fortelle hvor problemet er.

Prøv med vilje:

```python
print("Hei!)
```

Du vil få en feilmelding som inneholder `SyntaxError`.

**Syntax (syntaks)** er reglene for hvordan Python-kode skal skrives. Her mangler det avsluttende anførselstegnet.

Rett linjen:

```python
print("Hei!")
```

Når du møter en feilmelding:

1. se hvilken linje Python peker på
2. les navnet på feilen
3. se nøye på koden rundt stedet Python markerer
4. endre én ting og prøv igjen

Du trenger ikke forstå hele feilmeldingen med én gang.

## Lag det selv

Lag et lite program som skriver ut:

- en overskrift
- to tekstlinjer
- resultatet av minst to regnestykker

Bruk minst én av operatorene `+`, `-`, `*` og `/`.

Kjør programmet og kontroller at resultatene er som du forventet.

## Dette har du lært

Du kan nå:

- gi Python en enkel instruksjon
- bruke `print()`
- skrive ut tekst og tall
- bruke Python som en enkel kalkulator
- se forskjellen på tekst og et matematisk uttrykk
- kjenne igjen `SyntaxError` og begynne å lese en feilmelding

Neste steg er å gi verdier navn ved hjelp av **variabler (variables)**.
