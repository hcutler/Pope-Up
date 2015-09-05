from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/issues")
def issues():
	return render_template("issues.html")

if __name__ == "__main__":
    app.run(debug=True)
