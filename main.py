from flask import Flask, render_template, request, make_response, redirect, url_for
import json

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.route('/')
def start():
  return "hi"

@app.route('/input')
def index():
  x = request.args.get('x')
  dict = {"lat": str(x)}
  json_data = json.dumps(dict)
  return json_data



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
