def find_averages_of_subarrays(K, arr):
    r = []
    s = 0.0
    start = 0
    for i in range(len(arr)):
        s += arr[i]
        if i >= K -1:
            r.append(s/K)
            s -= arr[start]
            start += 1
    return r
print(find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))