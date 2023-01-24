// https://www.codeground.org/practice 3번 문제
// Solution 1
// C++

#include <iostream>
#include <algorithm>

using namespace std;

int Answer;

// sort in descending order
bool compare(int a, int b) {
    return a > b;
}

int main(int argc, char** argv) {
    int T, test_case;
    int N, K;

    // number of test cases
    cin>>T;

    for(test_case = 0 ; test_case < T ; test_case ++) {
        // store the maximum total score
        Answer = 0;

        // N: the number of total subjects given
        // K: the number of subjects 정우 can study
        cin>>N>>K;

        int *scores = new int[N];
        for(int i = 0 ; i < N ; i ++) 
            cin>>scores[i];

        // sort the elements in 'scores'
        sort(scores, scores + N, compare);

        // extract the first K scores in 'scores' and add them to 'Answer'
        for(int i = 0 ; i < K ; i ++) 
            Answer += scores[i];
        
        cout << "Case #" << test_case + 1 << endl;
        cout << Answer << endl;
        delete[] scores;
    }
    return 0;
}

/*
    <C++ STL sort 함수>
    : STL 라이브러리의 algorithm 헤더에 있음
    
    // 기본적으로 오름차순 정렬 수행
    sort(배열의 시작점 주소, 배열의 마지막 주소+1)

    // 숨겨진 부분까지 적으면 
    sort(배열의 시작점 주소, 배열의 마지막 주소+1, compare)

    bool compare(int a, int b) { // 오름차순 정렬
        return a < b
    }
*/ 
