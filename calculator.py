from re import sub


class Calculator:

    def adder(self, x, y):
        return x + y
    
    def subtractor(self, x, y):
        return x - y

    def multiplier(self, x, y):
        return x * y

    def divider(self, x, y):
        return x / y
    
    def clear(self):
        return 0

x,y = input('input 2 nums: ').split()

c = Calculator()
print(c.adder(int(x),int(y)))
print(c.subtractor(int(x),int(y)))
print(c.multiplier(int(x),int(y)))
print(c.divider(int(x),int(y)))
print(c.clear())