#start out with 10 cooperations
#begin analysis of opponents response
#if average response is cooperation/staying silent (1): also cooperate
#if average response is betrayal (0): also betray

def strategy(history, memory):
    choice = 1

    coop_count = 0
    defect_count= 0

    if history.shape[1] > 1: 
        for x in range(history.shape[1]):
            prev = history[1,x]
            if prev == 1:
                coop_count += 1
            elif prev == 0:
                defect_count += 1
        
        if defect_count > coop_count:
            choice = 0

    return choice, None

