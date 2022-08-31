import requests
import json

class Dictionary:
	def __init__(self,language):
		language = language.lower()
		if language == "turkish":
			language="tr"
		if language == "english":
			language ="en"
		if language == "russian":
			language == "ru"
		if language == "german":
			language = "de"
		self.language = language


	def search(self,word):
		if self.language == "en":
			try:
				page = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word.replace(" ","%20"))
				outputDict = json.loads(page.content)

			except:
				return {"SCC":False,"out":[]}

			try:
				output = outputDict[0]["meanings"]
				try:
					phonetics = outputDict[0]["phonetics"]
				except:
					phonethics = []
			except:
				try:
					return {"SCC":False,"error":outputDict["title"],"out":[]}
				except:
					return {"SCC":False,"error":"","out":[]}



			return {"SCC":True,"output":output,"phonetics":phonetics}



