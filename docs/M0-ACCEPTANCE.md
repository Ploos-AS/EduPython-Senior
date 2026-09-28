# M0 Acceptance Report

Dato: 2026-09-28

## Resultat

M0-grunnarkitekturen er operativ og den samlede publiseringskjeden er kvalifisert i GitHub Actions.

Kvalifisert CI-run: 36364570396.

## Verifisert

- [x] Norsk er hovedspråk.
- [x] Engelsk er en fullverdig sidestilt utgave.
- [x] Kurset forutsetter ingen tidligere programmeringserfaring.
- [x] Første norske og engelske leksjon finnes.
- [x] Python-eksempler kjøres automatisk.
- [x] Web bygges fra felles kurskilder.
- [x] EPUB bygges for norsk og engelsk.
- [x] Kindle-profil validerer begge EPUB-utgavene.
- [x] PDF bygges for norsk og engelsk som bokutgave.
- [x] Alle fire leveranseformer inngår i samme CI-kjede.
- [x] Programvare og kursinnhold har eksplisitt lisensdeling.
- [x] MIT brukes for programvare/kjørbare eksempler.
- [x] CC BY 4.0 brukes for kursinnhold og dokumentasjon.

## Fortsatt M0-arbeid

- [ ] sterkere link/content-validering
- [ ] EPUBCheck eller tilsvarende standardvalidering
- [ ] eksplisitt accessibility/readability policy og automatiserbare kontroller
- [ ] kvalifisere siste lisensendringer i CI
- [ ] oppdatere ROADMAP/Issue #1 når alle gates er grønne

## Konklusjon

Publiseringsarkitekturen er kvalifisert: Web, EPUB, Kindle-profil og PDF fungerer fra den delte tospråklige kursbasen. M0 lukkes først når de gjenværende kvalitetsgatene over er implementert og grønne.
