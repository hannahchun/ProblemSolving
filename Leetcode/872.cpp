// https://leetcode.com/problems/leaf-similar-trees/
// Solution 1
// C++

#include <iostream>
#include <stack>

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
        bool leafSimilar(TreeNode* root1, TreeNode* root2) {
            stack<TreeNode*> s1, s2;
            s1.push(root1);
            s2.push(root2);
            while(!s1.empty() && !s2.empty()) {
                if(dfs(s1) != dfs(s2))
                    return false;
            }
            return s1.empty() && s2.empty();
        }

        int dfs(stack<TreeNode*>& s) {
            while(1) {
                TreeNode* node = s.top();
                s.pop();
                if(node->right)
                    s.push(node->right);
                if(node->left)
                    s.push(node->left);
                if(!node->right && !node->left)
                    return node->val;
            }
        }
};

int main() {
    Solution s1;

    TreeNode *root1 = new TreeNode(3);
    root1->left = new TreeNode(5);
    root1->left->left = new TreeNode(6);
    root1->left->right = new TreeNode(2);
    root1->left->right->left = new TreeNode(7);
    root1->left->right->right = new TreeNode(4);
    root1->right = new TreeNode(1);
    root1->right->left = new TreeNode(9);
    root1->right->right = new TreeNode(8);

    TreeNode *root2 = new TreeNode(3);
    root2->left = new TreeNode(5);
    root2->left->left = new TreeNode(6);
    root2->left->right = new TreeNode(7);
    root2->right = new TreeNode(1);
    root2->right->left = new TreeNode(4);
    root2->right->right = new TreeNode(2);
    root2->right->right->left = new TreeNode(9);
    root2->right->right->right = new TreeNode(8);

    if(s1.leafSimilar(root1, root2))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
}