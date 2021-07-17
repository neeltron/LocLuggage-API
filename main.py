from flask import Flask, render_template, request, make_response, redirect, url_for
import json
from flask_cors import CORS, cross_origin
from replit import db

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

cors = CORS(app, resources={r"/input": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def start():
  return "hi"

@app.route('/input')
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def index():
  x = request.args.get('x')
  y = request.args.get('y')
  db['lat'] = x
  db['long'] = y
  dict = {"lat": str(x), "long": str(y)}
  json_data = json.dumps(dict)
  return json_data



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
