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

class node{
  private:
    int data;
  public:
    node *left;
    node *right;
    node(){
      data=-1;
      left=NULL;
      right=NULL;
    }
    node(int n){
      data=n;
      left=NULL;
      right=NULL;
    }
    int getData(){
      return data;
    }
    void setData(int n){
      data=n;
      return;
    }
    void printChildren(){
      if(left==NULL && right==NULL)
        cout<<"It is a leaf node";
      if(left!=NULL)
        cout<<"Left child is "<<left->getData()<<". ";
      if(right!=NULL)
        cout<<"Right child is "<<right->getData()<<".";
      cout<<endl;
    }
};

class BST{
  private:
    node *root;
    int numNodes;
  public:
    BST(){
      root=NULL;
      numNodes=0;
    }
    node* getRoot(){
      return root;
    }
    int size(){
      return numNodes;
    }
    node* find(int n){
      node *curNode=root;
      while(curNode!=NULL){
        if(curNode->getData()>n)
          curNode=curNode->left;
        else if(curNode->getData()<n)
          curNode=curNode->right;
        else
          return curNode;
      }
      return NULL;
    }
    node* insert(int n){
      cout<<"Inserting "<<n<<endl;
      if(root==NULL){
        root=new node(n);
        return root;
      }
      else{
        node *curNode=root;
        while(1){
          if(curNode->getData()>n){
            if(curNode->left!=NULL){
              curNode=curNode->left;
            }
            else{
              curNode->left=new node(n);
              ++numNodes;
              return curNode->left;
            }
          }
          else if(curNode->getData()<n){
            if(curNode->right!=NULL){
              curNode=curNode->right;
            }
            else{
              curNode->right=new node(n);
              ++numNodes;
              return curNode->right;
            }
          }
          else return curNode;
        }
      }
    }
    void preorder(node *curNode=NULL, bool recurse=false){
      if(recurse==false && curNode==NULL) curNode=root;
      if(curNode==NULL) return;
      cout<<curNode->getData()<<" ";
      preorder(curNode->left,true);
      preorder(curNode->right,true);
    }
    void inorder(node *curNode=NULL, bool recurse=false){
      if(recurse==false && curNode==NULL) curNode=root;
      if(curNode==NULL) return;
      preorder(curNode->left,true);
      cout<<curNode->getData()<<" ";
      preorder(curNode->right,true);
    }
    void postorder(node *curNode=NULL, bool recurse=false){
      if(curNode==NULL && recurse==false) curNode=root;
      if(curNode==NULL) return;
      preorder(curNode->left,true);
      preorder(curNode->right,true);
      cout<<curNode->getData()<<" ";
    }
};

int main(int argc, char **argv){
  if(argc<2) {cout<<"Provide the input file as a command line argument"; return 0;}
  ifstream is(argv[1]);
  int cnt=0;
  int temp=0;
  is>>cnt;
  BST tree;
  for(int i=0;i<cnt;++i){
    is>>temp;
    tree.insert(temp);
  }
  is.close();
  cout<<"Printing Inorder Traversal\n";
  tree.inorder(); cout<<endl;
  temp=6;
  cout<<"Finding node "<<temp<<endl;
  node* curNode=tree.find(temp);
  cout<<"Found node "<<curNode->getData()<<". "; curNode->printChildren();
  return 0;

}
