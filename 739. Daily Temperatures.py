class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # monotonic stack | (temperature, day)
        heat_days = []
        result = [0] * len(temperatures)
        for day, temperature in enumerate(temperatures):
            while heat_days and temperature > heat_days[-1][0]:
                colder_temperature, previous_day = heat_days.pop()
                result[previous_day] = day - previous_day
            heat_days.append( (temperature, day) )
        return result  