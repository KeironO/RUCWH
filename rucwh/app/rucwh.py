from flask import Flask

app = Flask(__name__)

@app.route("/")
def rucwh():
    return render_template("index.html")
