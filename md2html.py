import sys

def html_text(tag, text):
    return f'<{tag}>{text}</{tag}>'

def html_header(markdown_header_line):
    h_num = len(markdown_header_line.split()[0])
    header_text = markdown_header_line.replace('#','').strip()
    tag = f'h{h_num}'
    return html_text(tag, header_text)

def html(markdown_line):
    if line.startswith('#'):
        return html_header(markdown_line)
    if markdown_line == '':
        return None
    if line.strip().startswith('<'):
        return line # assumes html, prob janky
    return html_text('p', markdown_line)


for line in sys.stdin:
    x = html(line.strip())
    if x:
        print(x)
