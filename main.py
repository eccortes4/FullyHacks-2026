from flask import Flask, render_template, request

app = Flask("__name__")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/dive')
def dive():
    lat = float(request.args.get("lat"))
    long = float(request.args.get("long"))
    depth = int(request.args.get("depth"))
    creatures = []

    return render_template("divedeeper.html", lat=lat, long=long, dep=depth, creatures=creatures)

if __name__ == "__main__":
    index()
