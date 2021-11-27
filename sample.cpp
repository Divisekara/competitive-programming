#include <iostream> // this is a pre processor directory this is a file
// we are including a header file that this program needs to run later on

using namespace std;
// this is a standard library this is a library

//  in CPP indentation is something the program does not care about. we can have indentation as many as we need as well we can avoid indentation

// this is a function Every computer program starts with a function called main.
// Even in python we start the program using main

//  int  means what types of data we are working with inside this function.

// we can add many functions as we want but only one main function.

int main()
{
    // inside the curly bracers we have statements. All functions are made of statements.
    // every statement needs to end with semi colan
    // cout means print something on the screen as the output
    cout << "Hello \n asitha" << endl;

    // int tuna = 6;
    // cout << tuna << endl;

    // int a = 12;
    // int b = 14;
    // int sum = a + b;
    // cout << "the answer is ";
    // cout << sum;

    int a;
    int b;
    int answer;

    cout << "Insert a: " << endl;
    cin >> a;
    cout << "Insert b: " << endl;
    cin >> b;
    answer = a + b;
    cout << "The answer is: " << answer << endl;

    // addition 
    int a = 3+4;
    // subtraction
    int b = 5-3;
    // multiplication
    int c = a*b;
    // division
    int d = 10/3;
    // modulo division
    int e = 10%3;
     
    return 0;
}

// start with 36.31

// << is the insertion operator
// endl after insertion operator in cout return the next line of printing into a new line.
// more easy way is to use new line character after escape character. \n
// if we do not use either of the above methods next print will be on the same line as well.
// declaring the variable can be done in the same line where the variable is defined or else after the defining.
// for reading the inputs we can use cin and extraction operator
// dont write the variables twice.
// variable can be overwritten.
// 
