class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque

        waiting = deque()
        days = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while waiting and temperatures[i] > waiting[-1][0]:
                _, j = waiting.pop()
                days[j] = i - j

            waiting.append((temperatures[i], i))

        # print(days)
        return days
        