def top_3_words(text):
    text = text.strip(' ,#/\, ').split()
    result = {}
    for i in text:
        result[i] = result.get(i, 0) + 1
    sorted_keys = sorted(result.items(), key=lambda x: (-x[1], x[0]))
    sorted_result = dict(sorted_keys)
    final = [i.lower() for i in list(sorted_result.keys())]
    return final[:3]

print(top_3_words('e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e'))