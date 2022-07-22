from concurrent.futures import thread
from black import out
from click import password_option
from flask import render_template,redirect,request,abort,make_response,Flask
import templates
import auth
from databasekentel import db


app = Flask(__name__)
k7app = db("K7")

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


@app.route("/register",methods=["POST","GET"])
def register():
	if request.method == "POST":
		fullName = request.form.get("fullName")
		try:
			fullName.split()[1]
		except:
			return templates.Templates.return_register_unknown_tr()
		birthyear = request.form.get("birthyear")

		citylivingin = request.form.get("city")
		talents = request.form.get("talents")
		username = request.form.get("username")
		password = request.form.get("password")
		output = k7app.createuser(username=username,password=password,fullname=fullName,talents=talents,city=citylivingin,birthyear=birthyear)
		if output["SCC"] == True:

			return templates.Templates.return_register_done_tr(username)
		else:
			return templates.Templates.register_err_tr(output)



		

				
	response = make_response(templates.Templates.return_register_tr())
	return response

app.run(debug=True)



