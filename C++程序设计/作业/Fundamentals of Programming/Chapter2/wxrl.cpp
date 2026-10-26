#include <iostream>

int main()
{
    float grmma = 1;
    float e = 2;
    float i = 1;


    while (1/grmma>0.0000001)
    {
        i = i + 1;
        grmma = grmma * i;
        e = e + 1 / grmma;
    }

    printf("e的估计值为：", e);
    return 0;
}
