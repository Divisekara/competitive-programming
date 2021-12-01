// classes is a suitable way to group bunch of functions, variables together

// following is the way to declare a class
// inside the curly braces you have the body of the class.

#include <iostream>

using namespace std;

class AsithaClass // it is good practice to start the name of the class with capital letter and then camel case convention
{
public:
    void coolSaying()
    {
        cout << "This is awesome man." << endl;
    }
};

// access specifiers or access modifiers are keywords in object oriented languages that set the acccessibility
// of classes methods and other members
// if you want to use the function defined inside the class to use in the main function then
// you need to make the class public and if not you need to make this function private
// whenever you use the public specifiers then you can use it outside the class as well.

int main()
{
    AsithaClass
}
