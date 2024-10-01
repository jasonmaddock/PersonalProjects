def interview_task(array):
    current_num = array[0]
    num_count = 1
    output_array = []
    for i in array[1:]:
        if i == current_num:
            num_count += 1
        else:
            output_array.append(num_count)
            output_array.append(current_num)
            current_num = i
            num_count = 1
    output_array.append(num_count)
    output_array.append(current_num)
    current_num = i
    num_count = 1
    return output_array

test_array = [80,80,80,80,80,80,1,2,2,2,12,1,1,1,1,1]

result = interview_task(test_array)
print(result)
    