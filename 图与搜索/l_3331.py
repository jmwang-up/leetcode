from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        # 先构造多叉树
        n = len(parent)
        children = [[] for _ in range(n)]

        for node in range(1, n):
            children[parent[node]].append(node)

        # 更新父节点
        last = [-1] * 26

        def update_parent_node(node):

            char_id = ord(s[node]) - ord('a')
            previous = last[char_id]

            if previous != -1:
                parent[node] = previous

            last[char_id] = node

            for child in children[node]:

                update_parent_node(child)

            last[char_id] = previous

        update_parent_node(0)

        new_children = [[] for _ in range(n)]
        
        for node in range(1, n):
            new_children[parent[node]].append(node)

        ans = [0] * n

        def count_node_size(node):

            size = 1

            for child in new_children[node]:
                size += count_node_size(child)

            ans[node] = size
            return size

        count_node_size(0)

        return ans


if __name__ == "__main__":

    so = Solution()
    res = so.findSubtreeSizes([-1,0,0,1,1,1], "abaabc")
    print(res)
