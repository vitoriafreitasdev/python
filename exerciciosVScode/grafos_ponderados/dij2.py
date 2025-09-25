
from collections import defaultdict
import heapq
n = 5 
k = 1
# times = [[1, 2, 1], [1, 4, 4], [2, 5, 10], [5, 4, 4], [3, 4, 1]] esse retorna -1
times = [
    [1, 2, 2],   # 1 → 2 (2)
    [1, 3, 4],   # 1 → 3 (4)
    [2, 4, 7],   # 2 → 4 (7)
    [3, 5, 1],   # 3 → 5 (1)
    [4, 5, 3]    # 4 → 5 (3) (caminho alternativo)
]

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, time in times:
        graph[u].append(((v, time)))


    min_times = {}
    min_heap = [(0, k)] # (distance from source to node, node)

    while min_heap:
        time_k_to_i, i = heapq.heappop(min_heap)
        if i in min_heap:
            continue

        min_times[i] = time_k_to_i
        for nei, nei_time in graph[i]:
            if nei not in min_times:
                heapq.heappush(min_heap, (time_k_to_i + nei_time, nei))

    
    
    if len(min_times) == n:
        return max(min_times.values())
    else:
        return -1
    


print(networkDelayTime(times, 5, 1))