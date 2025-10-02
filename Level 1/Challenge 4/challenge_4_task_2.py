def boredom(staff):
    # define score dictionary
    scores = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25 
    }
    
    boredom_total = 0
    
    # iterate through staff dictionary mapping their department to the boring score while keeping a running total
    for person, dept in staff.items():
        boredom_total += scores[dept]
    
    # evaluation of total boredom
    if boredom_total <= 80:
        return "kill me now"
    elif 80 < boredom_total < 100:
        return "i can handle this"
    else:
        return "party time!!"
