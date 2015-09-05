from flask import Flask, render_template
from form import IssuesForm, UserDataForm

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def hello():
	form = IssuesForm()
	return render_template("home.html", form=form)

@app.route("/issues")
def issues():
	return render_template("issues.html")

if __name__ == "__main__":
    app.run(debug=True)
