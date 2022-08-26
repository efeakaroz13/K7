#include <fstream>
//Copyright (c) 2022 Efe Akaröz
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
    json newjsonarray = {};
    json arrayobj = json::array();
    newjsonarray["listofarticles"] = arrayobj;
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

    if (httpCode == 200)
    {
        
        json myjsondata= json::parse(*httpData.get());
        json articlearray = myjsondata["articleviews"];
        int databasecounter = articlearray.size();
        cout<<"\n";

        for (auto eid = articlearray.begin(); eid != articlearray.end(); ++eid)
        {
            if(myjsondata["articleviews"][eid.key()]["visibility"]=="public"){
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
                
                bool today;
                bool thisweek;
                if(durationbetweenpublishandnow<86400){

                    today = true;
                    thisweek = false;

                }else if(durationbetweenpublishandnow<604800){

                    today = false;
                    thisweek = true;

                }else{

                    today = false;
                    thisweek = false;

                }

                float viewspointsnew;

                if(today==true){
                    viewspointsnew = viewspoints*0.1f+viewspoints*0.2f;
                }
                else if(thisweek==true){
                    viewspointsnew = viewspoints*0.1f+viewspoints*0.1f;

                }else{
                    viewspointsnew = viewspoints*0.1f;
                }
               
                float totalpoints = viewspointsnew+articlepoints;
                cout<<"Points for article:"<<totalpoints<<"\n\n";
                myjsondata["articleviews"][eid.key()]["points"] = totalpoints;
                newjsonarray["listofarticles"].push_back(myjsondata["articleviews"][eid.key()]);
            }
        }
        ofstream c("sort.json");
        c << setw(4) << newjsonarray << endl;
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