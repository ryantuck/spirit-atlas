import json

import jinja2


def main():
    template_body = open('source/template.html').read()

#    sheets = [
#        ('cover', 'table-of-contents'),
#        ('dag', 'mandelbrot-set'),
#    ]

    sheet_1 = jinja2.Template(template_body).render(page_1=open('target/pages/page-1.html').read(),page_2=open('target/pages/page-2.html').read())

    sheet_2 = jinja2.Template(template_body).render(page_1=open('target/pages/page-3.html').read(),page_2=open('target/pages/page-4.html').read())

    print(json.dumps({'sheets': [sheet_1, sheet_2]}))


main()
