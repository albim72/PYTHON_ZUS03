class Count:
    def __init__(self,count):
        self._count = count

    def __add__(self, other):
        total_count = self._count + other._count
        return Count(total_count)

    def __str__(self):
        return f"Count: {self._count}"

c1 = Count(45)
c2 = Count(12)
c3 = Count(111)

c4 = c1+c2+c3
print(c4)
print(type(c4))
