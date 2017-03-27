# Write a function that takes in a list of names, and returns a list # # where the names are
# sorted in alphabetical order of last name

# Example:
# Input: ['Baolin Liu', 'Barack Obama', 'Ada Lovelace', 'Alan Turing']
# Output: ['Baolin Liu', 'Ada Lovelace', 'Barack Obama', 'Alan Turing']


def sort_by_last_name(lst):
    
    sort_split = [name.split() for name in lst]
    
    sorted_split = sorted(sort_split, key = lambda x: x[-1])
    
    sorted_split = [' '.join(name) for name in sorted_split]
    
    return sorted_split


lst =  ['Baolin Liu', 'Barack Hussien Obama', 'Ada Lovelace', 'Alan Turing']
sort_by_last_name(lst)

