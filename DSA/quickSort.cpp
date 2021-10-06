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
    return;
}

void swap(int &one, int &two){
  int temp=one;
  one=two;
  two=temp;
  return;
}

int partition(int arr[], int start, int end){ //Put all elements less than partition behind it, and the rest ahead of it
  int pivot=arr[end];
  int j=start-1;
  for(int i=start;i<=end-1;++i){
    if(arr[i]<pivot)
      swap(arr[++j],arr[i]);
  }
  swap(arr[++j],arr[end]);
  return j;
}

void quickSort(int arr[], int start, int end){ //Divide and conquer, O(nlogn) complexity. In-place, so doesn't use much memory
  if(start>end) return;
  int p=partition(arr,start,end);
  quickSort(arr,start,p-1);
  quickSort(arr,p+1,end);
  return;
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
  quickSort(arr,0,cnt-1);
  printArray(arr,cnt);
  return 0;

}
