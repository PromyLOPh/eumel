BUILDDIR=_build
STATICFILES=01_readme_INSTALL.txt releases.svg eumel_logo.svg

all: $(BUILDDIR)/index.html links

$(BUILDDIR):
	mkdir -p $(BUILDDIR)

$(BUILDDIR)/index.ttl: $(glob ttl/*.ttl) | $(BUILDDIR)
	cat ttl/* > $@

$(BUILDDIR)/bib.rst: $(BUILDDIR)/index.ttl tools/formatRefs.py | $(BUILDDIR)
	cat $(BUILDDIR)/index.ttl | ./tools/formatRefs.py https://6xq.net/eumel/ | sort -n > $(BUILDDIR)/bib.rst

$(BUILDDIR)/software.html: $(BUILDDIR)/index.ttl tools/formatSoftware.py
	cat $(BUILDDIR)/index.ttl | ./tools/formatSoftware.py > $@

$(BUILDDIR)/index.html: $(BUILDDIR)/software.html $(BUILDDIR)/bib.rst history.rst artifacts.rst popularity.rst hardware.rst internals.rst index.rst software.rst about.rst trivia.rst quickstart.rst overview.rst
	rst2html5.py --cloak-email-addresses --math-output=mathjax \
		--syntax-highlight=short --link-stylesheet \
		--stylesheet=../style.min.css \
		--template=./template.txt \
		--footnote-references=superscript < index.rst > $@

links: $(STATICFILES) | $(BUILDDIR)
	ln -f $(STATICFILES) $(BUILDDIR)

.PHONY: clean

clean:
	$(RM) -r $(BUILDDIR)

