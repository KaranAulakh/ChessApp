from flask import Flask, render_template, jsonify, request
from game.GameState import GameState


app = Flask(__name__)
gameState = GameState()


@app.route('/')
def index():
    return render_template('chessboard.html')

@app.route('/get-start-position')
def get_start_position():
    return jsonify(gameState.get_start_position())
    
@app.route('/get-possible-moves')
def get_possible_moves():
    square = request.args.get('square', 'None')
    return jsonify(gameState.find_moves(square))

@app.route('/move')
def move():
    start_square = request.args.get('start', 'None')
    destination_square = request.args.get('destination', 'None')
    return jsonify(gameState.move(start_square, destination_square))

if __name__ == '__main__':
    #app.run()
    app.run(debug=True)


'''
    Current bugs
        if there are no possible moves for a piece, you get undefined passed of off null
        not falsing is_first_move
'''
