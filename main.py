from flask import Flask,render_template
import pandas as zx


web = Flask(__name__)
stations = zx.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@web.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@web.route("/ap1/ver1/<stn>/<date>")
def about(stn, date):
    data = zx.read_csv("data_small/TG_STAID" + str(stn).zfill(6) + ".txt", skiprows=20,
                       parse_dates=["    DATE"])
    temp = data.loc[data['    DATE'] == date]['   TG'].squeeze() / 10
    return {"Station": stn,
            "Date": date,
            "Temperature": temp}


if __name__ == "__main__":
    web.run(debug=True)


