# 복소수 클래스 정의
class comx:
    def __init__(self, x, y):
        self.real = x
        self.image = y

    def __str__(self):
        return f"{self.real} + {self.image}i"

    def __add__(self, b):
        return comx(self.real + b.real, self.image + b.image)

    def __sub__(self, b):
        return comx(self.real - b.real, self.image - b.image)

    def __mul__(self, b):
        return comx(self.real * b.real - self.image * b.image, self.real * b.image + self.image * b.real)

    def __truediv__(self, b):
        real_part = (self.real * b.real + self.image * b.image) / (b.real**2 + b.image**2)
        image_part = (self.image * b.real - self.real * b.image) / (b.real**2 + b.image**2)
        return comx(real_part, image_part)

num1 = comx(1, 2)
num2 = comx(2, 3)
a = num1 + num2
b = num1 - num2
c= num1 * num2
d= num1 / num2
print('덧셈:{}, 뺄셈:{}, 곱셈:{}, 나눗셈:{}'.format(a,b,c,d))

