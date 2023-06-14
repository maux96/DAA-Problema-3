
def _solution(k: int, lists: list[set[int]],mask: set[int], _index: int):
    if k == 0: 
        empty: list[set[int]]=[]
        return empty

    for index,l in enumerate(lists, start=_index):
        union=mask | l
        if len(union) == len(l) + len(mask):
            # la intereccion es nula
            solutions = _solution(k-1, lists, union, _index+1)
            if solutions is not None:
                return solutions + [l]

    return None

def solution(k: int,lists: list[set[int]]):
    return _solution(k, lists, set(), 0)


if __name__ == '__main__':
    k,n=3,5
    lists = [{98, 67, 37, 16, 86, 23, 91, 28}, {78, 81, 56, 57, 88, 31}, {24, 67, 59, 4}, {97, 71, 78, 47, 53, 89, 93}, {49, 77, 25, 87}, {75, 19, 50, 23}]
    print(solution(k,lists))