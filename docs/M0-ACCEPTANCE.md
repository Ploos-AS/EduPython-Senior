# M0 Acceptance Report

Dato: 2026-09-28

## Resultat

**PASS**

M0-grunnarkitekturen er operativ og hele den planlagte kvalitets- og publiseringskjeden er kvalifisert i GitHub Actions.

Endelig kvalifisert CI-run: 36364822613.

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

## Kvalitetsgater

- [x] lokal link/content-validering
- [x] EPUBCheck-standardvalidering
- [x] accessibility/readability-policy
- [x] automatiserbare accessibility-kontroller
- [x] lisensendringer kvalifisert i CI
- [x] samlet sluttkvalifisering

## Konklusjon

M0 er **PASS**. Web, EPUB, Kindle-profil og PDF fungerer fra den delte tospråklige kursbasen, og alle planlagte M0-kvalitetsgater er grønne.
