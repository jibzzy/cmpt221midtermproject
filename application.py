from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/action.php")
def "/action.php"():
    return render_template("project.html")