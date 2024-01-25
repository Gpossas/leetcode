class TimeMap:
    def __init__(self) -> None:
        self._map = {}

    def set(self, key: str, value: str, timestamp: int):
        if key not in self._map:
            self._map[key] = []
        self._map[key].append( (value, timestamp) )
    
    def get(self, key: str, timestamp: int):
        timestamps = self._map.get(key)
        if not timestamps:
            return ""
        
        left, right = 0, len(timestamps) - 1
        while left < right:
            # upper bound
            middle = (1 + left + right) >> 1

            if timestamp < timestamps[middle][1]:
                right = middle - 1
            else:
                left = middle
        return "" if timestamp < timestamps[0][1] else timestamps[left][0]
    
# tm = TimeMap()

# tm.set('foo', 'bar', 1)
# print(tm.get('foo', 1))
# print(tm.get('foo', 3))

# tm.set('foo', 'bar2', 4)
# print(tm.get('foo', 4))
# print(tm.get('foo', 5))