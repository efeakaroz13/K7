from concurrent.futures import thread
import ssl
from flask import render_template,redirect,request,abort,make_response,Flask
import templates
app = Flask(__name__)

@app.route("/")
def index():
    return templates.Templates.return_index_tr()

@app.route("/login")
def login():
	return templates.Templates.return_login_tr()

app.run(debug=True)