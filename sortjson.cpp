#include <fstream>
#include <iostream>
#include <ostream>
#include <nlohmann/json.hpp>
#include <array>
#include <string>
#include <sstream>
#include <curl/curl.h>
#include <time.h>
#include <algorithm> 
#include <chrono>

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

void getdatabase(){
	ifstream f2("secret.json");
    json credentialdataread = json::parse(f2);
    string databaseurlBase = credentialdataread["firebaseConfig"]["databaseURL"];
    string databaseurl = databaseurlBase+"K7APP.json";






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
        json articlearray = myjsondata["articleviews"];
        int databasecounter = articlearray.size();
        cout<<"\n";

        for (auto eid = articlearray.begin(); eid != articlearray.end(); ++eid)
        {

            time_t curtime;
            struct tm nowLocal;
            curtime =time(NULL);
            float timefloat = curtime*1.0f;



            json articledataitself = myjsondata["articleviews"][eid.key()];
            string article = articledataitself["article"];
            float timedatabase = articledataitself["lastsaved"];
            remove(article.begin(), article.end(), ' ');
            float articlepoints = article.size()/100.0f;
            
            float viewspoints = myjsondata["articleviews"][eid.key()]["views"].size();
            float durationbetweenpublishandnow = timefloat-timedatabase;
            if(durationbetweenpublishandnow<86400){
                cout<<"Today\n";
            }
            if(durationbetweenpublishandnow<604800){
                cout<<"This week\n";
            }else{
                cout<<"More than one week\n";
            }

            cout<<"ARTICLE "<<eid.key()<<" |\n";
            cout<<"Time since it written(seconds):"<<durationbetweenpublishandnow<<"\n";
            cout<<"Points for text:"<<articlepoints<<"\n\n";

            cout<<"\n";
        }
        
        int i;
        cout<<databasecounter;
        
        cout<<"\n\n";



        
        
    }
    else
    {
        std::cout << "ERR | DATABASE LOAD FAILED  " << url << " - exiting\n" << std::endl;

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