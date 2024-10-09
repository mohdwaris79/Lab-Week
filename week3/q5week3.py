def remove_characters_from_n(str, n):
    
    
    result = ""

    
    for ind in range(n):
        result += str[ind]

    return result

str= "Hello, World!"
n = 7
result = remove_characters_from_n(str, n)
print("Original string:", str)
print("Modified string:", result)
