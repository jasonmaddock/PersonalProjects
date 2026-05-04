# “ccaaabbac” -> “aaabba”
# “ccacaabbac” -> “ccacaa”

def interview_q(string):
    h_map = {}
    count = 0
    start = 0
    longest_sub_s = ""
    while count < len(string):
        sub_s = string[start:count+1]
        if len(set(sub_s)) == 3:
            larget_first = 0
            breakpoint()
            for item in h_map.values():
                if item["first"] > larget_first:
                    larget_first = item["first"]
            h_map = {}
            start = larget_first
            continue

        if sub_s > longest_sub_s:
            longest_sub_s = sub_s


        letter = string[count]
        in_dict = h_map.get(letter)
        if not in_dict:
            h_map[letter] = {"first": count, "last": count}
        elif count > 0:
            if string[count - 1] != string[count]:
                h_map[letter] = {"first": count, "last": count}
            else:
                in_dict["last"] = count
        count += 1

interview_q("ccacaabbac")