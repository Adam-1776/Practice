#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <iterator>
#include <algorithm>
#include <array>
using namespace std;
//https://leetcode.com/problems/minimum-absolute-difference
void printVector(vector<int> vec){
    for(int i=0;i<vec.size();++i)
      cout<<vec[i]<<" ";
    cout<<endl;
}

vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
    vector<vector<int>> vec;
    sort(arr.begin(),arr.end()); //Sorting makes things much more efficient
    //since it guarantees that elements with the smallest absolute difference will be adjacent
    //We can thus find all pairs with minimum difference linearly
    int smallest=9999;
    for(int i=0;i<arr.size()-1;++i){
        if(arr[i+1]-arr[i]<smallest){
            smallest=arr[i+1]-arr[i];
            vec={}; //Clear out vector if new minimum absolute difference has been found
            vec.push_back({arr[i],arr[i+1]}); //Push back a new vector containing the newly found pair into the empty vector
        }
        else if(arr[i+1]-arr[i]==smallest){
            vec.push_back({arr[i],arr[i+1]}); //Push back the next minimum difference pair
        }
        else{
            continue;
        }
    }
    return vec;
}

//In this problem, find the minimum absolute difference between any pair of integers in a vector.
//Then, return a list of pairs whose absolute difference is this minimum
int main(int argc, char **argv){
  if(argc<2) {cout<<"Provide the input file as a command line argument"; return 0;}
  ifstream is(argv[1]);
  int cnt=0;
  int temp=0;
  is>>cnt;
  vector<int> nums;
  for(int i=0;i<cnt;++i){
    is>>temp;
    nums.push_back(temp);
  }
  is.close();
  vector<vector<int>> ans = minimumAbsDifference(nums);
  //printVector(ans); Not gonna work since the return is a 2D vector
  return 0;

}
