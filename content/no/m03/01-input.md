# M3.1 – La brukeren skrive inn noe

Til nå har alle verdiene stått i programmet på forhånd. Nå skal programmet kunne spørre brukeren.

Python-funksjonen `input()` stopper programmet og venter på at brukeren skriver noe.

## Prøv det

```python
navn = input("Hva heter du? ")
print("Hei!")
print(navn)
```

Når programmet kommer til `input()`:

1. teksten `Hva heter du? ` vises
2. programmet venter
3. du skriver et svar og trykker Enter
4. svaret lagres i variabelen `navn`
5. programmet fortsetter

## input() gir tekst

Dette er viktig:

**`input()` gir alltid tekst tilbake.**

Prøv:

```python
alder = input("Hvor gammel er du? ")
print(alder)
```

Hvis du skriver `70`, har Python foreløpig fått teksten `"70"`, ikke tallet `70`.

Det er ikke en feil. Det er slik `input()` fungerer.

## Endre det

Lag et program som spør etter to ting:

```python
navn = input("Navn: ")
sted = input("Sted: ")

print("Du skrev:")
print(navn)
print(sted)
```

Endre spørsmålene til noe annet.

## Tekst kan brukes direkte

Når svaret faktisk skal være tekst, trenger vi ingen konvertering:

```python
favoritt = input("Skriv noe du liker å lære om: ")
print("Du skrev:")
print(favoritt)
```

## Men hva med regning?

Dette ser kanskje naturlig ut:

```python
tall = input("Skriv et tall: ")
print(tall + 1)
```

men det virker ikke.

`tall` inneholder tekst. Python kan ikke uten videre legge tallet `1` til en tekststreng.

I neste leksjon lærer vi å gjøre tekst som `"42"` om til tallet `42`.

## Lag det selv

Lag et lite spørreprogram som:

- stiller minst tre spørsmål
- lagrer hvert svar i en variabel
- skriver svarene ut igjen med forklarende tekst

Bruk bare tekstsvar foreløpig.

## Dette har du lært

Du kan nå:

- bruke `input()`
- lagre brukerens svar i en variabel
- forklare at programmet venter ved `input()`
- forklare at resultatet fra `input()` er tekst

Neste leksjon gjør tekstinput om til tall vi kan regne med.
