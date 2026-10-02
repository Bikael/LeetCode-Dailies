from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stk = []

        for i in range(n):
            
            if tokens[i] not in "-+*/":
                stk.append(int(tokens[i]))
                # print(tokens[i])
            else:
                # print(tokens[i])
                val1 = stk.pop()
                val2 = stk.pop()
                
                if tokens[i] == "*":
                    # print(f"operation: {val1}{tokens[i]}{val2}")
                    stk.append(val1 * val2)
                elif tokens[i] == "/":
                    # print(f"operation: {val2}{tokens[i]}{val1}")
                    if val2 / val1 < 0:
                        stk.append(ceil(val2 / val1))
                    else:
                        stk.append(floor(val2 / val1))
                    
                elif tokens[i] == "+":
                    # print(f"operation: {val1}{tokens[i]}{val2}")
                    stk.append(val1 + val2)
                elif tokens[i] == "-":
                    # print(f"operation: {val2}{tokens[i]}{val1}")
                    stk.append(val2 - val1)
            # print(f"stack: {stk}")
        return stk[0]


            

