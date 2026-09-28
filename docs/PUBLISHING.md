# Publisering / Publishing

EduPython-Senior bruker én felles kursbase med norsk som hovedspråk og engelsk som fullverdig sidestilt språk.

## Førsteklasses mål

1. Web
2. EPUB
3. Kindle
4. PDF

Kindle behandles som en egen leveranse- og QA-profil over EPUB, ikke som en separat innholdskilde. PDF skal være en reell bokutgave for skjerm og utskrift, ikke bare en nettleserutskrift.

## M0-regler

- Alle Python-eksempler skal kunne kjøres i CI.
- Norsk og engelsk innholdsstruktur skal valideres.
- Ingen publiseringsvariant skal kreve en separat kopi av selve kursinnholdet.
- E-ink og gråtone skal tas hensyn til i figurer og layout.
- Web-spesifikke instruksjoner må ha et meningsfullt alternativ i bokformatene.

## Build-grensesnitt

```sh
make check
make web
make epub
make kindle
make pdf
make books
```

M0 etablerer og kvalifiserer dette grensesnittet. Senere milepæler fyller målene med den valgte produksjonsverktøykjeden.
