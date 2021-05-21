#start out as a cooperation
#begin analysis of opponents response
#if majority response is cooperation/staying silent (1): also cooperate
#if majority response is betrayal (0): also betray
#uses linear weighting (more recent turns are weighted as more important)

def strategy(history, memory):
    choice = 1


    if history.shape[1] > 1: 
        coop_count = 0
        defect_count= 0

        for x in range(history.shape[1]):
            prev = history[1,x]
            if prev == 1:
                coop_count += x
            elif prev == 0:
                defect_count += x
        
        if defect_count > coop_count:
            choice = 0

    return choice, None
