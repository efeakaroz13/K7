#include <iostream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

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
	
	if(argc>1){
		string search = argv[1];
		int nm;
		std::replace(search.begin(),search.end(),' ','+');
		
		cout<<"INFO | Searching:"<<search<<"\n\n";
		string url = "https://www.googleapis.com/customsearch/v1?cx=0cb3ac5a5df2563b5&key=AIzaSyAjTG1n9cdbZPYzu1b1GwIx1TlKzIgGqEg&q="+search;
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
	    if(httpCode == 200){
	    	json googlejsonsearch = json::parse(*httpData.get());
	    	json results= googlejsonsearch["items"];
	    	for (int i=0; i<results.size();i++)
	    	{
	    		cout<<results[i]["title"];
	    		cout<<"\n\n";

			}
		}
	}

}