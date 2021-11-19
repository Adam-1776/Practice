#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <iterator>
#include <map>
#include <algorithm>
#include <array>
using namespace std;

void printArray(int arr[], int n){
    for(int i=0;i<n;++i) cout<<arr[i]<<" ";
    cout<<endl;
}

void printVectorItr(vector<int> vec){
  for(auto itr=vec.begin();itr!=vec.end();++itr)
    cout<<*itr<<" ";
  cout<<endl;
}

void printMultiMap(multimap<string,int> Map){
  for(auto itr=Map.begin(); itr!=Map.end(); ++itr)
    cout<<itr->first<<" "<<itr->second<<endl;
  cout<<endl;
}

int main(int argc, char **argv){
  multimap <string, int> testMap; //Declaring STL multimap
  testMap.insert(pair<string,int>("First",1));
  testMap.insert(pair<string,int>("Second",2));
  testMap.insert(pair<string,int>("Third",3));
  testMap.insert(pair<string,int>("First",4)); //Inserting another key-value pair with key First. Allowed in multimap, not in map
  printMultiMap(testMap); //Notice how the second pair is First and 4, even though they were inserted last
  //This is because multimap keeps keys in sorted order (sorted alphabetically and then by order of insertion, in this case)
  testMap.insert(pair<string,int>("Aa",6));
  testMap.insert(pair<string,int>("Aa",5));
  testMap.insert(pair<string,int>("Third",3));
  testMap.insert(pair<string,int>("Third",6));
  testMap.insert(pair<string,int>("Third",7));
  printMultiMap(testMap); //Notice how the two Aa pairs now print first
  cout<<"Number of Aa keys = "<<testMap.count("Aa")<<endl<<endl;
  
  for(auto itr=testMap.lower_bound("Third"); itr!=testMap.upper_bound("Third"); ++itr)
    cout<<itr->second<<"\n"; //Printing all values with key "Third"
  cout<<endl;

} 