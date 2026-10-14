from bisect import bisect_right, bisect_left, insort_right

class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = [{'t': timestamp, 'v': value}]
        else:
            tl = self.keys[key]
            i = bisect_left(tl, timestamp, key = lambda x: x['t'])
            
            if (i > len(tl) - 1) or (tl[i]['t'] != timestamp):
                insort_right(tl, {'t': timestamp, 'v': value}, key = lambda x: x['t'])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ''
        
        tl = self.keys[key]
        i = bisect_left(tl, timestamp, key = lambda x: x['t'])
        # print(f"{timestamp = }, {i = }, {tl = }")
        
        if i < len(tl) and tl[i]['t'] <= timestamp:
            return tl[i]['v']
        elif i > 0 and tl[i-1]['t'] < timestamp:
            return tl[i-1]['v']

        return ''
        
