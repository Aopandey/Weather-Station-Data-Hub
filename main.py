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


@web.route("/ap1/ver1/<stn>")
def all_data(stn):
    data = zx.read_csv("data_small/TG_STAID" + str(stn).zfill(6) + ".txt", skiprows=20,
                       parse_dates=["    DATE"])
    result = data.to_dict(orient="records")
    return result


@web.route("/ap1/ver1/year/<stn>/<year>")
def date_data(stn, year):
    data = zx.read_csv("data_small/TG_STAID" + str(stn).zfill(6) + ".txt", skiprows=20)
    data["    DATE"] = data["    DATE"].astype(str)
    result = data[data["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result

if __name__ == "__main__":
    web.run(debug=True)


