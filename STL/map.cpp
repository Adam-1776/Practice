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

int main(int argc, char **argv){
  if(argc<2) {cout<<"Provide the input file as a command line argument"; return 0;}
  ifstream is(argv[1]);
  int cnt=0;
  int temp=0;
  is>>cnt;
  int arr[cnt]={0};
  for(int i=0;i<cnt;++i){
    is>>temp;
    arr[i]=temp;
  }
  is.close();


  char letter = 'A';
  map<char, int> testMap;
  for(int i=0;i<cnt;++i){
      testMap.insert(pair<char, int>(letter, arr[i]));
      ++letter;
  }
  testMap['G']=99; //You can also insert key value pairs using this syntax
  cout<<"Printing testMap\n";
  map<char, int>::iterator itr;
  for(itr = testMap.begin(); itr != testMap.end(); ++itr) { //Using iterators to print contents of Map
        cout << itr->first <<" "<< itr->second << "\n";
  }
  cout<<endl;
  if(testMap.count('C')!=0){ //You can use count to determine whether a key is present. Since keys are unique, it returns 0 or 1
    testMap['C']++; //You can access and change values using this syntax too
    cout<<"Found key C in testMap with value = "<<testMap.find('C')->second<<endl;
    //find() returns an iterator to the position of the key
  }
  testMap.erase('C'); //erase() accepts either an iterator or a const key value
  if(testMap.find('C')==testMap.end()) cout<<"Couldn't find key C\n"; //If the key isn't there, it returns an iterator equaling end()
  //The above if condition is equivilant to if(testMap.count('C')==0)
  cout<<"size of testMap = "<<testMap.size()<<", maxsize = "<<testMap.max_size()<<endl<<endl; //Getting size of map


  map<char, int[1000]> mapArray;  //Dealing with an a map that stores an array for each key
  mapArray['A'][0]=5;
  mapArray['A'][1]=4;
  mapArray.at('A')[2]=2;
  cout<<"mapArray = "; printArray(mapArray['A'],3);
  cout<<endl;


  map<string, vector<int>> mapVector; //Dealing with a map that a vector for each key string
  vector<int> vec= {1,2,3};
  mapVector.insert(pair<string,vector<int>>("First",vec)); //Mapping vec to key string First
  mapVector.at("First").push_back(4); //Adding element 4 to end of vector mapped to First
  mapVector.at("First").insert( mapVector.at("First").begin(),8); //Adding element 8 to beginning of this vector
  vec.clear(); //Deleting all data held in vec, thus resetting its size to zero
  vec.push_back(99);
  mapVector["Second"]=vec;
  cout<<"mapVector[First] = "; printVectorItr(mapVector["First"]);
  cout<<"mapVector[Second] = "; printVectorItr(mapVector.at("Second"));
  return 0;

}