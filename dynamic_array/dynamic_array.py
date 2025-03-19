class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        # size is initialized to 0 - no elements in the array
        self.size = 0 

    # assuming i is a valid index
    # this method returns the element at index i
    # O(1) time operation
    def get(self, i: int) -> int:
        return self.arr[i]

    # Overwriting the existing value at index i
    # assuming i is a valid index
    # O(1) time operation
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # check if the capcity is full - then resize the array with double capacity
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1
        

    # removing and return the element at the end of array
    def popback(self) -> int:
        # decrement the size by 1
        self.size -= 1
        # returning the element at the end of array
        return self.arr[self.size]

    # we are doubling the capacity of the array
    # O(n) time operation
    def resize(self) -> None:
        # double the capacity
        self.capacity = self.capacity * 2
        # create a new array with double capacity
        new_arr = [0] * self.capacity
        # copy the elements from the previous arr to the new array
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        # assign the new array to the prev array
        self.arr = new_arr

    # O(1) time operation
    def getSize(self) -> int:
        # already keeping track of the size of the array - just return it
        return self.size
        
    # O(1) time operation
    def getCapacity(self) -> int:
        # already keeping track of the capacity as well - just return it
        return self.capacity
