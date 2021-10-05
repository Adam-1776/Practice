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

void rotateArray(int arr[], int cnt, int r){ //positive r to shift towards left
  int ret[cnt];                             //negative r to shift towards right
  if(r<0){r=cnt+r;}
  for(int i=0;i<cnt;++i){
    ret[i]=arr[(i+r)%cnt];
  }
  for(int i=0;i<cnt;++i){
    arr[i]=ret[i];
  }
  return ;
}

int main(int argc, char **argv){
  if(argc<2) {cout<<"Provide the input file as a command line argument"; return 0;}
  ifstream is(argv[1]);
  int cnt=0;
  int temp=0;
  is>>cnt;
  int arr[cnt];
  for(int i=0;i<cnt;++i){
    is>>temp;
    arr[i]=temp;
  }
  is.close();
  cout<<"Before rotation\n";
  printArray(arr,cnt);
  cout<<"After rotating to the left by one\n";
  rotateArray(arr,cnt,1);
  printArray(arr,cnt);
  return 0;

}