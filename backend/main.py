from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins': '*'}})
# maybe define to localhost 8080 with allow_header: access-control-allow-origin

# test
@app.route('/', methods=['GET'])
def test():
  return ("Hello")

if __name__ == "__main__":
  app.run(debug=True)