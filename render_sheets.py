import json

import jinja2


template_body = open('source/template.html').read()

sheet_1 = jinja2.Template(template_body).render(
    page_1=open('target/pages/page-1.html').read(),
    page_2=open('target/pages/page-2.html').read(),
)

sheet_2 = jinja2.Template(template_body).render(
    page_1=open('target/pages/page-3.html').read(),
    page_2=open('target/pages/page-4.html').read(),
)

sheet_3 = jinja2.Template(template_body).render(
    page_1=open('target/pages/page-5.html').read(),
    page_2=open('target/pages/page-6.html').read(),
)

sheet_4 = jinja2.Template(template_body).render(
    page_1=open('target/pages/page-7.html').read(),
    page_2=open('target/pages/page-8.html').read(),
)



print(json.dumps({'sheets': [sheet_1, sheet_2, sheet_3,sheet_4]}))
