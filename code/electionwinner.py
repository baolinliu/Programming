# Find the highest vote.  
# if tie, go with the person with the highest letter in alphabet.

def  electionWinner(votes):
    votes = list(votes)
    d = {}
    for i in votes:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
            
    high = max(d.values())
    
    inv_map = {}
    
    for i,j in zip(d.values(),d.keys()):
        inv_map.setdefault(i, []).append(j)
    
    name = sorted(inv_map[high], reverse = True)[0]
 
    return name
        

 votes = ['Victor','Veronica','Ryan',
 'Dave','Maria,','Maria','Farah',
 'Farah','Ryan','Veronica']

electionWinner(votes)

# output 'Veronica'