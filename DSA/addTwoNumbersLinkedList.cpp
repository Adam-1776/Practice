#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <iterator>
#include <algorithm>
#include <array>
using namespace std;
//https://leetcode.com/problems/add-two-numbers

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *beg = new ListNode(0); //In this implementation, I preemptively instantiate the next node
        ListNode *ans = beg; //This is the node pointer we actually work with
        ListNode *prev = nullptr;
        int carry=0;
        int one=0;
        int two=0;
        while(1){
            if(l1!=nullptr) {
                one=l1->val;
            }
            else one=0; //if l1 is null, it doesn't add anything
            if(l2!=nullptr) {
                two=l2->val;
            }
            else two=0; //l2 is null
            if(l1==nullptr && l2==nullptr){ //Returning sequence
                if(carry>0){
                    ans->val = carry;
                } //If there's a carry, we set the last element
                else{
                    prev->next=nullptr; //if there's no carry, we delete the last element
                    delete ans;
                }
                return beg;
            }
            if(l1!=nullptr) l1=l1->next;
            if(l2!=nullptr) l2=l2->next;
            if(one+two+carry<10){
                ans->val = one+two+carry; //We have already instantiated the current node, we just need to set its value
                cout<<"Adding "<<one+two+carry<<endl;
                carry = 0; //Reset the carry since the sum in this step was less than ten
                prev = ans;
                ans->next = new ListNode(0); //Preemtively instantiating the next node
                ans = ans->next;
            }
            else{
                int temp = (one+two+carry)%10; //Similar logic except we pass on the carry
                ans->val = temp;
                cout<<"Adding "<<temp<<endl;
                carry = 1;
                prev = ans;
                ans->next=new ListNode(0);
                ans = ans->next;
            }
        }
    }
int main(int argc, char **argv){
  /*
  In this problem, are given two linked lists. Each linked list represents a number.
  Inside each linked list, each element represents a single digit (0-9). Also, the digits are in reverse order
  Our job is to construct and return a new linked list that represents the sum of these two numbers.
  The linked list we make also follows the same format (one digit per element, reverse order)
  */
  return 0;

}
