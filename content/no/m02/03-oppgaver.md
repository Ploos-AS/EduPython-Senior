# M2.3 – Oppgaver og feilsøking

Prøv hver oppgave selv før du leser veiledningen eller løsningen.

## Oppgave 1 – Gi verdiene navn

Skriv om:

```python
print(12 * 4.50)
```

slik at begge tallene først lagres i variabler med tydelige navn.

### Mulig løsning

```python
antall = 12
pris_per_stykk = 4.50
print(antall * pris_per_stykk)
```

## Oppgave 2 – Lagre resultatet

Utvid programmet slik at resultatet også får et navn.

### Mulig løsning

```python
antall = 12
pris_per_stykk = 4.50
total = antall * pris_per_stykk

print("Total:")
print(total)
```

## Oppgave 3 – Hva blir skrevet ut?

Forutsi resultatet før du kjører:

```python
tall = 5
dobbel = tall * 2
tall = 8

print(tall)
print(dobbel)
```

### Løsning

Programmet skriver:

```text
8
10
```

`dobbel` fikk verdien `10` da den linjen ble kjørt. Den beregnes ikke automatisk på nytt når `tall` senere blir `8`.

## Oppgave 4 – Finn NameError

Hva er galt?

```python
pris = 25
antall = 3
total = pris * antall

print(totalt)
```

### Veiledning

Sammenlign navnet som får resultatet med navnet som brukes i `print()`.

### Løsning

Variabelen heter `total`, men programmet prøver å bruke `totalt`.

```python
print(total)
```

Variabelnavn må skrives konsekvent.

## Oppgave 5 – Bedre navn

Denne koden virker:

```python
a = 120
b = 3
c = a / b
print(c)
```

Skriv den om med navn som forklarer at 120 kilometer skal fordeles på 3 dager.

### Mulig løsning

```python
avstand_km = 120
antall_dager = 3
km_per_dag = avstand_km / antall_dager

print(km_per_dag)
```

## Oppgave 6 – Mellomresultater

Lag et program med:

```text
effekt = 1500 watt
tid = 2 timer
pris = 1.25 per kWh
```

Beregn først kilowatt, deretter kWh, deretter kostnaden. Bruk en variabel for hvert steg.

### Mulig løsning

```python
effekt_watt = 1500
timer = 2
pris_per_kwh = 1.25

effekt_kw = effekt_watt / 1000
forbruk_kwh = effekt_kw * timer
kostnad = forbruk_kwh * pris_per_kwh

print(kostnad)
```

## Miniprosjekt

Lag et program som beregner noe du synes er nyttig eller interessant.

Krav:

- minst tre startvariabler
- tydelige variabelnavn
- minst ett mellomresultat
- et sluttresultat lagret i en variabel
- forklarende output
- endre minst én startverdi og kontroller at det nye resultatet gir mening

Eksempler kan være kostnader, avstander, mengder, tidsbruk eller en annen enkel beregning.

## Før du går videre

Du er klar for M3 når du kan forklare:

- hvorfor en variabel er nyttig
- hva `=` gjør i Python
- hvorfor gode navn hjelper
- hvorfor et tidligere beregnet resultat ikke endres automatisk
- hva du først bør kontrollere ved `NameError`

I M3 skal programmet slutte å være helt fast: brukeren skal kunne skrive inn verdier mens programmet kjører.
