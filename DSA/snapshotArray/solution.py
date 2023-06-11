#https://leetcode.com/problems/snapshot-array/


import bisect

#The key to this problem is that whenever we make a new snapshot, we don't copy the values in the entire array, in fact we don't copy anything at all.
#It's only when we call set() on an index, where append a new list [snapshot_id, value] to arr[index] with the current snapshot and the updated value
#When get(snap_id) is called, we traverse all the lists consisting of [snapshot_id, value] in arr[index] to find the biggest snapshot_id that is <= current snaps
#It is okay to get a snapshot_id that is smaller than the current snaps because that just means that index hasn't been updated since the snapshot_id, so it's still the latest
#value. We also use the bisect method which uses binary search to find the appropriate entry in arr[index]. This allows us to perform get() in O(log(snaps))
class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[0,0]] for i in range(length)] #3D List where each element is a list of [snap_id, valueAtSnapId]
        # arr[3][1] = [2,4] means that the third element in the array had a value of 4 at snap_id 2. Each element
        # has multiple such lists since we have to record multiple snapshots
        self.snaps = 0 #Number of snapshots that have been taken
        

    def set(self, index: int, val: int) -> None:
        if self.snaps == self.arr[index][-1][0]: #If the latest entry at this index has the current snapshot, update the value at this snapshot
            self.arr[index][-1][1] = val
        else: #Otherwise, append a new entry with the latest snapshot Id and the value
            self.arr[index].append([self.snaps, val])

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1

        

    def get(self, index: int, snap_id: int) -> int:
        #Note that the first element in all the lists in arr[index] are sorted by their first element (the snapshotId)
        #We can use bisect to find the correct snapId in arr[index] that is smaller than (snap_id+1). This is equal to finding the smallest entry that is >= snapshot_id
        #The bisect() method uses binary search internally. Notice how we compare with a list [snap_id+1] since list cannot be compared to integer
        i = bisect.bisect(self.arr[index], [snap_id+1])
        return self.arr[index][i-1][1]



def main():

    print("No test case")
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method