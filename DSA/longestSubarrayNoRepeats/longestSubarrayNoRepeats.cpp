#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <iterator>
#include <algorithm>
#include <array>
using namespace std;
//https://leetcode.com/problems/longest-substring-without-repeating-characters/

int lengthOfLongestSubstring(string s) {
        int length=s.size();
        if(length==0) return 0;
        int i=0;
        int j=0;
        int longest=1;
        set<char> charSet;
        while(j<length){
            char r=s[j];
            while(charSet.find(r)!=charSet.end()){ //This while loop is key! If the next character in the right index isn't in the set, we move on
                char l=s[i]; //If we're in this loop, it's because the character at the right index already exists in the set
                charSet.erase(l); //We delete characters from the set as we move the left index forward. Obviously, the set should only represent characters in our window
                ++i; //We keep incrementing the left index until we reach the character equal to the upcoming right index
            } //At the end of this loop, i points to the index after the left repeating character
            charSet.insert(r);
            if(j-i+1>longest){
                longest=j-i+1;
            }
            ++j;
        }
        return longest;
    }

/*
Basically, when you find that the next character in the right index already exists in the set
We don't just move the left index one space. We need to keep moving it until we reach
the character that's causing the repetiton!
*/


//In this problem, we find the length of the longest substring that has all unique characters
int main(int argc, char **argv){
  string input = "aardvard";
  cout<<solution(input);
  return 0;

}
