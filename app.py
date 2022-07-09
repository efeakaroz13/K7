from concurrent.futures import thread
import ssl
from flask import render_template,redirect,request,abort,make_response,Flask
import templates
import auth
app = Flask(__name__)

@app.route("/")
def index():
	username = request.cookies.get("username")
	password = request.cookies.get("password")
	if username == None:
		return templates.Templates.return_index_tr()
	else:
		sign_in_stuff = auth.auth.sign_in(username,password)
		if sign_in_stuff["login"] == True:
			return templates.Templates.return_home_tr(username)
		else:
			return templates.Templates.return_index_tr()


@app.route("/login",methods=["POST","GET"])
def login():
	if request.method=="POST":
		username = request.form.get("username")
		password = request.form.get("password")
		the_val = auth.auth.sign_in(username,password)
		if the_val["login"] == True:
			response = make_response(redirect("/"))
			response.set_cookie("username",username)
			response.set_cookie("password",password)
			return response
		else:
			return templates.Templates.return_login_err_tr()


	return templates.Templates.return_login_tr()
@app.route("/logout")
def logout():
	response = make_response(redirect("/"))
	response.set_cookie("username",max_age=0)

	return response


@app.route("/register")
def register():
	response = make_response(templates.Templates.return_register_tr())
	return response
app.run(debug=True)