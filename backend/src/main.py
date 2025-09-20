import logging 
from typing import Union, Dict, Any, List
from flask import Flask, jsonify, Response
from flask_cors import CORS

from gameplay.gameState import GameState

app = Flask(__name__)
app.config.from_object(__name__)
gameState = GameState()
logger = logging.getLogger(__name__)

# todo - make CORS restrictions tighter
CORS(app, resources={r"/*":{'origins': '*'}})

# todo - create a valuable home page
@app.route('/', methods=['GET'])
def test() -> str:
  return ("Home page incoming")

@app.route('/play', methods=['GET'])
def play() -> str:
  return ("Let's play chess")

@app.route('/get-start-positions')
def get_start_position() -> Response:
    return jsonify(gameState.get_start_position())

@app.route('/get-possible-moves')
def get_possible_moves() -> Union[Response, tuple[Response, int]]:
    from flask import request
    square = request.args.get('square')
    if not square:
        return jsonify({"error": "Square parameter is required"}), 400
    
    # Check if there's a piece at this square
    if square not in gameState.piece_positions:
        return jsonify({"error": "Square must contain a piece upon it"}), 400
    
    try: 
        return jsonify(gameState.get_legal_moves(square))
    except Exception as e: 
        logger.error(f"error getting start positions: {str(e)}")
        return jsonify({"error": "failed to get start positions"}), 500

@app.route('/make-move', methods=['POST'])
def make_move() -> Union[Response, tuple[Response, int]]:
    from flask import request
    data = request.json
    start_square = data.get('start')
    end_square = data.get('end')
    
    if not start_square or not end_square:
        return jsonify({"error": "Both start and end squares are required"}), 400
    
    try:
        return jsonify(gameState.move(start_square, end_square))
    except Exception as e:
        logger.error(f"error making a move: {str(e)}")
        return jsonify({"error": "failed to make a move"}), 500

@app.route('/get-piece-positions')
def get_piece_positions() -> Response:
    from flask import request
    move = request.args.get('move')

    try: 
        return jsonify(gameState.get_piece_positions)
    except:
        logger.error(f"error getting piece positions: {str(e)}")
        return jsonify({"error": "failed to get piece positions"}), 500

if __name__ == "__main__":
  app.run(debug=True, port=5001)