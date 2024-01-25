class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        steps = []
        for index in range(len(position)):
            step = (target - position[index]) / speed[index]
            steps.append( (position[index], step) )
        
        steps.sort(reverse=True)

        # increasing monotonic stack
        # cars with step <= will be at same fleet, don't need to add
        # add cars with bigger steps, they will not catch to the front car 
        fleet = []
        for position, step in steps:
            if not fleet or step > fleet[-1]:
                fleet.append(step)
        return len(fleet)

class NoStackSolution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        steps = []
        for index in range(len(position)):
            step = (target - position[index]) / speed[index]
            steps.append( (position[index], step) )
        
        steps.sort(reverse=True)

        fleets = front_car_speed = 0
        for position, behind_car_speed in steps:
            if behind_car_speed > front_car_speed:
                fleets += 1
                front_car_speed = behind_car_speed
        return fleets