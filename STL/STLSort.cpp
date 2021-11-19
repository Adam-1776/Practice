#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <iterator>
#include <algorithm>
#include <array>
using namespace std;

void printArray(int arr[],int cnt){
    for(int i=0;i<cnt;++i) cout<<arr[i]<<" ";
    cout<<endl;
}

void printVector(vector<int> vec){
    for(int i=0;i<vec.size();++i)
      cout<<vec[i]<<" ";
    cout<<endl;
}

bool compareInts(int one, int two){
  if(one<two) return false;
  else return true;
}


int main(int argc, char **argv){
  if(argc<2) {cout<<"Provide the input file as a command line argument"; return 0;}
  ifstream is(argv[1]);
  int cnt=0;
  int temp=0;
  is>>cnt;
  int arr[cnt];
  vector<int> vec;
  for(int i=0;i<cnt;++i){
    is>>temp;
    arr[i]=temp;
    vec.push_back(temp);
  }
  is.close();
  cout<<"Before STL Sort\n";
  printArray(arr,cnt);
  printVector(vec);
  cout<<"After STL Sort\n";
  sort(arr,arr+cnt);
  //sort(arr,arr+cnt,compareInts); This will sort in descending order. Third optional parameter is bool function
  sort(vec.begin(),vec.end());
  printArray(arr,cnt);
  printVector(vec);
  return 0;

}
