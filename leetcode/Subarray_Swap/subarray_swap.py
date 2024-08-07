def canBeEqual(target, arr):
    """
    :type target: List[int]
    :type arr: List[int]
    :rtype: bool
    """
    count = 0
    for i in arr:
        
        if target == arr:
            return True
        if target[count] == i:
            count += 1
            continue
        search_count = 0
        for j in arr[count:]:
            if j == target[count]:
                new_arr = arr[count:count+search_count+1][::-1]
                arr[count:count+search_count+1] = new_arr
                break
            search_count += 1
        count += 1
    return False

arr1 = [809,107,274]
arr2 = [809,274,107]

print(canBeEqual(arr2, arr1))