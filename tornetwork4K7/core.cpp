#include <iostream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>
#include <fstream>
#include "TorHttpRequest.hpp"
#include "Util.hpp"

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
		
		/*
		CURL* curl = curl_easy_init();
		curl_easy_setopt(curl, CURLOPT_URL, onionURL.c_str());
		curl_easy_setopt(curl, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V4);
		curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10);
		curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
		long httpCode(0);
		std::unique_ptr<std::string> httpData(new std::string());
		curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, callback);
		curl_easy_setopt(curl, CURLOPT_USERAGENT, userAgent.c_str());
		curl_easy_setopt(curl, CURLOPT_PROXYTYPE, CURLPROXY_SOCKS5);
		curl_easy_setopt(curl, CURLOPT_PROXY, "socks5://127.0.0.1:9050");

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
		*/

		TorHttpResponse result;
	    string proxyHost = "127.0.0.1";
	    int proxyPort =9050;
	    string requestHost = "4usoivrpy52lmc4mgn2h34cmfiltslesthr56yttv2pxudd3dapqciyd.onion";
	    string requestUrl = "/";
	    /* initialise curl handle */
	    CURL *curl;

	    /* define the full request url */
	    string url = "http://" + requestHost + requestUrl;

	    /* buffer to write result into */
	    string readBuffer;
	    vector<TorHttpResponseHeader> headerList;

	    /* initialise curl */
	    curl = curl_easy_init();
	    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());


		curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L); 

	    /* add headers if any were supplied 
	    if(this->requestHeaderList.size() > 0){
	        struct curl_slist *chunk = NULL;

	        for(int h=0; h<this->requestHeaderList.size(); h++){
	            string headerText = requestHeaderList[h].first + ": " + requestHeaderList[h].second;
	            chunk = curl_slist_append(chunk, headerText.c_str());
	        }

	      	pass the header list to curl 
	        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, chunk);
	    }

	    check if method is post and send post data */
	    

	    curl_easy_setopt(curl, CURLOPT_USERAGENT, userAgent.c_str());
	    curl_easy_setopt(curl, CURLOPT_NOPROGRESS, 1L);
	    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, TorHttpRequest::writeResponse);
	    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
	    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, false); 
	    curl_easy_setopt(curl, CURLOPT_HEADERFUNCTION, TorHttpRequest::writeResponseHeader);
	    curl_easy_setopt(curl, CURLOPT_HEADERDATA, &headerList);


	    if(proxyHost.length() > 0 && proxyPort > 0){

	        string proxyUrl = "socks5h://" + proxyHost + ":" + std::to_string(proxyPort);
	        curl_easy_setopt(curl, CURLOPT_PROXY, proxyUrl.c_str());
	    }

	    /* kill and clean up curl */
	    CURLcode res = curl_easy_perform(curl);
	    if(res == CURLE_OK) {

	        curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &result.status);
	    }else{

	        result.content = "";

	        /* 
	            502 Bad Gateway 
	            The server was acting as a gateway or proxy 
	            and received an invalid response from the 
	            upstream server.
	        */
	        result.status = 502;

	        /* check specific error */
	        if(res == CURLE_OPERATION_TIMEDOUT){
	            /*
	                504 Gateway Timeout
	                The server was acting as a gateway or proxy 
	                and did not receive a timely response from 
	                the upstream server.
	            */
	            result.status = 504;
	        }
	    }

	    /* clean up curl */
	    curl_easy_cleanup(curl);

	    /* build up the result struct */
	    //result.headerList = headerList;
	    
	    cout<<readBuffer<<"\n";












	}
	else{
		cout<<"Arguments are not enough\n";
	}
	
	

}
