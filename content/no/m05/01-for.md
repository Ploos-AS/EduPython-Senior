# M5.1 – Gjør noe flere ganger med for

Programmer må ofte gjøre den samme typen arbeid flere ganger.

Vi kunne kopiert samme instruksjon:

```python
print("Anna")
print("Bjørn")
print("Cecilie")
```

Men hvis vi har mange verdier, blir slik kopiering tungvint. En **løkke** lar programmet gjenta en blokk med kode.

## Prøv det

```python
navn = ["Anna", "Bjørn", "Cecilie"]

for navn_i_liste in navn:
    print(navn_i_liste)

print("Ferdig")
```

Resultatet blir:

```text
Anna
Bjørn
Cecilie
Ferdig
```

Du trenger ikke forstå alle detaljene i hakeparentesene ennå. Akkurat nå kan du lese første linje som «her er tre verdier».

## Les for som en setning

Denne linjen:

```python
for navn_i_liste in navn:
```

kan leses:

**For hvert navn i navn, gjør dette.**

Python tar én verdi om gangen og legger den midlertidig i variabelen `navn_i_liste`.

Første gang er den `"Anna"`, så `"Bjørn"`, og til slutt `"Cecilie"`.

## Innrykket viser hva som gjentas

```python
for navn_i_liste in navn:
    print("Hei")
    print(navn_i_liste)

print("Alle er behandlet")
```

Begge de innrykkede linjene kjøres for hver verdi.

Den siste linjen har ikke innrykk. Den kjøres derfor først etter at løkka er ferdig.

## Følg programmet steg for steg

For:

```python
verdier = [2, 4, 6]

for verdi in verdier:
    print(verdi)
```

skjer dette:

1. `verdi` blir `2`, og blokken kjøres
2. `verdi` blir `4`, og blokken kjøres
3. `verdi` blir `6`, og blokken kjøres
4. det finnes ingen flere verdier, så løkka er ferdig

## En vanlig feil

Denne koden mangler innrykk:

```python
for verdi in verdier:
print(verdi)
```

Python forventer en innrykket blokk etter `for`.

Riktig:

```python
for verdi in verdier:
    print(verdi)
```

Legg også merke til kolonet `:` etter `for`-linjen.

## Endre det

Endre:

```python
navn = ["Anna", "Bjørn", "Cecilie"]
```

til tre andre tekster.

Forutsi først hva programmet vil skrive ut. Kjør det deretter.

## Lag det selv

Lag et program med tre eller flere verdier og en `for`-løkke.

Programmet skal:

- gå gjennom verdiene én om gangen
- skrive hver verdi
- ha minst én ekstra instruksjon inne i løkka
- skrive en avsluttende melding etter løkka

## Dette har du lært

Du kan nå:

- forklare hvorfor løkker er nyttige
- lese en enkel `for`-løkke
- forklare at løkkevariabelen får én verdi om gangen
- se hvilke instruksjoner som gjentas ved hjelp av innrykk
- se når løkka er ferdig

Neste leksjon bruker `range()` til å gjenta kode et bestemt antall ganger.
