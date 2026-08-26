class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        subres = []
        def dfs(i, subres):
            if i == len(digits):
                if subres:
                    res.append(''.join(subres))
                return

            numb = digits[i]
            chars = self.getchars(numb)

            for char in chars:
                subres.append(char)
                dfs(i+1, subres)
                subres.pop()

        dfs(0, subres)

        return res
            

    def getchars(self, number):
        numbInt = int(number)

        if numbInt == 2:
            return ['a', 'b', 'c']
        elif numbInt == 3:
            return ['d', 'e', 'f']
        elif numbInt == 4:
            return ['g', 'h', 'i']
        elif numbInt == 5:
            return ['j', 'k', 'l']
        elif numbInt == 6:
            return ['m', 'n', 'o']
        elif numbInt == 7:
            return ['p', 'q', 'r', 's']
        elif numbInt == 8:
            return ['t', 'u', 'v']
        else:
            return ['w', 'x', 'y', 'z']
    

