// https://leetcode.com/problems/diameter-of-binary-tree/ 
// Solution 1
// C++

#include <iostream>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    int max_num = 0;
    public :
        int diameterOfBinaryTree(TreeNode* root) {
            diameter(root);
            return max_num;
        }

        int diameter(TreeNode* root) {
            if (root == nullptr)
                return 0;
            int left = diameter(root->left);
            int right = diameter(root->right);
            max_num = max(max_num, left+right);
            return max(left, right) + 1;
        }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    Solution sol1;

    cout<<"The diameter of the tree is "<< sol1.diameterOfBinaryTree(root)<<"\n";
    return 0;
}