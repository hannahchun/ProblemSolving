// https://leetcode.com/problems/merge-two-binary-trees/
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
        TreeNode * mergeTrees(TreeNode * root1, TreeNode * root2) {
            if (root1 == nullptr && root2 == nullptr)
                return nullptr;
            if (root1 != nullptr && root2 == nullptr)
                return root1;
            if (root1 == nullptr && root2 != nullptr)
                return root2;
            root1->val += root2->val;
            root1->left = mergeTrees(root1->left, root2->left);
            root1->right = mergeTrees(root1->right, root2->right);
            return root1;
        }

        void printNode(TreeNode * root) {
            queue<TreeNode *> a1;
            TreeNode * t;
            if (root == NULL)
                return;
            a1.push(root);
            while(1) {
                if (a1.size() == 0)
                    return;
                t = a1.front();
                a1.pop();
                cout<<t->val<<" ";
                if (t->left != nullptr)
                    a1.push(t->left);
                if (t->right != nullptr)
                    a1.push(t->right);
            }
        }
};

int main() {
    Solution s1;

    TreeNode *root1 = new TreeNode(1);
    root1->left = new TreeNode(3);
    root1->right = new TreeNode(2);
    root1->left->left = new TreeNode(5);

    TreeNode *root2 = new TreeNode(2);
    root2->left = new TreeNode(1);
    root2->right = new TreeNode(3);
    root2->left->right = new TreeNode(4);
    root2->right->right = new TreeNode(7);

    TreeNode *root3 = s1.mergeTrees(root1, root2);
    s1.printNode(root3);
}