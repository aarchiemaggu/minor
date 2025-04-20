def get_longest_subarray(arr, k):
    n = len(arr)
    max_len = 0

    for i in range(n):  # starting index
        for j in range(i, n):  # ending index
            s = 0
            for idx in range(i, j + 1):  # sum of subarray arr[i...j]
                s += arr[idx]
            if s == k:
                max_len = max(max_len, j - i + 1)
    
    return max_len
