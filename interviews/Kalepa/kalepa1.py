def maximumProfit(price):
    stock = 0
    bought = 0
    sold = 0
    for count, i in enumerate(price):
        if count == len(price):
            if stock:
                sold += stock*i
                stock = 0
            break
        if i == max(price[count:]):
            if stock:
                sold += stock*i
                stock = 0
        else:
            stock += 1
            bought -= i
    return sold + bought

if __name__ == 'main':
    print(maximumProfit([3,4,5,3,5,2]))