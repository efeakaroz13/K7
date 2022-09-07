from flask import Flask,request
from dictk7 import DictK7
mydictionary = DictK7()
app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def index():
	if request.method == "POST":
		language = request.form.get("language")
		entry = request.form.get("q")
		output = mydictionary.search(entry,language)
		return {"out":output}
	return """
		<form action="" method="POST">
			<center><input name="q" style="margin-right:10px;" placeholder="Kelime Girin..."><label for="language">Çıkış Dili:</label><select name="language"><option value="en">🇬🇧</option><option value="ru">🇷🇺</option><option value="de">🇩🇪</option></select><button>Search</button>
		</form>
	"""

app.run(debug=True)