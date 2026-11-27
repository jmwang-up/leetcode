

class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:

        # 0 表示alice 1 给bob
        counter = [0] * 2
        n = len(rain)
        res = []
        for i in range(n - 1):
            #
            if rain[i] == 0:
                res.append("None")
                continue
            # bob 需要伞
            elif rain[i] == 1:
                # 都需要伞的时候，切次数相同, 则给alice
                if rain[i + 1] == 1:
                    if counter[0] <= counter[1]:
                        counter[0] += 1
                        res.append("Alice")
                    else:
                        counter[1] += 1
                        res.append("Bob")
                # 只有bob需要
                else:
                    counter[1] += 1
                    res.append("Bob")

        if rain[n - 1] == 1:
            res.append("Bob")
        else:
            res.append("None")
        return res

if __name__ == "__main__":

    so = Solution()
    res = so.assignUmbrella([1, 1, 0, 1, 1])
    print(f"res:{res}")

    res = so.assignUmbrella([0, 1, 0, 1])
    print(f"res:{res}")
