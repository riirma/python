# 標準機能　色々

# 複数のリストを同時にソートする
def sort_lists():
    a = [2, 1, 3]
    b = ['b', 'a', 'c']
    ab_set = sorted(zip(a, b))
    a_sorted, b_sorted = zip(*ab_set)
    print(a_sorted)
    print(b_sorted)


if __name__ == '__main__':
    sort_lists()