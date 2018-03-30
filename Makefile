BUILDDIR:=_build
STATICFILES:=assets/01_readme_INSTALL.txt \
		assets/releases.svg \
		assets/eumel_logo.svg \
		assets/eumel_logo_2.svg \
		assets/eumel-tagung-84.jpg
TTLFILES:=$(shell find ttl -name '*.ttl' | sort)

all: $(BUILDDIR)/index.html $(BUILDDIR)/assets/eumel-tagung-84-resized.jpg links

$(BUILDDIR):
	mkdir -p $(BUILDDIR)

$(BUILDDIR)/assets:
	mkdir -p $@

$(BUILDDIR)/index.ttl: $(TTLFILES) | $(BUILDDIR)
	cat $(TTLFILES) > $@

$(BUILDDIR)/bib.rst: $(BUILDDIR)/index.ttl tools/formatRefs.py | $(BUILDDIR)
	cat $(BUILDDIR)/index.ttl | ./tools/formatRefs.py https://6xq.net/eumel/ | sort -n > $(BUILDDIR)/bib.rst

$(BUILDDIR)/software.html: $(BUILDDIR)/index.ttl tools/formatSoftware.py
	cat $(BUILDDIR)/index.ttl | ./tools/formatSoftware.py > $@

$(BUILDDIR)/assets/eumel-tagung-84-resized.jpg: assets/eumel-tagung-84.jpg | $(BUILDDIR)/assets
	convert -scale 1000x $< -quality 75 $@

$(BUILDDIR)/index.html: $(BUILDDIR)/software.html $(BUILDDIR)/bib.rst history.rst artifacts.rst popularity.rst hardware.rst internals.rst index.rst software.rst about.rst trivia.rst quickstart.rst overview.rst
	rst2html5.py --cloak-email-addresses --math-output=mathjax \
		--syntax-highlight=short --link-stylesheet \
		--stylesheet=../style.min.css \
		--template=./template.txt \
		--footnote-references=superscript < index.rst > $@

links: $(STATICFILES) | $(BUILDDIR)/assets
	ln -f $(STATICFILES) $(BUILDDIR)/assets

.PHONY: clean links

clean:
	$(RM) -r $(BUILDDIR)

