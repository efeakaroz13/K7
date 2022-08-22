#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <array>

using json = nlohmann::json;
using namespace std;


int main(void) {

    ifstream f("sort.json");
    json data = json::parse(f);
    json articlelist = data["listofarticles"];
    int articlecounter = articlelist.size();
    cout<<"Articles counted:";
    cout<<articlecounter<<"\n";



    // for (auto it = articlelist.begin(); it != articlelist.end(); ++it) {
        
    //     cout<<it.value()<<"\n";
    // }
    for (auto eid = articlelist.begin(); eid != articlelist.end(); ++eid)
    {
        json elem = eid.value();
        int n = sizeof(articlelist)/sizeof(articlelist[0]);
        int indexof = 0;
        while (indexof < n)
        {
            if (articlelist[indexof] == elem) {
                break;
            }
            indexof++;
        }
        cout<<indexof<<"\n";
    }

    
}