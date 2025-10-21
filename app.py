from flask import Flask, request, redirect, render_template_string
import json, os

app = Flask(__name__)
DATA_FILE = "jedinjenja.json"

def ucitaj():
    if not os.path.exists(DATA_FILE): return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def sacuvaj(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

HTML_TEMPLATE = open("index.html", encoding="utf-8").read()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        naziv = request.form["naziv"]
        formula = request.form["formula"]
        drugi = request.form.get("drugi", "")
        if naziv and formula:
            jedinjenja = ucitaj()
            jedinjenja.append({"naziv": naziv, "formula": formula, "drugi_naziv": drugi})
            sacuvaj(jedinjenja)
        return redirect("/")
    return render_template_string(HTML_TEMPLATE, jedinjenja=ucitaj())

if __name__ == "__main__":
    app.run()
