from concurrent.futures import thread
from select import select
from flask import redirect,request,abort,make_response,Flask
import templates
import auth
from databasekentel import db
import random
import time
from cryptography.fernet import Fernet
import json 
import os

app = Flask(__name__)
k7app = db("K7")


key = b'D71kHIq7Wsyrjd30avvyzrS7BTT74lAXBB5y6mllnsQ='
fernet = Fernet(key)


def encrypt(text):
	encodedtext = fernet.encrypt(text.encode())
	return encodedtext.decode()


def decrypt(text):
	encodedtext = fernet.decrypt(text.encode())
	return encodedtext.decode()


@app.errorhandler(404)
def fourofour(e):
	return templates.Templates.notfound()
@app.route("/")
def index():
	
	username = request.cookies.get("username")
	password = request.cookies.get("password")
	try:
		username= decrypt(username)
		password = decrypt(password)
	except:
		return templates.Templates.return_index_tr()
	if username == None:
		return templates.Templates.return_index_tr()
	else:
		sign_in_stuff = k7app.login(username,password)
		if sign_in_stuff["SCC"] == True:
			selecteds = []
			allarticles = os.listdir("static/articles")
			for ar in allarticles:
				if ar.split("JDGFJAMDYCNAKLRUN")[0]==username.strip():
					textinfo = json.loads(decrypt(open("static/articles/{}".format(ar)).read()))
					selecteds.insert(0,{"filename":ar,"data":textinfo})
			return templates.Templates.return_home_tr(username,articles=selecteds)
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
			response.set_cookie("username",encrypt(username))
			response.set_cookie("password",encrypt(password))
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

@app.route("/writearticle",methods=["POST","GET"])
def writeanarticle():
	if request.method == "POST":
		try:
			username = decrypt(request.cookies.get("username"))
			password = decrypt(request.cookies.get("password"))
			the_val = k7app.login(username,password)
			if the_val["SCC"] == True:
				title = request.form.get("title")
				article = request.form.get("article")
				visibility = request.form.get("visibility")
				fontfamily = request.form.get("fontfamily")
				articleid = f"{username}JDGFJAMDYCNAKLRUN{random.randint(34234,2346723534237)}"
				articledata = {"title":title,"article":article,"visibility":visibility,"fontfamily":fontfamily,"lastsaved":time.time(),"username":username,"articleid":articleid}
				
				open(f"static/articles/{articleid}.ar","w").write(encrypt(json.dumps(articledata,indent=4)))
				return articledata
			else:
				return {"403":"FORBIDDEN DUMBASS"}
		except Exception as e :
			return{"SCC":False,"e":str(e)}
	username = decrypt(request.cookies.get("username"))
	password = decrypt(request.cookies.get("password"))
	the_val = k7app.login(username,password)
	if the_val["SCC"] == True:
		return templates.Templates.writeart(username)
	else:
		return redirect("/")

@app.route("/articles/<username>")
def articles(username):
	selecteds = []
	allarticles = os.listdir("static/articles")
	for ar in allarticles:
		if ar.split("JDGFJAMDYCNAKLRUN")[0]==username.strip():
			textinfo = json.loads(decrypt(open("static/articles/{}".format(ar)).read()))
			selecteds.insert(0,{"filename":ar,"data":textinfo})
	return {"out":selecteds}


@app.route("/read/<articleid>",methods=["POST","GET"])
def readersingle(articleid):
	editmode = request.args.get("edit")
	if editmode == "BLYAD":
		username = request.cookies.get("username")
		password = request.cookies.get("password")
		try:
			username = decrypt(username)
			password = decrypt(password)

		except:
			return abort(403)
		if request.method == "POST":
			articlereader = json.loads(decrypt(open(f"static/articles/{articleid}.ar","r").read()))
			theout = k7app.login(username,password)
			if theout["SCC"] == True and articlereader["username"] == username:
				title = request.form.get("title")
				article = request.form.get("article")
				lastchange = time.time()
				visibility = request.form.get("visibility")
				fontfamily = request.form.get("fontfamily")
				articlereader["title"] = title 
				articlereader["article"] = article 
				articlereader["lastsaved"] = lastchange
				articlereader["fontfamily"] = fontfamily
				articlereader["visibility"] = visibility

				writer = open(f"static/articles/{articleid}.ar","w")
				writer.write(encrypt(json.dumps(articlereader,indent=4)))
				return redirect("/read/"+articleid+"?edit=BLYAD")

		try:
			articlereader = json.loads(decrypt(open(f"static/articles/{articleid}.ar","r").read()))
		except:
			return abort(404)
		theout = k7app.login(username,password)
		if theout["SCC"] == True and articlereader["username"] == username:
			editormode = True 
			edit=True
			mydata = {"edit":edit,"data1":articlereader}

			return templates.Templates.articleedit(username=username,articledata=mydata)
		else:
			return redirect("/read/"+articleid)
	else:
		if request.method == "POST":
			return abort(403)
		try:
			articlereader = json.loads(decrypt(open(f"static/articles/{articleid}.ar","r").read()))
			username = request.cookies.get("username")
			password = request.cookies.get("password")
			if articlereader["visibility"] == "public":
				visibility = True 
			else:
				visibility = False
			if username == None or password == None:
				if visibility == True:
					edit = False
					mydata= {"edit":edit,"data1":articlereader}
					return templates.Templates.articlereadsingle(mydata)
				else:
					return abort(404)
			else:
				try:
					username = decrypt(username)
					password = decrypt(password)
				except:
					if visibility == True:
						edit = False
						mydata= {"edit":edit,"data1":articlereader}
					else:
						return abort(404)
				logcheck = k7app.login(username,password)
				if logcheck["SCC"] == True and articleid.split("JDGFJAMDYCNAKLRUN")[0] == username:
					edit=True
					mydata= {"edit":edit,"data1":articlereader}
					return templates.Templates.articlereadsingle(mydata,username=username)
				else:
					if visibility == True:
						mydata= {"edit":False,"data1":articlereader}
						return templates.Templates.articlereadsingle(mydata,username=username)

					else:
						return abort(404)
		except Exception as e:
			print(e)
			return abort(404)
		
app.run(debug=True,port=3000)



