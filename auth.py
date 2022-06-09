from operator import sub
import subprocess
import os

class auth:
    def sign_in(email,password):
        out = os.popen("./auth-module login {} {}".format(email,password)).read()
        try:
            out.split("200")[1]
            return {"login":True,"password":True,"email":True}
        except:
            try:
                out.split("403p")[1]
                return {"login":False,"password":False,"email":True}
            except:
                return  {"login":False,"password":False,"email":False}


print(auth.sign_in("efeakaroz13","1234"))


    

