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

void insertionSort(int arr[], int n){ //Best case time is O(n), when element is already sorted
  int i; //For this reason, it may work well when an array is almost sorted
  int key;
  int j;
  for(i=1;i<n;i++){
    key=arr[i]; 
    j=i-1;
    while(j>=0 && arr[j]>key){
      arr[j+1]=arr[j];
      --j;
    }
    arr[j+1]=key;
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
  cout<<"Before Insertion Sort\n";
  printArray(arr,cnt);
  cout<<"After Insertion Sort\n";
  insertionSort(arr,cnt);
  printArray(arr,cnt);
  return 0;

}