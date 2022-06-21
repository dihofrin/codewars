"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"""

def to_camel_case(text):
    if len(text) == 0:
        return ''
    words = text.replace('_', ' ')
    words = words.replace('-', ' ')
    result = words.split()[0]
    return result + ''.join(i.capitalize() for i in words.split()[1:])

test = "the_stealth-warrior"
print(to_camel_case(test))