from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def fizzbuzz(number_range):
    while number_range != 100:
        print(number_range)
        number_range += 1
        
    return render_template("fizzbuzz.html", number_range=number_range)

if __name__ == '__main__':
    app.run(debug=True)