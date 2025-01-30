def twoSum(arr, target):
    dict = {}
    for i in range(len(arr)):
        if target - arr[i] in dict:
            return (arr[i], target - arr[i])
        else:
            dict[arr[i]] = True
    return

print(twoSum([2, 3, 5, 9], 14))