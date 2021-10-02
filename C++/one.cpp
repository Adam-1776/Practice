#include <iostream>
#include <map>
#include <vector>
void square(int &n){n=n*n;return;} //Pass by reference using reference arguments
//square only accepts an lvalue, because &n needs a memory location. &n is an lvalue reference
//However, if the parameter was const int &n, then it would work since it's also compatible with rvalues
int rsquare(int &&n){return n*n;} //This function only accepts rvalues or 'temporary' lvalues
//The double ampersands in int &&n denotes an rvalue.
int globalInt=0;
int &func1(){return globalInt;} //return by reference
//returns a reference to the global variable in this case. Return by reference is handy when a resource controlled
//by the function needs to manipulated within the calling function, such as func1()=10;
int *func2(){return &globalInt;} //function that returns pointer to globalInt

int main(){
int num {8};
int arr[10] {2,2,2,2,2,2,2,2,2,2};

for(auto x:arr) ++x; //This does NOT change anything in the array, because each element of the arrays is copied to x.
                     //You are only incrementing the copy x, not the actual array elements.
for(auto x:arr) std::cout<<x<<" "; std::cout<<"\n"; //Printing the array again

for(auto &x:arr) ++x; //This time, x refers to the actual array elements. & means "reference to" and doesn't require * to access value
for(auto x:arr) std::cout<<x<<" "; std::cout<<"\n"; //This time, the values did actually increase

//The & means different things when it's in a declaration vs an expression
//declaration is when you create the variable in the first place like int a=5;
//expression is when you use it like ++a;
//In an expression, it's denotes "address of"
//In a declaration, it creates an alias variable, or reference variable
//This can be used in place of pointers to manipulate variables using a different function
//Unlike pointers, you do not need to deference it using *
int &j=num;
++j;
std::cout<<j<<" "<<num<<"\n"; //J is an alias or reference variable of num, so manipulating j is the same as manipulating num
square(num); //This will actually modify num (and thus j) since square() accepts a alias variable
std::cout<<j<<" "<<num<<"\n"; //It has been squared
//rsquare(j); //Error since j is an lvalue
//rsquare(num); //Error since num is an lvalues
std::cout<<rsquare(7)<<std::endl; //This will work since 7 is an rvalue
//const means the value is determined at runtime and cannot be modified after that
//constexpr means the value is determined during compile time

int *p=NULL;
func1()=func1()+10; //adding ten to globalInt using return by reference
func1()=func1()+10; //adding ten more
std::cout<<globalInt<<std::endl;

p=func2(); //p is an integer pointer that now points towards globalInt
(*p)++; //incrementing globalInt
std::cout<<globalInt<<std::endl;

using userId=int; //type aliasing. userId is a new type that is equivalent to an integer. Similar to typedef
using userStrings=std::map<userId, std::vector<std::string>>; //userStrings is a new type that maps each
//userId (integer) to a vector of strings.
userId Adam=8; //Adam is an lvalue (it has a memory location). 8 is an rvalue (temporary data that hasn't have a memory location)
//You cannot do 8=Adam or square(8) because square only accepts lvalues. Because square modifies the memory the variable is stored in
square(Adam); //Note how square() accepts Adam even though it's type is userId, since it's an alas of int
std::cout<<Adam<<std::endl; //type aliasing is especially handly since it's compatible with template alias or generic alias


return 0;
}
