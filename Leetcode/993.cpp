// https://leetcode.com/problems/cousins-in-binary-tree/description/
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
    public :
        int xdepth, ydepth, xparent, yparent;

        bool isCousins(TreeNode *root, int x, int y) {
            if (root->val == x || root->val == y)
                return false;
            depth(root, x, y, 0, 0);  

            if (xdepth == ydepth && xparent != yparent)
                return true;
            return false;
        }

        // find the depth and parent node value of x and y 
        void depth(TreeNode *root, int x, int y, int d, int p) { // d : depth , p : parent node value
            if (root == nullptr)
                return;
            if (root->val == x) {
                xdepth = d;
                xparent = p;
                return;
            }
            if (root->val == y) {
                ydepth = d;
                yparent = p;
                return;
            }
            depth(root->left, x, y, d+1, root->val);
            depth(root->right, x, y, d+1, root->val);
        }
};

int main() {
    Solution s1;

    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right = new TreeNode(3);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(7);

    if(s1.isCousins(root,4,5))
        cout<<"The given nodes are cousins"<<"\n";
    else
        cout<<"The given nodes are not cousins"<<"\n";
}