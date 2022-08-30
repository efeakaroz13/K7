#include <iostream>
#include <cstring>




using namespace std;
string title;
void splitstr(string str, string deli = " ")
{
    int start = 0;
    int end = str.find(deli);
    while (end != -1) {
        string myvar =str.substr(start, end - start);
        if (myvar.size()>3){
        	title = myvar;
        }
        start = end + deli.size();
        end = str.find(deli, start);
    }
    //title = str.substr(start, end - start);
}


int main(){

	

	string mystring = "<title>Hello</title>";
	
	splitstr(mystring, "<title>");
	splitstr(title, "</title>");
	cout<<title<<"\n";
	
}
