from flask import Flask, render_template, jsonify, request
from game.GameState import GameState


app = Flask(__name__)
gameState = GameState()


@app.route('/')
def index():
    return render_template('chessboard.html')

# Takes Argument move which is the previous move in chess notation, or 'start' to initalize the game
@app.route('/get-piece-positions')
def get_position():
    move = request.args.get('move', 'start')
    if (move == 'start'):
        return jsonify(gameState.piece_positions)
    else:
        return jsonify(gameState.move(move))


if __name__ == '__main__':
    app.run()
    #app.run(debug=true)
