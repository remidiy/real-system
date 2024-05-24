import heapq
from typing import List
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minHeap = [(t, p, i) for i, (t, p) in enumerate(tasks)]
        heapq.heapify(minHeap)

        time, res, q = 0, [], [] # [process_time, i]

        while q or minHeap:
            while minHeap and minHeap[0][0] <= time:
                t, p, i = heapq.heappop(minHeap)
                heapq.heappush(q, (p,i))
            print(time, q)
            if q: 
                p, i = heapq.heappop(q)
                time += p
                res.append(i)
            else:
                time += 1

        return res
    

if __name__ == "__main__":
    s = Solution()
    # s.getOrder([[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]])

    ROWS = 6

    def getCoords(curr):
            rem, qou = curr%ROWS, curr//ROWS
            r = qou-1 if rem == 0 else qou
            r = ROWS - 1 - r
            if qou%2:
                c = ROWS-rem if rem != 0 else ROWS-1
            else: 
                c = rem-1 if rem != 0 else rem
            return (r,c)
    res = []
    for i in range(1, ROWS**2+1):
        res.append(getCoords(i))
    print(res)




