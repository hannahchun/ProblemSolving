// https://leetcode.com/problems/same-tree/
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
        bool isSameTree(TreeNode *p, TreeNode *q) {
            if (numOfNodes(p) != numOfNodes(q))
                return false;
            return equal_test(p, q);
        }

        int numOfNodes(TreeNode *root) {
            if (root == nullptr)
                return 0;
            return 1 + numOfNodes(root->left) + numOfNodes(root->right);
        }

        bool equal_test(TreeNode *root1, TreeNode *root2) {
            if (root1 == nullptr && root2 == nullptr)
                return true;
            if (root1 == nullptr)
                return false;
            if (root2 == nullptr)
                return false;
            if(root1->val != root2->val)
                return false;
            if(equal_test(root1->left, root2->left) && equal_test(root1->right, root2->right))
                return true;
            else
                return false;
        }
};

int main() {
    Solution s1;

    TreeNode *root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(3);

    TreeNode *root2 = new TreeNode(1);
    root2->left = new TreeNode(2);
    root2->right = new TreeNode(3);

    if(s1.isSameTree(root1, root2))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
}