#include <fstream>
#include <iostream>
#include <ostream>
#include <nlohmann/json.hpp>
#include <array>
#include <string>
#include <sstream>
#include <curl/curl.h>


//g++ sortjson.cpp -std=c++11 -lcurl -Iinclude -I/opt/local/include

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
void bubbleSort(json& arr, int n)
{
	int i, j;
	for (i = 0; i < n - 1; i++)

		for (j = 0; j < n - i - 1; j++)
			if (arr[j]["points"] > arr[j + 1]["points"])
				swap(arr[j], arr[j + 1]);
}


void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}
void printJsonArray(json& jsonarr){
	for (auto eid = jsonarr.begin(); eid != jsonarr.end(); ++eid)
    {
    	cout<<eid.value();
    	cout<<"\n\n";
    }
}
/*
static size_t WriteCallback(void *contents,size_t size,size_t nmemb,void*userp){
((std :: string*)userp)->append((char*)contents,size*nmemb);
return size*nmemb;
}
string readBuffer;
*/

void getdatabase(){
	ifstream f2("secret.json");
    json credentialdataread = json::parse(f2);
    string databaseurlBase = credentialdataread["firebaseConfig"]["databaseURL"];
    string databaseurl = databaseurlBase+"K7APP/articleviews.json";






    const std::string url(databaseurl);

    CURL* curl = curl_easy_init();

    // Set remote URL.
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());

    // Don't bother trying IPv6, which would increase DNS resolution time.
    curl_easy_setopt(curl, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V4);

    // Don't wait forever, time out after 10 seconds.
    curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10);

    // Follow HTTP redirects if necessary.
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);

    // Response information.
    long httpCode(0);
    std::unique_ptr<std::string> httpData(new std::string());

    // Hook up data handling function.
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, callback);

    // Hook up data container (will be passed as the last parameter to the
    // callback handling function).  Can be any pointer type, since it will
    // internally be passed as a void pointer.
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, httpData.get());

    // Run our HTTP GET command, capture the HTTP response code, and clean up.
    curl_easy_perform(curl);
    curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &httpCode);
    curl_easy_cleanup(curl);

    if (httpCode == 200)
    {

        json myjsondata= json::parse(*httpData.get());
        cout<<myjsondata;

        
        cout<<"\n\n";



        
        
    }
    else
    {
        std::cout << "Couldn't GET from " << url << " - exiting" << std::endl;

    }



    
    
}

int main()
{	
	getdatabase();

	ifstream f("sort.json");
    json data = json::parse(f);
    json articlelist = data["listofarticles"];

    int articlecounter = articlelist.size();
    cout<<"Articles counted:";
    cout<<articlecounter<<"\n";
    bubbleSort(articlelist,articlecounter);
    data["listofarticles"]= articlelist;

    ofstream o("sort.json");
    o << setw(4) << data << endl;
	return 0;
}


/*
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <array>

using json = nlohmann::json;
using namespace std;

void bubbleSort(json& arr, int n)
{
	int i, j;
	for (i = 0; i < n - 1; i++)

		for (j = 0; j < n - i - 1; j++)
			if (arr[j]["points"] > arr[j + 1]["points"])
				swap(arr[j], arr[j + 1]);
}


void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}
void printJsonArray(json& jsonarr){
	for (auto eid = jsonarr.begin(); eid != jsonarr.end(); ++eid)
    {
    	cout<<eid.value();
    	cout<<"\n\n";
    }
}


int main()
{
	ifstream f("sort.json");
    json data = json::parse(f);
    json articlelist = data["listofarticles"];

    int articlecounter = articlelist.size();
    cout<<"Articles counted:";
    cout<<articlecounter<<"\n";
    bubbleSort(articlelist,articlecounter);
    data["listofarticles"]= articlelist;

    ofstream o("sort.json");
    o << setw(4) << data << endl;
	return 0;
}


*/