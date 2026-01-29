from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    temperature=20
    weather_json = {"station":station, "date": date, "temperature":temperature}
    return weather_json


if __name__ == "__main__":
    app.run(debug=True,)
    # if your port is occupied you can specify the port=5001 or whatever