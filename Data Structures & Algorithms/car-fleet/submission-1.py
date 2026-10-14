class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0
        t = -1

        ps_pair = sorted(zip(position, speed), reverse=True)
        for p, s in ps_pair:
            rt = (target - p) / s
            if rt > t:
                fleet_count += 1
                t = rt
        
        return fleet_count