class TimeMap:

    def __init__(self):
        self.mymap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mymap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.mymap[key]

        l = 0
        r = len(vals)

        res = ""
        while l < r:
            m = (r - l) // 2 + l

            if vals[m][0] > timestamp:
                r = m
            else:
                res = vals[m][1]
                l = m + 1

        return res
