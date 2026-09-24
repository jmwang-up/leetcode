import sys


def largest_network(weights):
    # 权重小于 2**60：把二进制位作为并查集节点。
    parent = list(range(60))
    account_count = [0] * 60

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    answer = 0
    for weight in weights:
        lowest_bit = weight & -weight
        root = find(lowest_bit.bit_length() - 1)
        remaining = weight ^ lowest_bit

        # 同一账号包含的所有置位属于同一个社交网络。
        while remaining:
            bit = remaining & -remaining
            other = find(bit.bit_length() - 1)
            if root != other:
                # 将账号数较少的分量合并到较大的分量。
                if account_count[root] < account_count[other]:
                    root, other = other, root
                parent[other] = root
                account_count[root] += account_count[other]
            remaining ^= bit

        # 一个账号只计数一次，即使它包含多个置位。
        account_count[root] += 1
        answer = max(answer, account_count[root])

    return answer


def solve():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    test_cases = next(data)
    results = []

    for _ in range(test_cases):
        n = next(data)
        weights = (next(data) for _ in range(n))
        results.append(str(largest_network(weights)))

    sys.stdout.write('\n'.join(results))


if __name__ == '__main__':
    solve()
