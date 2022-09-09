#Copyright (c) 2022 Efe Akaröz
from concurrent.futures import thread
from select import select
from flask import redirect, request, abort, make_response, Flask,render_template
import templates
import auth
from databasekentel import db
import random
import time
from cryptography.fernet import Fernet
import json
import os
from operator import itemgetter
import pyrebase
from credentials import firebase_credentials
import requests
from sorterAPI import Sorter
from dictionary_globalK7.dictk7 import DictK7
from RSOR_K7.rsor import RSOR


app = Flask(__name__)
k7app = db("K7")

firebasevar = firebase_credentials()
mydb = firebasevar.db
databaseURL = firebasevar.databaseurl
threelangDict = DictK7()
key = b'D71kHIq7Wsyrjd30avvyzrS7BTT74lAXBB5y6mllnsQ='
fernet = Fernet(key)

def jsonRequestFirebase(databaseURL,path=".json"):
	#with / end of the url
	page = requests.get(databaseURL+path).content
	jsonobj = json.loads(page)
	return jsonobj


def secondstostring(calculatorx):
	if calculatorx < 500:
		lastarticle = " Şimdi"
	else:
		if calculatorx <1500:
			lastarticle="Kısa süre önce"
		else:
			if calculatorx <2000:
				lastarticle = " Yarım saat önce"
			else:
				if calculatorx < 3600:
					lastarticle = " Bir saat önce"
				else:
					if calculatorx <7200:
						lastarticle = " İki saat önce"
					else:
						if calculatorx <108000:
							lastarticle = " Üç saat önce"
						else:
							if calculatorx <14400:
								lastarticle = " Dört saat önce"
							else:
								if calculatorx < 86400:
									lastarticle = " Gün içerisinde"
								else:
									if calculatorx < 172800:
										lastarticle = " Dün"
									else:
										if calculatorx < 604800:
											lastarticle = " Bu hafta"
										else:
											if calculatorx < 2592000:
												lastarticle = " Bu ay "
											else:
												if calculatorx < 5184000:
													lastarticle = " Geçen ay "
												else:
													if calculatorx < 31557600:
														lastarticle= " Bu yıl"
													else:
														years = calculatorx/31557600
														lastarticle= f" {str(years)[:4]} yıl önce"

	return lastarticle
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
				return redirect("/read/"+articleid)
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
	try:
		views_count = str(len(jsonRequestFirebase(databaseURL,"K7APP/articleviews/{}/views.json".format(articleid))))
	except Exception as e:
		views_count = str(0)

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

			try:
				ip_addr = request.environ['REMOTE_ADDR']
			except:
				try:
					ip_addr = request.environ['HTTP_X_FORWARDED_FOR']
				except:
					ip_addr = "00000"

			ip_addr = ip_addr.replace(".", "")
			mydb.child("K7APP").child("articleviews").child(articleid).update(articlereader)
			mydb.child("K7APP").child("articleviews").child(articleid).child("views").child(ip_addr).set(
				{"useragent": str(request.headers.get('User-Agent'))})

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
					return templates.Templates.articlereadsingle(mydata,views=views_count)
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
					return templates.Templates.articlereadsingle(mydata,username=username,views=views_count)
				else:
					if visibility == True:
						mydata= {"edit":False,"data1":articlereader}
						return templates.Templates.articlereadsingle(mydata,username=username,views=views_count)

					else:
						return abort(404)
		except Exception as e:
			print(e)
			return abort(404)



@app.route("/user/<username>")
def usernameuser(username):
	try:
		username_current = decrypt(request.cookies.get("username"))
		password_current = decrypt(request.cookies.get("password"))
		theauthchecker = k7app.login(username_current,password_current)
		if theauthchecker["SCC"] == True and username == username_current:
			profileofmine = True
		else:
			profileofmine = False


	except:
		profileofmine = False
	userdata1 =k7app.getuser(username)
	


	if userdata1["SCC"] == True:
		currenttime = time.time()
		allarticles = os.listdir("static/articles")
		outlist=[]
		for ar in allarticles:
			print(ar)
			if ar.split("JDGFJAMDYCNAKLRUN")[0] == username:
				myfiletoopen = open("static/articles/{}".format(ar),"r").read()
				outlist.append(json.loads(decrypt(myfiletoopen)))

		if len(outlist) == 0:
			lastarticle=""
		else:
			selectorlist = sorted(outlist, key=itemgetter('lastsaved')) 
			calculatorx = currenttime-selectorlist[-1]["lastsaved"]
			lastarticle = secondstostring(calculatorx)


		return templates.Templates.profiler(outlist=outlist,userdata=userdata1,lastarticle=str(lastarticle),profileofmine=profileofmine)
	else:
		return abort(404)


@app.route("/change/password",methods=["POST","GET"])
def passwordchangerroute():
	if request.method == "POST":
		username = decrypt(request.cookies.get("username"))
		password = decrypt(request.cookies.get("password"))
		theauthchecker = k7app.login(username, password)
		if theauthchecker["SCC"] == True:
			oldpassword = request.form.get("oldpassword").strip()
			newpassword = request.form.get("newpassword").strip()
			if oldpassword == newpassword:
				return templates.Templates.changepassword_err(username,"Eski şifren ile yeni şifren aynı olamaz")
			else:
				usernamechecker = request.form.get("username_verify")
				if usernamechecker.strip() == username:
					passwordchangervariable = k7app.changepassword(username,oldpassword,newpassword)
					if passwordchangervariable["SCC"] == True:
						return redirect("/login")
					else:
						return templates.Templates.changepassword_err(username,"Şifre değiştirilirken bir hata oluştu")
				else:
					return templates.Templates.changepassword_err(username,"Kullanıcı adları uyuşmuyor")
		else:
			return redirect("/login")
	try:
		username = decrypt(request.cookies.get("username"))
		password = decrypt(request.cookies.get("password"))
		theauthchecker = k7app.login(username,password)
		if theauthchecker["SCC"] == True:

			return templates.Templates.changepassword(username,None)
		else:
			return redirect("/login")
	except Exception as e:
		return str(e)

@app.route("/explore")
def explorePage():
	p = request.args.get("p")
	if p == None:
		p = 0
	try:
		p = int(p)
	except:
		p = 0

	mysorter = Sorter()
	try:
		mysorter.init()
	except:
		pass
	try:
		mydata = mysorter.getData()
	except:
		mydata = []


	return render_template("explore.html",data=mydata)
@app.route("/rsor",methods=["POST","GET"])
def rsorroute():
	stringstuff = ["I","Z","K","R","P","A","O","U","Y","N"]
	session = f"{random.choice(stringstuff)}{random.choice(stringstuff)}{random.choice(stringstuff)}{random.randint(1,2345345546)}"

	if request.method == "POST":
		q = request.form.get("search")
		qnew = f"{q}"
		
		qnew = qnew.replace("ö","o").replace("ğ","g").replace("ü","u").replace("ı","i").replace("ç","c").replace("Ö","O").replace("Ğ","G").replace("Ü","U").replace("İ","I").replace("Ç","C")




		os.system(f"""RSOR_K7/wikipedia  "{qnew}" {session} """)
		os.system(f"""RSOR_K7/duckie  "{q}" {session} """)
		os.system(f"""RSOR_K7/googler  "{q}" {session} """)
		jsontoreturn = json.loads(open(session+".json","r").read())
		os.system(f"rm {session}.json")


		return templates.Templates.rsorthingPOST(q,jsontoreturn)
	return templates.Templates.rsorthing()
@app.route("/wikipediaopener/<pageid>")
def wikipediaredirect(pageid):
	try:
		a = int(pageid)
		page = json.loads(requests.get("https://tr.wikipedia.org/w/api.php?action=query&prop=info&pageids={}&inprop=url&format=json".format(pageid)).content)
		return redirect(page["query"]["pages"][pageid]["fullurl"])
	except Exception as e:
		return abort(403)

@app.route("/wikipedia_data",methods=["POST","GET"])
def wikidata():
	q = request.args.get("q")
	head="""<meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Vikipedi Hızlı Arama - RSOR</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet"/><link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" rel="stylesheet"/><link href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css" rel="stylesheet"/><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@300&display=swap" rel="stylesheet">"""
	if request.method == "POST":
		search = request.form.get("search")
		return redirect(f"/wikipedia_data?q={search}")
	if q!=None:
		q = q.replace("ö","o").replace("ğ","g").replace("ü","u").replace("ı","i").replace("ç","c").replace("Ö","O").replace("Ğ","G").replace("Ü","U").replace("İ","I").replace("Ç","C")
		stringstuff = ["I","Z","K","R","P","A","O","U","Y","N"]
		session = f"{random.choice(stringstuff)}{random.choice(stringstuff)}{random.choice(stringstuff)}{random.randint(1,2345345546)}"

		os.system(f"""RSOR_K7/wikipedia "{q}" {session} """)
		outData = json.loads(open("{}.json".format(session),"r").read())
		output=""""""
		os.system(f"rm {session}.json")
		for w in outData["wikipedia"]:
			if outData["wikipedia"].index(w) == 0:
				snippetter = f"""
	            
	              <h2>{w['title']}</h2>
	              <p style="margin-left:5px;font-size:15px">{w['snippet']}...</p><br>
	              <i style="color:#2d2d2d">Kelime sayısı:{w['wordcount']}</i><br>
	              <a href="/wikipediaopener/{w['pageid']}">Vikipedi'de Oku</a>
	            <br>
	            """
				output = output +str(snippetter)+"<br>"
				continue
			snippetter = f"""
            <details>
              <summary>{w['title']}</summary>
              <p style="margin-left:5px;font-size:15px">{w['snippet']}...</p><br>
              <i style="color:#2d2d2d">Kelime sayısı:{w['wordcount']}</i><br>
              <a href="/wikipediaopener/{w['pageid']}">Vikipedi'de Oku</a>
            </details>
            """
			output = output +str(snippetter)+"<br>"

		return render_template("vikipedi.html",resulting=True,data=outData,headstuff=head,query=q,output=output)
	else:
		pass

	
	return render_template("vikipedi.html",headstuff=head)

app.run(debug=True,port=3000)



