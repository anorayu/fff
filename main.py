from datetime import date
class Man:
    instances_count = 0
    def __init__(self, name):
        self.name = name
        Man.instances_count += 1

    @staticmethod
    def counter():
        return Man.instances_count


a = Man("a")
b = Man("aa")
c = Man("fga")

print(Man.counter())
print("Hello git")