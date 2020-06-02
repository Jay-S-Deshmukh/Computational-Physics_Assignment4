#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <cmath>

using namespace std;

int main() {
    
    int N = 10000;
    double exp_sample[N];
    double num;
    
    int i;
    for(i=0; i<N; i++)
    {
        num = ((double)rand()/(RAND_MAX));
        exp_sample[i] = -0.5*log(num);
    }
    
    ofstream data;
    data.open("pdf_exp.txt");
    
    for(i=0;i<N;i++)
    {
        data << exp_sample[i] << endl;
    }
    data.close();
    
    system("python pdf_exp.py");
    
    return 0;

}
