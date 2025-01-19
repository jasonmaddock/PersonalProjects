def maximumProfit(price):
    profit = 0
    count = 0
    while count < len(price):
        max_val = max(price[count:])
        max_ind = price[count:].index(max_val)
        buy = sum(price[count:count+max_ind])
        profit += (max_val * max_ind) - buy
        count += max_ind + 1
    return profit




if __name__ == 'main':
    print(maximumProfit([3,4,5,3,5,2]))