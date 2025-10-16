---
title: Beginner Tree Problems
icon: fa-tree
---

### Invert Binary Tree

[source](https://leetcode.com/problems/invert-binary-tree/)
[submission](https://leetcode.com/problems/invert-binary-tree/submissions/1802931304/)

```cpp
class Solution {
public:

    void dfs(TreeNode* root){
        // Handle Base Case:
        if (root == NULL) return;

        // Process Child
        swap(root->left, root->right);

        dfs(root->left);
        dfs(root->right);
    }

    TreeNode* invertTree(TreeNode* root) {
        dfs(root);
        return root;
    }
};
```


### Balanced Binary Tree

```cpp
class Solution {
public:
    int dfs(TreeNode* root){
        if(root == NULL) return 0;

        int h1 = dfs(root->left);
        if(h1 == -1) return -1;

        int h2 = dfs(root->right);
        if(h2 == -1) return -1;

        if(abs(h1-h2) > 1) return -1;

        return max(h1, h2) + 1;
    }

    bool isBalanced(TreeNode* root) {
        return dfs(root) != -1;
    }
};
```

### Diametere of Binary Tree

[source](https://leetcode.com/problems/diameter-of-binary-tree/)
[susmission](https://leetcode.com/problems/diameter-of-binary-tree/submissions/1802941483/)

```cpp
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int res = 0;
        diameter(root, res);
        return res;
    }

private:
    int diameter(TreeNode* curr, int& res){
        // Base Case
        if (!curr) return 0;

        // Process Child
        int left = diameter(curr->left, res);
        int right = diameter(curr->right, res);

        // Finalize
        res = max(res, left + right);

        // Return
        return max(left, right) + 1;
    }
};
```


### Height/Depth of Binary Tree

```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL) return 0;
        int h1 = maxDepth(root->left);
        int h2 = maxDepth(root->right);
        return max(h1, h2) + 1;
    }
};
```


### Binary Tree Level Order Traversal

[submission](https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1802956404/)

`BFS`

```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root) return {};

        queue<TreeNode*> q;
        q.push(root);

        vector<vector<int>> ans;

        while(!q.empty()){
            int size = q.size();
            vector<int> curr;
            while(size--){
                TreeNode* top = q.front();q.pop();
                curr.push_back(top->val);
                if(top->left) q.push(top->left);
                if(top->right) q.push(top->right);
            }
            ans.push_back(curr);
        }
        return ans;
    }
};
```



### Leaf Sum

### Height of Tree



