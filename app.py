from flask import Flask, render_template, request
import ott_scraping as ott

app = Flask(__name__, template_folder='template')


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/display", methods=["POST"])
def display():
    if request.method == "POST":
        data_select = request.form.get('category')
        data_type = ott.ott(data_select)
        return render_template('output.html', data=data_type)


if __name__ == "__main__":
    app.run(debug=True)
