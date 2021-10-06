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

void merge(int arr[], int start, int mid, int end){
  if(end<start) return;
  int size1 = mid-start+1;
  int size2 = end-mid;
  int arr1[size1]={0};
  int arr2[size2]={0};
  for(int i=0;i<size1;++i) arr1[i]=arr[i+start];
  for(int i=0;i<size2;++i) arr2[i]=arr[i+mid+1];
  int Mindex=start;
  int index1=0;
  int index2=0;
  while(index1<size1 && index2<size2){
    if(arr1[index1]<arr2[index2]){
      arr[Mindex]=arr1[index1];
      ++Mindex;
      ++index1;
    }
    else{
      arr[Mindex]=arr2[index2];
      ++Mindex;
      ++index2;
    }
  }
  while(index1<size1){
    arr[Mindex]=arr1[index1];
    ++index1;
    ++Mindex;
  }
  while(index2<size2){
    arr[Mindex]=arr2[index2];
    ++index2;
    ++Mindex;
  }
  return;
}

void mergeSort(int arr[], int start, int end){ //Divide and conquer, O(nlogn) complexity
  if(end<=start) return;
  int mid=((end-start)/2)+start;
  mergeSort(arr,start,mid);
  mergeSort(arr,mid+1,end);
  merge(arr,start,mid,end);
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
  cout<<"Before Merge Sort\n";
  printArray(arr,cnt);
  cout<<"After Merge Sort\n";
  mergeSort(arr, 0, cnt-1);
  printArray(arr,cnt);
  return 0;

}