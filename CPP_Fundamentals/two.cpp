#include <iostream>
#include <memory>

class Rectangle{
  int length; //private by default
  int breadth;
  public:
  Rectangle(int l=0,int b=0): length{l}, breadth{b} {} //You may assign values in constructor this way
  ~Rectangle(){std::cout<<"Destroying Rectangle with l="<<length<<" and b="<<breadth<<std::endl;}
  Rectangle(const Rectangle &r){length=r.length; breadth=r.breadth;} //Copy constructor
  //in copy constructor the function parameter is rhs, lhs actually calls the function
  //alternatively, the first paraameter may the lhs and second parameter may be the rhs in a free function
  Rectangle &operator =(const Rectangle &r){
    if(this!=&r){length=r.length; breadth=r.breadth;}
    return *this;
  }
  Rectangle operator +(const Rectangle &r){return Rectangle(length+r.length,breadth+r.breadth);}
  int area(){return length*breadth;}                    //constructor in this manner
  friend std::ostream &operator <<(std::ostream &out, const Rectangle &r); //Need to specify it as a
};   //friend since the function is defined outside the class and needs to access private variables

std::ostream &operator <<(std::ostream &out, const Rectangle &r){ //Overloading << operator for Rectangle
  out<<"length is "<<r.length<<" and breadth is "<<r.breadth<<std::endl; //Notice how it's defined outside the class
  return out; //Can access private variables since it's a friend function
}

int main(){
Rectangle r1(3,4); //Declaring a Rectangle object the old fashioned way
//Rectangle r11=r1; //Copy constructor will be called
Rectangle r11; r11=r1; //Invokes assignment operator
r11=r1+r11; //Invokes our + operator overload
std::cout<<r11; //works as you expect

std::shared_ptr<Rectangle> r2(new Rectangle(5,6)); //r2 is a smart pointer that points to a Rectangle r2
std::cout<<*r2; //since r2 is a pointer, we need to deference it before passing it to our << function
//r2 is a unique_ptr, so it is the only pointer that can point to that particular Rectangle instance

std::unique_ptr<Rectangle> r3 = std::make_unique<Rectangle>(7,8); //r3 is similar to r2, but it is initialized
std::cout<<*r3;  //using make_unique. Note how the constructor Rectangle() isn't explicitly called
//overall, make_unique is a more sophisticated way of declaring an object than the new keyword.
//Because this is a smart pointer, any memory used in the heap will automatically be deallocated when it goes out of scope
//make_unique can avoid memory leakage even when an unexepected exception or error occurs (memory leak)

std::shared_ptr<Rectangle> r4;
r4=r2;  //This is allowed since r2 and r4 are shared_ptr, so multiple pointers can point towards the same object
std::cout<<r2.use_count()<<" "<<r4.use_count()<<std::endl; //Print how many pointers are pointing towards the object
// r4=r3; //This is not allowed becaues r3 is a unique_ptr, so no other pointer is allowed to point towards the object r3 points to
r4=std::move(r3); //We transfer ownership of the Rectangle object pointed to by r3 to r4. r3 now points to nothing
std::cout<<*r4;

return 0;
}
