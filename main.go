package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
)

func main() {
	// Let's first read the `config.json` file
	content, err := ioutil.ReadFile("./sort.json")
	if err != nil {
		log.Fatal("Error when opening file: ", err)
	}

	var payload map[string]interface{}
	err = json.Unmarshal(content, &payload)
	if err != nil {
		log.Fatal("Error during Unmarshal(): ", err)
	}

	log.Printf(" %s", payload["myjson"])

}
