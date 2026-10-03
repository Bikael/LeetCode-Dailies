class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        out = [0] * n
        for i in range(n):
            val = (temperatures[i], i)
            while True:
                # print(f"stk: {stk}")
                if not stk:
                    break
                top = stk[-1]
                if top[0] < val[0]:
                    out[top[1]] = val[1] - top[1]
                    stk.pop()
                else:
                    break
            stk.append(val)
            # print(val)
            
            # print(f"out?: {out}")
        return out