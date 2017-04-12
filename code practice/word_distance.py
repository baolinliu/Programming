# find the min distance between words in list
# example 'the' and 'quick' is 3 or 3 words away
# lst = ['the','brown','cat','bat','quick']

lst = ['the','brown','the','fox','quick','quick']


def distance(lst,word1,word2):
    dist1 = [index for index,word in enumerate(lst) if word1==word]
    dist2 = [index for index,word in enumerate(lst) if word2==word]
    
    distance = [abs(dis1-dis2) for dis1 in dist2 for dis2 in dist1]
    return min(distance)

distance(lst, 'the', 'brown')

# should be 1
