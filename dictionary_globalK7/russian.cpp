//Author: Efe Akaröz
#include <iostream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>
#include <fstream>
using json = nlohmann::json;
//compile g++ -Wall -std=c++11 russian.cpp  -l curl
using namespace std;
namespace
{
    std::size_t callback(
            const char* in,
            std::size_t size,
            std::size_t num,
            std::string* out)
    {
        const std::size_t totalBytes(size * num);
        out->append(in, totalBytes);
        return totalBytes;
    }
}

int main(int argc, char *argv[]){
	std::ifstream credentials("yandex.json");
	if(credentials){
		json credentialsThing = json::parse(credentials);
		//string key = credentialsThing["apiKey"];
		if(!credentialsThing["apiKey"].is_null()){
			if(argc>2){
				string search = argv[1];
				string session = argv[2];
				json output;
				std::ifstream mf(session+".json");
				if(mf){
					output = json::parse(mf);
				}else{
					output = {};
				}
				

				json myoutarray = json::array();
				output["yandexdictionary"]=myoutarray;
				
				

				std::replace(search.begin(),search.end(),' ','+');
				struct curl_slist* headers = NULL;
				headers = curl_slist_append(headers, "Accept: application/json");
				headers = curl_slist_append(headers, "Content-Type: application/json");
				string APIKEY = credentialsThing["apiKey"];

				cout<<"INFO | Searching:"<<search<<"\n\n";
				string url = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key="+APIKEY+"&lang=tr-ru&text="+search;
				
				CURL* curl = curl_easy_init();
				curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
			    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
			    curl_easy_setopt(curl, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V4);
			    curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10);
			    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
			    long httpCode(0);
			    std::unique_ptr<std::string> httpData(new std::string());
			    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, callback);
			    curl_easy_setopt(curl, CURLOPT_WRITEDATA, httpData.get());
			    curl_easy_perform(curl);
			    curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &httpCode);
			    curl_easy_cleanup(curl);

			    cout<<"\n";
			    json rnobj;
			    if(httpCode == 200){
			    	json yandexout = json::parse(*httpData.get());
			    	json results= yandexout["def"];
			    	if(results.size()>0){
			    		for (int i=0; i<results.size();i++)
			    		{	
			    			output["yandexdictionary"].push_back(results[i]);
			    			cout<<results[i]["tr"][0];
			    			cout<<"\n";
						}
			    	}

			    	
				}else{
					cout<<"Network Error\n";
					cout<<httpCode<<"\n";
				}
				std::ofstream o(session+".json");
				o << std::setw(4) << output << std::endl;
			}


		}
		else{
			cout<<"There isn't any variable called 'apiKey'\n";
		}
		
	}else{
		cout<<"NO CREDENTIALS!\n";
	}
	

	
	
	

}