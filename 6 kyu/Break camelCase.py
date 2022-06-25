"""Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    result = []
    tmp = ''
    for i in s:
        if not i.isupper():
            tmp += i
        else:
            result.append(tmp)
            tmp = ''
            tmp += i
    result.append(tmp)
    return ' '.join(result)

test = 'helloWorld'
print(solution(test))