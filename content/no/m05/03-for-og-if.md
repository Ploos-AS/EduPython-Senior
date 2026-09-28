# M5.3 – Beslutninger inne i en løkke

En løkke kan gjøre mer enn å skrive hver verdi. Den kan også ta en beslutning for hver verdi.

Det betyr at kunnskap fra M4 kan brukes inne i en `for`-løkke.

## Prøv det

```python
for tall in range(1, 6):
    if tall < 3:
        print(tall, "er mindre enn 3")
    else:
        print(tall, "er 3 eller større")
```

Løkka går gjennom tallene 1 til 5.

For hvert tall testes:

```python
tall < 3
```

Beslutningen tas altså på nytt i hver runde.

## Følg programmet steg for steg

Når `tall` er `1`:

- `1 < 3` er sant
- første melding skrives

Når `tall` er `2`:

- `2 < 3` er sant
- første melding skrives

Når `tall` er `3`:

- `3 < 3` er usant
- `else`-meldingen skrives

Det samme skjer for `4` og `5`.

## To nivåer med innrykk

Se nøye på:

```python
for tall in range(1, 6):
    if tall < 3:
        print("Lavt tall")
```

Her har vi to blokker:

1. `if` ligger inne i `for`-blokken
2. `print()` ligger inne i `if`-blokken

Innrykket viser strukturen.

Du trenger ikke telle mellomrom for hånd. En vanlig kodeeditor hjelper med innrykket.

## En beslutning trenger ikke alltid else

```python
for tall in range(1, 6):
    if tall == 3:
        print("Fant 3")

    print("Behandler", tall)
```

Meldingen `Fant 3` skrives bare én gang.

`Behandler` skrives i hver runde fordi den fortsatt ligger inne i `for`, men ikke inne i `if`.

## Kombinerte betingelser virker også

```python
for tall in range(1, 11):
    if tall >= 4 and tall <= 6:
        print(tall, "er i området")
```

Her blir `if`-testen utført for hvert tall fra 1 til 10.

## En vanlig innrykksfeil

Sammenlign:

```python
for tall in range(1, 4):
    if tall == 2:
        print("Fant 2")
    print("Runde", tall)
```

med:

```python
for tall in range(1, 4):
    if tall == 2:
        print("Fant 2")

print("Runde", tall)
```

I den siste versjonen er den siste `print()` utenfor løkka. Den kjøres bare én gang etterpå.

Koden kan altså være gyldig Python og likevel gjøre noe annet enn du hadde tenkt. Innrykk er både syntaks og programstruktur.

## Endre det

Endre grensen i:

```python
if tall < 3:
```

Forutsi hvilke runder som tar hver gren før du kjører programmet.

## Lag det selv

Lag et program som:

- bruker `for` og `range()`
- går gjennom minst fem tall
- bruker `if` inne i løkka
- gir minst to forskjellige typer resultat
- har en melding etter at hele løkka er ferdig

Forutsi resultatet før du kjører programmet.

## Dette har du lært

Du kan nå:

- bruke `if` inne i en `for`-løkke
- forklare at beslutningen tas på nytt i hver runde
- lese kode med to nivåer av innrykk
- skille kode inne i `if`, inne i `for` og etter løkka
- oppdage logiske feil som skyldes feil blokkstruktur

Neste leksjon viser hvordan en løkke kan bygge opp et resultat over flere runder.
