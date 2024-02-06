from flask import Flask,render_template

web = Flask(__name__)


@web.route("/")
def home():
    return render_template("home.html")


@web.route("/ap1/ver1/<stn>/<date>")
def about(stn, date):
    temp = 23
    return {"Station": stn,
            "Date": date,
            "Temperature": temp}


if __name__ == "__main__":
    web.run(debug=True)


