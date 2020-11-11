#include <iostream>
#include <cstring>
using namespace std;

int main(int argc, const char** argv) {
    int a = 0x0fffffff;
    printf("%d", sizeof(a));
}