class Circle:
    circle_list = []
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

        # add the instance to the circle list
        # if self is appended then object will be returned
        self.circle_list.append(radius)

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius
 

c1 = Circle(10)
c2 = Circle(20)

print(len(Circle.circle_list))  # 2
print(c2)

# accesing class attribute
class Test:
    x = 10

    def __init__(self):
        self.x = 20


test = Test()
print(test.x)  # 20
print(Test.x)  # 10

# private attribute using underscore (_)
class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0

counter = Counter()
print(counter._current)

# name mingling using double underscore (__)
class Counter2:
    def __init__(self):
        self.__current2 = 0

    def increment(self):
        self.__current2 += 1

    def value(self):
        return self.__current2

    def reset(self):
        self.__current2 = 0


counter2 = Counter2()
counter2.increment()
print(counter2._Counter2__current2)