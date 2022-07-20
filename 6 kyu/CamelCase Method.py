def camel_case(string):
    result = [i.capitalize() for i in string.split()]
    return ''.join(result)