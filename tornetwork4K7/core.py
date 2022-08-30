from bs4 import BeautifulSoup
import os
from colorama import Fore
import random

class tor4K7:
	def __init__(self):
		self.core = "./core"
		self.session = f"{random.randint(234,234235345)}"
	def searchOnTor(self,q):
		os.system(f"""./core "{q}" "{self.session}" """)

		htmlfilereader = open(f"{self.session}.html","r").read()
		self.soup = BeautifulSoup(htmlfilereader,"html.parser")
		out = []
		os.system(f"rm {self.session}.html")
		allh5 = self.soup.find_all("h5")
		for h in allh5:
			hid = h.get("id")
			if hid == "" or hid==None:
				out.append(h.get_text())
			else:
				pass

		return out

print("===============================================")
print("Welcome to ",Fore.RED,"tornetwork4K7",Fore.RESET)
print("")
print("Author: ",Fore.GREEN,"efeakaroz13",Fore.RESET)
print("===============================================")
torchsearch = input("Search on TORCH>")
torobj = tor4K7()
myout = torobj.searchOnTor(torchsearch)
for o in myout:
	print(myout.index(o))
	print(o)
	print("\n")