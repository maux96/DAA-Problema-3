import heuristica
import brute_force
import random

def generate_case(n):
    case = []
    while n >0:
        n-=1
        temp = []
        count = random.randint(3,10)
        while count>0:
            count-=1
            temp.append(random.randint(1,60))
        case.append(set(temp))    
    return case

def start(n):
    N = n
    accuracy = 0
    while n >0:
        n-=1    
        r = random.randint(4,15)
        case = generate_case(r)
        # print("    ------CONJUNTO  = " + str(case)+"--------")
        case_1 = [c for c in case]
        k = random.randint(1,r-1)
        
        r_heuristic = heuristica.first_min_intersection(k, case)
        r_brute = brute_force.solution(k, case_1)
        print(str(n) + ".  k = "+str(k) + "    n = " + str(r))
        if r_heuristic != None:
            print("    -heuristic_len = " + str(len(r_heuristic)))
            # print("    -heuristic resutl  = " + str(r_heuristic))
        else:
            print("    -heuristic_len = " + str(r_heuristic))

        if r_brute != None:
            print("    -brute_len = " + str(len(r_brute)))
        else:
            print("    -brute_len = " + str(r_brute))

        if r_brute == None or r_heuristic == None:
            if r_brute == r_heuristic:
                accuracy+=1
        else:
            if len(r_brute) == len(r_heuristic):
                accuracy+=1

    print ("accuracy = " + str(accuracy/N))
