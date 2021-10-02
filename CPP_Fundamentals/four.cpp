#include<iostream>
#include<iterator>
#include<vector>
#include<algorithm>
#include<array>
int main(){
  std::vector<int> ar={1,2,3,4,5}; //Declaring a new vector. Vectors are a type of container
  ar.push_back(6); //Adding integer 6 to the end
  std::vector<int>::iterator ptr; //Declaring a new vector iterator ptr
  for(ptr=ar.begin();ptr<ar.end();ptr++)
      std::cout<<*ptr<<" "; //Must print using *ptr since the iterator functions like a pointer
  std::cout<<std::endl;//ptr is now out of bounds of the vector size, we can reverse it
  ptr=std::prev(ptr,3); //prev returns a new iterator, taking an iterator and backing it up the number of time specified
  std::cout<<*ptr<<std::endl;
  std::advance(ptr,1); //ptr now points towards index 3, which contains integer 4 in this case
  ptr=std::next(ptr,1); //similar to advance, but it acts upon the iterator passed to the function instead of returning a new iterator
  std::cout<<*ptr<<std::endl;
  std::cout<<ar.size()<<std::endl; //size() returns the number of elements in the vector
  std::vector<int> ar1={10,20,30}; //New vector
  ptr=std::next(ar.begin(),1); //Setting ptr to the second element
  std::copy(ar1.begin(),ar1.end(),std::inserter(ar,ptr)); //Inserting ar1 starting from the second place in ar
  //inserter() returns an insert_iterator, allowig it to insert in the middle of the vector instead of overwriting
  //copy is an STL function that simply copies a range of elements from one container to another, overwriting them
  //copy takes iterator that points to beginning of source, iterator for end of source, and starting point of destination container
  ar.insert(ar.begin()+1,12); //vector.insert() allows you to insert element at location pointed to by iterator. Here, we insert 12 at second position
  for(int i:ar) std::cout<<i<<" "; //Quicker way to print vector if you know the underlying data type
  std::cout<<std::endl;
  std::cout<<ar.front()<<" "<<ar.back()<<std::endl; //vector.front() and .back() return first and last elements of the container
  std::cout<<"Arrays\n";
  std::array<int,10> a1; //declare STL array of size ten and type integer
  a1.fill(-1); //set all elements in a1 to 01;
  a1.at(2)=3; //array.at(index) is the best way to get an element
  a1[1]=4; //the old fashioned way also works
  auto p2=a1.end(); p2=std::prev(p2,2); //p2 is a pointer that now points towards the second last element of the array
  a1.back()=8; //array.back() and front() are lvalues, so they can be set
  std::cout<<*p2<<std::endl;
  *p2=13; //making the last element in array 13. The iterator is like a pointer, you can deference it to manipulate the actual element
  std::sort(a1.begin(),a1.end()); //Using std sort
  for(auto i:a1) std::cout<<i<<" ";
  std::cout<<std::endl;

  return 0;
}
