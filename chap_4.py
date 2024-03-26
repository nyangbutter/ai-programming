#4.1
def my_greet(n):
    for _ in range(n):
        print('환영합니다')
my_greet(2)

#4.3
def max2(m,n):
    if m>n:
        return m
    else:
        return n
def min2(m,n):
    if m<n:
        return m
    else:
        return n
a=max2(100,200)
b=min2(100,200)
print('100과 200 중 큰 수는:',a)
print('100과 200 중 작은 수는:',b)

#4.5
def inch2cm(n):
    a=n*2.54
    return a
for n in range(1,6):
    print(n,'인치=',a)

#4.7
a,b,c=map(int,input('세 수를 입력하시오:').split())
def mean3(a,b,c):
    return (a+b+c)/3
def max3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
def min3(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c

print(a,b,c,'의 평균 값은',mean3(a,b,c))
print(a,b,c,'의 최댓값은',max3(a,b,c))
print(a,b,c,'의 최솟값은',min3(a,b,c))

#4.9
nums=list(map(float,input('숫자들:').split()))

def mean_of_n(nums):
    total = 0
    for i in nums:
        total+=i
    return total/len(nums)
def max_of_m(nums):
    return max(nums)
def min_of_m(nums):
    return min(nums)

print('평균값은',mean_of_n(nums))
print('최댓값',max_of_m(nums))
print('최솟값',min_of_m(nums))

#4.11
x1=int(input('x1좌표를 입력하시오:'))
x2=int(input('x2좌표를 입력하시오:'))
y1=int(input('y1좌표를 입력하시오:'))
y2=int(input('y2좌표를 입력하시오:'))
def area(x1,x2,y1,y2):
    return (x2-x1)*(y2-y1)/2
print('직각삼각형의 면적은',area(x1,x2,y1,y2))

#4.13
#(1)
def s(a):
    return a**3
print('정육면체의 부피는',s(12))

#(2)
def s(a):
    return a**3
print('정육면체의 부피는',s(20))

#(3)
def lwh(a,b,c):
    return a*b*c
print('직육면체의 부피는:',lwh(3,5,6))

#(4)
def cone(a,b):
    return (1/3)*3.14*(a**2)*b
print('원뿔의 부피는:',cone(20,10))

#(5)
def goo(a):
    return (4/3)*3.14*(a**3)
print('구의 부피는:',goo(a))

#(6)
def one(r,h):
    return 3.14*(r**2)*h
print('원기둥의 부피는:',one(20,10))

#4.15
def my_sort(*nums):
    return sorted(nums)
print('결과:',my_sort(45,3,4,56,5))
print('결과:',my_sort(9,8,7,6,5,4,3))

#4.17
def sum_range(n1,n2):
    total=0
    for i in range(n1,n2+1):
        total+=i
        i+=1
    return total
print('{}에서 {}까지의 정수의 합: {}'.format(10, 20, sum_range(10, 20)))
print('{}에서 {}까지의 정수의 합: {}'.format(40, 100, sum_range(40, 100)))

#4.19
n=int(input('fibo(n)의 n을 입력하세요:'))
def fi(n):
    if n<=1:
        return 1
    else:
        return fi(n-1)+fi(n-2)
print('fi(',n,')=',fi(n))

#4.21
a,b,c,d,e,f=map(int,input('주민등록번호 첫 6숫자 입력:').split())
if a>5:
    print('19',a,b,'년',c,d,'월',e,f,'일')
else:
    print('20',a,b,'년',c,d,'월',e,f,'일')


#4.23
def area_and_circumference():
    while True:
        r = int(input("반지름을 입력하세요: "))
        if r < 0:
            print("음수가 입력되어 프로그램을 종료합니다.")
            break
        area = (r ** 2) * 3.14
        circum = 2 * 3.14 * r
        print("원의 넓이: {:.2f}, 원의 둘레: {:.2f}".format(area, circum))
area_and_circumference()


#4.25
s1='Kang Yong Min'
s2='Kang Young-Min'
s3='Park Dong Min'
s4='Park Dong-Yun'
def convert(s1,s2,s3,s4):
    a=s1.upper().replace(' ','').replace('-','')
    b=s2.upper().replace('-','').replace(' ','')
    c=s3.upper().replace(' ','').replace('-','')
    d=s4.upper().replace(' ','').replace('-','')
    return  a,b,c,d,a.count("N"),b.count("N"),c.count("N"),d.count("N")
result=convert(s1, s2, s3, s4)
for i in range(4):
    print(result[i], ":", result[i].count("N"), '개의 N이 나타남')

#4.27
def unit_fraction(frac):
    n=1
    diff=1.0
    while True:
        new_diff=abs(1/n-frac)
        if (new_diff<=diff):
            diff=new_diff
            print('frac={:0.3f}, n={:0.3f},1/n={:0.3f},diff={:0.3f}'.format(frac,n,1/n,diff))
        else:
            break
        n+=1
    return n-1
f_val=float(input('1보다 작고 0보다 큰 소수를 입력하세요:'))
if f_val<=0.0 or f_val>0.1:
    print('입력 오류입니다')
else:
    nf=unit_fraction(f_val)
    print('가장 가까운 단위분수는 1/{0}이며 이 값은 {1:.5f}입니다.'.format(nf,1/nf))
