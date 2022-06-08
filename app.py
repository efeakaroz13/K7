from concurrent.futures import thread
import ssl
from flask import render_template,redirect,request,abort,make_response,Flask
import templates
app = Flask(__name__)

@app.route("/")
def index():
    return templates.Templates.return_index()


app.run(debug=True)