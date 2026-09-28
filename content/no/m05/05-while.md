# M5.5 – Gjenta så lenge noe er sant med while

En `for`-løkke passer godt når programmet skal gå gjennom en kjent sekvens.

Noen ganger vet vi i stedet at programmet skal fortsette **så lenge en betingelse er sann**.

Da kan vi bruke `while`.

## Prøv det

```python
tall = 1

while tall <= 5:
    print(tall)
    tall = tall + 1

print("Ferdig")
```

Programmet skriver tallene 1 til 5.

## Les while som en setning

Denne linjen:

```python
while tall <= 5:
```

kan leses:

**Så lenge tall er mindre enn eller lik 5, gjør dette.**

Før hver runde tester Python betingelsen på nytt.

## Tre viktige deler

Denne typen `while`-løkke har tre deler.

### 1. Startverdi

```python
tall = 1
```

### 2. Betingelse

```python
while tall <= 5:
```

### 3. Oppdatering

```python
tall = tall + 1
```

Oppdateringen gjør at betingelsen etter hvert blir usann.

## Følg programmet

Første test:

```text
1 <= 5 → sant
```

Programmet skriver 1 og endrer `tall` til 2.

Senere:

```text
5 <= 5 → sant
```

Programmet skriver 5 og endrer `tall` til 6.

Neste test:

```text
6 <= 5 → usant
```

Løkka stopper.

## En uendelig løkke

Se på:

```python
tall = 1

while tall <= 5:
    print(tall)
```

Hva endrer `tall`?

Ingenting.

Verdien forblir 1, og `1 <= 5` fortsetter å være sann. Løkka stopper derfor ikke av seg selv.

Dette kalles en **uendelig løkke**.

Hvis et program ser ut til å kjøre uten å bli ferdig, er en løkke som aldri når stoppbetingelsen noe av det første du bør undersøke.

## while kan også stoppe med input

```python
svar = input("Skriv ja for å fortsette: ")

while svar == "ja":
    print("Du valgte å fortsette.")
    svar = input("Skriv ja for å fortsette: ")

print("Ferdig")
```

Her vet vi ikke på forhånd hvor mange runder løkka vil kjøre.

Betingelsen testes på nytt etter hvert svar.

## Hvorfor leses input både før og inne i løkka?

Programmet trenger et første svar før det kan teste:

```python
while svar == "ja":
```

Inne i løkka leser vi et nytt svar slik at betingelsen kan endre seg.

Hvis den andre `input()`-linjen mangler, vil et første svar på `ja` føre til at løkka fortsetter uten å spørre igjen.

## for eller while?

På dette stadiet kan du bruke denne tommelfingerregelen:

- bruk `for` når du går gjennom en kjent sekvens eller et kjent antall runder
- bruk `while` når repetisjonen styres av en betingelse som kan endre seg

Det finnes flere muligheter senere, men dette er en god start.

## Endre det

Endre:

```python
tall = 1
while tall <= 5:
```

slik at løkka skriver andre start- og sluttverdier.

Forutsi siste verdi som blir skrevet.

## Lag det selv

Lag en trygg `while`-løkke som:

- har en startverdi
- har en tydelig betingelse
- endrer en verdi inne i løkka
- til slutt gjør betingelsen usann
- skriver en melding etter at løkka er ferdig

Før du kjører den, forklar for deg selv **hvorfor løkka vil stoppe**.

## Dette har du lært

Du kan nå:

- forklare hva en `while`-løkke gjør
- lese en `while`-betingelse
- identifisere startverdi, betingelse og oppdatering
- forklare hvorfor en løkke kan bli uendelig
- bruke input til å styre hvor lenge en løkke fortsetter
- velge mellom en enkel `for`- og `while`-løkke

Neste del bruker løkker i et komplett praktisk program.
