arr = [4, 5, 734, 43, 45, 100, 4, 56, 23, 67, 23, 58, 45]

# Your code go here:



def sum_odds(arr):
    total_odds = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            total_odds += arr[i]
    return total_odds

print(sum_odds(arr))
