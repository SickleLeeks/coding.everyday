from typing import Optional

from utils import TreeNode


class Solution:
    def __init__(self):
        self.maxSum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxGain(node):
            if not node:
                return 0
            # 递归计算左右子节点的最大贡献值
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点左右子树的最大贡献值
            priceNewPath = node.val + leftGain + rightGain
            # 更新答案
            self.maxSum = max(self.maxSum, priceNewPath)
            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
