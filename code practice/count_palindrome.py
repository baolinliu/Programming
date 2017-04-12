# find all palindromes and subpalindromes in a string

def  count_palindromes(s):
    p = []
    for i in range(len(s)):
        for j in range(len(s)):
            cut = s[i:j+1]
            palindrome = cut[::-1]

            if cut == palindrome and len(cut):
                p.append(cut)
    return len(p)


