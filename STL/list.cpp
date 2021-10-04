#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <iterator>
#include <list>
using namespace std;

void printArray(int arr[], int n){
    for(int i=0;i<n;++i) cout<<arr[i]<<" ";
    cout<<endl;
}

void printList(list <int> g){
  for(auto itr = g.begin(); itr != g.end(); ++itr)
      cout << *itr <<" ";
  cout<<endl;
}

void printList2(list<int> g){
  auto itr=g.begin();
  for(int i=0;i<g.size();++i){
    cout<<*itr<<" ";
    ++itr;
  }
}

int main(int argc, char **argv){
  //lists are STL implementation of linked list, therefore, it does not have random access
  //But elements can be inserted or deleted at any point efficiently, since memory is not contiguous
  if(argc<2) {cout<<"Provide the input file as a command line argument"; return 0;}
  ifstream is(argv[1]);
  int cnt=0;
  int temp=0;
  is>>cnt;
  list<int> linkedList; //Declaring an STL list. Obviously, we do not specify the length.
  for(int i=0;i<cnt;++i){
    is>>temp;
    linkedList.push_back(temp); //Adding elements to the end of the list.
  }
  is.close();
  linkedList.push_front(7); //We can efficiently add an element to the beginning of the list
  printList(linkedList);

  auto itr = linkedList.begin(); //creating iterator pointing towards first element
  advance(itr,2); //We increment it twice, so that it points to the third element
  linkedList.insert(itr,14); //Insert 14 as third element in list (displaces subsequent elements)
  printList(linkedList);

  cout<<"Popping last element "<<linkedList.back()<<endl; //Removing last element
  linkedList.pop_back();
  cout<<"Popping first element "<<linkedList.front()<<endl; //Removing first element
  linkedList.pop_front();
  printList(linkedList);

  linkedList.sort();
  linkedList.reverse(); //We can readily sort or reverse the contents of the linked list
  linkedList.resize(10,99); //Resize list to ten elements, fill newly created spots, if any, with 99 
  printList2(linkedList);

  return 0;
} 