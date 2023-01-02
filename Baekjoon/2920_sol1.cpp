// https://www.acmicpc.net/problem/2920
// Solution 1
// c++

# include <iostream>
using namespace std;

int main() {
    int num[8] = {0, };

    for(int i=0 ; i<8 ; i++) {
        cin >> num[i];
    }
    
    bool asc = true; 
    bool dsc = true; 

    for(int i=1 ; i<8 ; i++) {
        if (num[i] < num[i-1]) 
            asc = false;
        if (num[i-1] < num[i]) 
            dsc = false;
    }

    if (asc == true) 
        cout<<"ascending\n";
    else if (dsc == true)
        cout<<"descending\n";
    else
        cout<<"mixed\n";
    return 0;
}
