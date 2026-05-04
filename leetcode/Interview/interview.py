int_arr2 = [0,1,-2,-1,3,4,-5,6,7,8,9,10,11,-12,13,-5,6,7,-9,2,-4,3,5,6,1,-54,8,-6,3,2]

def max_sub_subarray(int_arr):
    start = 0
    current_max = 0
    while start < len(int_arr) - 1:
        end = start
        while end < len(int_arr) - 1:
            current_sum = sum(int_arr[start:end])
            if current_sum <= 0:
                start = end
                break 
            if current_sum > current_max:
                current_max = current_sum
            end += 1
        start += 1
    return current_max


    # count_l = 0
    # count_r = len(int_arr) - 1
    # current_max = 0
    # while count_l != count_r:
    #     sub_arr_sum = sum(int_arr[count_l:count_r])
    #     if sub_arr_sum > current_max:
    #         current_max = sub_arr_sum
    #     if int_arr[count_l] < int_arr[count_r]:
    #         count_l += 1
    #     else:
    #         count_r -= 1
    # return current_max

print(max_sub_subarray(int_arr2))

