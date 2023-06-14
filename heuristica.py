MAX_VALUE = 1000000000000
def first_min_intersection(k,prop_list:list):
    result = []
    while len(prop_list) > 0 or len(result) >= k:
        min = MAX_VALUE
        best = None
        delete = None

        if len(prop_list) == 0 or len(result)>=k: 
            break

        for prop in prop_list:
            intersection = instersections_len(prop, prop_list)
            if intersection[0] < min:
                best = prop
                min = intersection[0]
                delete = intersection[1]

        result.append(best)
        for p in delete:
            prop_list.remove(p)

    if len(result) >= k: 
        return result
    else:
        return None        

def instersections_len(prop, prop_list):
    result = 0
    intersections = [prop]
    for p in prop_list:
        if p != prop:
            if len(p & prop) > 0:
                result +=1
                intersections.append(p)

    return result, intersections
