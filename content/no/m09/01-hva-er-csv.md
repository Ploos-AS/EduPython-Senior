# M9.1 — Hva er CSV?

I M8 lærte du å lese og skrive tekstfiler. Nå skal vi bruke tekstfiler til **data i tabellform**.

CSV er en enkel måte å lagre rader og kolonner på. Navnet kommer fra *Comma-Separated Values* — verdier skilt med komma.

Et lite datasett kan se slik ut:

```text
måned,kwh
januar,820
februar,760
mars,640
```

Første rad er **overskriften** (*header*). Den forteller hva kolonnene betyr. De neste radene inneholder data.

Her har hver rad to felt:

- `måned` — navnet på måneden
- `kwh` — et strømforbruk

## CSV er fortsatt tekst

En CSV-fil er ikke et spesielt regnearkformat. Den er en vanlig tekstfil med en avtalt struktur. Det betyr at du kan åpne den i en teksteditor og se innholdet selv.

Regnearkprogrammer kan også åpne CSV-filer, men vi trenger ikke et regneark for å arbeide med dem i Python.

## Skilletegnet

Komma er vanlig, men CSV-filer kan også bruke andre skilletegn, for eksempel semikolon. Derfor er det viktig å vite hvordan filen du arbeider med faktisk er bygget opp.

I kurset starter vi med komma, slik at strukturen er lett å se.

## Prøv det

Eksempelfilen `examples/m09/energy.csv` inneholder:

```text
month,kwh
January,820
February,760
March,640
April,510
```

Det første programmet leser foreløpig filen som vanlig tekst:

```python
from pathlib import Path

path = Path(__file__).with_name("energy.csv")

with open(path, "r", encoding="utf-8") as file:
    print(file.read())
```

Kjør `examples/m09/show_csv.py`.

Poenget er å se at CSV bygger direkte på det du allerede kan om filer. I neste leksjon bruker vi Pythons `csv`-modul til å forstå radene og kolonnene.

## Endre det

Åpne `energy.csv` og legg til en ny rad:

```text
May,430
```

Kjør programmet igjen. Den nye raden skal vises.

## Lag det selv

Lag en liten CSV-fil med tre kolonner som passer til noe du vil registrere. Eksempler kan være dato, temperatur og sted — eller tittel, forfatter og år.

Du trenger ikke skrive Python-kode som tolker filen ennå. Målet er å kunne kjenne igjen:

1. overskriften
2. radene
3. kolonnene
4. skilletegnet

### Husk

CSV er enkel tekst med struktur. Før vi analyserer data med Python, skal vi forstå selve filformatet.
