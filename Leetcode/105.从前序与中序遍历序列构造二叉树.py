from typing import List

from utils import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        index_map = {element: i for i, element in enumerate(inorder)}

        def building(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right or inorder_left > inorder_right:
                return None
            preorder_root = preorder_left
            inorder_root = index_map[preorder[preorder_root]]

            root = TreeNode(preorder[preorder_root])
            size_left = inorder_root - inorder_left
            root.left = building(preorder_left + 1, preorder_left + size_left, inorder_left, inorder_root - 1)
            root.right = building(preorder_left + 1 + size_left, preorder_right, inorder_root + 1, inorder_right)
            return root

        return building(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    today = Solution()
    preorder = list(map(int, input('preorder = ').strip().split(',')))
    inorder = list(map(int, input('inorder = ').strip().split(',')))
    tree_root = today(preorder=preorder, inorder=inorder)