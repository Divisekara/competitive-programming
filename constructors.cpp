#include <iostream>
#include "Burrito.h"

using namespace std;

int main()
{
    cout << "Hello world!" << endl;
    Burrito bo; // creating a class object
    return 0;
}

// say we have bunch of classes then we cant put all classes into one file where main code is written.
// therefore we put seperate classes into seperate files.
// if you are working with couple of people at a time then its easy to work single file or one file for one person
// we uncheck has destructor and virtual destructor
// usually all the class files locally on the same directory where main cpp file is located

// we need to make 2 files in order to create a header file
// first one is a header file where all the classes, function prototyping and variables are stored
// we use the extension .h for the header file
// in cpp source file where the extension is .cpp that is the file where we actually creating the objects and building the functions.

// :: this is the double colan and call this "Binary scope resolution operator"
