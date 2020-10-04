#include <iostream>

class Foo{
    public:
        void bar(){
            std::cout << "Hello" << std::endl;
        }
};
void printname(){
    std::cout<< "vinay patil";
}
extern "C" {
    Foo* Foo_new(){ 
        return new Foo(); 
        }

    void Foo_bar(Foo* foo){ 
        foo->bar(); 
        }
    
    // void print(){
    //     printname();
    // }
    // printname()

}