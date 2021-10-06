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

void partition(int arr[], int start, int mid, int end){

  return;
}

void quickSort(int arr[], int start, int end){ //Divide and conquer, O(nlogn) complexity

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
  cout<<"Before Quick Sort\n";
  printArray(arr,cnt);
  cout<<"After Quick Sort\n";
  quickSort(arr, 0, cnt-1);
  printArray(arr,cnt);
  return 0;

}
