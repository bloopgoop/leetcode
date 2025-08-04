class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0

        l = r = 0

        res = 1
        held = [fruits[0]]
        last_seen = []

        for idx, fruit in enumerate(fruits):
            if fruit in held:
                prev_fruit = fruits[idx - 1]
                if idx != 0 and fruit == prev_fruit:
                    last_seen.append(last_seen[idx - 1])
                else:
                    last_seen.append(idx)

                # compare len of current window to res
                if (idx - l + 1) > res:
                    res = idx - l + 1

            elif len(held) == 2:
                last_seen.append(idx)
                l = last_seen[idx - 1]

                # remove the fruit that is not the prev fruit and current fruit
                held.remove(fruits[last_seen[idx - 1] - 1])
                held.append(fruit)

            else:
                held.append(fruit)
                last_seen.append(idx)
                # compare len of current window to res
                if (idx - l + 1) > res:
                    res = idx - l + 1

            # print("held: ", held)
            # print("last_seen: ", last_seen)

        return res
