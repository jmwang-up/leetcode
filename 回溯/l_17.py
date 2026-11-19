class Solution:
    def letterCombinations(self, digits: str) -> list[str]:


        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
            }
        
        n = len(digits)
        res = []


        def back_track(index, path):

            if index == n:
                res.append(path)
                return


            num_str = digits[index]
            letters = mapping.get(num_str)

            for l in letters:
                back_track(index + 1, path + l)

        back_track(0, "")
        return res