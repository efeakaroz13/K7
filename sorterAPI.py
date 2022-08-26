#Copyright (c) 2022 Efe Akaröz
#26/08/2022
#FOR K7 PROJECT
import os
import json


class Sorter:
    def __init__(self):
        self.script = "./sorter_script"
        self.outfile = "sort.json"

    def init(self):

        os.system(self.script)

    def getData(self):
        thejsonfilesorted = open(self.outfile, "r")
        try:
            jsonobjsorted = json.loads(thejsonfilesorted.read())
            out = []
            dataofarticlelist = jsonobjsorted["listofarticles"]
            for m in dataofarticlelist:
                out.insert(0,m)
        except:
            raise SyntaxError
        return out

"""
Example which shows how this Class works:
sortobj = Sorter()
sortobj.init()
mydata = sortobj.getData()
print(mydata)
"""



