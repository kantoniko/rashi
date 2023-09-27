import yaml
import os
from jinja2 import Environment, FileSystemLoader


letters = [
    'א',
    'ב',
    'ג',
    'ד',
    'ה',
    'ו',
    'ז',
    'ח',
    'ט',
    'י',
    'כ',
    'ך',
    'ל',
    'מ',
    'ם',
    'נ',
    'ן',
    'ס',
    'ע',
    'פ',
    'ף',
    'צ',
    'ץ',
    'ק',
    'ר',
    'ש',
    'ת',
    'בﬞ',
    'גﬞ',
    'דﬞ',
    'זﬞ',
    'טﬞ',
    'כﬞ',
    'פﬞ',
    'שﬞ',
    ]

html_path = "_site"

def main():

    buttons = ""
    for letter in letters:
        buttons += f"""<button class="button letter rashi">{letter}</button>"""

    render("index.html", "index.html", buttons=buttons)

    #    #html = create_table()
    #    #fh.write(html)

def create_table():
    file = 'words_2.yaml'
    with open(file) as fh:
        words = yaml.safe_load(fh)
    html = """
      <table class="table is-striped is-hoverable">
      <thead>
        <tr><th>Latin</th><th>Rashi</th><th>Square</th></tr>
      </thead>
      """

    for word in words:
        html += f"""<tr><td><a href="https://kantoniko.com/words/ladino/{word['latin']}">{word['latin']}</a></td><td class="rashi" dir="rtl">{word['rashi']}</td><td dir="rtl">{word['rashi']}</td></tr>\n"""
    html += "</table>\n"
    return html

def render(template, filename=None, **args):
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, "templates")
    env = Environment(loader=FileSystemLoader(templates_dir), autoescape=True)
    html_template = env.get_template(template)
    html = html_template.render(**args)

    full_path = os.path.join(html_path, filename)
    dir_path = os.path.dirname(full_path)
    os.makedirs(dir_path, exist_ok=True)

    with open(full_path, "w") as fh:
        fh.write(html)


main()
