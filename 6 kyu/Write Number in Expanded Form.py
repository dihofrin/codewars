"""Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!

"""

def expanded_form(num):
    part = lambda x: int(str(x)[0]) * 10 ** (len(str(x))-1)
    result = [part(num)]
    while num > 0:
        num -= part(num)
        if num == 0:
            break
        result.append(part(num))
    return ' + '.join(str(i) for i in result)