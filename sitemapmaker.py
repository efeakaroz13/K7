import credentials
import json
import requests


databaseurl = credentials.firebase_credentials().databaseurl

dataobj = json.loads(requests.get(databaseurl+"K7APP.json").content)

sitemap = open("static/sitemap.xml","w")

sitemap.write('<?xml version="1.0" encoding="UTF-8"?>')
sitemap.write('<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">')

for v in dataobj["articleviews"]:
    try:
        if dataobj["articleviews"][v]["approved"] == True and dataobj["articleviews"][v]["visibility"] == "public":

            sitemap.write("<url>")
            sitemap.write('<loc>'+'https://www.k7.org.tr/read/'+v+'</loc>')
            sitemap.write('<priority>0.9</priority>')
            sitemap.write('<changefreq>daily</changefreq>')
            sitemap.write("</url>")
    except:
        pass
sitemap.write('<url>')
sitemap.write('<loc>https://www.k7.org.tr</loc>')
sitemap.write('<priority>1</priority>')
sitemap.write('</url>')

sitemap.write("</urlset>")
