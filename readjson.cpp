#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
using json = nlohmann::json;

int main(void) {
    std::ifstream f("sort.json");
    json data = json::parse(f);
    std::cout<< data;
}