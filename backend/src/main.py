from flask import Flask, jsonify
from flask_cors import CORS
from gameplay.gameState import GameState

app = Flask(__name__)
app.config.from_object(__name__)
gameState = GameState()

CORS(app, resources={r"/*":{'origins': '*'}})
# maybe define to localhost 8080 with allow_header: access-control-allow-origin

# test
@app.route('/', methods=['GET'])
def test():
  return ("Home page incoming")

@app.route('/play', methods=['GET'])
def play():
  return ("Let's play chess")

@app.route('/get-start-positions')
def get_start_position():
    return jsonify(gameState.get_start_position())

@app.route('/get-possible-moves')
def get_possible_moves():
    from flask import request
    square = request.args.get('square')
    if not square:
        return jsonify({"error": "Square parameter is required"}), 400
    
    # Check if there's a piece at this square
    if square not in gameState.piece_positions:
        return jsonify([])
    
    possible_moves = gameState.get_legal_moves(square)
    return jsonify(possible_moves)

@app.route('/make-move', methods=['POST'])
def make_move():
    from flask import request
    data = request.json
    start_square = data.get('start')
    end_square = data.get('end')
    
    if not start_square or not end_square:
        return jsonify({"error": "Both start and end squares are required"}), 400
    
    try:
        result = gameState.move(start_square, end_square)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get-piece-positions')
def get_piece_positions():
    from flask import request
    move = request.args.get('move')
    
    if move == 'start':
        return jsonify(gameState.get_start_position())
    else:
        # Return current positions
        return jsonify(gameState.get_serialized_piece_positions())

if __name__ == "__main__":
  app.run(debug=True, port=5001)