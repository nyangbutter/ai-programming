#3.1

print(100>200)
print(100>=200)
print(100<200)
print(100<=200)
print(100==200)
print(100!=200)
print(200==200)
print(200!=200)
print(True or True)
print(True or False)
print(True and False)
print(True and True)
print(True or True and False)
print(True and True or False)
print('Morning'<'morning')
print('A' > 'B')

#3.3
a=int(input('나이를 입력하세요:'))
b=int(input('키를 입력하세요:'))
if(a>=19) and (b>=150):
    print('입장할 수 있습니다')
else:
     print('입장 할 수 없습니다')

#3.5
a=int(input('첫 번째 정수를 입력하세요:'))
b=int(input('두 번째 정수를 입력하세요:'))
if a<b:
    print(a,b)
else:
    print(b,a)

#3.7
score=int(input('게임점수를 입력하시오:'))
if score>=1000:
    print('고수입니다')
else:
    print('입문자입니다')

#3.9
a=int(input('정수를 입력하시오:'))
if a%2==0:
    print(a,'는(은) 2로 나누어집니다.')
else:
    print(a,'는(은) 2로 나누어지지 않습니다')

if a%3==0:
    print(a,'는(은) 3으로 나누어집니다.')
else:
    print(a,'는(은) 2로 나누어지지 않습니다')

if (a%2==0) and (a%3==0):
    print(a,'는(은) 2와(과) 3으로 나누어집니다.')
else:
    print(a,'는(은) 2와(과) 3으로 나누어지지 않습니다.')

#3.11
a,b,c=map(int,input('세 복권번호를 입력하시오:').split())
if a==2:
    if b==3 and c==9:
        print('상금 1억원')
    elif b==3 or c==9:
        print('상금 1천만원')
    elif b!=3 or c!=9:
        print('상금 1만원')
    else:
            print('다음 기회에')
elif b==3:
    if a==2 and c==9:
        print('상금 1억원')
    elif a==2 or c==9:
        print('상금 1천만원')
    elif a!=2 or c!=9:
        print('상금 1만원')
    else:
        print('다음 기회에')
elif c==9:
    if b==3 and a==2:
        print('상금 1억원')
    elif b==3 or a==2:
        print('상금 1천만원')
    elif b!=3 or a!=2:
        print('상금 1만원')
    else:
        print('다음 기회에')
else:
    print('다음 기회에')

#3.13
x,y=map(int,input('점의 좌표 x,y를 입력하시오:').split())
if (-10<=x<=10) and (-10<=y<=10):
    print('원의 내부에 있음')
else:
    print('원의 외부에 있음')

#3.15
a=0
for i in range(0,9,1):
    i+=1
    a=2*i
    print('2*',i,'=',a)

#3.17
for i in range(3):
    print('Python ')
    print('is ')
    print('FUN! ')
    
for i in range(3):
    print('Python ')
    print('is.')
print('FUNI! ')

for i in range(3):
    print('Python ')
print('is ')
print('FUN! ')

#3.19
print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다. \n -햄버거(입력b) \n -치킨(입력c) \n -피자(입력p)')
menu=input('메뉴를 선택하세요(알파벳 b,c,p 입력):')
while menu not in ['b', 'c', 'p' ]:
    menu=input('메뉴를 다시 입력하세요:')
if menu=='b':
    print('햄버거를 선택하였습니다')
if menu=='c':
    print('치킨을 선택하였습니다')
if menu=='p':
    print('피자를 선택하였습니다')

#3.21
a=int(input('숫자를 입력하세요:'))
if (a%2!=0) or (a%3!=0) or (a%4!=0) or (a%5!=0) or (a%6!=0) or (a%7!=0) or (a%8!=0) or (a%9!=0):
    print(a,'는 소수입니다')
else:
    print(a,'는 소수가 아닙니다')

#3.23
n=int(input('숫자를 입력하세요:'))
total=0
for i in range(1,n+1):
    total+=i**2
    i+=1
print('결과는',total,'입니다')

#3.25
total=7
day=1
while total<32:
    print('day:',day,'달팽이의 위치:',total,'미터')
    day+=1
    total+=2

#3.27
for a in range(100,1000,1):
    if (a//100)**3+((a//10)%10)**3+(a%10)**3==a:
        print(a)

#3.29
a=500
while a>=50:
    b=int(input('충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오:'))
    a=a+b
    print('현재 탱크량은',a,'입니다')
    
print('경고: 연료가 10%미만이니 충전하세요!')

#3.31
for i in range(1,20001):
    a=0
    total=0
    for m in range(1,i):
        if i%m ==0:
            a=a+m
    for k in range(1,a):
        if a%k == 0:
            total=total+k
    if i == total and i!=a:
        print(i,'의 친화수:',a)
