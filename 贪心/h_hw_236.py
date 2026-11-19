import sys


def solve():

    data = sys.stdin.read().strip().split()
    budget = int(data[0])
    n = int(data[1])

    product_info = []
    list(map(int, data[2:]))

    i = 0
    for _ in range(n):
        product_info.append(list(map(int, data[2:]))[i:i+4])
        i = i + 4

    product_info.sort(key=lambda x:x[3], reverse=True)

    # 根据预算计算能买几件

    def cal_satisfaction():
        # 总开销
        cosl = 0
        # 总类别
        cate = set()
        # 编号 
        pro_num = []
        for product in product_info:
            # 单件大于预算直接跳过
            if product[2] > budget:
                continue
            # 如果买过直接跳过
            if product[0] in pro_num:
                continue
            pro_num.append(product[0])
            # 记录类别
            cate.add(product[1])
            cosl += product[2]
            # 算价格
            if len(cate) > 3:
                pass

            # 算满意度



        

        



if __name__ == "__main__":
    solve()