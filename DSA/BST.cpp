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

struct Trunk{
  Trunk *prev;
  string str;
  Trunk(Trunk *prev, string str){
    this->prev=prev;
    this->str=str;
  }
};

void showTrunks(Trunk *p){
  if(p==nullptr){
      return;
  }
  showTrunks(p->prev);
  cout << p->str;
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
        cout<<"It is a leaf node.";
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
    node* find_parent(int n){
      node *curNode=root;
      node *lastNode=root;
      while(curNode!=NULL){
        if(curNode->getData()>n){
          lastNode=curNode;
          curNode=curNode->left;
        }
        else if(curNode->getData()<n){
          lastNode=curNode;
          curNode=curNode->right;
        }
        else
          return lastNode;
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
    node* find_successor(node *curNode){
      if(curNode->left!=NULL){
        curNode=curNode->left;
      }
      else return NULL;
      while(curNode->right!=NULL){
        curNode=curNode->right;
      }
      return curNode;
    }
    void remove(int n){
      node *curNode=find(n);
      if(curNode==NULL) return;
      if(curNode->left==NULL && curNode->right==NULL){
        curNode=find_parent(n);
        if(curNode->left->getData()==n){
          free(curNode->left);
          curNode->left=NULL;
          --numNodes;
          return;
        }
        if(curNode->right->getData()==n){
          free(curNode->right);
          curNode->right=NULL;
          --numNodes;
          return;
        }
      }
      else if(curNode->left==NULL && curNode->right!=NULL){
        curNode->setData(curNode->right->getData());
        free(curNode->right);
        curNode->right=NULL;
        --numNodes;
        return;
      }
      else if(curNode->left!=NULL && curNode->right==NULL){
        curNode->setData(curNode->left->getData());
        free(curNode->left);
        curNode->left=NULL;
        --numNodes;
        return;
      }
      else{
        node *successor=find_successor(curNode);
        int data=(successor->getData());
        //cout<<"Successor is "<<data<<endl;
        remove(data);
        curNode->setData(data);
        --numNodes;
        return;
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
      inorder(curNode->left,true);
      cout<<curNode->getData()<<" ";
      inorder(curNode->right,true);
    }
    void postorder(node *curNode=NULL, bool recurse=false){
      if(curNode==NULL && recurse==false) curNode=root;
      if(curNode==NULL) return;
      postorder(curNode->left,true);
      postorder(curNode->right,true);
      cout<<curNode->getData()<<" ";
    }
    void printTree(node* curNode=NULL, Trunk *prev=nullptr, bool isLeft=false, bool recurse=false){
      if(curNode==NULL && recurse==false) {curNode=root;}
      if(curNode==NULL || curNode==nullptr){
        return;
      }
      string prev_str = "    ";
      Trunk *trunk = new Trunk(prev, prev_str);
      printTree(curNode->right, trunk, true, true);
      if(!prev){
        trunk->str = "———";
      }
      else if(isLeft){
        trunk->str=".———";
        prev_str="   |";
      }
      else{
        trunk->str="`———";
        prev->str=prev_str;
      }
      showTrunks(trunk);
      cout<<curNode->getData()<<endl;
      if(prev){
        prev->str = prev_str;
      }
      trunk->str="   |";
      printTree(curNode->left, trunk, false, true);
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
  temp=14;
  //cout<<"Finding node "<<temp<<endl;
  //node* curNode=tree.find(temp);
  //cout<<"Found node "<<curNode->getData()<<". "; curNode->printChildren();
  cout<<"Printing Tree\n\n";
  tree.printTree();
  tree.remove(11);
  cout<<"\n\n";
  tree.printTree();
  return 0;

}
