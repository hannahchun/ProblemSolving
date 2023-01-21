// https://www.acmicpc.net/problem/5639 
// Solution 1
// C++

#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};

Node* insert(Node* node, int data) {
    if (node == NULL) {
        node = new Node();
        node->data = data;
        node->left = node->right = NULL;
    }
    else if (data <= node->data) {
        node->left = insert(node->left, data);
    }
    else {
        node->right = insert(node->right, data);
    }
    return node;
}

void postorder(Node* node) {
    if(node->left != NULL)
        postorder(node->left);
    if(node->right !=NULL)
        postorder(node->right);
    cout<<node->data<<"\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Node *root = NULL;
    int val;
    // EOF를 입력받을 때 까지 수를 받기 위해 While(cin>>val) 을 사용
    while(cin>>val) {
        if (val == EOF)
            break;
        root = insert(root, val);
    }
    postorder(root);
    return 0;
}