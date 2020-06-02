# from flask import Flask, render_template
from top5_artists import app,routes
# app = Flask(__name__)
# #index route so no 404
# @app.route("/")
# def base():
#     return render_template('base.html')
if __name__ == "__main__":
    app.run(debug = True)