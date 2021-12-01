#include <iostream> // this is a pre processor directory this is a file
// we are including a header file that this program needs to run later on

using namespace std;
// this is a standard library this is a library

//  in CPP indentation is something the program does not care about. we can have indentation as many as we need as well we can avoid indentation

// this is a function Every computer program starts with a function called main.
// Even in python we start the program using main

//  int  means what types of data we are working with inside this function.

// we can add many functions as we want but only one main function.

// computer programs works top to down.
// so we need to add this function to before the main function
// but we can do function prototyping to script the functions after the main function

void printSomething();        // this is function prototyping
void printCrap(int x);        // this is function prototyping
int addNumbers(int x, int y); // this is function prototyping

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

    // cout << "Insert a: " << endl;
    // cin >> a;
    // cout << "Insert b: " << endl;
    // cin >> b;
    // answer = a + b;
    // cout << "The answer is: " << answer << endl;

    // addition
    int c = 3 + 4;
    // subtraction
    int d = 5 - 3;
    // multiplication
    int e = a * b;
    // division
    int f = 10 / 3;
    // modulo division
    int i = 10 % 3;

    // bodmas convention is applied to any arithmetic expression.

    if (c > 5)
    {
        cout << "Asitha is awesome";
    }
    else if (c < 5)
    {
        cout << "Asitha is freaking awesome";
    }
    else
    {
        cout << "Asitha is amazingly mazmerizing awesome";
    }

    // printSomething();
    // printCrap(1779);
    // we can also print the output of the addNumbers function directly
    cout << endl
         << "Printing directly : " << addNumbers(10, 12);
    int out = addNumbers(100, 1);
    cout << endl
         << "answer is : " << out << endl;

    return 0;
}

void printSomething()
{
    cout << endl
         << "print something";
}

int addNumbers(int x, int y)
{
    int answer = x + y;
    return answer;
}

void printCrap(int x)
{
    cout << endl
         << "Asithas favourite number is" << x << endl;
}

// lets make functions
// if we want to return a number from the funtion we need to define as int function(){}
// if we dont want to return anything back froma a funtion then we can use void insetead of int or types

// start with 1.02

// << is the insertion operator
// endl after insertion operator in cout return the next line of printing into a new line.
// more easy way is to use new line character after escape character. \n
// if we do not use either of the above methods next print will be on the same line as well.
// declaring the variable can be done in the same line where the variable is defined or else after the defining.
// for reading the inputs we can use cin and extraction operator
// dont write the variables twice.
// variable can be overwritten.
// logic operators - < , > , <=, >=, =, !=,
