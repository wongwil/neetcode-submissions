class CountSquares:

    def __init__(self):
        self.mymap = defaultdict(lambda:defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.mymap[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1 = point[0]  
        y1 = point[1]

        for y2, size in self.mymap[x1].items():
            # same x coordinate

            s = y1 - y2
            if s == 0:
                continue # same point

            res += size * self.mymap[x1+s][y1] * self.mymap[x1+s][y2]
            res += size * self.mymap[x1-s][y1] * self.mymap[x1-s][y2]

        return res
