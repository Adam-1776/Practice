#include <iostream>
#include <memory>

class Rectangle{
private:
  int *length;
  int *breadth;
public:
  Rectangle(const int l=0,const int b=0){ //Constructor
    length=new int; *length=l;
    breadth=new int; *breadth=b;
  }
  ~Rectangle(){ //Destructor
    if(length!=nullptr&&breadth!=nullptr)
      std::cout<<"Destroying Rectangle with l="<<*length<<" and b="<<*breadth<<std::endl;
    else
      std::cout<<"Destroying hollow Rectangle"<<std::endl;
    delete length; delete breadth;
  }
  Rectangle(const Rectangle &r){ //Copy constructor
    std::cout<<"Copying Rectangle with l="<<*r.length<<" and b="<<*r.breadth<<std::endl;
    length=new int; *length=*r.length;
    breadth=new int; *breadth=*r.breadth;
  }
  Rectangle(Rectangle &&r){//Move constructor
    length=r.length;
    r.length=nullptr;
    breadth=r.breadth;
    r.breadth=nullptr;
    std::cout<<"Moved!\n";
  }
  Rectangle operator +(const Rectangle &r){ //Adder
    return Rectangle(*length+*r.length,*breadth+*r.breadth);
  }
  Rectangle &operator =(const Rectangle &r){ //Assignment operator
    if(this!=&r){
      *length=*r.length;
      *breadth=*r.breadth;
    }
    return *this;
  }
  Rectangle &operator =(Rectangle &&r){ //Move Assignment
    if(this==&r) return *this;
    delete length; length=r.length; r.length=nullptr;
    delete breadth; breadth=r.breadth; r.breadth=nullptr;
    std::cout<<"Move Assignment!\n";
    return *this;
  }
  int area(){
    return (*length)*(*breadth);
  }
  friend std::ostream &operator <<(std::ostream &out, const Rectangle &r);
};

std::ostream &operator <<(std::ostream &out, const Rectangle &r){
  if(r.length==nullptr||r.breadth==nullptr){out<<"printing null object"<<std::endl; return out;}
  out<<"length is "<<*r.length<<" and breadth is "<<*r.breadth<<std::endl;
  return out;
}

int main(){
  Rectangle r1(5,6);
  Rectangle r11(3,4);
  std::cout<<r1;
  //Rectangle r2=r1; //This invokes copy constructor which is NOT the same thing as assignment operator
  //Rectangle r2; r2=std::move(r1);  //This invokes move assignment operator, which we have to define by overloading =
  //Rectangle r2=std::move(r1); //Invokes move constructor
  Rectangle r2; r2=r1+r11; //Invokes move assignment since r1+r11 is an rvalue
  std::cout<<r2;
  std::cout<<r1;

return 0;
}
