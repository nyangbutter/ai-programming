#2.1
print(200,'+',300,'+',400,'=',200+300+400)

#2.3
width=30
height=60
area=width*height
print(area)

#2.5
a=int(input('정사각형의 밑변을 입력하시오:'))
print(a*a)

#2.7
a=0
a=(a+1)*(a+2)*(a+3)*(a+4)*(a+5)*(a+6)*(a+7)*(a+8)*(a+9)*(a+10)
print('10!=',a)

#2.9
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temp= [0, 10, 20, 30, 40, 50]

for celsius in celsius_temp:
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(fahrenheit)

#2.11
cel=int(input('화씨 온도를 입력하세요:'))
fah=(9/5)*cel+32
print('화씨',cel, '도는  섭씨', fah, '도 입니다')

#2.13
PI=3.141592
r=int(input('원의 반지름을 입력하세요:'))
C=2*PI*r
S=PI*r*r
print('원의 둘레:',C,'원의 넓이:',S)

#2.15
a1=int(input('밑변의 길이:'))
b=int(input('높이의 길이:'))
c=(a1**2+b**2)**(1/2)
print(c)

#2.17
bin(2)
a=0b10<<0
b=0b10<<1
c=0b10<<2
d=0b10<<3
e=0b10<<4
f1=0b10<<5
g=0b10<<6
h=0b10<<7
i=0b10<<8
j=0b10<<9
print(a,b,c,d,e,f1,g,h,i,j)

#2.19
n=int(input('정수를 입력하시오:'))
n1=(n%2==0)
print('이 수가 짝수인가요?',n1)

#2.21
n2=int(input('정수를 입력하시오:'))
n3=bin(n2)
print(n3)

#2.23
n4=int(input('세 자리 정수를 입력하시오:'))
hun=n4//100
ten=(n4//10)%10
one=n4%10
print('백의자리:',hun)
print('십의자리:',ten)
print('일의자리:',one)
