// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
// Solution 1
// C++

#include <iostream>

using namespace std;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    public :
        int sumRootToLeaf(TreeNode* root) {
            if (root == nullptr)
                return 0;
            if (root->left == nullptr && root->right == nullptr)
                return root->val;
            if (root->left)
                root->left->val += root->val * 2;
            if (root->right)
                root->right->val += root->val * 2;
            return sumRootToLeaf(root->left) + sumRootToLeaf(root->right);
        }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(0);
    root->left->left = new TreeNode(0);
    root->left->right = new TreeNode(1);
    root->right = new TreeNode(1);
    root->right->left = new TreeNode(0);
    root->right->right = new TreeNode(1);

    Solution sol1;

    cout<<sol1.sumRootToLeaf(root)<<"\n";
}