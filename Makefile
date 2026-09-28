.PHONY: check examples web epub kindle pdf books

check: examples
	python3 tools/check_content.py

examples:
	python3 tools/check_examples.py

web:
	@echo "M0 web target: shared-source pipeline scaffold ready"

epub:
	@echo "M0 EPUB target: shared-source pipeline scaffold ready"

kindle: epub
	@echo "M0 Kindle profile: validate the EPUB-derived Kindle edition"

pdf:
	@echo "M0 PDF target: print-quality pipeline scaffold ready"

books: epub kindle pdf
