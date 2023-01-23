// https://leetcode.com/problems/invert-binary-tree/
// Solution 1 
// C++

#include <iostream>
#include <queue>

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
        TreeNode * invertTree(TreeNode *root) {
            if (root == NULL)
                return NULL;
            TreeNode * p = root; 
            TreeNode * temp = root->left;
            root->left = root->right;
            root->right = temp;
            invertTree(root->left);
            invertTree(root->right);
            return p;
        }

        void printNode(TreeNode *root) {
            queue<TreeNode*> a1;
            TreeNode* t;
            if(root == NULL)
                return;
            a1.push(root);
            while(1) {
                if (a1.size() == 0)
                    return;
                t = a1.front();
                a1.pop();
                cout<<t->val<<" ";
                if (t->left != NULL)
                    a1.push(t->left);
                if (t->right != NULL)
                    a1.push(t->right);
            }
        }
};

int main() {
    Solution s1;

    TreeNode *root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right = new TreeNode(7);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(9);

    TreeNode * root3 = s1.invertTree(root);
    s1.printNode(root3);
}