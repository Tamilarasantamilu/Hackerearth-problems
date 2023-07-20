def solve(n_arr, k, len_n_arr):
    if k == 0:
        return n_arr
    if k > len_n_arr:
        return False
    if k == len_n_arr:
        return []
    k_use = 0
    max_first_digit = n_arr[0]
    for i in range(1,k+1):
        if n_arr[i] > max_first_digit:
            k_use = i
            max_first_digit = n_arr[i]
    return [max_first_digit] + solve(n_arr[(k_use+1):], k-k_use, len_n_arr-k_use-1)
    
 
n, k = list(map(int, input().split()))
n_arr = [int(x) for x in str(n)]
ret_arr = solve(n_arr, k, len(n_arr))
print("".join([str(x) for x in ret_arr]))