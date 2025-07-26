all : sheets

# ___controls___________________________________

.PHONY : clean setup

clean :
	rm -r target

setup :
	mkdir -p target
	mkdir -p target/pages
	mkdir -p target/sheets
	mkdir -p target/books/1984
	mkdir -p target/crops

restart : clean setup

# ___books___________________________________

BOOKS_DIR := ~/Desktop/books

1984 : target/books/1984/1.jpeg target/books/1984/2.jpeg target/books/1984/3.jpeg target/books/1984/4.jpeg

1984-setup :
	cp $(BOOKS_DIR)/1984/1984\ -\ 10.jpeg target/books/1984/1.jpeg
	cp $(BOOKS_DIR)/1984/1984\ -\ 20.jpeg target/books/1984/2.jpeg
	cp $(BOOKS_DIR)/1984/1984\ -\ 30.jpeg target/books/1984/3.jpeg
	cp $(BOOKS_DIR)/1984/1984\ -\ 40.jpeg target/books/1984/4.jpeg


# ___sheets_______________________________

css : target/sheet.css

target/sheet.css : source/sheet.css
	cp $< $@

sheets : target/sheets/sheet-0.html target/sheets/sheet-1.html target/sheets/sheet-2.html target/sheets/sheet-3.html

target/sheets/sheet-0.html : css pages render_sheets.py
	python render_sheets.py | jq '.sheets[0]' -r > $@

target/sheets/sheet-1.html : css pages render_sheets.py
	python render_sheets.py | jq '.sheets[1]' -r > $@

target/sheets/sheet-2.html : css pages render_sheets.py
	python render_sheets.py | jq '.sheets[2]' -r > $@

target/sheets/sheet-3.html : css pages render_sheets.py
	python render_sheets.py | jq '.sheets[3]' -r > $@

pages : target/pages/page-1.html target/pages/page-2.html target/pages/page-3.html target/pages/page-4.html target/pages/page-5.html target/pages/page-6.html target/pages/page-7.html target/pages/page-8.html

target/pages/page-1.html : source/cover.md
	cat $< | python md2html.py > $@

target/pages/page-2.html : source/table-of-contents.md
	cat $< | python md2html.py > $@

target/pages/page-3.html : source/dag.md target/dag.svg
	cat $< | python md2html.py > $@

target/pages/page-4.html : source/mandelbrot-set.md
	cat $< | python md2html.py > $@

target/pages/page-5.html : target/crops/crop-0.html
	cat $< > $@

target/pages/page-6.html : target/crops/crop-1.html
	cat $< > $@

target/pages/page-7.html : target/crops/crop-2.html
	cat $< > $@

target/pages/page-8.html : target/crops/crop-3.html
	cat $< > $@

crops : target/crops/crop-0.html target/crops/crop-1.html target/crops/crop-2.html target/crops/crop-3.html

target/crops/crop-0.html : target/books/1984/1.jpeg render_crops.py
	python render_crops.py | jq '.crops[0]' -r > $@

target/crops/crop-1.html : target/books/1984/2.jpeg render_crops.py
	python render_crops.py | jq '.crops[1]' -r > $@

target/crops/crop-2.html : target/books/1984/3.jpeg render_crops.py
	python render_crops.py | jq '.crops[2]' -r > $@

target/crops/crop-3.html : target/books/1984/4.jpeg render_crops.py
	python render_crops.py | jq '.crops[3]' -r > $@


# ___dag___________________________________


target/dag.svg : target/dag.gv
	dot -Tsvg -o $@ $<

target/dag.gv : Makefile make2dag.py
	echo "digraph {" > $@
	echo "rankdir=LR;" >> $@
	echo "bgcolor=transparent;" >> $@
	echo "node [fontname=\"Courier New\", shape=rectangle];" >> $@
	cat Makefile \
		| grep : | grep -v clean | grep -v setup | grep -v := \
		| python make2dag.py | jq '.edges[]' \
		| sed -e 's/\//_/g' | sed -e 's/-/_/g' | sed -e 's/\./_/g' \
		| jq '"\(.source) -> \(.target);"' -r >> $@
	echo "}" >> $@
