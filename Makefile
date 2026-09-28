PANDOC ?= pandoc
PYTHON ?= python3
DIST ?= dist

NO_INPUTS = $(shell $(PYTHON) tools/book_inputs.py no)
EN_INPUTS = $(shell $(PYTHON) tools/book_inputs.py en)

.PHONY: check examples web epub kindle pdf books clean

check: examples
	$(PYTHON) tools/check_content.py
	$(PYTHON) tools/check_accessibility.py
	$(PYTHON) tools/check_links.py
	$(PYTHON) tools/book_inputs.py no >/dev/null
	$(PYTHON) tools/book_inputs.py en >/dev/null

examples:
	$(PYTHON) tools/check_examples.py

web: $(DIST)/web/no/index.html $(DIST)/web/en/index.html

$(DIST)/web/no/index.html: $(NO_INPUTS) book/no.yaml web/template.html web/style.css
	mkdir -p $(DIST)/web/no $(DIST)/web/en
	cp web/style.css $(DIST)/web/style.css
	$(PANDOC) --metadata-file=book/no.yaml --template=web/template.html --standalone -o $@ $(NO_INPUTS)

$(DIST)/web/en/index.html: $(EN_INPUTS) book/en.yaml web/template.html web/style.css
	mkdir -p $(DIST)/web/no $(DIST)/web/en
	cp web/style.css $(DIST)/web/style.css
	$(PANDOC) --metadata-file=book/en.yaml --template=web/template.html --standalone -o $@ $(EN_INPUTS)

epub: $(DIST)/EduPython-Senior-NO.epub $(DIST)/EduPython-Senior-EN.epub

$(DIST)/EduPython-Senior-NO.epub: $(NO_INPUTS) book/no.yaml book/epub.css
	mkdir -p $(DIST)
	$(PANDOC) --metadata-file=book/no.yaml --css=book/epub.css --toc -o $@ $(NO_INPUTS)

$(DIST)/EduPython-Senior-EN.epub: $(EN_INPUTS) book/en.yaml book/epub.css
	mkdir -p $(DIST)
	$(PANDOC) --metadata-file=book/en.yaml --css=book/epub.css --toc -o $@ $(EN_INPUTS)

kindle: epub
	$(PYTHON) tools/check_kindle.py $(DIST)/EduPython-Senior-NO.epub $(DIST)/EduPython-Senior-EN.epub

pdf: $(DIST)/EduPython-Senior-NO.pdf $(DIST)/EduPython-Senior-EN.pdf

$(DIST)/EduPython-Senior-NO.pdf: $(NO_INPUTS) book/no.yaml
	mkdir -p $(DIST)
	$(PANDOC) --metadata-file=book/no.yaml --toc --pdf-engine=xelatex -V papersize:a4 -V geometry:margin=25mm -V fontsize=12pt -V linestretch=1.15 -V mainfont="DejaVu Serif" -V monofont="DejaVu Sans Mono" -o $@ $(NO_INPUTS)

$(DIST)/EduPython-Senior-EN.pdf: $(EN_INPUTS) book/en.yaml
	mkdir -p $(DIST)
	$(PANDOC) --metadata-file=book/en.yaml --toc --pdf-engine=xelatex -V papersize:a4 -V geometry:margin=25mm -V fontsize=12pt -V linestretch=1.15 -V mainfont="DejaVu Serif" -V monofont="DejaVu Sans Mono" -o $@ $(EN_INPUTS)

books: epub kindle pdf

clean:
	rm -rf $(DIST)
