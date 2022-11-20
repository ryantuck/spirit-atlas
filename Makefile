all : targets

# ___controls___________________________________

.PHONY : clean setup

clean :
	rm -r target

setup :
	mkdir -p target
	mkdir -p target/pages

restart : clean setup

# ___sheet.html_______________________________

targets : target/sheet.html

target/sheet.html : html cmd md css pages
	cat source/sheet-section-1.html > $@
	cat target/pages/page-1.html | python md2html.py >> $@
	cat source/sheet-section-3.html >> $@
	cat target/pages/page-2.html | python md2html.py >> $@
	cat source/sheet-section-5.html >> $@

cmd : md2html.py
md : table-of-contents.md cover.md
html : source/sheet-section-1.html source/sheet-section-3.html source/sheet-section-5.html
pages : target/pages/page-1.html target/pages/page-2.html
css : target/sheet.css

target/sheet.css : source/sheet.css
	cp $< $@

target/pages/page-1.html : cover.md
	cat cover.md | python md2html.py > $@

target/pages/page-2.html : table-of-contents.md
	cat table-of-contents.md | python md2html.py > $@
