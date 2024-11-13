SOURCES=sources/Cormorant.glyphs sources/Cormorant-Italic.glyphs sources/CormorantUpright.glyphs
FAMILY=Cormorant

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontbakery"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo

build: build.stamp

venv: venv/touchfile

venv-test: venv-test/touchfile

sources/generated/CormorantInfant.glyphs: sources/Cormorant.glyphs venv
	. venv/bin/activate; babelfont $< --filter 'applyCustomParameters:instance=Cormorant Infant Regular' --filter 'dropUnexportedGlyphs:force=true' $@

sources/generated/CormorantInfant-Italic.glyphs: sources/Cormorant-Italic.glyphs venv
	. venv/bin/activate; babelfont $< --filter 'applyCustomParameters:instance=Cormorant Infant Italic' --filter 'dropUnexportedGlyphs:force=true' $@

sources/generated/CormorantGaramond.glyphs: sources/Cormorant.glyphs venv
	. venv/bin/activate; babelfont $< --filter 'applyCustomParameters:instance=Cormorant Garamond Regular' --filter 'dropUnexportedGlyphs:force=true' $@

sources/generated/CormorantGaramond-Italic.glyphs: sources/Cormorant-Italic.glyphs venv
	. venv/bin/activate; babelfont $< --filter 'applyCustomParameters:instance=Cormorant Garamond Italic' --filter 'dropUnexportedGlyphs:force=true' $@

sources/generated/CormorantUnicase.glyphs: sources/Cormorant.glyphs venv
	. venv/bin/activate; babelfont $< --filter 'applyCustomParameters:instance=Cormorant Unicase Regular' --filter 'dropUnexportedGlyphs:force=true' $@

GENERATED_SOURCES=sources/generated/CormorantInfant.glyphs sources/generated/CormorantInfant-Italic.glyphs sources/generated/CormorantGaramond.glyphs sources/generated/CormorantGaramond-Italic.glyphs sources/generated/CormorantUnicase.glyphs

customize: venv
	. venv/bin/activate; python3 scripts/customize.py

build.stamp: venv $(wildcard sources/config*.yaml) $(SOURCES) $(GENERATED_SOURCES)
	(for config in sources/config*.yaml; do . venv/bin/activate; gftools builder $$config || exit 1; done)  && touch build.stamp

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

venv-test/touchfile: requirements-test.txt
	test -d venv-test || python3 -m venv venv-test
	. venv-test/bin/activate; pip install -Ur requirements-test.txt
	touch venv-test/touchfile

test: venv-test build.stamp
	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; . venv-test/bin/activate; mkdir -p out/ out/fontbakery; fontbakery check-googlefonts -l WARN --full-lists --succinct --badges out/badges --html out/fontbakery/fontbakery-report.html --ghmarkdown out/fontbakery/fontbakery-report.md $$TOCHECK  || echo '::warning file=sources/config.yaml,title=Fontbakery failures::The fontbakery QA check reported errors in your font. Please check the generated report.'

proof: venv build.stamp
	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; . venv/bin/activate; mkdir -p out/ out/proof; diffenator2 proof $$TOCHECK -o out/proof

images: venv $(DRAWBOT_OUTPUT)

%.png: %.py build.stamp
	. venv/bin/activate; python3 $< --output $@

clean:
	rm -rf venv
	find . -name "*.pyc" -delete

update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/

update: venv venv-test
	venv/bin/pip install --upgrade pip-tools
	# See https://pip-tools.readthedocs.io/en/latest/#a-note-on-resolvers for
	# the `--resolver` flag below.
	venv/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements.in
	venv/bin/pip-sync requirements.txt

	venv-test/bin/pip install --upgrade pip-tools
	venv-test/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements-test.in
	venv-test/bin/pip-sync requirements-test.txt

	git commit -m "Update requirements" requirements.txt requirements-test.txt
	git push
