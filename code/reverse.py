list_of_tuples = [('How are you today','I am doing fine')]

#output:
#[('today are you How', 'I am doing fine')]

def the_reverse(list_of_tuples):
    tuples = list_of_tuples[0][0].split()
    temp = tuples[0]
    temp2= tuples[-1]
    tuples[-1] = temp
    tuples[0]  = temp2
    reverse = ' '.join(tuples)
    
    list_of_tuples = list(list_of_tuples[0])
    list_of_tuples[0] = reverse
    
    return [tuple(list_of_tuples)]
    