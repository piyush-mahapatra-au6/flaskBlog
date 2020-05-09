from flask import Flask, render_template
app = Flask(__name__)

posts = [{
    'author': "piyush Mahapatra",
    'title': "Best developer in Town",
    'date_posted': "may9th ,2020 "
},
{
    'author': "Neharika",
    'title': "Best dental student in Town",
    'date_posted': "may9th ,2020 "
}]
@app.route("/")
def hello():
    return render_template('home.html',posts = posts)


@app.route("/about")
def about():
    return render_template('about.html',title = "title")

# to avoid setting env and flask run command
if __name__ == "__main__":
    app.run(debug=True)