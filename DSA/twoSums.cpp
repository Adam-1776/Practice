#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <iterator>
#include <algorithm>
#include <array>
using namespace std;

void printVector(vector<int> vec){
    for(int i=0;i<vec.size();++i)
      cout<<vec[i]<<" ";
    cout<<endl;
}

vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> vec;
        map<int,int> keepTrack;
        int temp;
        for(int i=0;i<nums.size();++i){
            keepTrack.insert(pair<int,int>(nums[i],i));
        }
        for(int i=0;i<nums.size();++i){
            temp=target-nums[i];
            auto found = keepTrack.find(temp);
            if(keepTrack.find(temp)!=keepTrack.end() && keepTrack.find(temp)->second!=i){
                vec.push_back(i);
                vec.push_back(keepTrack.find(temp)->second);
                return vec;
            }
        }
        return vec;
    }
//In this problem we use map because we need to return the indices. If we only needed
//to return the actual numbers, we could use a set
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
  int target=29;
  vector<int> ans = twoSum(nums,target);
  printVector(ans);
  return 0;

}
