def encrypt(text, n):
    result = text
    for i in range(n):
        left = ''.join(result[1::2])
        right = ''.join(result[::2])
        result = left + right
    return result

def decrypt(encrypted_text, n):
    result = encrypted_text
    for i in range(n):
        middle = len(result) // 2
        left = ''.join(result[:middle])
        right = ''.join(result[middle:])
        tmp = ''
        for j in range(middle):
            tmp = tmp + right[j] + left[j]
        result = tmp
        if len(right) > len(left):
            result += right[-1]
        if len(left) > len(right):
            result += left[-1]
    return result

print(decrypt('This is a test!', 4))