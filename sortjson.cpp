#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <array>
#include <string>
#include <sstream>

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
	ifstream f2("secret.json");
    json credentialdataread = json::parse(f2);
    string databaseurl = credentialdataread["firebaseConfig"]["databaseURL"];
    cout<<databaseurl<<"\n";

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