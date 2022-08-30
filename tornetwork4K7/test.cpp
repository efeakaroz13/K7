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
		string onionURL = "http://4usoivrpy52lmc4mgn2h34cmfiltslesthr56yttv2pxudd3dapqciyd.onion/";
		string session = "out";
		json output;
		std::ifstream mf(session+".json");
		if(mf){
			output = json::parse(mf);
		}else{
			output = {};
		}
		int nm;
		string userAgent="TORCORE.CPP/Mr404";
		
		
		CURL* curl = curl_easy_init();
		curl_easy_setopt(curl, CURLOPT_URL, onionURL.c_str());
		curl_easy_setopt(curl, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V4);
		curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10);
		curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, false);
		curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L); 
		long httpCode(0);
		std::unique_ptr<std::string> httpData(new std::string());
		curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, callback);
		curl_easy_setopt(curl, CURLOPT_USERAGENT, userAgent.c_str());
		curl_easy_setopt(curl, CURLOPT_PROXYTYPE, CURLPROXY_SOCKS5);
		curl_easy_setopt(curl, CURLOPT_PROXY, "socks5h://127.0.0.1:9050");

		curl_easy_setopt(curl, CURLOPT_WRITEDATA, httpData.get());
		curl_easy_perform(curl);
		curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &httpCode);
		curl_easy_cleanup(curl);


	    cout<<"\n";
	    
	    if(httpCode == 200){
	    	cout<<"\n200!!!!\n";
	    	cout<<*httpData.get();
	    	output["html"] = 200;
		}
		cout<<httpCode<<"\n";
		


		std::ofstream o(session+".json");
		o << std::setw(4) << output << std::endl;
		





	}
	else{
		cout<<"Arguments are not enough\n";
	}
	
	

}
