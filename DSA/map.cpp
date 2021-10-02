#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
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
  printArray(arr,cnt);
  return 0;

}