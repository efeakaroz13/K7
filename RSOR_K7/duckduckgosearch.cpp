#include <iostream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>
#include <fstream>
using json = nlohmann::json;

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
		output["duckduckgo"]=myoutarray;
		
		
		int nm;
		std::replace(search.begin(),search.end(),' ','+');
		
		cout<<"INFO | Searching:"<<search<<"\n\n";
		string url = "https://duckduckgo.com/?format=json&q="+search;
		CURL* curl = curl_easy_init();
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
	    	json duckduckgoenginesearch = json::parse(*httpData.get());

	    	json results= duckduckgoenginesearch["Results"];
	    	if (results.size()>0){
		    	for (int i=0; i<results.size();i++)
		    	{	

		    		output["duckduckgo"].push_back(results[i]);
		    		cout<<results[i]["Result"];
		    		cout<<"\n\n";

				}
			}else{
				cout<<"No results!";
			}
			output["duckduckgoWIKI"]["Abstract"]=duckduckgoenginesearch["AbstractText"];
			output["duckduckgoWIKI"]["AbstractURL"] = duckduckgoenginesearch["AbstractURL"];
			output["duckduckgoWIKI"]["AbstractSRC"] = duckduckgoenginesearch["AbstractSource"];

		}

		std::ofstream o(session+".json");
		o << std::setw(4) << output << std::endl;
	}
	
	

}