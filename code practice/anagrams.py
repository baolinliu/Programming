'''
find the minimum number of characters of the first string 
he needs to change to enable him to make it an anagram of the second string.

Note: A word x is an anagram of another word y if we can produce y 
by rearranging the letters of x.

'''


def anagram(s):
    if len(s) % 2 != 0:
        return -1
    else:
        dist = len(s)// 2
        string1 = sorted(s[:dist])
        string2 = sorted(s[dist:])

        if string1 == string2:
            return 0
        else:
            count = sum([1 for d,c in zip(string1,string2) if d != c])
            return count

t = input()

for _ in xrange(t):
    s = raw_input()
    print anagram(s)
    