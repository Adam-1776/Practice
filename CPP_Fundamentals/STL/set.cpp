#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <iterator>
#include <list>
using namespace std;

void printArray(int arr[], int n){
    for(int i=0;i<n;++i) cout<<arr[i]<<" ";
    cout<<endl;
}

void printSet(set<int> testSet){
  for(auto itr=testSet.begin();itr!=testSet.end();++itr)
    cout<<*itr<<" ";
  cout<<endl;
}


int main(int argc, char **argv){
  if(argc<2) {cout<<"Provide the input file as a command line argument"; return 0;}
  ifstream is(argv[1]);
  int cnt=0;
  int temp=0;
  is>>cnt;
  set<int> testSet; //Declaring an STL set. Obviously, we do not specify the length.
  for(int i=0;i<cnt;++i){
    is>>temp;
    testSet.insert(temp); //Adding elements to the end of the list.
  }
  is.close();
  printSet(testSet); //Notice how the set automatically stores values in sorted order
  testSet.insert(11); //Doesn't get inserted since 11 is already present
  testSet.erase(11); //Elements cannot be modified, only inserted and deleted
  if(testSet.find(11)==testSet.end()) cout<<"testSet doesn't contain value 11"<<endl;
  
  //Overall, set and multiset are very similar to map and multimap respectively, except the keys exist on their own instead
  //of being mapped to another value
  //The syntax of unordered_set is identical to set. Only difference is that unordered_set does not guarantee any order

  return 0;
} 
