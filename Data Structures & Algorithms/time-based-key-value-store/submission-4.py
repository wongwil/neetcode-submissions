class TimeMap:

    def __init__(self):
        self.mymap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mymap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.mymap[key]

        if len(values) == 0:
            return res

        l, r = 0, len(values) - 1

        while l <= r:
            m = (r-l) // 2 + l

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        if l == 0:
            return res

        return values[l-1][0]
