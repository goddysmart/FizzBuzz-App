from flask import Flask, render_template 

app = Flask(__name__)

@app.get("/")
def index(number_range):
    while number_range != 100:
        number_range += 1
    return render_template("fizzbuzz.html", number_range=number_range)


if __name__ == '__main__':
    app.run(debug=True)