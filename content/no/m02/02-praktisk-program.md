# M2.2 – Et program som er lett å endre

I M1 skrev vi tallene direkte i beregningen. Nå kan variabler gjøre programmet tydeligere og lettere å endre.

## Fra uttrykk til program

Dette virker:

```python
print(5 * 1.50)
```

Men hva betyr `5` og `1.50`?

Med variabler blir hensikten tydelig:

```python
forbruk_kwh = 5
pris_per_kwh = 1.50

print(forbruk_kwh * pris_per_kwh)
```

## Gi også resultatet et navn

Et resultat kan lagres i en ny variabel:

```python
forbruk_kwh = 5
pris_per_kwh = 1.50
kostnad = forbruk_kwh * pris_per_kwh

print("Beregnet kostnad:")
print(kostnad)
```

Les linjen:

```python
kostnad = forbruk_kwh * pris_per_kwh
```

fra høyre mot venstre:

1. Python finner verdiene til `forbruk_kwh` og `pris_per_kwh`.
2. Python multipliserer dem.
3. Resultatet tilordnes navnet `kostnad`.

## Prøv det

Lag programmet over og kjør det.

Endre deretter bare:

```python
forbruk_kwh = 8
```

Kjør programmet igjen. Resten av programmet trenger ikke endres.

Det er en viktig grunn til å bruke variabler.

## Mellomresultater

Vi kan også dele en beregning opp i forståelige steg:

```python
effekt_watt = 1000
timer = 3
pris_per_kwh = 1.20

effekt_kw = effekt_watt / 1000
forbruk_kwh = effekt_kw * timer
kostnad = forbruk_kwh * pris_per_kwh

print("Forbruk i kWh:")
print(forbruk_kwh)
print("Kostnad:")
print(kostnad)
```

Programmet er lengre enn ett stort regnestykke, men hvert steg har fått et navn.

Det gjør koden lettere å lese, kontrollere og endre.

## Endre det

Prøv med:

```python
effekt_watt = 750
timer = 4
pris_per_kwh = 1.10
```

Før du kjører programmet, prøv å anslå hva resultatet blir.

## Verdien beregnes når linjen kjøres

Se nøye på dette:

```python
pris = 10
dobbel_pris = pris * 2

pris = 20

print(dobbel_pris)
```

Programmet skriver ut `20`, ikke `40`.

Da `dobbel_pris = pris * 2` ble kjørt, var `pris` lik `10`. Resultatet `20` ble lagret i `dobbel_pris`.

Å endre `pris` senere beregner ikke gamle linjer på nytt.

## Lag det selv

Lag et lite program som beregner en total fra minst tre navngitte verdier.

Du kan for eksempel bruke:

- antall og pris
- avstand og kostnad per kilometer
- antall porsjoner og mengde per porsjon
- timer og en verdi per time

Krav:

1. bruk tydelige variabelnavn
2. lag minst ett mellomresultat
3. lagre sluttresultatet i en variabel
4. skriv ut forklarende tekst og resultatet
5. endre én startverdi og kjør programmet igjen

## Dette har du lært

Du kan nå bruke variabler til både startverdier, mellomresultater og sluttresultater. Du har også sett at Python utfører tilordninger når programmet kommer til dem — gamle beregninger oppdateres ikke automatisk.

Neste del gir deg flere øvelser før vi går videre til interaktive programmer.
