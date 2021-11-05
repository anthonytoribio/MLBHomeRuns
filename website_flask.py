#website_flask.py
#creators: Anthony Toribio and Robert Toribio
#date: 10/29/2021

from flask import Flask, render_template, request, url_for
from retrieve_images import getImage_url
import getHrs
from datetime import date



app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    index_list = 0
    game_ids = getHrs.getGames(date.today().strftime("%m/%d/2021"))
    #game_ids = getHrs.getGames("11/02/2021")
    all_homeruns = getHrs.getTodaysHr(game_ids)
    total_homeruns = getHrs.totalhrsToday(all_homeruns)
    [player.append(getImage_url(player[0]+ " " + player[2])) for player in all_homeruns]
    return render_template('index.html', totalHrs = total_homeruns, hrsList = all_homeruns, index = index_list, size = len(all_homeruns))




if __name__=="__main__":
    app.run(debug=True)
