'''
K7 KENTEL DATABASE AND AUTH MODULE BY EFE AKARÖZ
2022
JULY
13TH

WITH PYTHON AND C
EDITOR:VIM
'''
import subprocess
import os

class db:
	def __init__(self,project_name):
		self.projname = project_name

	def createuser(self,username,password,fullname=None,city=None,birthyear=None,talents=None):
		if username == None:
			return {"SCC":False,"err":"USERNAME CAN'T BE NONE!","project":self.projname}
		if password == None:
			return {"SCC":False,"err":"YOU NEED TO SPECIFY PASSWORD!","project":self.projname}

		try:
			os.listdir("users")
		except:
			os.system("mkdir users")
		try:
			open(f"users/{username}.K7USERFILE","r")

			return {"SCC":False,"err":"USER EXISTS","project":self.projname}
		except:
			checkout = str(subprocess.check_output(f"./auth-module login {username} {password}",shell=True))
			try:
				checkout.split("200")[1]
				return {"SCC":False,"err":"USER EXISTS","project":self.projname}

			except:

				userfile = open(f"users/{username}.K7USERFILE","a")
				if fullname == None:
					fullname = "EMPTY"	
				if city == None:
					city="EMPTY"
				if birthyear ==None:
					birthyear = "EMPTY"
				if talents == None:
					talents = "EMPTY"

				userfile.write("PROJECT={};--;\n".format(self.projname))
				userfile.write("USERNAME={};--;\n".format(username))
				userfile.write("PASSWORD={};--;\n".format(password))
				userfile.write("FULLNAME={};--;\n".format(fullname))
				userfile.write("CITY={};--;\n".format(city))
				userfile.write("BIRTHYEAR={};--;\n".format(birthyear))
				userfile.write("TALENTS={}".format(talents))
				userfile.write(";--;")
			
			
				userfile.close()
				theout = str(subprocess.check_output(f"./auth-module register {username} {password}",shell=True))
				try:
					theout.split("200")[1]
					return {"SCC":True,"err":"","project":self.projname}
				except:
					return {"SCC":False,"err":"C MODULE FAILED!","project":self.projname}

	def login(self,username,password):
		try:
			out = str(subprocess.check_output(f"./auth-module login {username} {password}",shell=True))
		except Exception as e:
			
			return {"SCC":False,"err":"MODULE ERR","porject":self.projname}
		try:
			out.split("200")[1]
			return {"SCC":True,"err":"","project":self.projname}	

		except Exception as e:
			
			try:
				out.split("403p")[1]
				return {"SCC":False,"err":"WRONG PASSWORD","project":self.projname}
			except:
				return {"SCC":False,"err":"USER NOT EXISTS","project":self.projname}
