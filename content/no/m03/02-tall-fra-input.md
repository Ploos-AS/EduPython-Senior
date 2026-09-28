# M3.2 – Gjør input om til tall

`input()` gir alltid tekst. Skal vi regne med det brukeren skriver, må teksten først konverteres til et tall.

## Hvorfor trenger vi konvertering?

Dette virker ikke:

```python
alder = input("Alder: ")
print(alder + 1)
```

Hvis du skriver `70`, inneholder `alder` teksten `"70"`.

Python kan ikke legge tallet `1` til en tekststreng.

## Heltall med int()

`int()` kan gjøre tekst som representerer et heltall om til et Python-heltall:

```python
alder_tekst = input("Alder: ")
alder = int(alder_tekst)

print("Neste år:")
print(alder + 1)
```

Du kan også skrive det kortere:

```python
alder = int(input("Alder: "))
print(alder + 1)
```

Den første versjonen viser tydeligere de enkelte stegene. Begge er gyldig Python.

## Desimaltall med float()

For verdier med desimaler bruker vi ofte `float()`:

```python
pris = float(input("Pris per kWh: "))
forbruk = float(input("Forbruk i kWh: "))

kostnad = pris * forbruk

print("Kostnad:")
print(kostnad)
```

Når Python-kode bruker desimalpunktum, skriver du for eksempel `1.25`, ikke `1,25`.

## Prøv det

Kjør programmet over med:

```text
Pris per kWh: 1.25
Forbruk i kWh: 6
```

Python kan nå regne med begge svarene fordi de er konvertert til tall.

## int eller float?

Bruk `int()` når du vil ha et heltall, for eksempel:

```python
antall = int(input("Antall: "))
```

Bruk `float()` når verdien kan inneholde desimaler:

```python
temperatur = float(input("Temperatur: "))
```

`float()` kan også lese tekst som `"6"`; resultatet blir da desimaltallet `6.0`.

## Når teksten ikke kan bli et tall

Prøv:

```python
antall = int(input("Antall: "))
```

og skriv:

```text
seks
```

Python rapporterer en feil som ligner:

```text
ValueError: invalid literal for int() with base 10: 'seks'
```

**ValueError** betyr her at Python fikk en verdi, men verdien kunne ikke brukes slik operasjonen krevde.

`int()` vet hvordan teksten `"6"` skal bli et tall. Den vet ikke hvordan ordet `"seks"` skal konverteres.

## Les feilen

Når du ser `ValueError` ved tallinput:

1. se hvilken konvertering som ble brukt – `int()` eller `float()`
2. se hva brukeren skrev
3. kontroller om teksten faktisk har et gyldig tallformat

Senere lærer vi hvordan et program kan håndtere ugyldig input selv. Foreløpig lærer vi å forstå hvorfor feilen oppstår.

## Endre det

Lag et program som spør etter antall og pris:

```python
antall = int(input("Antall: "))
pris = float(input("Pris per stykk: "))

total = antall * pris

print("Total:")
print(total)
```

Prøv flere gyldige verdier.

Prøv deretter med vilje en ugyldig verdi og les feilmeldingen.

## Lag det selv

Lag et program som:

- spør brukeren etter minst to tall
- bruker `int()` eller `float()` på riktig sted
- beregner et resultat
- lagrer resultatet i en variabel
- skriver forklarende tekst og resultatet

## Dette har du lært

Du kan nå:

- forklare hvorfor `input()` må konverteres før tallregning
- bruke `int()`
- bruke `float()`
- velge mellom heltall og desimaltall
- kjenne igjen og begynne å forstå `ValueError`

Neste leksjon setter dette sammen til et komplett lite interaktivt program.
