import yaml
import os

def main():
    file = 'words_2.yaml'
    with open(file) as fh:
        words = yaml.safe_load(fh)
    with open('templates/header.html') as fh:
        header = fh.read()
    with open('templates/footer.html') as fh:
        footer = fh.read()

    html = """
      <table class="table is-striped is-hoverable">
      <thead>
        <tr><th>Latin</th><th>Rashi</th><th>Square</th></tr>
      </thead>
      """

    for word in words:
        html += f"""<tr><td><a href="https://kantoniko.com/words/ladino/{word['latin']}">{word['latin']}</a></td><td class="rashi" dir="rtl">{word['hebrew']}</td><td dir="rtl">{word['hebrew']}</td></tr>\n"""
    html += "</table>\n"


    os.makedirs("_site", exist_ok=True)
    with open("_site/index.html", "w") as fh:
        fh.write(header)
        fh.write(html)
        fh.write(footer)

main()
