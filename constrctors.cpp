// constructor is a function that get caught automatically as soon as you create an object of a class
// constructor name should be class name itself.
#include <iostream>
#include <string>
using namespace std;

class AsithaClass
{
public:
    AsithaClass(string z)
    {
        setName(z);
        cout << "This is printed using the constructor" << endl;
    }
    // no one will print something under constructor if so slap him.
    // constructors is used for getting varibales intial values
    // whenever you have bunch of variables and you have to set them equal to values intially 
    void setName(string x)
    {
        name = x;
    }

    string getName()
    {
        return name;
    }

    // only public things can be accessed when we use the class.
private:
    string name;
};

int main()
{
    AsithaClass asi("this is sample text");
    cout << asi.getName() << endl
         << asi.name;
}
