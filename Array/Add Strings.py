def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """



    return int("".join(map(str, num1))) + int("".join(map(str, num2)))

print(addStrings("123","345"))