from classfication.calculator2 import Calculator

class MoreCalculator(Calculator):
    # 2x2x2x2
    def pow(self):
        num = 1
        for i in range(0, self.y):
            num = num * self.x
        return num

    """
    def pow(self):
        return self.x ** self.y
    """



