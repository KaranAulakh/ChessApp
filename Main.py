from flask import Flask, render_template, jsonify, request
from game.gameState import GameState


app = Flask(__name__)
gameState = GameState()


@app.route('/')
def index():
    return render_template('chessboard.html')

# Takes Argument move which is the previous move in chess notation, or Start to initalize the game
@app.route('/piece-positions')
def piece_positions():
    move = request.args.get('move', 'Start')
    positions = gameState.generate_piece_positions(move)
    return jsonify(positions)

if __name__ == '__main__':
    app.run(debug=True)
