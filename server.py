from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import re
app = Flask(__name__)

# routes

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/getting-started')
def templates():
   return render_template('getting-started.html')

@app.route('/templates')
def templates():
   return render_template('templates.html')

@app.route('/guides')
def guides():
   return render_template('guides.html')

@app.route('/forum')
def forum():
   return render_template('forum.html')

if __name__ == '__main__':
   app.run(debug = True)