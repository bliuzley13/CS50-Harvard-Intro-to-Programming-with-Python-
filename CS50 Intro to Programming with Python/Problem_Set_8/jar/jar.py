class Jar:
    def __init__(self, capacity=12):
        #Checks if capacity is a non-negative number
        if capacity < 0:
            raise ValueError('Capacity Mistake')
        #capacity is the static value, size can change, but zero by default
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        #Returns the number of cookies in a string times the number of size
        return self.size * "🍪"

    def deposit(self, n):
        #Cookies added exceed capacity of what is possible
        if n > self.capacity:
            raise ValueError('Exceeding Capacity')
        #Cookies added to the current number in the jar
        if self.size + n > self.capacity:
            raise ValueError('Exceeding Capacity')
        #Adds to the current amount of cookies in the Jar
        self._size += n

    def withdraw(self, n):
        #Cookes withdrawn are more than what exists in the jar
        if self._size < n:
            raise ValueError('Below Capacity')
        #Subtracts the current amount of cookies in the jar by an amount
        self._size -= n

    @property
    #Getter for a class attribute
    def capacity(self):
        return self._capacity

    @property
    #Getter for a class attribute
    def size(self):
        return self._size

