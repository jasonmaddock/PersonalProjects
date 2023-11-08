def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    mappings = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    li = [i for i in s]
    nums_list = []
    for item in li:
        nums_list.append(mappings[item])

    full_nums_list = []
    for index, item in enumerate(nums_list):
        if index + 1 == len(nums_list):
            full_nums_list.append(item)
        elif item > nums_list[index + 1]:
            full_nums_list.append(item)
        elif item < nums_list[index + 1]:
            full_nums_list.append(item)
        else:
            til = index + nums_list[
                index : index + 3
                if 2 < len(nums_list) - index + 1
                else len(nums_list) - index + 1
            ].count(item)
            full_nums_list.append(item * (til - index))
            for i in range(index, til - 1):
                nums_list.pop(i)
    add_list = []
    sub_list = []
    for index, item in enumerate(full_nums_list):
        if index + 1 == len(nums_list):
            add_list.append(item)
        elif item > nums_list[index + 1]:
            add_list.append(item)
        elif item < nums_list[index + 1]:
            sub_list.append(item)
    return sum(add_list) - sum(sub_list)


tests = ["DCXXI", "III", "LVIII", "MCMXCIV"]

for i in tests:
    print(romanToInt(i))
