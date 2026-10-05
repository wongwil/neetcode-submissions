class CountSquares:

    def __init__(self):
        self.mymap = defaultdict(lambda:defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.mymap[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1 = point[0]
        y1 = point[1]
        for y, size in self.mymap[x1].items():
            
            s = y1 - y
            if s == 0:
                continue

            curr = size * self.mymap[x1+s][y] * self.mymap[x1+s][y1]
            curr += size * self.mymap[x1-s][y] * self.mymap[x1-s][y1]

            res += curr

        return res
