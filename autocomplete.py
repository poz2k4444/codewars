# my solution (ugly one)
def autocomplete(input_, dictionary):
    #your code here
        res = list()
        new_str = ""
        for letter in input_:
            if letter.isalpha():
                new_str += letter
        for item in dictionary:
            if item.lower().startswith(new_str) and len(res) < 5:
                res.append(item)
        return res

# best soultion (shoud've known better to refactor mine with list comprenhension
def autocomplete2(input_, dictionary):
    input_ = ''.join( [ c for c in list(input_) if c.isalpha() ])
    return [ x for x in dictionary if x.lower().startswith(input_.lower()) ][:5]
