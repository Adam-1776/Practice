#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <iterator>
#include <algorithm>
#include <array>
using namespace std;

void printArray(array<int,6> arr){ //The size of STL arrays are totally constant
    for(int i=0;i<arr.size();++i) cout<<arr[i]<<" "; //The size can be retrieved using size()
    cout<<endl;
}

int main(int argc, char **argv){
  if(argc<2) {cout<<"Provide the input file as a command line argument"; return 0;}
  ifstream is(argv[1]);
  int cnt=0;
  int temp=0;
  is>>cnt;
  array <int, 6> arr; //Declaring an STL array, the length has to be compile-time constant.
  for(int i=0;i<cnt;++i){
    is>>temp;
    arr[i]=temp;
  }
  is.close();
  printArray(arr);
  
  return 0;

}