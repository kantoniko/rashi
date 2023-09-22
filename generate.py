import yaml
import os


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

def main():
    with open('templates/header.html') as fh:
        header = fh.read()
    with open('templates/footer.html') as fh:
        footer = fh.read()


    buttons = ""
    for letter in letters:
        buttons += f"""<button class="button letter rashi">{letter}</button>"""
    footer = footer.replace("BUTTONS", buttons)

    os.makedirs("_site", exist_ok=True)
    with open("_site/index.html", "w") as fh:
        fh.write(header)
        #html = create_table()
        #fh.write(html)
        fh.write(footer)

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

main()
