
def instersections_len(prop, prop_list, used_sets):
    result = 0
    intersections = []
    for index, p in enumerate(prop_list):
        if p != prop and not used_sets[index]:
            if len(p & prop) > 0:
                result +=1
                intersections.append(index)
    return result, intersections 

def get_all_intersections_lens_sorted(prop_list, used_sets):
    sorted_list=[]
    for index, prop in enumerate(prop_list):
        if not used_sets[index]:
            result, intersections=instersections_len(prop, prop_list, used_sets)
            sorted_list.append(
                (result,index,intersections)) 
    sorted_list.sort()
    return sorted_list


def mark_(intersections: list[int],used_sets: list[bool], used= True):
    for i in intersections:
        used_sets[i] = True


def _solution(k: int, lists: list[set[int]], used_sets: list[bool]):
    if k == 0: 
        empty: list[set[int]]=[]
        return empty

    valid_sets = get_all_intersections_lens_sorted(lists, used_sets)
     
    for _, index, intersections in valid_sets:
        used_sets[index] = True
        mark_(intersections, used_sets, True)
        sol = _solution(k-1, lists, used_sets)
        if sol is not None:
            return sol + [lists[index]]
        mark_(intersections, used_sets, False)
        used_sets[index] = False 
     
    return None             


def solution( k: int,lists: list[set[int]]):
    return _solution(k, lists, [False] * len(lists))


if __name__ == '__main__':
    k,n=3,5
    lists = [{98, 67, 37, 16, 86, 23, 91, 28}, {78, 81, 56, 57, 88, 31}, {24, 67, 59, 4}, {97, 71, 78, 47, 53, 89, 93}, {49, 77, 25, 87}, {75, 19, 50, 23}]
    print(solution(k,lists))
