from flask import Flask, render_template

app = Flask("Weather API")

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/api/v1/<station>/<date>')
def api(station, date):
    weather = 12
    return {
        "Station": station,
        "date": date,
        "weather": str(weather)
    }



if __name__ == "__main__":
    app.run(debug=True)
