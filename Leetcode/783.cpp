// https://leetcode.com/problems/minimum-distance-between-bst-nodes/
// Solution 1
// C++

#include <iostream>
#include <vector>

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
        vector<int> inorder_traversal;
        int ans = INT_MAX; //int 형식 변수의 최대값

        int minDiffInBST(TreeNode *root) {
            inorder(root);
            for (int i=1 ; i<inorder_traversal.size() ; i++)
                ans = min(ans, inorder_traversal[i]-inorder_traversal[i-1]);
            return ans;
        }

        void inorder(TreeNode *root) {
            if (root != nullptr) {
                inorder(root->left);
                inorder_traversal.push_back(root->val);
                inorder(root->right);
            }
        }
};

int main() {
    Solution s1;

    TreeNode *root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right = new TreeNode(6);
    
    cout<<s1.minDiffInBST(root)<<"\n";
}