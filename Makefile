all : sheets

# ___controls___________________________________

.PHONY : clean setup

clean :
	rm -r target

setup :
	mkdir -p target
	mkdir -p target/pages
	mkdir -p target/sheets

restart : clean setup

# ___vars___________________________________

BOOKS_DIR := ~/Desktop/books

# ___sheet.html_______________________________

sheets : target/sheets/sheet-1.html target/sheets/sheet-2.html

target/sheets/sheet-1.html : css pages render_jinja.py
	python render_jinja.py | jq '.sheets[0]' -r > $@

target/sheets/sheet-2.html : css pages render_jinja.py
	python render_jinja.py | jq '.sheets[1]' -r > $@

pages : target/pages/page-1.html target/pages/page-2.html target/pages/page-3.html target/pages/page-4.html

css : target/sheet.css


target/sheet.css : source/sheet.css
	cp $< $@

target/pages/page-1.html : source/cover.md
	cat $< | python md2html.py > $@

target/pages/page-2.html : source/table-of-contents.md
	cat $< | python md2html.py > $@

target/pages/page-3.html : source/dag.md target/dag.svg
	cat $< | python md2html.py > $@

target/pages/page-4.html : source/mandelbrot-set.md
	cat $< | python md2html.py > $@


# ___dag___________________________________


target/dag.svg : target/dag.gv
	dot -Tsvg -o $@ $<

target/dag.gv : Makefile make2dag.py
	echo "digraph {" > $@
	echo "rankdir=LR;" >> $@
	echo "node [fontname=\"Courier New\", shape=rectangle];" >> $@
	cat Makefile \
		| grep : | grep -v clean | grep -v setup | grep -v := \
		| python make2dag.py | jq '.edges[]' \
		| sed -e 's/\//_/g' | sed -e 's/-/_/g' | sed -e 's/\./_/g' \
		| jq '"\(.source) -> \(.target);"' -r >> $@
	echo "}" >> $@
