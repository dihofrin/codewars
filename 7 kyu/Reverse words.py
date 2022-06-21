"""Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"""

def reverse_words(text):
    words = ''.join([i[::-1] for i in text.split()])
    start = 0
    result = ''
    for i in range(len(text)):
        if text[i] != ' ':
            result += words[start]
            start += 1
        else:
            result += ' '
    return result