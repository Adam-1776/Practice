#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <iterator>
#include <algorithm>
#include <vector>
using namespace std;

void printVector(vector<int> vec){ //The number of elements is kept track inside the vector object,
    for(int i=0;i<vec.size();++i)
      cout<<vec[i]<<" "; //Get number of elements using size(). Can retrieve elements at index using [] syntax
    cout<<endl;
}

void printVectorItr(vector<int> vec){ //Printing vector using iterators
  for(auto itr=vec.begin();itr!=vec.end();++itr)
    cout<<*itr<<" "; //Use asterix to deference iterator to print it
  cout<<endl;
}

int main(int argc, char **argv){
  if(argc<2) {cout<<"Provide the input file as a command line argument"; return 0;}
  ifstream is(argv[1]);
  int cnt=0;
  int temp=0;
  is>>cnt;
  vector<int> vec; //Declaring STL vector
  for(int i=0;i<cnt;++i){
    is>>temp;
    vec.push_back(temp); //push_back adds an element to end of the vector
  }
  is.close(); 
  printVectorItr(vec);
  vec.resize(10,0); //Increase size (number of elements) to ten. If the current size is less than 10,
  //then append values of zero to the vector until its size is ten
  cout<<"Last element about to be popped is "<<vec.back()<<endl;
  vec.pop_back(); //Last element in the vector is deleted and the size has decreased to 9
  printVector(vec); 
  vec.insert(vec.begin()+2,5); //You can also insert elements in between a vector, and thus shifting the elements after the index
  //insert() accepts an iterator as its first parameter, and the value to be inserted as the second. Here we insert 5 at index 2
  vector<int> arr= {1,2,3};
  vec.insert(vec.end()-1,arr.begin(),arr.end()); //You can insert one vector into another, starting from any given index like this
  printVector(vec); //Here, we insert vector arr from the second last index
}