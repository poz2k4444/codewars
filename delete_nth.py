# my solution
def delete_n(order, max_e):
    new_list = list()
    num = dict()
    for key in order:
        num[key] = num.get(key,1)
        if num[key] <= max_e:
            num[key] += 1
            new_list.append(key)
    return new_list

# best solution
def delete_nth(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
