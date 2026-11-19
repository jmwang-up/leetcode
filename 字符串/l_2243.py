class Solution:
    def digitSum(self, s: str, k: int) -> str:

        def traverse(new_s):
    
            n = len(new_s)
    
            if n <= k:
                return new_s

            copy_new_s = ''
            for i in range(0, n, k):
                sub_s = new_s[i:i+k]
                sub_val = sum(list(map(int, sub_s)))
                copy_new_s += str(sub_val)

            res = traverse(copy_new_s)

            return res

        res = traverse(s)

        return res