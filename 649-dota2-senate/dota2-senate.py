class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        i = 0
        while len(senate) != 1:
            # print(senate, i)
            if senate[i] == "R":
                # find Dire after current index
                d_index = senate.find("D", i)

                # if not found, find it before the current index
                if d_index == -1:
                    d_index = senate.find("D")

                # if not found in senate string, return "Radiant"
                if d_index == -1:
                    return "Radiant"

                senate = senate[0:d_index] + senate[d_index + 1:]
                if not d_index < i:
                    i += 1
                if len(senate) <= i:
                    i = 0
                continue
            else:
                # find Radiant after current index
                r_index = senate.find("R", i)

                # if not found, find it before the current index
                if r_index == -1:
                    r_index = senate.find("R")
                
                # if not found in senate string, return "Dire"
                if r_index == -1:
                    return "Dire"

                senate = senate[0:r_index] + senate[r_index + 1:]
                if not r_index < i:
                    i += 1
                if len(senate) <= i:
                    i = 0
                continue


        if senate == "R":
            return "Radiant"
        else:
            return "Dire"