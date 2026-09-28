# M4.2 – To mulige veier med else

En `if` kan velge om en kodeblokk skal kjøres. Ofte ønsker vi i stedet at programmet skal velge mellom **to** veier.

Da bruker vi `else`.

## Prøv det

```python
temperatur = float(input("Temperatur: "))

if temperatur < 0:
    print("Temperaturen er under null.")
else:
    print("Temperaturen er null eller høyere.")
```

Programmet kjører nøyaktig én av de to meldingene.

Hvis betingelsen er sann, kjøres blokken under `if`.

Hvis betingelsen er usann, kjøres blokken under `else`.

## else har ingen egen betingelse

Legg merke til:

```python
else:
```

Vi skriver ikke et nytt spørsmål etter `else`.

`else` betyr ganske enkelt: **ellers** – altså når `if`-betingelsen ikke var sann.

## Grenseverdien betyr noe

I eksemplet er betingelsen:

```python
temperatur < 0
```

Hva skjer når temperaturen er nøyaktig `0`?

Uttrykket `0 < 0` er usant. Derfor går programmet til `else`.

Når du skriver betingelser, bør du alltid tenke på selve grensen.

## Endre det

Prøv:

```python
tall = int(input("Skriv et heltall: "))

if tall >= 10:
    print("Tallet er minst 10.")
else:
    print("Tallet er mindre enn 10.")
```

Kjør programmet med:

- `9`
- `10`
- `11`

Legg spesielt merke til hva som skjer med `10`.

## Innrykk viser de to blokkene

```python
if tall >= 10:
    print("Første vei")
    print("Betingelsen var sann.")
else:
    print("Andre vei")
    print("Betingelsen var usann.")

print("Denne linjen kjøres etter valget.")
```

Etter at én av blokkene er ferdig, fortsetter programmet med kode som ikke lenger er innrykket under `if` eller `else`.

## En vanlig strukturfeil

Dette er feil:

```python
if tall >= 10:
    print("Minst 10")
    else:
        print("Mindre enn 10")
```

`else` skal stå på samme innrykksnivå som `if`:

```python
if tall >= 10:
    print("Minst 10")
else:
    print("Mindre enn 10")
```

Når Python klager på strukturen rundt `else`, kontroller kolon og innrykk først.

## Lag det selv

Lag et program som:

- spør etter én verdi
- konverterer den til et tall
- bruker `if` og `else`
- skriver én melding når betingelsen er sann
- skriver en annen melding når den er usann

Test verdier på begge sider av grensen, og test selve grenseverdien.

## Dette har du lært

Du kan nå:

- bruke `if` og `else` sammen
- forklare at bare én av de to blokkene kjøres
- forklare hva `else` betyr
- undersøke hva som skjer ved en grenseverdi
- plassere `if` og `else` med riktig innrykk

Neste leksjon introduserer `elif` når programmet trenger mer enn to mulige veier.
