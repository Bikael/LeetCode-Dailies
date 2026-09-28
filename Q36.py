class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        occur = {}
        # check all the rows
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    pass
                elif int(board[i][j]) <= 9 and int(board[i][j]) > 0:
                    if board[i][j] not in occur:
                        occur[board[i][j]] = 0
                    elif occur[board[i][j]] == 1:
                        # print("found a row dupe")
                        # print(occur[row[i]])
                        return False
                    occur[board[i][j]]+=1  
            # print(occur)
            occur = {}

        # print("---------------------------")
            

        # check all the columns
        for i in range(n):
            for j in range(n):
                if board[j][i] == ".":
                    pass
                elif int(board[j][i]) <= 9 and int(board[j][i]) > 0:
                    if board[j][i] not in occur:
                        occur[board[j][i]] = 0
                    elif occur[board[j][i]] == 1:
                        # print("found a row dupe")
                        # print(occur[row[i]])
                        return False
                    occur[board[j][i]]+=1  
            # print(occur)
            occur = {}

        occur_1 = {}
        occur_2 = {}
        occur_3 = {}
        count = 1
        for i in range(n):
            for j in range(n):
                # print(i,j)
                # print(board[j][i])
                if board[i][j] == ".":
                    pass
                elif int(board[i][j]) <= 9 and int(board[i][j]) > 0:
                    if j < 3:
                        if board[i][j] not in occur_1:
                            occur_1[board[i][j]] = 0
                        elif occur_1[board[i][j]] == 1:
                            return False
                        occur_1[board[i][j]] += 1
                    elif j >= 3 and j < 6:
                        print(board[i][j])
                        if board[i][j] not in occur_2:
                            occur_2[board[i][j]] = 0
                        elif occur_2[board[i][j]] == 1:
                            return False
                        occur_2[board[i][j]] += 1
                    else:
                        if board[i][j] not in occur_3:
                            occur_3[board[i][j]] = 0
                        elif occur_3[board[i][j]] == 1:
                            return False
                        occur_3[board[i][j]] += 1
            
            # print(f"i: {i+1}")
            if (i + 1) % 3 == 0:
                occur_1 = {}
                occur_2 = {}
                occur_3 = {}
        return True

