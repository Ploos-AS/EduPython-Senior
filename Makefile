PANDOC ?= pandoc
PYTHON ?= python3
DIST ?= dist

NO_INPUTS = $(shell $(PYTHON) tools/book_inputs.py no)
EN_INPUTS = $(shell $(PYTHON) tools/book_inputs.py en)

.PHONY: check examples web epub kindle pdf books clean

check: examples
	$(PYTHON) tools/check_content.py
	$(PYTHON) tools/book_inputs.py no >/dev/null
	$(PYTHON) tools/book_inputs.py en >/dev/null

examples:
	$(PYTHON) tools/check_examples.py

web:
	@echo "Web renderer is the next M0 publishing target"

epub: $(DIST)/EduPython-Senior-NO.epub $(DIST)/EduPython-Senior-EN.epub

$(DIST)/EduPython-Senior-NO.epub: $(NO_INPUTS) book/no.yaml book/epub.css
	mkdir -p $(DIST)
	$(PANDOC) --metadata-file=book/no.yaml --css=book/epub.css --toc -o $@ $(NO_INPUTS)

$(DIST)/EduPython-Senior-EN.epub: $(EN_INPUTS) book/en.yaml book/epub.css
	mkdir -p $(DIST)
	$(PANDOC) --metadata-file=book/en.yaml --css=book/epub.css --toc -o $@ $(EN_INPUTS)

kindle: epub
	@echo "Kindle profile uses the generated EPUB files; Kindle-specific validation follows in M0."

pdf: $(DIST)/EduPython-Senior-NO.pdf $(DIST)/EduPython-Senior-EN.pdf

$(DIST)/EduPython-Senior-NO.pdf: $(NO_INPUTS) book/no.yaml
	mkdir -p $(DIST)
	$(PANDOC) --metadata-file=book/no.yaml --toc --pdf-engine=xelatex -V papersize:a4 -V geometry:margin=25mm -V fontsize=12pt -V linestretch=1.15 -o $@ $(NO_INPUTS)

$(DIST)/EduPython-Senior-EN.pdf: $(EN_INPUTS) book/en.yaml
	mkdir -p $(DIST)
	$(PANDOC) --metadata-file=book/en.yaml --toc --pdf-engine=xelatex -V papersize:a4 -V geometry:margin=25mm -V fontsize=12pt -V linestretch=1.15 -o $@ $(EN_INPUTS)

books: epub kindle pdf

clean:
	rm -rf $(DIST)
