import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')


class Djur:
    def __init__(self, name, carnivore, wiki_url):
        self.name = name
        self.carnivore = carnivore
        self.wiki_url = wiki_url

    def carnivore_or_vegetarian(self):
        if self.carnivore:
            return "Köttätare"
        else:
            return "Vegetarian"

    def get_html_table_row(self, html):
        html += f'<tr><td><a href="{self.wiki_url}">{self.name}</a></td><td>{self.carnivore_or_vegetarian()}</td></tr>\n'
        return html


if __name__ == '__main__':
    djur = []
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    giraff = Djur('Giraff', False, 'https://sv.wikipedia.org/wiki/Giraff')
    jaguar = Djur('Jaguar', True, 'https://sv.wikipedia.org/wiki/Jaguar')
    panda = Djur('Panda', False, 'https://en.wikipedia.org/wiki/Giant_panda')
    djur.append(zebra)
    djur.append(tiger)
    djur.append(giraff)
    djur.append(jaguar)
    djur.append(panda)
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Djur!</title>
</head>
<body>

<table>"""

    for d in djur:
        html = d.get_html_table_row(html)

    html += '</table></body></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))
