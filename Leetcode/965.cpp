// https://leetcode.com/problems/univalued-binary-tree/
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
        bool check(TreeNode* root, int val) {
            if (root == NULL)
                return true;
            if (root->val != val || !check(root->left, val) || !check(root->right, val))
                return false;
            return true;
        }
        
        bool isUnivalTree(TreeNode* root) {
            int rootVal = root->val;
            return check(root, rootVal);
        }
};

int main(){
    Solution s1;

    TreeNode *root = new TreeNode(2);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(5);
    root->left->right = new TreeNode(2);
    root->right = new TreeNode(2);

    if(s1.isUnivalTree(root))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
}   