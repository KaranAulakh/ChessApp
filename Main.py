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
    return jsonify(gameState.get_legal_moves(square))

@app.route('/move')
def move():
    start_square = request.args.get('start', 'None')
    destination_square = request.args.get('destination', 'None')
    return jsonify(gameState.move(start_square, destination_square))

@app.route('/promote-pawn')
def promote_pawn():
    pawn_location = request.args.get('pawnLocation', 'None')
    promote_to = request.args.get('promoteTo', 'None')
    return jsonify(gameState.promote_pawn(pawn_location, promote_to))

if __name__ == '__main__':
    #app.run()
    app.run(debug=True)


''' 
    Next Steps
        validate pawn promotions
        need to implement end game logic, checkmate or draws
        add invalid input safety to methods
        can't castle through check: look up rules
        handle onRefresh
'''
