import yaml
import os
import glob

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

    render(template="editor.html", filename="index.html", buttons=buttons)

    for filename in glob.glob("words-*.yaml"):
        name = filename[0:-5]
        with open(filename) as fh:
            words = yaml.safe_load(fh)
        render(template="words.html", filename=f"{name}.html", words=words)


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
