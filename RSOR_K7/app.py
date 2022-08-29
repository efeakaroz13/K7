from flask import Flask,render_template,request,redirect
from rsor import RSOR 
import requests

app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def index():
	if request.method == "POST":
		searchq = request.form.get("search")
		engine = RSOR()
		result = engine.search(searchq)

		return render_template("search.html",Res=True,res=result,search=searchq)
	return render_template("search.html")
@app.route("/wikipedia/<pageid>")
def wikipediaopener(pageid):

	return redirect(f"https://tr.wikipedia.org/wiki?curid={pageid}")


app.run(debug=True)