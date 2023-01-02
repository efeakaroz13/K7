import json 
import requests
import random 
from selenium import webdriver
import time 
import colorama
import pickle
 

allcookies = json.loads(open("cookies.json","r").read())
s = requests.Session()
for cookie in allcookies:
	s.cookies.set(cookie['name'], cookie['value'])
	
domain_details = json.loads(s.post("https://www.isimtescil.net/panel/domain/gelismis-dns-ayarlari.aspx/GetDomainInfo",headers={"Content-Type":"application/json"},data='{"domainName":"k7.org.tr"}').content)
for r in domain_details["d"]:
	if r["Type"] == "A":
		oldip = r["Data"]

newip = json.loads(requests.get("http://ip-api.com/json").content)["query"]
if oldip == newip:
	print(colorama.Fore.WHITE,"NO IP DIFFERENCE FOUND!",colorama.Fore.RESET)
else:
	updater = json.loads(s.post("https://www.isimtescil.net/panel/domain/gelismis-dns-ayarlari.aspx/UpdateRecord",headers={"Content-Type":"application/json"},data='{"domainName":"k7.org.tr","recordType":"A","recordName":"*.k7.org.tr","recordInfo":"'+newip+'","oldrecordName":"*.k7.org.tr","oldrecordInfo":"'+oldip+'","priority":"","oldPriority":""}').content)
	print(colorama.Fore.BLUE,"SERVER RESPONDED ",colorama.Fore.WHITE,updater["Type"],colorama.Fore.RESET)
	updater = json.loads(s.post("https://www.isimtescil.net/panel/domain/gelismis-dns-ayarlari.aspx/UpdateRecord",headers={"Content-Type":"application/json"},data='{"domainName":"k7.org.tr","recordType":"A","recordName":"k7.org.tr","recordInfo":"'+newip+'","oldrecordName":"k7.org.tr","oldrecordInfo":"'+oldip+'","priority":"","oldPriority":""}').content)
	print(colorama.Fore.BLUE,"SERVER RESPONDED ",colorama.Fore.WHITE,updater["Type"],colorama.Fore.RESET)
	
	


print(colorama.Fore.BLUE,"OLD IP ADDRESS ",colorama.Fore.WHITE," | ",oldip,colorama.Fore.RESET)
