// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
// Solution 1
// C++

#include <iostream>
#include <vector>

using namespace std;

// Definition for a Node.
class Node {
    public :
        int val;
        vector<Node*> children;

        Node() {}

        Node(int _val) {
            val = _val;
        }

        Node(int _val, vector<Node*> _children) {
            val = _val;
            children = _children;
        }
};

class Solution {
    public :
        int maxDepth(Node* root) {
            if (root == nullptr)
                return 0;
            int n = root->children.size();
            int max_node = 0;
            for (int i=0 ; i<n ; i++) {
                int m = maxDepth(root->children[i]);
                max_node = max(max_node, m);
            }
            return max_node + 1;
        }
};

int main() {
    Solution s1;

    Node *root = new Node(1);
    (root->children).push_back(new Node(3));
    (root->children).push_back(new Node(2));
    (root->children).push_back(new Node(4));
    (root->children[0]->children).push_back(new Node(5));
    (root->children[0]->children).push_back(new Node(6));

    cout<<s1.maxDepth(root)<<"\n";
}