package main

import (
	"io/ioutil"
	"log"
	"net/http"
	"encoding/json"
	"os"


)

func main() {
	type NotFound struct {
	    title string
	    SCC bool

	}


	search := os.Args[1]
	resp, err := http.Get("https://api.dictionaryapi.dev/api/v2/entries/en/"+search)
	if err != nil {
		log.Fatalln(err)
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	sb := string(body)
	var objMap []map[string]interface{}
    err = json.Unmarshal([]byte(sb), &objMap)
    if(err!=nil){
    	myjsonobj := NotFound{"Not found",false}
    	bytes, _ := json.MarshalIndent(myjsonobj, "", "  ")
		ioutil.WriteFile("config.json", bytes, 0644) 
    }
    if(objMap!=nil){
	    bytes, _ := json.MarshalIndent(objMap, "", "  ")
		ioutil.WriteFile("config.json", bytes, 0644)  
	}else{
		myjsonobj := NotFound{"Not found",false}
    	bytes, _ := json.MarshalIndent(myjsonobj, "", "  ")
		ioutil.WriteFile("config.json", bytes, 0644)
	}

}