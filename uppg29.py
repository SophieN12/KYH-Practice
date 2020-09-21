import webbrowser
import requests
from pathlib import Path

r = requests.get('https://api.adviceslip.com/advice')
data = r.json()
dict = data["slip"]
value = dict['advice']

content = Path("uppg29_template.html").read_text()
s = content.replace('QUOTE_TEXT', value)
p = Path('goat_quote.html')
p.write_text(s, encoding="utf8")

webbrowser.open('goat_quote.html')




