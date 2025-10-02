def outed(meet, boss):
    # start happiness count to calculate room happiness later
    happiness_total = 0
    
    # initialise for loop to iterate through dictionary of person and happiness
    for person, score in meet.items():
        if person == boss: # if this person is my boss double their happiness score
            happiness_total += score * 2
        else:
            happiness_total += score
    # length of the number of keys (number of people)        
    num_people = len(meet)
    
    # room happiness is the score over the number of people
    avg_happiness = happiness_total / num_people
    
    # responses based on the average happiness
    return f"Get Out Now!" if avg_happiness <= 5 else f"Nice Work Champ!"
