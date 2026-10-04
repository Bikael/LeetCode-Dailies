class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        steps = []
        fleets = 1
        last_time = None 
        for i in range(n):
            steps.append((position[i] , (target - position[i]) / speed[i]))
        sorted_steps = sorted(steps)
        # print(sorted_steps)
        for i in range(n-1,-1,-1):
            if last_time == None:
                last_time = sorted_steps[i][1]
            elif last_time < sorted_steps[i][1]:
                # print(f"addin fleet {sorted_steps[i][1]}")
                last_time = sorted_steps[i][1]
                fleets +=1

            
        # print(fleets)
        return fleets
            