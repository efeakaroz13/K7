from databasekentel import db
project = db("KENTEL")
print(project.changepassword(username="Efeakaroz",password="password",newpassword="userpassword"))
