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
        cout << itr->first <<" "<< itr->second << '\n';
  }
  cout<<endl;
  if(testMap.count('C')!=0){ //You can use count to determine whether a key is present. Since keys are unique, it returns 0 or 1
    testMap['C']++; //You can access values using this syntax too
    cout<<testMap.find('C')->second<<endl; //find() returns an iterator to the position of the key
  }
  testMap.erase('C'); //erase() accepts either an iterator or a const key value
  if(testMap.find('C')==testMap.end()) cout<<"Couldn't find it\n"; //If the key isn't there, it returns an iterator equaling end()
  //The above if condition is equivilant to if(testMap.count('C')==0)
  cout<<"size = "<<testMap.size()<<", maxsize = "<<testMap.max_size()<<endl; //Getting size of map



  map<char, int[1000]> mapArray;  //Dealing with an a map that store an array for each key
  mapArray['A'][0]=5;
  mapArray['A'][1]=4;
  mapArray.at('A')[2]=2;
  printArray(mapArray['A'],3);


  return 0;

}