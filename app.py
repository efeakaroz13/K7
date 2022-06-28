from concurrent.futures import thread
import ssl
from flask import render_template,redirect,request,abort,make_response,Flask
import templates
import auth
app = Flask(__name__)

@app.route("/")
def index():
    return templates.Templates.return_index_tr()

@app.route("/login",methods=["POST","GET"])
def login():
	if request.method=="POST":
		username = request.form.get("username")
		password = request.form.get("password")
		the_val = auth.auth.sign_in(username,password)
		if the_val["login"] == True:
			response = make_response(redirect("/"))
			return response
		else:
			return templates.Templates.return_login_err_tr()


	return templates.Templates.return_login_tr()

app.run(debug=True)