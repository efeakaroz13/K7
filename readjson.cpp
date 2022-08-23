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
    int counter1 = 0;
    int counter2 = 0;
    for (auto eid = articlelist.begin(); eid != articlelist.end(); ++eid)
    {
        json elem1 = articlelist[counter1];
        
        counter1 +=1;
        for (auto eid2 = articlelist.begin(); eid2 != articlelist.end(); ++eid2){
                json elem = articlelist[counter2];
                counter2 += 1;
                cout<<elem<<"\n\n";
                if (articlelist[counter2] == articlelist.size()-1)
                {
                    cout<<" ";
                }else
                {
                    if (articlelist[counter2]["points"]<articlelist[counter2+1]["points"] )
                    {
                        json oldvalue1 = articlelist[counter2]["points"];
                        json oldvalue2 = articlelist[counter2+1]["points"];
                        articlelist[counter2] = oldvalue2;
                        articlelist[counter2+1] = oldvalue1;
                        
                    }
                    
                }
                
                
                
            }
        counter2 = 0;    

    }
    cout<<articlelist<<"\n===============\n";
    
}