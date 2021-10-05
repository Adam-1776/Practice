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

void swap(int &one, int &two){
  int temp=one;
  one=two;
  two=temp;
}

void selectionSort(int arr[], int cnt){
  int minIndex; //N^2 time complexity in all cases, and at most N swaps. O(1) space complexity (in-place)
  for(int i=0;i<cnt;++i){ //Not stable in its basic form
    minIndex=i;
    for(int j=i;j<cnt;++j){
      if(arr[j]<arr[minIndex]){
        minIndex=j;
      }
    }
    swap(arr[i],arr[minIndex]);
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
  cout<<"Before Selection Sort\n";
  printArray(arr,cnt);
  cout<<"After Selection Sort\n";
  selectionSort(arr,cnt);
  printArray(arr,cnt);
  return 0;

}