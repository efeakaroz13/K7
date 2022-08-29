import json
import random
import os

stringstuff = ["I","Z","K","R","P","A","O","U","Y","N"]

class RSOR:
	def __init__(self):
		self.session = f"{random.choice(stringstuff)}{random.choice(stringstuff)}{random.choice(stringstuff)}{random.randint(1,2345345546)}"

	def search(self,query):

		os.system(f"""./wikipedia  "{query}" {self.session} """)
		os.system(f"""./duckie  "{query}" {self.session} """)
		os.system(f"""./googler  "{query}" {self.session} """)
		jsontoreturn = json.loads(open(self.session+".json","r").read())
		os.system(f"rm {self.session}.json")
		return jsontoreturn

