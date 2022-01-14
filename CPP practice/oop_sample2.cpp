#include <iostream>
#include <string>
using namespace std;

class AsithaClass
{
public:
    void setName(string x)
    {
        name = x;
    }

    string getName()
    {
        return name;
    }

private:
    string name;
}; // this is keep in mind to put the semi colan at the end of the class

int main()
{
    AsithaClass asi;
    asi.setName("Asitha Indrajith");
    cout << "My name is " << asi.getName() << endl;
    return 0;
}

// making variables public is a bad bad mistake as a software engineer.