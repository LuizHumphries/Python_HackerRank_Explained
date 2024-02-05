n, n_arr = int(input()), set(map(int, input().split()))
m, m_arr = int(input()), set(map(int, input().split()))
print("\n".join(map(str, sorted(n_arr.symmetric_difference(m_arr)))))
