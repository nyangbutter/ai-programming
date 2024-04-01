#5.1
list_ex=[10, 20, 30, 40, 50, 60, 70]
high=5
low=3
#(1)
print(list_ex[low])
#(2)
print(list_ex[low+2])
#(3)
print(list_ex[high-low])
#(4)
print(list_ex[low-high])
#(5)
print(list_ex[-1])
#(6)
print(list_ex[-low])
#(7)
print(list_ex[2*3])
#(8)
print(list_ex[2]*3)
#(9)
print(list_ex[5%4])
#(10)
print(len(list_ex))

#5.3
list1=[3, 5, 7]
list2=[2, 3, 4, 5, 6]
n=0
for i in list2:
    for n in list1:
        print(i,'*',n,'=',i*n)

#5.5
list1=['I like ','I love ']
list2=['pancakes','kiwi juice', 'espresso']
for i in range(len(list1)):
    for n in range(len(list2)):
        print(list1[i]+list2[n])

#5.7
n_list=[10, 20, 30, 50, 60]
total=0
for i in n_list:
    total+=i
print('리스트 원소들의 합:', total)

#5.9
n_list=[10, 20, 30, 50, 60]
max1= n_list[0]
for num in n_list[1:]:
    if num > n_list[0]:
        max1=num

print("리스트 원소들 중 최댓값:", max1)

#3.11
i_list=list(map(int,input('5개의 수를 입력하세요:').split()))
a=sum(i_list)
b=sum(i_list)/len(i_list)
c=min(i_list)
d=max(i_list)
print('합:',a)
print('평균:',b)
print('최댓값:',d)
print('최솟값:',c)

#3.13
a_list=list(map(int,input('10개의 수를 입력하세요:').split()))
sigma=0
sigma1=0
for i in a_list:
    sigma+=(i-(sum(a_list)/len(a_list)))**2
    sigma1=(sigma/len(a_list))**(1/2)
print('합:',sum(a_list))
print('평균:',sum(a_list)/len(a_list))
print('표준편차',sigma1)

#3.15
greet='Have a beautiful day'
print(greet[:4])
print(greet[7:16])
print(greet[17:20])

#3.17
animals=['cat', 'tiger', 'lion', 'dog']
print(animals)
first_item = animals.pop(0)
animals.append(first_item)
print(animals)
for i in animals:
    print('I love', i)

#3.19
s_list=['abc', 'bcd', 'abc', 'abbc', 'cddc', 'opq', 'opq']
new_s_list = []
[new_s_list.append(item) for item in s_list if item not in new_s_list]
print(new_s_list)

#5.21
src='a2b3c6a2c3f1g1'
for ch in src:
    if ch.isnumeric() :
        for i in range(int(ch)):
            print(ch_old, end='')
    else:
        ch_old=ch

#5.23
#(1)
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person3 + person4

def how_many_persons(person_list):
    count = 0
    for i in range(len(person_list)):
        if person_list[i] in ['온달', '평강', '혁거세']:
            count+=1
    return count

n_persons = how_many_persons(person_list)
print(str(n_persons) + '명의 정보가 담겨있습니다')

#(2)
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1+person2+person3+person4

def compute_average_age(person_list):
    return (person_list[1]+person_list[6]+person_list[11]+person_list[16])/4

average_age = compute_average_age(person_list)
print('평균 나이는 ' + str(average_age) + '세입니다')

#(3)
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]
person_list = person1 + person2 + person3 + person4

n_male = 0
n_female = 0

def count_males_females(person_list):
    global n_male, n_female
    for i in range(2, len(person_list), 5):
        if person_list[i] == 0:
            n_male += 1
        elif person_list[i] == 1:
            n_female += 1
    return n_female, n_male

n_female, n_male=count_males_females(person_list)
print('리스트에는 남자가', n_male, '명,', '여자가', n_female, '명입니다.')

#(4)
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]
person_list = [person1, person2, person3, person4]

def display_persons(person_list):
    for person in person_list:
        print('[',person[0],',',person[1],',',"남자" if person[2] == 0 else "여자",',',person[3],',', person[4],',',']')
display_persons(person_list)