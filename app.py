from flask import Flask, render_template, request
from form import IssuesForm, UserDataForm

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
	form = IssuesForm()
	if form.validate_on_submit():
		return redirect('/issues')
	return render_template("home.html", form=form)

@app.route("/issues", methods=['GET', 'POST'])
def issues():
	return render_template("issues.html", form=request.form)

if __name__ == "__main__":
    app.run(debug=True)
