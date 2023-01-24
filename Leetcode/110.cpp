// https://leetcode.com/problems/balanced-binary-tree/
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
        bool isBalanced(TreeNode *root) {
            bool res = true;
            getDepth(root, res);
            return res;
        }
        int getDepth(TreeNode *root, bool &res) {
            if(!res) // break recursion
                return 0;
            if (root == NULL)
                return 0;
            int left = getDepth(root->left, res); // depth of left sub tree
            int right = getDepth(root->right, res); // depth of right sub tree
            if (abs(left - right) > 1)
                res = false;
            return max(left, right) + 1;
        }
};

int main() {
    /*
    TreeNode *root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right=new TreeNode(20);
    root->right->left=new TreeNode(15);
    root->right->right=new TreeNode(7);
    */
    
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(3);
    root->left->left->left = new TreeNode(4);
    root->right = new TreeNode(2);
    root->right->right = new TreeNode(3);
    root->right->right->right = new TreeNode(4);
    
    Solution sol1;

    if(sol1.isBalanced(root))
        cout<<"true"<<"\n";
    else
        cout<<"false"<<"\n";
}