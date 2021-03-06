// classes is a suitable way to group bunch of functions, variables together

// when you create a file make sure to rename the file where no sapace is there.

// following is the way to declare a class
// inside the curly braces you have the body of the class.

#include <iostream>
#include <string> // in order to use the string variables we have to include the string file

using namespace std;

class AsithaClass // it is good practice to start the name of the class with capital letter and then camel case convention
{
public:
    string name; // this is not the correct way to make variables.
    // making class varibales under public is not a good practice.
    // whenever you make a variable under public it is vulnerable to the program to mess up.
    // best way to make the class variables are private. But I previously said that making varibales private
    // will block the access of main function from that variables.
    // Nothing outside of this varibales should not give access to the outside world.
    // so we make a public class inside this class that have the access to this variables.
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
    AsithaClass AsithaObject;
    AsithaObject.coolSaying();
    AsithaObject.name = "Asitha Divisekara";
    cout << endl
         << AsithaObject.name << endl;
}

// lets learn how to put variables into the classes. the proper way.
