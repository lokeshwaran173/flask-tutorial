from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    mark_list = [45,75,68,77,95,39]
# name = "Lokesh"
    return render_template("index.html", List=mark_list)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/dept')
def dept():
    return render_template("dept.html")

@app.route('/sports')
def sports():
    return render_template("sports.html")



if __name__ == "__main__":
    app.run(debug=True)
