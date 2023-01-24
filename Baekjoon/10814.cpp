// https://www.acmicpc.net/problem/10814
// Solution 2
// C++

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare (pair<int,string> x, pair<int,string> y) {
    if (x.first < y.first)
        return true;
    else
        return false;
}

int main() {
    int N;
    cin>>N;

    vector<pair<int,string> > a(N);

    for(int i = 0 ; i < N ; i ++) 
        cin>>a[i].first>>a[i].second;
    
    stable_sort(a.begin(), a.end(), compare); 
    // preserves the original order of input set when the records have equal keys 

    for(int i = 0 ; i < N ; i ++) 
        cout << a[i].first << " " << a[i].second << "\n";
}

/*  
    <stable sort> 
    It keeps the items with the same sorting key in order
    Ex. Suppose we have a list of 5-letter words:
        peach
        straw
        apple
        spork

        Sort the list (in ascending order) by just the first letter of each word:
        apple
        peach
        straw
        spork

Reference
: https://stackoverflow.com/questions/1517793/what-is-stability-in-sorting-algorithms-and-why-is-it-important 

*/