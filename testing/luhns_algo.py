import re
from cs50 import get_int


def main():
    number = get_number()
    if number == "INVALID":
        print(number)
        return 0
    check = luhns_check(number)
    if check != 0:
        print("INVALID")
        return 0
    print(provider_check(number))


def luhns_check(n):
    reversed = str(n)[::-1]
    odd_sum, even_sum = 0, 0
    for count, i in enumerate(reversed):
        if count % 2 == 0:
            odd_sum += int(i)
        else:
            multiplied = int(i) * 2
            if multiplied > 9:
                multiplied = multiplied - 9
            even_sum += multiplied
    result = (odd_sum + even_sum) % 10
    return result


def provider_check(n):
    card_string = str(n)
    if card_string[0] == "4" and (len(card_string) == 13 or len(card_string) == 16):
        return "VISA"
    elif int(card_string[:2]) < 56 and int(card_string[:2]) > 50 and len(card_string) == 16:
        return "MASTERCARD"
    elif (card_string[:2] == "34" or card_string[:2] == "37") and len(card_string) == 15:
        return "AMEX"
    else:
        return "INVALID"


def get_number():
    n = get_int("Number: ")
    check = re.search(r"^(\d{16}|\d{15}|\d{13})$", str(n))
    if check:
        return (n)
    return ("INVALID")


if __name__ == "__main__":
    main()
