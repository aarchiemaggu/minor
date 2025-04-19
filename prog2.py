def hasTripletSum(arr, target):
    n = len(arr)
    
    # Fix the first element as arr[i]
    for i in range(n - 2):
        
        # Fix the second element as arr[j]
        for j in range(i + 1, n - 1):
            
            # Now look for the third number
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return True
    
    # If we reach here, then no triplet was found
    return False