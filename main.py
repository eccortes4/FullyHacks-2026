from flask import Flask, render_template

app = Flask("__name__")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/dive/<latitude>/<longitude>/<depth>')
def dive(latitude, longitude, depth):
    return render_template("divedeeper.html", lat=latitude, long=longitude, dep=depth)

if __name__ == "__main__":
    index()
