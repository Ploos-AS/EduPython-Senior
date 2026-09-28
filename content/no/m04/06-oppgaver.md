# M4.6 – Oppgaver og feilsøking

Disse oppgavene samler hele M4. Prøv selv før du leser veiledningen.

## 1. Sant eller usant?

Anta:

```python
tall = 10
```

Hva blir resultatet av:

```python
tall > 5
tall == 10
tall != 10
tall <= 9
```

**Svar:**

- `tall > 5` → sant
- `tall == 10` → sant
- `tall != 10` → usant
- `tall <= 9` → usant

## 2. = eller ==?

Hvilken linje lagrer en verdi?

```python
alder = 70
alder == 70
```

**Svar:** `alder = 70` lagrer verdien. `alder == 70` sammenligner.

## 3. Finn syntaksfeilen

```python
temperatur = float(input("Temperatur: "))

if temperatur < 0
    print("Under null")
```

**Svar:** Det mangler kolon etter betingelsen:

```python
if temperatur < 0:
```

## 4. Finn innrykksfeilen

```python
tall = int(input("Tall: "))

if tall >= 10:
print("Minst 10")
else:
    print("Under 10")
```

Linjen under `if` må ha innrykk:

```python
if tall >= 10:
    print("Minst 10")
else:
    print("Under 10")
```

## 5. Hva skjer ved grensen?

```python
if temperatur < 20:
    print("Under 20")
else:
    print("20 eller høyere")
```

Hva skrives ut når `temperatur` er nøyaktig `20`?

**Svar:** `20 eller høyere`, fordi `20 < 20` er usant.

## 6. Finn logikkfeilen

```python
if temperatur < 20:
    print("Under 20")
elif temperatur < 0:
    print("Under null")
else:
    print("20 eller høyere")
```

Hvorfor vil `-5` aldri gi meldingen `Under null`?

**Svar:** Den første betingelsen, `temperatur < 20`, er allerede sann for `-5`. Første sanne gren vinner.

En mulig rettelse:

```python
if temperatur < 0:
    print("Under null")
elif temperatur < 20:
    print("Fra 0 til under 20")
else:
    print("20 eller høyere")
```

## 7. Fullfør området

Fullfør slik at meldingen bare skrives for tall fra og med 10 til og med 20:

```python
if tall >= 10 __________ tall <= 20:
    print("I området")
```

**Svar:**

```python
if tall >= 10 and tall <= 20:
```

## 8. and eller or?

Du vil skrive en melding når temperaturen er lavere enn 0 **eller** høyere enn 30.

**Mulig løsning:**

```python
if temperatur < 0 or temperatur > 30:
    print("Utenfor området")
```

## 9. Forutsi før du kjører

```python
poeng = 50

if poeng < 25:
    melding = "A"
elif poeng < 50:
    melding = "B"
elif poeng < 75:
    melding = "C"
else:
    melding = "D"

print(melding)
```

Hva skrives ut?

**Svar:** `C`. Betingelsen `poeng < 50` er usann når poeng er nøyaktig 50.

## 10. Mini-prosjekt

Lag et interaktivt beslutningsprogram.

Krav:

- minst én `input()`
- nødvendig `int()` eller `float()`
- `if`, `elif` og `else`
- minst tre mulige resultater
- minst én tydelig sammenligning
- bruk `and`, `or` eller `not` der det faktisk gjør programmet tydeligere
- lagre valgt resultat i en variabel
- skriv resultatet etter beslutningen
- test rett under, på og rett over viktige grenser

Skriv gjerne ned forventet resultat før hver test.

## Før du går videre

Du bør nå kunne forklare:

- hva en sann/usann-betingelse er
- forskjellen på `=` og `==`
- hvorfor kolon og innrykk er viktige
- hvordan `if`, `elif` og `else` velger en gren
- hvorfor rekkefølgen på betingelser kan endre resultatet
- hvordan `and`, `or` og `not` brukes
- hvordan grenseverdier testes

Neste milepæl handler om repetisjon: å få programmet til å utføre kode flere ganger uten å kopiere den.
