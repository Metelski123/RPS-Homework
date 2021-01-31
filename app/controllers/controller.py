from app import app
from flask import render_template
from app.models.game import Game
from app.models.player import Player

# @app.route('/')
# def index():
#     return "Rock Paper Scissors"

@app.route('/<name1>/<choice1>/<name2>/<choice2>')
def rpsgame(name1, choice1, name2, choice2):
    player1 = Player(name1, choice1)
    player2 = Player(name2, choice2)
    game = Game(player1, player2)
    result = game.rps(player1, player2)
    return render_template('index.html', rpsresult = result)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')