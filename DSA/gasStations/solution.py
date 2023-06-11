#https://leetcode.com/problems/gas-station/


class Solution:
    #A key to the problem is that if the (total gas) >= (total gas cost), only then is it possible to make a round trip
    #Assuming total gas >= total gas cost, our job is to find which gas station we need to start from
    #Another key to the problem is that if we start from gas station s and run out of gas departing from station e, then
    #all gas stations from s through e are not valid starting points. Think about it, we arrived at each station between s through e
    #with at least 0 gallons in the tank. If it was a valid starting point we would have been able to complete the circuit.
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas) #Number of gas stations
        totalSurplus = 0 #The total surplus fuel we have observed traversaing all the stations
        currentSurplus = 0 #The surplus we have observed starting from station 'start'
        start = 0 #We start with station 0. This is the last station that has not yet been proven to be an invalid start...

        for station in range(n): #We make a full circuit only
            totalSurplus += gas[station] - cost[station] #Got gas at station, spent gas departing from station. Their difference is the surplus
            currentSurplus += gas[station] - cost[station]
            if currentSurplus < 0: #Ran out of gas departing from the current station...
                start = station + 1 #We'll next start from the next station. It has not yet been proven to be invalid
                currentSurplus = 0

        return start if totalSurplus >= 0 else -1 #If the totalSurplus >= 0, then there must be a valid start, which by now is stored in variable start



def main():
    solution = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(solution.canCompleteCircuit(gas, cost)) #3
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method