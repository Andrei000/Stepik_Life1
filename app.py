from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)

@app.route('/')
def index_view():
    GameOfLife(20,20)
    return render_template('index.html')

@app.route('/live/')
def live_view():
    game = GameOfLife()
    if game.counter > 0:
        game.form_new_generation()
    game.next_counter()
    return render_template('live.html',
                           game=game)

if __name__=='__main__':
    app.run(debug=True)