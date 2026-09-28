# Kindle-profil

EduPython-Senior bruker EPUB som kildeformat for Kindle-leveransen. Vi vedlikeholder ikke en separat MOBI-kopi av kursinnholdet.

## M0-krav

Kindle-profilen skal kontrollere at:

- EPUB-filen finnes og ikke er tom
- EPUB-pakken har korrekt `mimetype`
- `META-INF/container.xml` finnes
- pakken inneholder lesbart HTML/XHTML-innhold
- innholdet er det samme kursinnholdet som brukes for web, EPUB og PDF
- layouten er reflowable og ikke avhengig av faste skjermmål
- informasjon ikke er avhengig av farge alene
- kodeblokker kan brytes/vises uten fast sidebredde

`make kindle` kjører Kindle-profilen mot både norsk og engelsk EPUB.

Dette er en teknisk M0-gate. Visuell testing på faktiske Kindle-enheter eller Amazons aktuelle preview-verktøy inngår i senere release-QA når en full bokutgave foreligger.
