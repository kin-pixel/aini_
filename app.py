from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():
    return render_template('Home.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/about")
def about():
    return render_template('About.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)
