# M8.2 – Les en fil linje for linje

I forrige leksjon brukte vi \`read()\` til å lese hele filen på én gang.

Ofte vil vi heller behandle én linje om gangen.

Da kan vi bruke en \`for\`-løkke.

## Prøv det

Tenk at filen \`temperaturer.txt\` inneholder:

```text
18
20
17
21
```

Programmet kan lese linjene slik:

```python
with open("temperaturer.txt", "r", encoding="utf-8") as fil:
    for linje in fil:
        print(linje)
```

Dette bruker samme \`for\`-idé som du allerede kjenner.

Python gir oss én linje fra filen om gangen.

## Følg løkka

Første runde:

```text
linje → "18" + linjeskift
```

Andre runde:

```text
linje → "20" + linjeskift
```

og slik fortsetter det til filen er ferdig lest.

escape-sekvensen for linjeskift representerer et linjeskift.

Du ser vanligvis ikke tegnene tegnene for escape-sekvensen for linjeskift i tekstfilen. De beskriver at linjen slutter og en ny begynner.

## Hvorfor kan print() gi ekstra luft?

\`print()\` legger normalt til sitt eget linjeskift.

Hvis teksten vi skriver ut allerede slutter med et linjeskift, kan resultatet se slik ut:

```text
18

20

17

21
```

Vi kan fjerne linjeskiftet før vi skriver ut teksten.

## strip()

```python
with open("temperaturer.txt", "r", encoding="utf-8") as fil:
    for linje in fil:
        linje = linje.strip()
        print(linje)
```

Nå blir resultatet:

```text
18
20
17
21
```

\`strip()\` lager en tekstverdi uten mellomrom og linjeskift i starten og slutten.

I dette eksempelet bruker vi den først og fremst for å fjerne linjeskiftet.

## Fil → linje → tekst

Det kan hjelpe å tenke slik:

```text
tekstfil
   │
   ├── linje 1 → "18"
   ├── linje 2 → "20"
   ├── linje 3 → "17"
   └── linje 4 → "21"
```

Løkka behandler én tekstlinje om gangen.

## Tall i en tekstfil er fortsatt tekst

Selv om filen inneholder:

```text
18
20
17
```

leses hver linje som tekst.

Hvis vi vil regne med verdien, må vi konvertere den:

```python
with open("temperaturer.txt", "r", encoding="utf-8") as fil:
    for linje in fil:
        temperatur = int(linje.strip())
        print(temperatur + 1)
```

Dette bygger på konverteringen du lærte tidligere.

## Beregn en sum

Vi kan kombinere fil, løkke og akkumulator:

```python
total = 0

with open("temperaturer.txt", "r", encoding="utf-8") as fil:
    for linje in fil:
        verdi = int(linje.strip())
        total = total + verdi

print("Total:", total)
```

For filen:

```text
18
20
17
21
```

blir totalen:

```text
Total: 76
```

## Hvorfor lese linje for linje?

\`read()\` er enkelt når vi vil ha hele teksten.

En \`for\`-løkke er nyttig når vi vil:

- behandle hver linje separat
- konvertere hver linje
- telle linjer
- lete etter bestemte verdier
- beregne noe fra dataene

Senere vil dette bli viktig når vi arbeider med datafiler.

## Tell linjene

```python
antall = 0

with open("temperaturer.txt", "r", encoding="utf-8") as fil:
    for linje in fil:
        antall = antall + 1

print("Antall linjer:", antall)
```

Her trenger vi ikke engang innholdet i linjen. Vi teller bare hvor mange ganger løkka kjører.

## Endre det

Bruk en tekstfil med minst fire tall.

Lag et program som:

1. leser filen linje for linje
2. bruker \`strip()\`
3. konverterer hver linje til \`int\`
4. skriver ut hvert tall
5. beregner totalen

Endre deretter ett tall i filen og kjør programmet igjen.

## Lag det selv

Lag en tekstfil med ett navn eller sted per linje.

Skriv et program som:

- leser filen linje for linje
- fjerner linjeskift med \`strip()\`
- skriver ut hver verdi
- teller hvor mange linjer filen inneholder

## Dette har du lært

Du kan nå:

- lese en tekstfil linje for linje
- bruke en fil direkte i en \`for\`-løkke
- forstå at tekstlinjer normalt inneholder linjeskift
- bruke \`strip()\`
- konvertere tekst fra en fil til tall
- beregne en sum fra filinnhold
- telle linjer
- velge mellom \`read()\` og linjevis behandling

Neste leksjon handler om å skrive en ny tekstfil.
