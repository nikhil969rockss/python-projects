from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

# If you have data which keep on adding data day by you could read the data
# inside the route(def) as well
# in this case since .txt files are according STAID, have to call df
# inside the route

# Reading station.txt for documentation purposes

stations_df = pd.read_csv("data_small/stations.txt", skiprows=17)
stations_df["STANAME"] = stations_df['STANAME                                 ']
stations_df = stations_df[['STAID','STANAME']]

@app.route("/")
def home():
    return render_template("index.html", data=stations_df.to_html())


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/api/v1/<station>/<date>")
def api(station, date):

    df = pd.read_csv("data_small/TG_STAID"+station.zfill(6) +".txt",
                     skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    df2= pd.read_csv("data_small/stations.txt",skiprows=17)

    STANAME = 'STANAME                                 '

    station_name = df2.loc[df2['STAID'] == int(station)][STANAME].squeeze().strip()
    print(station_name)

    weather_json = {"station_code":station,"station_name":station_name,
                    "date": date, "temperature":temperature}
    return weather_json


if __name__ == "__main__":
    app.run(debug=True,)
    # if your port is occupied you can specify the port=5001 or whatever