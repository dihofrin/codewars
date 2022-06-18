"""Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']"""

def solution(s):
    if not s:
        return []
    result = []
    tmp = ''
    for i in range(len(s)):
        tmp += s[i]
        if len(s) % 2 != 0 and i == len(s)-1:
            tmp += '_'
        if len(tmp) == 2:
            result.append(tmp)
            tmp = ''
    if len(result[-1]) != 2:
        result[-1] += '_'
    return result
