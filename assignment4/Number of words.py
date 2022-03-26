def words(s):
    numerator = 0
    for i in range(0, len(s)):
        if s[i] == " ":
            numerator += 1
    return numerator +1
s = input()
print("Output: ",words(s))
    