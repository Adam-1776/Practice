#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <iterator>
#include <deque>
using namespace std;

void printArray(int arr[], int n){
    for(int i=0;i<n;++i) cout<<arr[i]<<" ";
    cout<<endl;
}

void printdq(deque<int> g){
  for(auto itr = g.begin(); itr != g.end(); ++itr)
      cout << *itr <<" ";
  cout<<endl;
}


int main(int argc, char **argv){
  //dequeue is a double inded queue, and can thus be used as both a stack and a queue
  //Fairly efficient all around
  if(argc<2) {cout<<"Provide the input file as a command line argument"; return 0;}
  ifstream is(argv[1]);
  int cnt=0;
  int temp=0;
  is>>cnt;
  deque<int> dq; //Declaring an STL dequeue. Obviously, we do not specify the length.
  for(int i=0;i<cnt;++i){
    is>>temp;
    dq.push_back(temp); //Adding elements to the end of the list.
  }
  is.close();
  dq.push_front(77);
  dq.push_back(66);
  printdq(dq);

  cout<<"Popping rear element "<<dq.back()<<endl;
  dq.pop_back();
  cout<<"Popping first element "<<dq.front()<<endl;
  dq.pop_front();
  printdq(dq);

  return 0;
} 