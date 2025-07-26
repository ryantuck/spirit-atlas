import json
import jinja2


template_body = open('source/crop.html').read()
img_srcs = [f'./../books/1984/{i+1}.jpeg' for i in range(4)]
crops = [jinja2.Template(template_body).render(src=src) for src in img_srcs]
print(json.dumps({'crops': crops}))
