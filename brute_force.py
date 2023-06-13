
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


if __name__=='__main__':
    # k: cantiad de cursos
    # n: total de propuestas
    # lists: lista de propuestas
    k, n=map(int,input().split())
    lists=[]

    for i in range(n):
        lists.append(set(map(int, input().split())))
    print(solution(k, lists))
