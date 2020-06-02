from flask import Flask, render_template
from top5_artists import app,routes
#index route so no 404
#top5 route
@app.route('/home', methods=['GET','POST'])
def top5():
    item_dict = {1:"Wolfgang Amadeus Mozart", 2:"Ludwig van Beethoven", 3:"Johann Sebastian Bach",4:"Frédéric François Chopin",5:"Claude Debussy"}
    return render_template("top5.html", item_dict=item_dict)

# home Route
@app.route("/")
def home():
    home = "You are home:)"
    return render_template('home.html')
